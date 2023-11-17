from typing import Any, Callable
import protos.ui_pb2 as pb
import optic.components.checkbox.checkbox_pb2 as checkbox_pb
from optic.component_helpers import insert_component, handler_type
from optic.state.events import CheckboxEvent


def checkbox(
    *,
    label: str,
    on_update: Callable[[Any, CheckboxEvent], Any],
    key: str | None = None,
):
    """
    Creates a checkbox component with a specified label and update action.

    Args:
        label (str): The label for the checkbox.
        on_update (Callable[..., Any]): The function to be called when the checkbox is updated.

    The function appends the created checkbox component to the children of the current node in the runtime session.
    """
    insert_component(
        key=key,
        type=pb.Type(
            type="checkbox",
            value=checkbox_pb.CheckboxComponent(
                label=label,
                on_update_handler_id=handler_type(on_update),
            ).SerializeToString(),
        ),
    )