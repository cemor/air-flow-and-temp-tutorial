function ShowData () {
    OLED.writeStringNewLine("Temperature=")
    OLED.writeNumNewLine(Math.round(Temp))
    OLED.writeStringNewLine("Humidity=")
    OLED.writeNumNewLine(Math.round(humidity))
    basic.pause(3000)
    OLED.clear()
}
function GetTempHumidity () {
    dht11_dht22.queryData(
    DHTtype.DHT22,
    DigitalPin.P0,
    true,
    false,
    true
    )
    if (dht11_dht22.readDataSuccessful()) {
        basic.pause(1000)
        humidity = dht11_dht22.readData(dataType.humidity)
        basic.pause(2000)
        Temp = dht11_dht22.readData(dataType.temperature) * (9 / 5) + 32
        basic.pause(1000)
    }
}
function ControlFans () {
    if (Temp > TempHigh || humidity > HumidHigh) {
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.showIcon(IconNames.Sad)
    } else {
        pins.digitalWritePin(DigitalPin.P1, 0)
        basic.showIcon(IconNames.Happy)
    }
}
function Variables () {
    TempHigh = 75
    HumidHigh = 30
    H20TempHigh = 65
}
let H20TempHigh = 0
let HumidHigh = 0
let TempHigh = 0
let humidity = 0
let Temp = 0
basic.pause(100)
OLED.init(128, 64)
OLED.writeStringNewLine("starting program...")
basic.forever(function () {
    Variables()
    GetTempHumidity()
    ControlFans()
    ShowData()
})
