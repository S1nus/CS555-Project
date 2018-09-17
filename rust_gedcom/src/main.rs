use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::io::BufReader;
use std::io::BufRead;
use std::io::BufWriter;
use std::io::Write;
use std::io;

fn main() {

    let path = Path::new("../Family-2-17-Sep-2018-565.ged");
    let display = path.display();

    let f = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why.description()), 
        Ok(file) => file,
    };
    let file = BufReader::new(&f);
    let mut writer = BufWriter::new(io::stdout());

    for (num, line) in file.lines().enumerate() {
        let l = line.unwrap();
        writer.write((&l[1..]).as_bytes()).unwrap();
        writer.write(b"\n").unwrap();
    }

}

