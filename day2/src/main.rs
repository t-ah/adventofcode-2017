use std::fs::File;
use std::io::prelude::*;
use std::cmp;

fn main() {
    let mut f = File::open("input").expect("file not found");
    let mut input = String::new();
    f.read_to_string(&mut input).expect("could not read file");

    let mut sum = 0;
    for line in input.lines() {
        let numbers: Vec<u32> = line.split("\t").map(|n| n.parse::<u32>().unwrap()).collect();
        let mut min = numbers[0];
        let mut max = numbers[0];
        for i in 1..numbers.len() {
            min = cmp::min(min, numbers[i]);
            max = cmp::max(max, numbers[i]);
        }
        sum += max - min;
    }

    println!("Part 1: {}", sum);

    sum = 0;

    for line in input.lines() {
        let numbers: Vec<u32> = line.split("\t").map(|n| n.parse::<u32>().unwrap()).collect();
        'out: for i in 0..numbers.len() {
            let num1 = numbers[i];
            for j in i+1..numbers.len() {
                let num2 = numbers[j];
                let min = cmp::min(num1, num2);
                let max = cmp::max(num1, num2);
                if max % min == 0 {
                    sum += max / min;
                    break 'out;
                }
            }
        }
    }

    println!("Part 2: {}", sum);
}
