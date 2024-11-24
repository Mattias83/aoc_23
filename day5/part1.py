almanac: list[str] = []


def get_maps(index: int) -> list[list[int]]:
    ranges: list[list[int]] = []
    done = False
    while not done:
        index += 1
        if index >= len(almanac):
            done = True
            break
        if almanac[index].replace(" ", "").isnumeric():
            ranges.append(
                [int(i) for i in almanac[index].split(" ") if i.isdigit()]
            )
        else:
            done = True
    return ranges


def get_destination(source: int, range_maps: list[list[int]]) -> int:
    destination: int = 0
    for range_map in range_maps:
        if source >= range_map[1] and source <= range_map[1] + range_map[2]:
            destination = source - range_map[1] + range_map[0]
            break
        else:
            destination = source
    return destination


def main() -> None:
    seeds: list[int] = [
        int(i)
        for i in almanac[0][almanac[0].find(":") + 2 :].split(" ")
        if i.isdigit()
    ]

    for index, row in enumerate(almanac):
        if row == "seed-to-soil map:":
            seed_to_soil_map = get_maps(index)
        elif row == "soil-to-fertilizer map:":
            soil_to_fertilizer_map = get_maps(index)
        elif row == "fertilizer-to-water map:":
            fertilizer_to_water_map = get_maps(index)
        elif row == "water-to-light map:":
            water_to_light_map = get_maps(index)
        elif row == "light-to-temperature map:":
            light_to_temperature_map = get_maps(index)
        elif row == "temperature-to-humidity map:":
            temperature_to_humidity_map = get_maps(index)
        elif row == "humidity-to-location map:":
            humidity_to_location_map = get_maps(index)

    lowest_location: int = 0
    for seed in seeds:
        soil = get_destination(seed, seed_to_soil_map)
        fertilizer = get_destination(soil, soil_to_fertilizer_map)
        water = get_destination(fertilizer, fertilizer_to_water_map)
        light = get_destination(water, water_to_light_map)
        temperature = get_destination(light, light_to_temperature_map)
        humidity = get_destination(temperature, temperature_to_humidity_map)
        location = get_destination(humidity, humidity_to_location_map)

        if lowest_location == 0:
            lowest_location = location

        if location <= lowest_location:
            lowest_location = location

        # print(f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}")
    print(f"Lowest location: {lowest_location}")


if __name__ == "__main__":
    real_almanac = "puzzle_input.txt"
    with open(real_almanac, "r") as puzzle_input:
        almanac = [row.strip() for row in puzzle_input]
        main()
