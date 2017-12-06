use std::fs::File;
use std::io::prelude::*;

fn main() {
    let part2 = true;
    let mut f = File::open("input").expect("file not found");
    let mut input = String::new();
    f.read_to_string(&mut input).expect("could not read file");

    let mut vec: Vec<i32> = input.lines().map(|s| s.parse::<i32>().unwrap()).collect();
    let size = vec.len() as i32;
    
    let mut count: i32 = 0;
    let mut index: i32 = 0;

    loop {
        let jump = vec[index as usize];
        if part2 && jump >= 3 {
            vec[index as usize] -= 1;
        }
        else {
            vec[index as usize] += 1;
        }
        index += jump;
        count += 1;
        if index < 0 || index >= size {
            break;
        }
    }

    if part2 {
        println!("Part 2: {}", count);
    }
    else {
        println!("Part 1: {}", count);
    }
}
