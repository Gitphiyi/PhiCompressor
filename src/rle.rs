use std::fs;

pub fn parse_text() {
    let filename = "src/text.txt";
    let content = fs::read_to_string(filename).expect("Should have been able to read the file");
    println!("With text:\n{content}");
}