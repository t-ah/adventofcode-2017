use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() {
    let mut f = File::open("input").expect("file not found");
    let mut input = String::new();
    f.read_to_string(&mut input).expect("could not read file");

    let mut count = 0;
    for line in input.lines() {
        let mut map = HashMap::new();
        let mut valid = true;
        for word in line.split(" ") {
            if map.get(word).is_some() {
                valid = false;
                break;
            }
            map.insert(word, true);
        }
        if valid {
            count += 1;
        }
    }

    println!("Part 1: {}", count);

    count = 0;
    for line in input.lines() {
        let mut map = HashMap::new();
        let mut valid = true;
        for word in line.split(" ") {
            let mut chars: Vec<char> = word.chars().collect();
            chars.sort();
            let sorted: String = chars.iter().cloned().collect::<String>();
            if map.get(&sorted).is_some() {
                valid = false;
                break;
            }
            map.insert(sorted, true);
        }
        if valid {
            count += 1;
        }
    }

    println!("Part 2: {}", count);
}
