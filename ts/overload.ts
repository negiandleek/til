function hoge(a: number): number;
function hoge(a: number, b: string): string
function hoge(a: number, b?: string): any{
    if(typeof a === "number"){
        return 0
    }
    if(typeof b == "string"){
        return "string"
    }
}

const a = hoge(0)
const b = hoge(0, "b")

type Fuga = {
    (a: number): number;
    (a: number, b: string): string
}

const fuga:Fuga = (a: number, b?: string): any => {
    if(typeof a === "number"){
        return 0
    }
    if(typeof b == "string"){
        return "string"
    }
}

const c = fuga(0)
const d = fuga(0, "b")
