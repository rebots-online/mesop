from dataclasses import dataclass
from typing import Any, Callable, Literal

from pydantic import validate_arguments

import mesop.components.checkbox.checkbox_pb2 as checkbox_pb
from mesop.component_helpers import (
  handler_type,
  insert_composite_component,
  register_event_mapper,
)
from mesop.events import MesopEvent


@dataclass
class CheckboxChangeEvent(MesopEvent):
  checked: bool


register_event_mapper(
  CheckboxChangeEvent,
  lambda event, key: CheckboxChangeEvent(
    key=key,
    checked=event.bool,
  ),
)


@dataclass
class CheckboxIndeterminateChangeEvent(MesopEvent):
  indeterminate: bool


register_event_mapper(
  CheckboxIndeterminateChangeEvent,
  lambda event, key: CheckboxIndeterminateChangeEvent(
    key=key,
    indeterminate=event.bool,
  ),
)


@validate_arguments
def checkbox(
  *,
  key: str | None = None,
  aria_label: str = "",
  aria_labelledby: str = "",
  aria_describedby: str = "",
  id: str = "",
  required: bool = False,
  label_position: Literal["before", "after"] = "after",
  name: str = "",
  value: str = "",
  disable_ripple: bool = False,
  tab_index: float = 0,
  color: str = "",
  checked: bool = False,
  disabled: bool = False,
  indeterminate: bool = False,
  on_change: Callable[[CheckboxChangeEvent], Any] | None = None,
  on_indeterminate_change: Callable[[CheckboxIndeterminateChangeEvent], Any]
  | None = None,
):
  """Creates a Checkbox component.
  Checkbox is a composite component.

  Args:
    key (str|None): Unique identifier for this component instance.
    aria_label (str): Attached to the aria-label attribute of the host element. In most cases, aria-labelledby will take precedence so this may be omitted.
    aria_labelledby (str): Users can specify the `aria-labelledby` attribute which will be forwarded to the input element
    aria_describedby (str): The 'aria-describedby' attribute is read after the element's label and field type.
    id (str): A unique id for the checkbox input. If none is supplied, it will be auto-generated.
    required (bool): Whether the checkbox is required.
    label_position (Literal['before','after']): Whether the label should appear after or before the checkbox. Defaults to 'after'
    name (str): Name value will be applied to the input element if present
    value (str): The value attribute of the native input element
    disable_ripple (bool): Whether the checkbox has a ripple.
    tab_index (float): Tabindex for the checkbox.
    color (str): Palette color of the checkbox.
    checked (bool): Whether the checkbox is checked.
    disabled (bool): Whether the checkbox is disabled.
    indeterminate (bool): Whether the checkbox is indeterminate. This is also known as "mixed" mode and can be used to represent a checkbox with three states, e.g. a checkbox that represents a nested list of checkable items. Note that whenever checkbox is manually clicked, indeterminate is immediately set to false.
    on_change (Callable[[CheckboxChangeEvent], Any]|None): Event emitted when the checkbox's `checked` value changes.
    on_indeterminate_change (Callable[[CheckboxIndeterminateChangeEvent], Any]|None): Event emitted when the checkbox's `indeterminate` value changes.
  """
  return insert_composite_component(
    key=key,
    type_name="checkbox",
    proto=checkbox_pb.CheckboxType(
      aria_label=aria_label,
      aria_labelledby=aria_labelledby,
      aria_describedby=aria_describedby,
      id=id,
      required=required,
      label_position=label_position,
      name=name,
      value=value,
      disable_ripple=disable_ripple,
      tab_index=tab_index,
      color=color,
      checked=checked,
      disabled=disabled,
      indeterminate=indeterminate,
      on_checkbox_change_event_handler_id=handler_type(on_change)
      if on_change
      else "",
      on_checkbox_indeterminate_change_event_handler_id=handler_type(
        on_indeterminate_change
      )
      if on_indeterminate_change
      else "",
    ),
  )