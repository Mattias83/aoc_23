if __name__ == "__main__":

    def calc_distance(race_time: int, button_time: int) -> int:
        return (race_time - button_time) * button_time

    with open("puzzle_input.txt", "r") as puzzle_input:
        PUZZLE_INPUT = [row.strip() for row in puzzle_input]

        times = [
            int(i)
            for i in PUZZLE_INPUT[0][PUZZLE_INPUT[0].find(":") :].split(" ")
            if i.isdigit()
        ]
        distances = [
            int(i)
            for i in PUZZLE_INPUT[1][PUZZLE_INPUT[1].find(":") :].split(" ")
            if i.isdigit()
        ]

        number_of_ways_you_can_beat_record = []

        for index, time in enumerate(times):
            print(f"Race time: {time}, current record: {distances[index]}")
            record_beat = 0
            for button_time in range(0, time + 1):
                distance_to_beat = distances[index]
                if calc_distance(time, button_time) > distance_to_beat:
                    record_beat += 1
            number_of_ways_you_can_beat_record.append(record_beat)
            record_beat = 0
        print(number_of_ways_you_can_beat_record)
        result = 1
        for val in number_of_ways_you_can_beat_record:
            result *= val
        print(f"result: {result}")
