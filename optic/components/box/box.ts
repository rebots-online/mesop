import { Component, HostBinding, Input } from "@angular/core";
import {
  Click,
  Key,
  Type,
  UserEvent,
} from "optic/protos/ui_ts_proto_pb/protos/ui_pb";
import { BoxType } from "optic/optic/components/box/box_ts_proto_pb/optic/components/box/box_pb";
import { Channel } from "../../../web/src/services/channel";

@Component({
  selector: "optic-box",
  templateUrl: "box.ng.html",
  standalone: true,
})
export class BoxComponent {
  @Input({ required: true }) type!: Type;
  @Input() key!: Key;
  private _config: BoxType;
  isChecked = false;

  constructor(private readonly channel: Channel) {}

  ngOnChanges() {
    this._config = BoxType.deserializeBinary(
      this.type.getValue() as Uint8Array,
    );
  }

  config(): BoxType {
    return this._config;
  }

  @HostBinding("style") get style(): string {
    return `
    display: block;
    background-color: ${this.config().getBackgroundColor()};`;
  }
}