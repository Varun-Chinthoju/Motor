from time import sleep
from machine import Pin, PWM

# PWM pin 0
pwm = PWM(Pin(0))

pwm.freq(50)


def duty_ms(p: PWM, ds_ms: float):
    p.duty_ns(int(ds_ms * 1000000))


duty_ms(pwm, 1)
sleep(1)


def end():
    pwm.duty_ns(0)
    sleep(0.1)


try:
    duty_ms(pwm, 1.3)
    # while True:
    #     # pwm.duty_ns(1100000)
    #     sleep(.1)
    sleep(7)
except KeyboardInterrupt:
    end()
finally:
    end()
