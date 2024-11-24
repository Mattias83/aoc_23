# runs pretty slow, need to think of something else
race_time: int = 56717999
distance_to_beat: int = 334113513502430

distance_broken_counter: int = 0
for pressed_button_time in range(0, race_time + 1):
    if (
        race_time - pressed_button_time
    ) * pressed_button_time > distance_to_beat:
        distance_broken_counter += 1

print(f"result: {distance_broken_counter}")
