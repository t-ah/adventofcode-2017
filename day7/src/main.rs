extern crate regex;

use std::fs::File;
use std::io::prelude::*;
use regex::Regex;
use std::collections::HashSet;
use std::collections::HashMap;

fn main() {
    let mut f = File::open("input").expect("file not found");
    let mut input = String::new();
    f.read_to_string(&mut input).expect("could not read file");

    let re = Regex::new(r"(?P<name>[a-z]+) \((?P<weight>\d+)\)(?: -> (?P<progs>.+))?").unwrap();
    let mut progs = HashSet::new();
    let mut held_progs = HashSet::new();
    let mut tree : HashMap<&str,Vec<&str>> = HashMap::new();
    let mut weights = HashMap::new();
    
    for line in input.lines() {
        let caps = re.captures(line).unwrap();
        let name = caps.name("name").unwrap().as_str();
        progs.insert(name);
        weights.insert(name, caps.name("weight").unwrap().as_str().parse::<i32>().unwrap());
        let mut children = Vec::new();
        match caps.name("progs") {
            Some(h_progs) => {
                for h_prog in h_progs.as_str().split(", ") {
                    held_progs.insert(h_prog);
                    // part 2:
                    children.push(h_prog);
                }
            },
            None => {}
        }
        tree.insert(name, children);
    }

    for h_prog in held_progs {
        progs.remove(h_prog);
    }

    let mut root : &str = "";
    for prog in progs {
        root = prog;
    }
    println!("Part 1: {}", root);

    let mut carrying : HashMap<String, i32> = HashMap::new();
    let root_weight = rec_weight(root, &mut tree, &mut weights, &mut carrying);
    carrying.insert(root.to_owned(), root_weight);

    check_children(root, &mut tree, &mut carrying, &mut weights);
}

fn rec_weight(node_name : &str, tree : &HashMap<&str, Vec<&str>>, weights : &HashMap<&str,i32>, 
                carrying : &mut HashMap<String, i32>) -> i32 {
    let mut weight = *weights.get(&node_name).unwrap();
    let children = tree.get(node_name);
    if children.is_some() {
        for child in children.unwrap() {
            weight += rec_weight(child, tree, weights, carrying);
        }
    }
    carrying.insert(node_name.to_owned(), weight);
    weight
}

fn check_children(node_name: &str, tree : &HashMap<&str, Vec<&str>>, carrying : &HashMap<String,i32>,
                    weights : &HashMap<&str,i32>) {
    let children = tree.get(node_name);
    if children.is_some(){
        let mut vec = children.unwrap();
        let mut last_weight : i32 = 0;
        loop {
            if vec.len() > 1 {
                let w0 = carrying.get(vec[0]).unwrap();
                let mut index = 0;
                let mut different = false;
                for i in 1..vec.len() {
                    let wi = carrying.get(vec[i]).unwrap();
                    if w0 != wi {
                        last_weight = *weights.get(vec[i]).unwrap() + w0 - wi; // memorize own weight plus difference
                        different = true;
                        if index > 0 { // second entry differs from 0th -> 0th must be different from others
                            last_weight = *weights.get(vec[0]).unwrap() + wi - w0;
                            index = 0;
                            break;
                        }
                        else {
                            index = i;
                        }
                    }
                }
                if different {
                    vec = tree.get(vec[index]).unwrap();
                }
                else {
                    println!("Part 2: {}", last_weight);
                    break;
                }
            }
        }
    }
}

