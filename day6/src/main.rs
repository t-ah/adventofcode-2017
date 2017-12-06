use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() {
    println!("AoC Day 6");
    let mut f = File::open("input").expect("file not found");
    let mut input = String::new();
    f.read_to_string(&mut input).expect("could not read file");

    let mut mem: Vec<usize> = input.split_whitespace().map(|s| s.parse::<usize>().unwrap()).collect();
    let mut map: HashMap<String,bool> = HashMap::new();
    let len = mem.len();
    let mut count = 0;
    let mut count2 = 0;
    let mut done = false;
    let mut master_key = String::new();

    loop {
        if !done {
            count += 1;
        }
        else {
            count2 += 1;
        }
        let mut max = 0;
        let mut max_index = 0;
        for (i,n) in mem.iter().enumerate(){
            if *n > max {
                max = *n;
                max_index = i;
            }
        }
        mem[max_index] = 0;
        for i in max_index+1..max_index+1+max {
            mem[i%len] += 1;
        }
        let key_vec : Vec<String> = mem.iter().map(|i| i.to_string()).collect();
        let key = key_vec.join("");
        if !done {
            if map.contains_key(&key) {
                done = true;
                master_key = key.to_owned();
            }
            else {
                map.insert(key, true);
            }
        }
        else {
            if *key == master_key {
                break;
            }
        }
    }

    println!("Part 1: {}", count);
    println!("Part 2: {}", count2);
}
