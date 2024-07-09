import time
from fprime_gds.common.testing_fw import predicates


# def test_cmd_no_op(fprime_test_api):
#     """Test command CMD_NO_OP

#     Test that CMD_NO_OP can be sent and return without and errors
#     """
#     fprime_test_api.send_and_assert_command("cmdDisp.CMD_NO_OP")



def test_blinking(fprime_test_api):
    # Send command to enable blinking, then assert expected events are emitted
    blink_start_evr = fprime_test_api.get_event_pred("led.SetBlinkingState", ["ON"])
    led_on_evr = fprime_test_api.get_event_pred("led.LedState", ["ON"])
    led_off_evr = fprime_test_api.get_event_pred("led.LedState", ["OFF"])
    blink_stop_evr = fprime_test_api.get_event_pred("led.SetBlinkingState", ["OFF"])


    fprime_test_api.send_and_assert_event(
        "led.BLINKING_ON_OFF",
        args=["ON"],
        events=[blink_start_evr, led_on_evr, led_off_evr, led_on_evr],
    )

    # Assert that blink command sets blinking state on
    blink_state_on_tlm = fprime_test_api.get_telemetry_pred("led.BlinkingState", "ON")
    fprime_test_api.assert_telemetry(blink_state_on_tlm)

    # Send command to stop blinking, then assert blinking stops
    #TODO: Define blink_stop_evr
    fprime_test_api.send_and_assert_event(
        "led.BLINKING_ON_OFF", args=["OFF"], events=[blink_stop_evr]
    )

    blink_state_on_tlm = fprime_test_api.get_telemetry_pred("led.BlinkingState", "OFF")
    fprime_test_api.assert_telemetry(blink_state_on_tlm, timeout = 2)