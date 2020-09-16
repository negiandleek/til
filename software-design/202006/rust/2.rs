fn main() {
    // 1
    let mut x = 1;
    x = x + 1;
    println!("-----");
    println!("{}", x);
    
    // 2
    println!("-----");
    let y = 1;
    {
        let y = y + 1;
        println!("{}", y);
    }
    println!("{}", y);
    
    // 3
    println!("-----");
    {
        let x = 10;
        let x = x + x ;
        println!("3");
        println! ("{}", x);
    }
    
    // 4
    println!("-----");
    {
        let s = "Hello".to_string();
        let t = s;
        println!("{}", t);
        println!("{}", s);
    }
}