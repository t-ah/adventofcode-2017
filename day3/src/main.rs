use std::collections::HashMap;

fn main() {
    // calculate "ring" (x distance) and position on the outermost edge (y distance)
    let input = 265149;
    let mut ring = 1;
    let mut size = 1;
    
    while size < input {
        size += ring * 8;
        ring += 1;
    }

    let length = (2 * ring) - 1;

    // get position on the outermost ring
    let complete_rings = size - ((ring - 1) * 8);
    let pos = (input - complete_rings) % (length - 1);
    let dist_mid: i32 = pos - length / 2;
    let result = ring - 1 + dist_mid.abs();

    println!("Part 1: {}", result);

    // Quick & Dirty Part 2 pls don't judge me it's late

    let mut map: HashMap<(i32,i32),i32> = HashMap::new();

    map.insert((0,0), 1);

    let mut x = 0;
    let mut y = 0;
    let mut edge_length = 2;

    loop {
        x += 1;
        y += 1;
        for _ in 0..edge_length {
            y -= 1;
            let sum = get_sum(&mut map, x, y, input);
            map.insert((x,y), sum);
        }
        for _ in 0..edge_length {
            x -= 1;
            let sum = get_sum(&mut map, x, y, input);
            map.insert((x,y), sum);
        }
        for _ in 0..edge_length {
            y += 1;
            let sum = get_sum(&mut map, x, y, input);
            map.insert((x,y), sum);
        }
        for _ in 0..edge_length {
            x += 1;
            let sum = get_sum(&mut map, x, y, input);
            map.insert((x,y), sum);
        }

        edge_length += 2;
    }
}

fn get_sum(map: &HashMap<(i32,i32),i32>, x: i32, y: i32, input: i32) -> i32 {
    let mut sum = 0;
    for t in [(x+1,y), (x,y+1), (x+1,y+1), (x-1,y+1), (x+1,y-1), (x,y-1), (x-1,y), (x-1,y-1)].iter() {
        match map.get(t) {
            Some(i) => sum += i,
            None => {}
        }
    }
    if sum > input {
        println!("Part 2: {}", sum);
        std::process::exit(0);
    }
    return sum;
}