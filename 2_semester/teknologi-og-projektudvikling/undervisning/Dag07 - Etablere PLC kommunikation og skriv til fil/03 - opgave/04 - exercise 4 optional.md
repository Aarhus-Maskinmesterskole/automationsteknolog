# 04 - exercise 4 (optional)
I denne opgave skal du lave en PI controller for tankniveauet i emulate3d. Du skal logge og tidsstemple tankniveauet i en csv fil over en passende tidsperiode. Du skal bruge en Source, Tank, pipes og pumpe i emulate3d.

Husk fra regulering at en PI controller består af to dele: en proportional del (P) og en integrerende del (I). Den proportionale del reagerer på den aktuelle fejl (forskellen mellem setpoint og aktuelt niveau), mens den integrerende del reagerer på den akkumulerede fejl over tid.

En ren P regulator kan laves som:

```python
error = setpoint - current_level
control_signal = Kp * error
```
En ren I regulator kan laves som:

```python
integral = integral + error * dt
control_signal = Ki * integral
```
For at lave en PI controller, skal du kombinere begge dele:

```python
error = setpoint - current_level
integral = integral + error * dt
control_signal = Kp * error + Ki * integral
```

Når opgaven er færdig så kan du prøve at lave en graf i excel.