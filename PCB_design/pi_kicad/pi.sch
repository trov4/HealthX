EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L raspberry_pi_zero_w:ADA3708 A1
U 1 1 61800746
P 5400 3300
F 0 "A1" H 5400 4467 50  0000 C CNN
F 1 "ADA3708" H 5400 4376 50  0000 C CNN
F 2 "ADA3708_RPI-ZERO" H 5400 3300 50  0001 L BNN
F 3 "" H 5400 3300 50  0001 L BNN
F 4 "MAnufactutrer Recommendations" H 5400 3300 50  0001 L BNN "STANDARD"
F 5 "Raspberry" H 5400 3300 50  0001 L BNN "MANUFACTURER"
	1    5400 3300
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x04 J2
U 1 1 6180A98B
P 3200 3200
F 0 "J2" H 3118 3517 50  0001 C CNN
F 1 "Conn_01x04" H 3118 3425 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 3200 3200 50  0001 C CNN
F 3 "~" H 3200 3200 50  0001 C CNN
	1    3200 3200
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x05 J1
U 1 1 6180C379
P 3200 2400
F 0 "J1" H 3118 2817 50  0001 C CNN
F 1 "Conn_01x05" H 3118 2725 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 3200 2400 50  0001 C CNN
F 3 "~" H 3200 2400 50  0001 C CNN
	1    3200 2400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3400 2200 6500 2200
Wire Wire Line
	6500 2200 6500 2600
Wire Wire Line
	6500 2600 6300 2600
Wire Wire Line
	3400 2300 4500 2300
Wire Wire Line
	4500 2300 4500 2400
Wire Wire Line
	3400 2400 4000 2400
Wire Wire Line
	4400 2400 4400 2500
Wire Wire Line
	4400 2500 4500 2500
Wire Wire Line
	3400 2500 3800 2500
Wire Wire Line
	4300 2500 4300 2600
Wire Wire Line
	4300 2600 4500 2600
Wire Wire Line
	3400 2600 4200 2600
Wire Wire Line
	4200 2600 4200 2700
Wire Wire Line
	4200 2700 4500 2700
Wire Wire Line
	3400 3400 3700 3400
Wire Wire Line
	3700 3400 3700 4300
Wire Wire Line
	3700 4300 4500 4300
Wire Wire Line
	4400 3300 4400 3200
Wire Wire Line
	4400 3200 4500 3200
Wire Wire Line
	3400 3300 4400 3300
Wire Wire Line
	3400 3200 3800 3200
Wire Wire Line
	3800 3200 3800 2500
Connection ~ 3800 2500
Wire Wire Line
	3800 2500 4300 2500
Wire Wire Line
	3400 3100 4000 3100
Wire Wire Line
	4000 3100 4000 2400
Connection ~ 4000 2400
Wire Wire Line
	4000 2400 4400 2400
$EndSCHEMATC
