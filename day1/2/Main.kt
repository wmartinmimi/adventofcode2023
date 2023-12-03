
fun toInt(str: String): Int? {
  try {
    println(str)
    return when {
      str[0].isDigit() -> str[0].digitToInt()
      str.slice(0..3) == "one" -> 1
      str.slice(0..3) == "two" -> 2
      str.slice(0..3) == "six" -> 6
      str.slice(0..4) == "four" -> 4
      str.slice(0..4) == "five" -> 5
      str.slice(0..4) == "nine" -> 9
      str.slice(0..5) == "three" -> 3
      str.slice(0..5) == "seven" -> 7
      str.slice(0..5) == "eight" -> 8
      else -> null
    }
  } catch (e: StringIndexOutOfBoundsException) {
    return null
  }
}

fun main() {
  var sum = 0
  for (x in 1..1000) {
    val ln = readln()
    var i = 0
    var j = ln.length - 1
    var c1: Int? = null
    var c2: Int? = null

    while (c1 == null) {
      c1 = toInt(ln.slice(i..<ln.length))
      i++
    }
    while (c2 == null) {
      c2 = toInt(ln.slice(j..<ln.length))
      j--
    }
    sum += c1 * 10 + c2
  }
  println(sum)
}
