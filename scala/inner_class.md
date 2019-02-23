```scala
class Tree{
  class Node{
    var nodeList: List[Node] = Nil;
    def connectTo(item: Node) = {
      if(nodeList.find(it => it == item).isEmpty){
        nodeList = item::nodeList;
      }
    }
  };
  var nodes: List[Node] = Nil;
  def newNode(): Node = {
    val item = new Node;
    nodes = item::nodes;
    item
  }
}


val tree: Tree = new Tree;
val a: tree.Node = tree.newNode();
val b: tree.Node = tree.newNode();
val c: tree.Node = tree.newNode();
a.connectTo(b);
a.connectTo(b);
val tree2: Tree = new Tree;
val d: tree2.Node = tree2.newNode();
// a.connetTo(d); //error
// val d: tree2.Node = tree.newNode(); //error
```
