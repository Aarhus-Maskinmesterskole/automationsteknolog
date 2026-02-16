# Opgave 4: State machine (tilstandsmaskine) for systemadfærd

## Beskrivelse
Lav en state machine der beskriver tilstande og overgange.
Fx LED-system: LED_OFF ↔ LED_ON (event: Button pushed/released).
Hvis du vil udvide: tilføj en ekstra tilstand (fx BLINKING) og en guard/counter.

## Acceptance criteria
- Minimum **2 tilstande** og **2 overgange** med tydelige labels
- Starttilstand er markeret
- Overgange har betingelser/events (fx “Button pushed”)
- Diagrammet er overskueligt og kan forklares på 1 minut

## Skabelon

**Eksempel på state machine (tekstbaseret):**

```
[LED_OFF] --(Button pushed)--> [LED_ON]
[LED_ON] --(Button released)--> [LED_OFF]
```

**Eksempel med ekstra tilstand:**
```
[LED_OFF] --(Button pushed)--> [LED_ON]
[LED_ON] --(Button pushed again)--> [BLINKING]
[BLINKING] --(Button released)--> [LED_OFF]
```

*Du kan tegne diagrammet i hånden og indsætte et billede, eller bruge et værktøj som draw.io, PowerPoint, eller mermaid (se ovenfor).* 

## Referencer
- Introduktion + eksempler på state machines (LED, blinking, RGB)
- Teknisk dokumentation: state machine som standard-element
