"""
This example tests the following features:

- Unnamed slots
- Named slots
- Nested slots
- Nested slots with core content components
- Content components within content components within content components
"""

import mesop as me


@me.stateclass
class State:
  header_inner_text: str = "Header Inner Button"
  footer_inner_text: str = "Footer Inner Button"


@me.page(path="/testing/complex_slots")
def page():
  with container_wrapper():
    me.text(
      "This is an example of a custom component that uses custom components and nested custom components."
    )


@me.content_component
def container_wrapper():
  state = me.state(State)

  with me.box(style=me.Style(background="brown")):
    me.slot()

  with layout_named(color="yellow") as parent1:
    with parent1.header():
      with me.expansion_panel(
        key="header_outer",
        title="Header Outer",
        disabled=False,
        hide_toggle=False,
      ):
        with layout_named(color="black") as parent2:
          with parent2.header():
            with me.expansion_panel(
              key="header_inner",
              title="Header Inner",
              disabled=False,
              hide_toggle=False,
            ):
              with custom_card(color="pink"):
                me.button(
                  state.header_inner_text, on_click=on_click_header_inner
                )
          with parent2.footer():
            with me.expansion_panel(
              key="footer_inner",
              title="Footer Inner",
              disabled=False,
              hide_toggle=False,
            ):
              with custom_card(color="orange"):
                me.button(
                  state.footer_inner_text, on_click=on_click_footer_inner
                )
    with parent1.footer():
      with me.expansion_panel(
        key="footer_outer",
        title="Footer Outer",
        disabled=False,
        hide_toggle=False,
      ):
        me.text("This should display in the outer footer")


@me.slotclass
class LayoutSlots:
  header: me.NamedSlot
  footer: me.NamedSlot


@me.content_component(named_slots=LayoutSlots)
def layout_named(color: str):
  with me.box(
    style=me.Style(
      color="green",
      display="flex",
      flex_direction="column",
      background="red",
      border=me.Border.all(me.BorderSide(width=10, style="solid", color=color)),
    )
  ):
    with me.box(
      style=me.Style(
        flex="1",
        color="white",
        background="blue",
        border=me.Border.all(
          me.BorderSide(width=10, style="solid", color="green")
        ),
      )
    ):
      me.text("---Header Start---", style=me.Style(font_weight="bold"))
      with custom_card(color="orange"):
        me.text("HEADER - Custom container within custom container")
      me.slot(name="header")
      me.text("---Header End---", style=me.Style(font_weight="bold"))
      me.text("---Footer Start---", style=me.Style(font_weight="bold"))
      with custom_card(color="orange"):
        me.text("FOOTER - Custom container within custom container")
      me.slot(name="footer")
      me.text("---Footer End---", style=me.Style(font_weight="bold"))


@me.content_component
def custom_card(color: str = "red"):
  with me.card(style=me.Style(color=color)):
    me.card_header(title="Custom Card")
    with me.card_content():
      me.slot()


def on_click_header_inner(e: me.ClickEvent):
  state = me.state(State)
  state.header_inner_text = "Header Inner Button (Clicked)"


def on_click_footer_inner(e: me.ClickEvent):
  state = me.state(State)
  state.footer_inner_text = "Footer Inner Button (Clicked)"