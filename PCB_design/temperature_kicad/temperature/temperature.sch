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
L Connector_Generic:Conn_01x04 J1
U 1 1 6180265B
P 4500 3800
F 0 "J1" H 4418 4117 50  0001 C CNN
F 1 "Conn_01x04" H 4418 4025 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 4500 3800 50  0001 C CNN
F 3 "~" H 4500 3800 50  0001 C CNN
	1    4500 3800
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J2
U 1 1 61801C7D
P 6900 3700
F 0 "J2" H 6980 3646 50  0001 L CNN
F 1 "Conn_01x02" H 6980 3646 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 6900 3700 50  0001 C CNN
F 3 "~" H 6900 3700 50  0001 C CNN
	1    6900 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6300 3400 4800 3400
Wire Wire Line
	4800 3400 4800 3700
Wire Wire Line
	4800 3700 4700 3700
Wire Wire Line
	6300 3800 6700 3800
Wire Wire Line
	6300 3900 6600 3900
Wire Wire Line
	6600 3900 6600 3700
Wire Wire Line
	6600 3700 6700 3700
Wire Wire Line
	6300 4200 4800 4200
Wire Wire Line
	4800 3800 4700 3800
Wire Wire Line
	6300 3800 6300 3700
Wire Wire Line
	6300 3700 6300 3400
Wire Wire Line
	6300 3900 6300 4000
Wire Wire Line
	6300 4200 6300 4000
Connection ~ 6300 3700
Connection ~ 6300 4000
Wire Wire Line
	4800 4200 4800 3800
$Comp
L MLX90614ESF-BAA-000-TU:MLX90614ESF-BAA-000-TU U1
U 1 1 61806FA1
P 5700 3800
F 0 "U1" H 5700 4167 50  0001 C CNN
F 1 "MLX90614" H 5700 4075 50  0000 C CNN
F 2 "MLX90614ESF-BAA-000-TU:TO254P942H425-4" H 5700 3800 50  0001 L BNN
F 3 "" H 5700 3800 50  0001 L BNN
F 4 "Melexis" H 5700 3800 50  0001 L BNN "MANUFACTURER"
F 5 "4.25 mm" H 5700 3800 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
F 6 "IPC 7351B" H 5700 3800 50  0001 L BNN "STANDARD"
F 7 "13" H 5700 3800 50  0001 L BNN "PARTREV"
	1    5700 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	5100 3900 5100 4000
Wire Wire Line
	5100 3800 4900 3800
Wire Wire Line
	4900 3800 4900 4000
Wire Wire Line
	4900 4000 4700 4000
Wire Wire Line
	5100 4000 5000 4000
Wire Wire Line
	5000 4000 5000 3900
Wire Wire Line
	5000 3900 4700 3900
Connection ~ 6700 3800
Wire Wire Line
	6700 3800 6800 3800
$EndSCHEMATC
