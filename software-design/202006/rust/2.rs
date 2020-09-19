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
        let mut a = 1;
        let b = a;
        a = a + a;
        let s = "Hello".to_string();
        let t = s;
        println!("{}, {}, {}", t, a, b);
    }
    
    println!("-----");
    {
        fn myPrint<T: std::fmt::Display>(msg: &T){
            println!("{}", msg);
        }
        fn exePrint(){
            let s = "Hi".to_string();
            myPrint(&s);
            myPrint(&s);
        }
        exePrint();
    }
    
    println!("-----");
    {
        fn exec(){
          const N_THREAD : usize = 3;
          let series_range = 0..30;
          let add = 1;
          
          
          let chunks = (0..N_THREAD)
            .map(|ii| series_range.clone().skip(ii).step_by(N_THREAD));
            
          let handles : Vec<_> = chunks
            .map(|vv| std::thread::spawn(move || {
                vv.for_each(|nn| print!("{},", nn + add));
            })).collect();
            
          handles.into_iter().for_each(|hh| hh.join().unwrap());
        }
        exec()
    }
}