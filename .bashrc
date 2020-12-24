# For Advent of Code:
AOC_SESSION=''
aoc() {
    local day="$1"
    curl --cookie "session=${AOC_SESSION}" "https://adventofcode.com/2020/day/${day}/input"
}
