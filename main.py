def ShowData():
    OLED.write_string_new_line("Temperature=")
    OLED.write_num_new_line(Math.round(Temp))
    OLED.write_string_new_line("Humidity=")
    OLED.write_num_new_line(Math.round(humidity))
    basic.pause(3000)
    OLED.clear()
def GetTempHumidity():
    global humidity, Temp
    dht11_dht22.query_data(DHTtype.DHT22, DigitalPin.P0, True, False, True)
    if dht11_dht22.read_data_successful():
        basic.pause(1000)
        humidity = dht11_dht22.read_data(dataType.HUMIDITY)
        basic.pause(2000)
        Temp = dht11_dht22.read_data(dataType.TEMPERATURE) * (9 / 5) + 32
        basic.pause(1000)
def ControlFans():
    if Temp > TempHigh or humidity > HumidHigh:
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.show_icon(IconNames.SAD)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
        basic.show_icon(IconNames.HAPPY)
def Variables():
    global TempHigh, HumidHigh, H20TempHigh
    TempHigh = 75
    HumidHigh = 30
    H20TempHigh = 65
H20TempHigh = 0
HumidHigh = 0
TempHigh = 0
humidity = 0
Temp = 0
basic.pause(100)
OLED.init(128, 64)
OLED.write_string_new_line("starting program...")

def on_forever():
    Variables()
    GetTempHumidity()
    ControlFans()
    ShowData()
basic.forever(on_forever)
