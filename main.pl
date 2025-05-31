fn main() -> i32 {
    let inp: string = input();
    print(curl(inp, "GET", "", ""));
    
    print("Enter enter to exit...");
    input();

    return 0; // Success
}