import sys

def parse_basic_control_register(reg16b_val):
    print(f"[0x00] Basic Control Register: 0x{reg16b_val:04X}")
    
    if reg16b_val & (1 << 15):
        print(f"\tbit15: R/W PHY reset")
    else:
        print(f"\tbit15: R/W normal operation")

    if reg16b_val & (1 << 14):
        print(f"\tbit14: R/W PHY reset")
    else:
        print(f"\tbit14: R/W normal operation")

    speed_select = {
        0: "10 Mbit/s",
        1: "1000 Mbit/s",
        2: "100 Mbit/s",
        3: "reserved",
    }

    speed = ((((reg16b_val >> 13) & 1) << 1) | ((reg16b_val >> 6) & 1))

    if speed in speed_select:
        print(f"\tbit13: R/W SPEED_SELECT (LSB) = {((reg16b_val >> 13) & 1)}, {speed_select[speed]}")

    if reg16b_val & (1 << 12):
        print(f"\tbit12: R/W Error")
    else:
        print(f"\tbit12: R/W Auto negotiation not supported; always 0; a write access is ignored")

    if reg16b_val & (1 << 11):
        print(f"\tbit11: R/W power down and switch to Standby mode (provided ISOLATE = 0; ignored if "
              f"ISOLATE = 1 and CONTROL_ERR interrupt generated)")
    else:
        print(f"\tbit11: R/W  normal operation (clearing this bit automatically triggers a transition to Normal "
              f"mode, provided control bits POWER_MODE are set to 0011 Normal mode, see Table 18)")

    if reg16b_val & (1 << 10):
        print(f"\tbit10: R/W isolate PHY from MII/RMII (provided POWER_DOWN = 0; ignored if POWER_DOWN "
              f"= 1 and CONTROL_ERR interrupt generated)")
    else:
        print(f"\tbit10: R/W normal operation")

    if reg16b_val & (1 << 9):
        print(f"\tbit9: R/W Error")
    else:
        print(f"\tbit9:  R/W Auto negotiation not supported; always 0; a write access is ignored.")

    if reg16b_val & (1 << 8):
        print(f"\tbit8: R/W  only full duplex supported; always 1; a write access is ignored")
    else:
        print(f"\tbit8: R/W  Error")

    if reg16b_val & (1 << 7):
        print(f"\tbit7: R/W  error!")
    else:
        print(f"\tbit7: R/W  COL signal test not supported; always 0; a write access is ignored")

    if speed in speed_select:
        print(f"\tbit6: R/W SPEED_SELECT (MSB) = {((reg16b_val >> 6) & 1)}, {speed_select[speed]}")

    if reg16b_val & (1 << 5):
        print(f"\tbit5: R/W enable transmit from MII regardless of whether the PHY has determined that "
              f"a valid link has been established")
    else:
        print(f"\tbit5: R/W enable transmit from MII only when the PHY has determined that a valid "
              f"link has been established ")

    print("\n")

def parse_basic_status_register(reg16b_val):
    print(f"[0x01] Basic Status Register: 0x{reg16b_val:04X}")

    if reg16b_val & (1 << 15):
        print(f"\tbit15: PHY able to perform 100BASE-T4")
    else:
        print(f"\tbit15: PHY not able to perform 100BASE-T4")

    if reg16b_val & (1 << 14):
        print(f"\tbit14: PHY able to perform 100BASE-X full-duplex")
    else:
        print(f"\tbit14: PHY not able to perform 100BASE-X full-duplex")

    if reg16b_val & (1 << 13):
        print(f"\tbit13: PHY able to perform 100BASE-X half-duplex")
    else:
        print(f"\tbit13: PHY not able to perform 100BASE-X half-duplex")

    if reg16b_val & (1 << 12):
        print(f"\tbit12: PHY able to perform 10 Mbit/s full-duplex")
    else:
        print(f"\tbit12: PHY not able to perform 10 Mbit/s full-duplex")

    if reg16b_val & (1 << 11):
        print(f"\tbit11: PHY able to perform 10 Mbit/s half-duplex")
    else:
        print(f"\tbit11: PHY not able to perform 10 Mbit/s half-duplex")

    if reg16b_val & (1 << 10):
        print(f"\tbit10: PHY able to perform 100BASE-T2 full-duplex")
    else:
        print(f"\tbit10: PHY not able to perform 100BASE-T2 full-duplex")

    if reg16b_val & (1 << 9):
        print(f"\tbit9: PHY able to perform 100BASE-T2 half-duplex")
    else:
        print(f"\tbit9: PHY not able to perform 100BASE-T2 half-duplex")

    if reg16b_val & (1 << 8):
        print(f"\tbit8: extended status information in register 15h")
    else:
        print(f"\tbit8: no extended status information in register 15h")

    if reg16b_val & (1 << 7):
        print(f"\tbit7: PHY able to transmit from MII regardless of whether the PHY has determined "
              f"that a valid link has been established")
    else:
        print(f"\tbit7: PHY able to transmit from MII only when the PHY has determined that a valid "
              f"link has been established")

    if reg16b_val & (1 << 6):
        print(f"\tbit6: PHY will accept management frames with preamble suppressed")
    else:
        print(f"\tbit6: PHY will not accept management frames with preamble suppressed")

    if reg16b_val & (1 << 5):
        print(f"\tbit5: Autonegotiation process completed")
    else:
        print(f"\tbit5: Autonegotiation process not completed")

    if reg16b_val & (1 << 4):
        print(f"\tbit4: remote fault condition detected")
    else:
        print(f"\tbit4: no remote fault condition detected")

    if reg16b_val & (1 << 3):
        print(f"\tbit3: PHY able to perform Autonegotiation")
    else:
        print(f"\tbit3: PHY not able to perform Autonegotiation")

    if reg16b_val & (1 << 2):
        print(f"\tbit2: link is up")
    else:
        print(f"\tbit2: link is down")

    if reg16b_val & (1 << 1):
        print(f"\tbit1: jabber condition detected")
    else:
        print(f"\tbit1: no jabber condition detected")

    if reg16b_val & (1 << 0):
        print(f"\tbit0: extended register capabilities")
    else:
        print(f"\tbit0: basic register set capabilities only")

    print("\n")

def parse_extended_status_register(reg16b_val):
    print(f"[0x0F] Extended Status Register: 0x{reg16b_val:04X}")

    if reg16b_val & (1 << 15):
        print(f"\tbit15: PHY able to perform 1000BASE-X full-duplex")
    else:
        print(f"\tbit15: PHY not able to perform 1000BASE-X full-duplex")

    if reg16b_val & (1 << 14):
        print(f"\tbit14: PHY able to perform 1000BASE-X half-duplex")
    else:
        print(f"\tbit14: PHY not able to perform 1000BASE-X half-duplex")

    if reg16b_val & (1 << 13):
        print(f"\tbit13: PHY able to perform 1000BASE-T full-duplex")
    else:
        print(f"\tbit13: PHY not able to perform 1000BASE-T full-duplex")

    if reg16b_val & (1 << 12):
        print(f"\tbit12: PHY able to perform 1000BASE-T half-duplex")
    else:
        print(f"\tbit12: PHY not able to perform 1000BASE-T half-duplex")

    if reg16b_val & (1 << 7):
        print(f"\tbit7: PHY able to 1-pair 100BASE-T1 100 Mbit/s")
    else:
        print(f"\tbit7: PHY not able to 1-pair 100BASE-T1 100 Mbit/s")

    if reg16b_val & (1 << 6):
        print(f"\tbit6: PHY supports RTPGE")
    else:
        print(f"\tbit6: PHY not able to support RTPGE")

    print("\n")

def parse_power_mode(reg16b_val):
    print(f"    Power Mode:")
    power_modes = {
        0: "operating mode: no change",
        3: "operating mode: Normal mode (command)",
        9: "Silent mode (read only)",
        10: "Sleep mode (read only)",
        11: "Sleep Request mode (command)",
        12: "Standby mode (command)",
    }
    if reg16b_val in power_modes:
        print(f"\tbit14..11: {power_modes[reg16b_val]}")
    else:
        print(f"\tbit14..11: Error")

def parse_test_mode(reg16b_val):
    print(f"    Test Mode:")
    test_modes = {
        0: "R/W test mode selection: no test mode",
        1: "R/W test mode selection 100BASE-T1 test mode 1",
        2: "R/W test mode selection 100BASE-T1 test mode 2",
        3: "R/W test mode selection test mode 3",
        4: "R/W test mode selection 100BASE-T1 test mode 4",
        5: "R/W test mode selection 100BASE-T1 test mode 5",
        6: "R/W test mode selection scrambler and descrambler bypassed",
        7: "R/W test mode selection reserved",
    }
    if reg16b_val in test_modes:
        print(f"\tbit8..6: {test_modes[reg16b_val]}")
    else:
        print(f"\tbit8..6: Error")

def parse_loopback_mode(reg16b_val):
    print(f"    Loopback Mode:")
    loopback_modes = {
        0: "R/W internal loopback",
        1: "R/W external loopback",
        2: "R/W external loopback",
        3: "R/W remote loopback",
    }
    if reg16b_val in loopback_modes:
        print(f"\tbit4..3: {loopback_modes[reg16b_val]}")
    else:
        print(f"\tbit4..3: Error")

def parse_extended_control_register(reg16b_val):
    print(f"[0x11] Extended Control Register: 0x{reg16b_val:04X}")
    
    if reg16b_val & (1 << 15):
        print(f"\tbit15: link control enabled")
    else:
        print(f"\tbit15: link control disabled")

    power_mode = (reg16b_val >> 11) & 0b1111
    parse_power_mode(power_mode)

    if reg16b_val & (1 << 10):
        print(f"\tbit10: enable Slave jitter test")
    else:
        print(f"\tbit10: disable Slave jitter test")

    if reg16b_val & (1 << 9):
        print(f"\tbit9: forces a restart of the training phase")
    else:
        print(f"\tbit9: halts the training phase")

    test_mode = (reg16b_val >> 6) & 0b111
    parse_test_mode(test_mode)

    if reg16b_val & (1 << 5):
        print(f"\tbit5: forces TDR-based cable test")
    else:
        print(f"\tbit5: stops TDR-based cable test")

    loopback_mode = (reg16b_val >> 3) & 0b11
    parse_loopback_mode(loopback_mode)

    if reg16b_val & (1 << 2):
        print(f"\tbit2: configuration register access enabled")
    else:
        print(f"\tbit2: configuration register access disabled")

    print("\n")

def parse_mii_mode(mii_mode):
    print(f"    MII Mode:")
    mii_modes = {
        0: "MII mode enabled",
        1: "RMII mode enabled (50 MHz input on REF_CLK)",
        2: "RMII mode enabled (50 MHz output on REF_CLK)",
        3: "Reverse MII mode",
    }
    if mii_mode in mii_modes:
        print(f"\tbit9:8: R/W {mii_modes[mii_mode]}")
    else:
        print(f"\tbit9:8: R/W Error")

def parse_configuration_register_1(reg16b_val):
    print(f"[0x12] Configuration Register 1: 0x{reg16b_val:04X}")
    
    if reg16b_val & (1 << 15):
        print(f"\tbit15: R/W PHY configured as Master")
    else:
        print(f"\tbit15: R/W PHY configured as Slave")

    if reg16b_val & (1 << 14):
        print(f"\tbit14: R/W wake-up event forwarded locally")
    else:
        print(f"\tbit14: R/W wake-up event not forwarded locally")

    if reg16b_val & (1 << 11):
        print(f"\tbit11: R/W PHY reacts to a remote wake-up")
    else:
        print(f"\tbit11: R/W PHY does not react to a remote wake-up")

    if reg16b_val & (1 << 10):
        print(f"\tbit14: R/W PHY reacts to a local wake-up")
    else:
        print(f"\tbit14: R/W PHY does not react to a local wake-up")

    mii_mode = (reg16b_val >> 8) & 0b11
    parse_mii_mode(mii_mode)

    if reg16b_val & (1 << 7):
        print(f"\tbit7: R/W MII output driver reduced strength")
    else:
        print(f"\tbit7: MII output driver standard strength")

    if reg16b_val & (1 << 6):
        print(f"\tbit6: confirmation needed from another PHY before going to sleep")
    else:
        print(f"\tbit6: no confirmation needed from another PHY before going to sleep")

    if reg16b_val & (1 << 5):
        print(f"\tbit5: LPS/WUR disabled")
    else:
        print(f"\tbit5: LPS/WUR enabled")

    if reg16b_val & (1 << 4):
        print(f"\tbit4: sleep acknowledge timer enabled; auto-transition back from Sleep Request mode to Normal mode disabled during data transmission on MII or MDI")
    else:
        print(f"\tbit4: sleep acknowledge timer disabled; auto-transition back from Sleep Request mode to Normal mode enabled during data transmission on MII or MDI")

    if reg16b_val & (1 << 2):
        print(f"\tbit2: wake-up event forwarded remotely ")
    else:
        print(f"\tbit2: wake-up event not forwarded remotely  ")

    if reg16b_val & (1 << 1):
        print(f"\tbit1: autonomous power-down enabled ")
    else:
        print(f"\tbit1: autonomous power-down disabled ")

    if reg16b_val & (1 << 0):
        print(f"\tbit0: automatic transition from Normal to Sleep Request when LPS code group received enabled ")
    else:
        print(f"\tbit0: automatic transition from Normal to Sleep Request when LPS code group received disabled ")

    print("\n")

def parse_sqi(sqi):
    print(f"    SQI:")
    sqi_meanings = {
        0: "worse than class A SQI (unstable link)",
        1: "class A SQI (unstable link)",
        2: "class B SQI (unstable link)",
        3: "class C SQI (good link)",
        4: "class D SQI (good link; bit error rate < 1e-10)",
        5: "class E SQI (good link)",
        6: "class F SQI (very good link)",
        7: "class G SQI (very good link)",
    }
    if sqi in sqi_meanings:
        print(f"\tbit7..5: R/O {sqi_meanings[sqi]}")
    else:
        print(f"\tbit7..5: R/O Error")

def parse_phy_state(phy_state):
    print(f"    PHY State:")
    phy_states = {
        0: "PHY Idle",
        1: "PHY Initializing",
        2: "PHY Configured",
        3: "PHY Offline",
        4: "PHY Active",
        5: "PHY Isolate",
        6: "PHY Cable test",
        7: "PHY Test mode",
    }
    if phy_state in phy_states:
        print(f"\tbit2..0: R/O {phy_states[phy_state]}")
    else:
        print(f"\tbit2..0: R/O PHY Test mode")

def parse_communication_status_register(reg16b_val):
    print(f"[0x17] Communication Status Register: 0x{reg16b_val:04X}")
    
    if reg16b_val & (1 << 15):
        print(f"\tbit15: R/O link OK")
    else:
        print(f"\tbit15: R/O link failure")

    TX_modes = {
        0: "transmitter disabled",
        1: "transmitter in SEND_N mode",
        2: "transmitter in SEND_I mode",
        3: "transmitter in SEND_Z mode",
    }

    TX_mode = (reg16b_val >> 13) & 0b11

    if TX_mode in TX_modes:
        print(f"\tbit14:13: R/O {TX_modes[TX_mode]}")

    if reg16b_val & (1 << 12):
        print(f"\tbit12: R/O local receiver OK")
    else:
        print(f"\tbit12: R/O local receiver not OK")

    if reg16b_val & (1 << 11):
        print(f"\tbit11: R/O remote receiver OK")
    else:
        print(f"\tbit11: R/O remote receiver not OK")

    if reg16b_val & (1 << 10):
        print(f"\tbit10: R/O descrambler locked")
    else:
        print(f"\tbit10: R/O descrambler unlocked")

    if reg16b_val & (1 << 9):
        print(f"\tbit9: R/O SSD error detected")
    else:
        print(f"\tbit9: R/O no SSD error detected")

    if reg16b_val & (1 << 8):
        print(f"\tbit8: R/O ESD error detected")
    else:
        print(f"\tbit8: R/O no ESD error detected")

    sqi = (reg16b_val >> 5) & 0b111
    parse_sqi(sqi)

    if reg16b_val & (1 << 4):
        print(f"\tbit4: R/O receive error detected since register last read")
    else:
        print(f"\tbit4: R/O no receive error detected")

    if reg16b_val & (1 << 3):
        print(f"\tbit3: R/O transmit error detected since register last read")
    else:
        print(f"\tbit3: R/O no transmit error detected")

    phy_state = reg16b_val & 0b111
    parse_phy_state(phy_state)

    print("\n")

def parse_general_status_register(reg16b_val):
    print(f"[0x18] General Status Register: 0x{reg16b_val:04X}")
    
    if reg16b_val & (1 << 15):
        print(f"\tbit15: R/O unmasked interrupt pending")
    else:
        print(f"\tbit15: R/O all interrupts cleared")

    if reg16b_val & (1 << 14):
        print(f"\tbit14: R/O PLL stable and locked")
    else:
        print(f"\tbit14: R/O PLL unstable and not locked")

    if reg16b_val & (1 << 13):
        print(f"\tbit13: R/O local wake-up detected")
    else:
        print(f"\tbit13: R/O no local wake-up detected")

    if reg16b_val & (1 << 12):
        print(f"\tbit12: R/O remote wake-up detected")
    else:
        print(f"\tbit12: R/O no remote wake-up detected")

    if reg16b_val & (1 << 11):
        print(f"\tbit11: R/O 100BASE-T1 data detected at MDI or MII in Sleep Request mode")
    else:
        print(f"\tbit11: R/O no 100BASE-T1 data detected at MDI or MII in Sleep Request mode")

    if reg16b_val & (1 << 10):
        print(f"\tbit10: R/O EN switched LOW since register last read")
    else:
        print(f"\tbit10: R/O EN HIGH")

    if reg16b_val & (1 << 9):
        print(f"\tbit9: R/O hardware reset detected since register last read")
    else:
        print(f"\tbit9: R/O no hardware reset detected")

    link_fail_cnt = (reg16b_val >> 3) & 0b11111
    print(f"\tbit7:3: R/O linkFailCnt: [{link_fail_cnt}]")

    print(f"\tbit2:0: R/O reserved\n")

def parse_external_status_register(reg16b_val):
    print(f"[0x19] External Status Register: 0x{reg16b_val:04X}")
    
    if reg16b_val & (1 << 15):
        print(f"\tbit15: R/O undervoltage detected on pin VDDD(3V3)")
    else:
        print(f"\tbit15: R/O no undervoltage detected on pin VDDD(3V3)")

    if reg16b_val & (1 << 14):
        print(f"\tbit14: R/O undervoltage detected on pin VDDA(3V3)")
    else:
        print(f"\tbit14: R/O no undervoltage detected on pin VDDA(3V3)")

    if reg16b_val & (1 << 13):
        print(f"\tbit13: R/O undervoltage detected on pin VDDD(1V8)")
    else:
        print(f"\tbit13: R/O no undervoltage detected on pin VDDD(1V8)")

    if reg16b_val & (1 << 11):
        print(f"\tbit11: R/O undervoltage detected on pin VDD(IO)")
    else:
        print(f"\tbit11: R/O no undervoltage detected on pin VDD(IO)")

    if reg16b_val & (1 << 10):
        print(f"\tbit10: R/O temperature above high level")
    else:
        print(f"\tbit10: R/O temperature below high level")

    if reg16b_val & (1 << 9):
        print(f"\tbit9: R/O temperature above warning level")
    else:
        print(f"\tbit9: R/O temperature below warning level")

    if reg16b_val & (1 << 8):
        print(f"\tbit8: R/O short circuit detected since register last read")
    else:
        print(f"\tbit8: R/O no short circuit detected")

    if reg16b_val & (1 << 7):
        print(f"\tbit7: R/O open circuit detected since register last read")
    else:
        print(f"\tbit7: R/O no open circuit detected")

    if reg16b_val & (1 << 6):
        print(f"\tbit6: R/O polarity inversion detected at MDI")
    else:
        print(f"\tbit6: R/O no polarity inversion detected at MDI")

    if reg16b_val & (1 << 5):
        print(f"\tbit5: R/O interleave order of detected ternary symbols: TBn, TAn")
    else:
        print(f"\tbit5: R/O interleave order of detected ternary symbols: TAn, TBn")

    print()

def parse_loc_wu_tim(loc_wu_tim):
    print(f"    Local Wake-up Timer:")
    loc_wu_tim_values = {
        0: "longest (10 ms to 20 ms)",
        1: "long (250 us to 500 s)",
        2: "short (100 us to 200 s)",
        3: "shortest (10 us to 40 s)",
    }
    if loc_wu_tim in loc_wu_tim_values:
        print(f"\tbit8:7 R/W local wake-up timer: {loc_wu_tim_values[loc_wu_tim]}")
    else:
        print(f"\tbit8:7 R/W Error")

def parse_clk_mode(clk_mode):
    print(f"    Clock Mode:")
    clk_mode_values = {
        0: "25 MHz XTAL; no clock at CLK_IN_OUT",
        1: "25 MHz XTAL; 25 MHz output at CLK_IN_OUT",
        2: "25 MHz external clock at CLK_IN_OUT",
        3: "50 MHz input at REF_CLK; RMII mode only; no XTAL; no clock at CLK_IN_OUT",
    }
    if clk_mode in clk_mode_values:
        print(f"\tbit13:12 R/W {clk_mode_values[clk_mode]}")
    else:
        print(f"\tbit13:12 R/W Error")

def parse_common_configuration_register(reg16b_val):
    print(f"[0x1B] Common Configuration Register: 0x{reg16b_val:04X}")
    
    if reg16b_val & (1 << 15):
        print(f"\tbit15: R/W autonomous operation")
    else:
        print(f"\tbit15: R/W managed operation")

    clk_mode = (reg16b_val >> 12) & 0b11
    parse_clk_mode(clk_mode)

    if reg16b_val & (1 << 11):
        print(f"\tbit11: R/W external 1.8 V supply")
    else:
        print(f"\tbit11: R/W internal 1.8 V LDO enabled")

    if reg16b_val & (1 << 10):
        print(f"\tbit10:  R/W reduced output driver strength at output of CLK_IN_OUT ")
    else:
        print(f"\tbit10:  R/W standard output driver strength at output of CLK_IN_OUT")

    if reg16b_val & (1 << 9):
        print(f"\tbit9: R/W XTAL and CLK_IN_OUT output remain active until device switched to Sleep mode via SMI")
    else:
        print(f"\tbit9: R/W XTAL and CLK_IN_OUT output switched off in Sleep mode")

    loc_wu_tim = (reg16b_val >> 7) & 0b11
    parse_loc_wu_tim(loc_wu_tim)

    if reg16b_val & (1 << 6):
        print(f"\tbit6: R/W ratiometric input threshold (VDD(IO))")
    else:
        print(f"\tbit6: R/W absolute input threshold")

    if reg16b_val & (1 << 5):
        print(f"\tbit5:  R/W INH switched on in Disable mode")
    else:
        print(f"\tbit5:  R/W INH switched off in Disable mode")

    print("\tbit4:0:  R/W reserved")

    print("\n")

def parse_interrupt_status_register(reg16b_val):
    print(f"[0x15] Interrupt Status Register: 0x{reg16b_val:04X}")
    
    if reg16b_val & (1 << 15):
        print(f"\tbit15: R/O power-on detected")
    else:
        print(f"\tbit15: R/O power-on not detected")

    if reg16b_val & (1 << 14):
        print(f"\tbit14: R/O local or remote wake-up detected")
    else:
        print(f"\tbit14: R/O no local or remote wake-up detected")

    if reg16b_val & (1 << 13):
        print(f"\tbit13: R/O dedicated wake-up request detected")
    else:
        print(f"\tbit13: R/O no dedicated wake-up request detected")

    if reg16b_val & (1 << 12):
        print(f"\tbit12: R/O LPS code groups received")
    else:
        print(f"\tbit12: R/O no LPS code groups received")

    if reg16b_val & (1 << 11):
        print(f"\tbit11: R/O PHY initialization error detected")
    else:
        print(f"\tbit11: R/O no PHY initialization error detected")

    if reg16b_val & (1 << 10):
        print(f"\tbit10: R/O link status bit LINK_UP changed from 'link OK' to 'link fail'")
    else:
        print(f"\tbit10: R/O link status not changed")

    if reg16b_val & (1 << 9):
        print(f"\tbit9: R/O link status bit LINK_UP changed from 'link fail' to 'link OK'")
    else:
        print(f"\tbit9: R/O link status not changed")

    if reg16b_val & (1 << 8):
        print(f"\tbit8: R/O symbol error detected")
    else:
        print(f"\tbit8: R/O no symbol error detected")

    if reg16b_val & (1 << 7):
        print(f"\tbit7: R/O training phase failure detected")
    else:
        print(f"\tbit7: R/O no training phase failure detected")

    if reg16b_val & (1 << 6):
        print(f"\tbit6: R/O SQI value below warning limit and bit LINK_UP set")
    else:
        print(f"\tbit6: R/O SQI value above warning limit")

    if reg16b_val & (1 << 5):
        print(f"\tbit5: R/O SMI control error detected")
    else:
        print(f"\tbit5: R/O no SMI control error detected")

    if reg16b_val & (1 << 3):
        print(f"\tbit3: R/O undervoltage detected on VDD(IO), VDDD(3V3), VDDD(1V8) or VDDA(3V3)")
    else:
        print(f"\tbit3: R/O no undervoltage detected")

    if reg16b_val & (1 << 2):
        print(f"\tbit2: R/O undervoltage recovery detected")
    else:
        print(f"\tbit2: R/O no undervoltage recovery detected")

    if reg16b_val & (1 << 1):
        print(f"\tbit1: R/O overtemperature error detected")
    else:
        print(f"\tbit1: R/O no overtemperature error detected")

    if reg16b_val & (1 << 0):
        print(f"\tbit0: R/O transition from Sleep Request back to Normal as a result of the Sleep Request timer expiring")
    else:
        print(f"\tbit0: R/O no transition from Sleep Request back to Normal as a result of the Sleep Request timer expiring")

    print("\n")

def parse_interrupt_enable_register(reg16b_val):
    print(f"[0x16] Interrupt Enable Register: 0x{reg16b_val:04X}")
    
    interrupt_flags = {
        15: "PWON interrupt",
        14: "WAKEUP interrupt",
        13: "WUR_RECEIVED interrupt",
        12: "LPS_RECEIVED interrupt",
        11: "PHY_INIT_FAIL interrupt",
        10: "LINK_STATUS_FAIL interrupt",
        9: "LINK_STATUS_UP interrupt",
        8: "SYM_ERR interrupt",
        7: "TRAINING_FAILED interrupt",
        6: "SQI_WARNING interrupt",
        5: "CONTROL_ERR interrupt",
        3: "UV_ERR interrupt",
        2: "UV_RECOVERY interrupt",
        1: "TEMP_ERR interrupt",
        0: "SLEEP_ABORT interrupt",
    }
    
    for bit, interrupt in interrupt_flags.items():
        if reg16b_val & (1 << bit):
            print(f"\tbit {bit}: R/W {interrupt} enabled")
        else:
            print(f"\tbit {bit}: R/W {interrupt} disabled")
    
    print("\n")

def parse_link_fail_counter_register(reg16b_val):
    print(f"[0x1A] Link Fail Counter Register: 0x{reg16b_val:04X}")
    loc_rcvr_cnt = (reg16b_val >> 8) & 0xFF
    print(f"\tbit 15:8 R/O [{loc_rcvr_cnt}] The counter is incremented when local receiver is NOT_OK; when the counter overflows, the value FFh is retained. The counter is reset when the register is read.")

    rem_rcvr_cnt = reg16b_val & 0xFF
    print(f"\tbit 7:0 R/O [{rem_rcvr_cnt}] The counter is incremented when remote receiver is NOT_OK; when the counter overflows, the value FFh is retained. The counter is reset when the register is read.")
    print("\n")

def parse_symbol_error_counter_register(reg16b_val):
    print(f"[0x14] Symbol Error Counter Register: 0x{reg16b_val:04X}")
    sym_err_cnt = reg16b_val
    print(f"\tbit 15-0: [{sym_err_cnt}] R/O The symbol error counter is incremented when an invalid code symbol is received (including idle symbols). The counter is incremented only once per packet, even when the received packet contains more than one symbol error. This counter increments up to 216. When the counter overflows, the value FFFFh is retained. The counter is reset when the register is read.")
    print("\n")

def parse_configuration_register_2(reg16b_val):
    print(f"[0x13] Configuration Register 2: 0x{reg16b_val:04X}")
    
    phy_addr = (reg16b_val >> 11) & 0b11111
    print(f"\tbit15..11: R/O 5-bit PHY address: [{phy_addr}]")
    
    if reg16b_val & (1 << 2):
        print(f"\tbit2: R/W packets up to 16 kB supported")
    else:
        print(f"\tbit2: R/W packets up to 4 kB supported")

    print("\n")

def parse_configuration_register_3(reg16b_val):
    print(f"[0x1C] Configuration Register 3: 0x{reg16b_val:04X}")
    
    print(f"\tbit15:2: R/W reserved")
    
    if reg16b_val & (1 << 1):
        print(f"\tbit1: R/W force PHY to Sleep mode")
    else:
        print(f"\tbit1: R/W forced sleep inactive")
    
    print(f"\tbit0: R/W write 1; ignore on read")

    print("\n")

def parse_phy_identifier_1_register(reg16b_val):
    print(f"[0x02] PHY Identifier 1 Register: 0x{reg16b_val:04X}")
    
    print(f"\tbit15..0: Organizationally Unique Identifier 0x{reg16b_val:04x}")
    print("\n")

def parse_phy_identifier_2_register(reg16b_val):
    print(f"[0x03] PHY Identifier 2 Register: 0x{reg16b_val:04X}")
    
    phy_id = (reg16b_val >> 10) & 0b111111
    print(f"\tbit15..10: phyId 0x{phy_id:02x} (19 to 24 of the OUI)")
    
    type_no = (reg16b_val >> 4) & 0b111111
    print(f"\tbit9..4: manufacturer type number 0x{type_no:02x}")
    
    rev_no = reg16b_val & 0b1111
    print(f"\tbit3..0: manufacturer revision number 0x{rev_no:02x}")
    
    print("\n")

def parse_phy_identifier_3_register(reg16b_val):
    print(f"[0x10] PHY Identifier 3 Register: 0x{reg16b_val:04X}")
    print("\tLack of detalisation in datasheet")
    print("\n")

def parse_register(reg_addr, reg_val):
    parser_functions = {
        0x00: parse_basic_control_register,
        0x01: parse_basic_status_register,
        0x02: parse_phy_identifier_1_register,
        0x03: parse_phy_identifier_2_register,
        0x0F: parse_extended_status_register,
        0x10: parse_phy_identifier_3_register,
        0x11: parse_extended_control_register,
        0x12: parse_configuration_register_1,
        0x13: parse_configuration_register_2,
        0x14: parse_symbol_error_counter_register,
        0x15: parse_interrupt_status_register,
        0x16: parse_interrupt_enable_register,
        0x17: parse_communication_status_register,
        0x18: parse_general_status_register,
        0x19: parse_external_status_register,
        0x1A: parse_link_fail_counter_register,
        0x1B: parse_common_configuration_register,
        0x1C: parse_configuration_register_3
    }

    func = parser_functions.get(reg_addr)
    if func:
        func(reg_val)

def parse_registers_file(file_content):
    for line in file_content.strip().split('\n'):
        parts = line.split()
        reg_addr = int(parts[2], 16) 
        reg_val = int(parts[5], 16) 
        parse_register(reg_addr, reg_val)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_regs.py filename")
        exit()

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            registers = parse_registers_file(file_content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")