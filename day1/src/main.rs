use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut f = File::open("input").expect("file not found");
    let mut input = String::new();
    f.read_to_string(&mut input).expect("could not read file");

    let mut prev_char = 'a';
    let mut sum = 0;
    for (i, c) in input.trim().chars().enumerate() { 
        if i > 0 {
            if c == prev_char {
                sum += c.to_digit(10).expect("weird character");
            }
        }
        prev_char = c;
    }
    if prev_char == input.chars().nth(0).unwrap(){
        sum += prev_char.to_digit(10).unwrap();
    }

    println!("Part 1: {}", sum);

    /*
     * For Part 2, split string in half, iterate simultaneously and double the result.
     */

    let length = input.len() - 1;
    let in1 = &input[..length/2];
    let in2 = &input[length/2..length];
    sum = 0;

    for (c1, c2) in in1.chars().zip(in2.chars()) {
        if c1 == c2 {
            sum += c1.to_digit(10).unwrap();
        }
    }

    println!("Part 2: {}", 2*sum);
}
