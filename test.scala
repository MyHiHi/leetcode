import scala.util.matching.Regex

object Test {
  def findNum(v:String,a:Array[Int]){
    print(`v`,`a`,("\\d+".r.findAllIn(`v`) ).toList)
    a.foreach(println)
  }
   def main(args: Array[String]) {
     val array=Array[Int](12,2,3,4,5)
     findNum("ssa2134ff41f5",array)
   }
}