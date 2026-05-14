from machine import Pin
import time

# -------- الزر الأول --------
button1 = Pin(4, Pin.IN, Pin.PULL_UP)

# LED الأحمر القديم
led1 = Pin(5, Pin.OUT)

# LED الجديد الإضافي
led_extra = Pin(22, Pin.OUT)

# -------- الزر الثاني --------
button2 = Pin(19, Pin.IN, Pin.PULL_UP)
led2 = Pin(21, Pin.OUT)

# -------- الزر الثالث --------
button3 = Pin(18, Pin.IN, Pin.PULL_UP)
led_builtin = Pin(2, Pin.OUT)

# الحالات
state1 = 0
state2 = 0
state3 = 0

last1 = 1
last2 = 1
last3 = 1

while True:

    # -------- الزر الأول --------
    c1 = button1.value()

    if last1 == 1 and c1 == 0:

        state1 = 1 - state1

        # يشغل LEDين مع بعض
        led1.value(state1)
        led_extra.value(state1)

    last1 = c1

    # -------- الزر الثاني --------
    c2 = button2.value()

    if last2 == 1 and c2 == 0:

        state2 = 1 - state2
        led2.value(state2)

    last2 = c2

    # -------- الزر الثالث --------
    c3 = button3.value()

    if last3 == 1 and c3 == 0:

        state3 = 1 - state3
        led_builtin.value(state3)

    last3 = c3

    time.sleep(0.05)
    