
fun main() {
  var sum = 0
  for (x in 1..1000) {
    val ln = readln()
    var i = 0
    var j = ln.length - 1
    var c1: Int? = null
    var c2: Int? = null

    while (c1 == null) {
      c1 = ln[i].digitToIntOrNull()
      i++
    }
    while (c2 == null) {
      c2 = ln[j].digitToIntOrNull()
      j--
    }
    sum += c1 * 10 + c2
  }
  println(sum)
}
