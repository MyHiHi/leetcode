import scala.util.matching.Regex

object Test {
  def findNum(v:String,a:Array[Int]){
    print(`v`,`a`,("\\d+".r.findAllIn(`v`) ).toList)
    a.foreach(println)
  }
  abstract class Fun(val name:String){
    def sayH:String="hi"
    var age=12
  }
  class MyFun(name:String) extends Fun(name)
  class Person(val name:String,val age:Int)
  class Student( name:String, age:Int,var score:Double=1) extends Person(name,age){
    def this(name:String)=this(name,13,9);
    def this(age:Int)=this("Meo",age,0);
    def getScore():Double={
      if (this.score!=1){
        this.score*=10
      }
      this.score
    }
    def sayH:String="Hi!!"
  }
   def main(args: Array[String]) {
    //  val f=new MyFun("Leo");
    //  println(f.sayH)
    //  println(f.name)
    //  val s=new Student("Leo",12);
    //  println(s.sayH)
    //  println(s.age)
    //  println(s.getScore)

    //  val array=Array[Int](12,2,3,4,5)
    //  findNum("ssa2134ff41f5",array)
    // import math;
    println(math.abs(-123))

   }
}