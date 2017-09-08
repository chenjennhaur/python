# run as python3
import ev3dev.ev3 as ev3

# Attach large motors to ports B and C
ir = ev3.InfraredSensor()
print(ir.value())

mR = ev3.LargeMotor('outA')
mL = ev3.LargeMotor('outB')
steer = ev3.MediumMotor('outC')

# 1000 speed_sp = 100 duty_cycle_sp = power value 100
# Recommended to use between 900 to -900
# speed_sp : degrees per second, time_sp is in milliseconds
#mR.run_timed(time_sp=2000,speed_sp=-600)
#mR.run_timed(time_sp=2000,speed_sp=600)
#mL.run_timed(time_sp=2000,speed_sp=600)
# position_sp can be both positive and negative 
#steer.run_to_abs_pos(position_sp=45,speed_sp=360)
#steer.position

print(ir.value())

while(ir.value()>20):
  mR.run_forever(speed_sp=-600)
  mL.run_forever(speed_sp=-600)
      
mR.stop(stop_action='brake')
mL.stop(stop_action='brake')
