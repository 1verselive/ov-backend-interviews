/*
Write 3 classes - Derived class, base_1 class, and base_2 class. 
The derived class should inherit base_1 and base_2 classes.
Any derived class object created should be initiated with 2 variables - a,b.
Any base_1 class object created should be initiated with variable a and base_2 class object should be initiated with variable b.
On creating a base_1 class object, a new variable c should be attributed to the object with the value 5*a.
On creating a base_2 class object, a new variable d should be attributed to the object with the value 10*b.
Write a python program to create a derived class object with a=2,b=3 and print the 2 new variables (c,d) created.

i used this link, for getting output, here, i used the mixin concept because, js not supporting to multiple inheritance.

https://javascript.info/mixins
*/

class base_1{
    constructor(a){
        this.a=5*a;
    }
}
const obj_base_1=new base_1(2);
class base_2{
    constructor(b){
        this.b=10*b;
    }
}
const obj_base_2=new base_2(3);

class derived extends base_1{
    constructor(a){
        super(a);
        // console.log(this.a)
    }
}



Object.assign(derived.prototype, obj_base_2);
const obj_derived=new derived(2);
console.log(obj_derived.a)
console.log(obj_derived.b)


