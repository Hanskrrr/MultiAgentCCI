# Rectifier 逐样本追踪报告

## 汇总指标

- **xMatch (%)**: 15.0
- **BLEU-4**: 0.4914
- **GLEU**: 0.5371
- **Meteor**: 0.6919
- **SARI**: 0.629
- **Samples_Evaluated**: 100

## 汇总一览（按 SARI 升序，最差排前）

| # | ID | 检测到 | xMatch | BLEU-4 | SARI | METEOR | 原注释(前60) | 生成(前60) |
|---|---|---|---|---|---|---|---|---|
| 1 | `Summary_4` | ✓ |  | 0.152 | 0.106 | 0.412 | Create an instance based on current maven profile (as define | Create an instance based on MongoAssertions configuration. |
| 2 | `Summary_192` | ✓ |  | 0.165 | 0.125 | 0.493 | Returns an error, because querys could't add new records to  | Throws an error, because querys could't add new records to t |
| 3 | `Summary_92` | ✓ |  | 0.053 | 0.186 | 0.208 | Get the parent cuboid really on the spanning tree. | Get the best match cuboid. |
| 4 | `Summary_94` | ✓ |  | 0.007 | 0.192 | 0.119 | String representation of the signature. | String format of the signature. |
| 5 | `Summary_204` | ✓ |  | 0.500 | 0.222 | 0.885 | Returns the encoding used to send and receive lines from the | Returns the Charset used to send and receive lines from the  |
| 6 | `Summary_44` | ✓ |  | 0.418 | 0.269 | 0.668 | The  #add(Object...) method uses Java variable-length argume | The addSingleCol(Object value) method uses an Object array t |
| 7 | `Summary_110` | ✓ |  | 0.145 | 0.273 | 0.370 | Return XML schema for the specified type, suitable for inser | Return null for the specified type, unsuitable for insertion |
| 8 | `Summary_146` | ✓ |  | 0.736 | 0.296 | 0.944 | Converts a value from its logical format (BigDecimal) to its | Delegates the conversion of a value from its logical format  |
| 9 | `Summary_75` | ✓ |  | 0.045 | 0.314 | 0.408 | Loads the  JBossWebSocketHandler using reflection as it impo | Instantiates the JBossWebSocketHandler as it imports contain |
| 10 | `Summary_40` | ✗(漏检) |  | 0.013 | 0.345 | 0.041 | Determines if a specified set of columns from a specified re | Determines if a specified set of columns from a specified re |
| 11 | `Summary_100` | ✓ |  | 0.019 | 0.348 | 0.054 | Get entry data, read directly from internal data structure. | Get entry data, read directly from internal data structure. |
| 12 | `Summary_150` | ✓ |  | 0.573 | 0.351 | 0.822 | Returns the providers that have at least one common ISO 3166 | Returns the providers that have at least one common ISO 3166 |
| 13 | `Summary_69` | ✗(漏检) |  | 0.025 | 0.361 | 0.182 | Ensure that correct implementation is used for the component | Ensure that correct implementation is used for the component |
| 14 | `Summary_156` | ✓ |  | 0.022 | 0.365 | 0.198 | Gets sentry role objects for a given groupName from the pers | Gets sentry role objects for given groups from the persisten |
| 15 | `Summary_8` | ✓ |  | 0.428 | 0.382 | 0.669 | Provides a list containing four set, each containing project | Provides a SubProjectData object to be displayed on the proj |
| 16 | `Summary_73` | ✓ |  | 0.137 | 0.383 | 0.618 | Encodes a value in a canonical serialized string format, for | Encodes a value in a canonical serialized string format. |
| 17 | `Summary_67` | ✓ |  | 0.772 | 0.395 | 0.883 | If a Schema contains a reference to an other Schema with '$r | If a Schema contains a reference to an other Schema with '$r |
| 18 | `Summary_12` | ✓ |  | 0.019 | 0.396 | 0.144 | Only the views are mirrored. | The views are mirrored. |
| 19 | `Summary_52` | ✓ |  | 0.047 | 0.399 | 0.241 | Create a CoreMap representing a sentence from this protocol  | Create a CoreMap representing a word from this protocol buff |
| 20 | `Summary_142` | ✓ |  | 0.455 | 0.411 | 0.605 | All Paths are 'tagged' in swagger with the final entity type | All Paths are 'tagged' in swagger with a name. |
| 21 | `Summary_54` | ✓ |  | 0.031 | 0.411 | 0.236 | Checks if a flag is set. | Checks if a flag mask is set. |
| 22 | `Summary_122` | ✓ |  | 0.045 | 0.433 | 0.734 | Return a String to recreate the GRANTs given for the passed  | Return a Collection<TableGrant> of the GRANTs given for the  |
| 23 | `Summary_24` | ✓ |  | 0.566 | 0.444 | 0.671 | Check if the Elasticsearch  Node is connected and that the c | Check if the Elasticsearch Node is connected, deflector is u |
| 24 | `Summary_144` | ✓ |  | 0.167 | 0.445 | 0.226 | Gets the element for the method corresponding to this invoca | Gets the element for this expression. |
| 25 | `Summary_30` | ✓ |  | 0.036 | 0.449 | 0.335 | Checks if a flag is set. | Checks if any flag is set. |
| 26 | `Summary_0` | ✓ |  | 0.049 | 0.450 | 0.086 | Creates elastic node as single member of a cluster. | Creates elastic node. |
| 27 | `Summary_81` | ✗(漏检) |  | 0.154 | 0.472 | 0.820 | Installs a list of  RemotePackage and their dependent packag | Installs a list of  RemotePackage and their dependent packag |
| 28 | `Summary_104` | ✗(漏检) |  | 0.077 | 0.474 | 0.536 | Creates a renderscript allocation from a bitmap | Creates a renderscript allocation from a bitmap |
| 29 | `Summary_65` | ✓ |  | 0.490 | 0.477 | 0.749 | Returns all currently displayed sentences in plain text form | Returns all currently displayed sentences in plain text buff |
| 30 | `Summary_194` | ✗(漏检) |  | 0.042 | 0.493 | 0.310 | Checks if toolitem is selected | Checks if toolitem is selected |
| 31 | `Summary_199` | ✓ |  | 0.792 | 0.522 | 0.927 | Convert an object that may or may not be a JSONArray or JSON | Convert an object that may or may not be a JSON type into it |
| 32 | `Summary_164` | ✓ |  | 0.398 | 0.527 | 0.736 | Invoke the proprietary  CometSupport | Invoke the proprietary  CometSupport |
| 33 | `Summary_160` | ✓ |  | 0.336 | 0.531 | 0.607 | Returns collection containing all existing Simons matching t | Returns collection containing all existing Simons matching t |
| 34 | `Summary_16` | ✓ |  | 0.355 | 0.542 | 0.589 | Create a web page using the given template,  SecurityContext | Create a web page using the given template, SecurityContext. |
| 35 | `Summary_132` | ✓ |  | 0.470 | 0.551 | 0.656 | prepares an url-encoded HTTP queryString containing the grou | prepares an array of name-value pairs containing the group/j |
| 36 | `Summary_172` | ✗(漏检) |  | 0.227 | 0.554 | 0.872 | Helper method to return the constant string for a  CstInsn i | Helper method to return the constant string for a  CstInsn i |
| 37 | `Summary_106` | ✗(漏检) |  | 0.527 | 0.565 | 0.838 | Returns the sibling on the right of the end of given  Treepa | Returns the sibling on the right of the end of given  Treepa |
| 38 | `Summary_58` | ✗(漏检) |  | 0.570 | 0.575 | 0.831 | Creates and returns a new comparison object for the SQL "in" | Creates and returns a new comparison object for the SQL "in" |
| 39 | `Summary_79` | ✗(漏检) |  | 0.551 | 0.583 | 0.829 | Does this time interval contain the specified time interval  | Does this time interval contain the specified time interval  |
| 40 | `Summary_182` | ✗(漏检) |  | 0.534 | 0.585 | 0.802 | Tests if the editor is in word-wrap mode. | Tests if the editor is in word-wrap mode. |
| 41 | `Summary_178` | ✓ |  | 0.437 | 0.586 | 0.642 | Create and return a new Field instance that that is a copy o | Create and return a new Field instance that that is a copy o |
| 42 | `Summary_112` | ✓ |  | 0.515 | 0.596 | 0.721 | Looks up a field with a given name and if found returns its  | Looks up a field with a given name and if found returns the  |
| 43 | `Summary_170` | ✓ |  | 0.379 | 0.598 | 0.602 | Given a URL, attempt to infer and return the hostname from t | Given a URL, attempt to infer and return the host from the U |
| 44 | `Summary_176` | ✓ |  | 0.366 | 0.603 | 0.913 | Gets an integer value of the request method. | Gets a Method of the request method. |
| 45 | `Summary_61` | ✓ |  | 0.588 | 0.613 | 0.886 | Returns all currently displayed sentences in string buffer,  | Returns all currently displayed sentences in string, plain t |
| 46 | `Summary_85` | ✗(漏检) |  | 0.706 | 0.616 | 0.791 | Gets the total number of bytes uploaded by this uploader or  | Gets the total number of bytes uploaded by this uploader or  |
| 47 | `Summary_77` | ✓ |  | 0.437 | 0.616 | 0.542 | Returns the common base directory between a current base dir | Returns the common base directory between two files. |
| 48 | `Summary_36` | ✗(漏检) |  | 0.701 | 0.619 | 0.907 | Method that get's left and right incoming batch and produce  | Method that get's left and right incoming batch and produce  |
| 49 | `Summary_89` | ✗(漏检) |  | 0.791 | 0.628 | 0.921 | Create and return a new feature service with the default ser | Create and return a new feature service with the default ser |
| 50 | `Summary_46` | ✗(漏检) |  | 0.680 | 0.636 | 0.844 | Returns if this query should buffer before emitting results. | Returns if this query should buffer before emitting results. |
| 51 | `Summary_166` | ✗(漏检) |  | 0.837 | 0.637 | 0.936 | Returns the ScopeContext for the MODULE scope that will be a | Returns the ScopeContext for the MODULE scope that will be a |
| 52 | `Summary_20` | ✓ |  | 0.513 | 0.642 | 0.769 | Add a tag to the set of filters | Add a tag ID to the set of filters |
| 53 | `Summary_18` | ✗(漏检) |  | 0.208 | 0.642 | 0.432 | Return XML schema for the specified type, suitable for inser | Return XML schema for the specified type, suitable for inser |
| 54 | `Summary_184` | ✗(漏检) |  | 0.821 | 0.656 | 0.889 | If a ApiResponse contains a reference to an other ApiRespons | If a ApiResponse contains a reference to an other ApiRespons |
| 55 | `Summary_168` | ✗(漏检) |  | 0.613 | 0.661 | 0.710 | Expects principal of the format primary/instance@REALM. | Expects principal of the format primary/instance@REALM. |
| 56 | `Summary_26` | ✓ |  | 0.705 | 0.667 | 0.861 | Returns true if, the lockClient is keeping the lock for the  | Returns true if, the serverName is keeping the lock for the  |
| 57 | `Summary_63` | ✓ |  | 0.000 | 0.667 | 0.000 | DOCUMENT ME! | Handles HTML. |
| 58 | `Summary_71` | ✓ |  | 0.809 | 0.667 | 0.927 | Return the GraphItem representing the second (target) node i | Return the Node representing the second (target) node in the |
| 59 | `Summary_140` | ✓ |  | 0.035 | 0.667 | 0.154 | Allocate a bitmap with the specified width and height. | Allocate a bitmap. |
| 60 | `Summary_162` | ✓ |  | 0.783 | 0.667 | 0.927 | Looks up a specific revision based on some SCM-specific set  | Looks up a specific thing based on some SCM-specific set of  |
| 61 | `Summary_201` | ✓ |  | 0.753 | 0.667 | 0.871 | Parse a signature, with or without classname, with or withou | Parse a memberID, with or without classname, with or without |
| 62 | `Summary_174` | ✗(漏检) |  | 0.634 | 0.673 | 0.976 | Does this time interval contain or equal the specified time  | Does this time interval contain or equal the specified time  |
| 63 | `Summary_158` | ✓ |  | 0.595 | 0.674 | 0.865 | Create DrillFileSystem for given proxyUserName, configuratio | Create DrillFileSystem for given proxyUserName, configuratio |
| 64 | `Summary_188` | ✗(漏检) |  | 0.632 | 0.675 | 0.962 | Removes a converter from the set of converters, by index. | Removes a converter from the set of converters, by index. |
| 65 | `Summary_116` | ✓ |  | 0.000 | 0.682 | 0.133 | DOCUMENT ME! | The image sources |
| 66 | `Summary_138` | ✓ |  | 0.044 | 0.682 | 0.318 | DOCUMENT ME! | Returns all link HREFs. |
| 67 | `Summary_56` | ✗(漏检) |  | 0.661 | 0.683 | 0.882 | Parses a Specification out of the query string. | Parses a Specification out of the query string. |
| 68 | `Summary_126` | ✓ |  | 0.485 | 0.685 | 0.636 | Make fully qualified URI based on the default file system Sc | Make fully qualified URI or null based on the default file s |
| 69 | `Summary_136` | ✓ |  | 0.080 | 0.688 | 0.469 | DOCUMENT ME! | Generates a ParseException. |
| 70 | `Summary_6` | ✓ |  | 0.114 | 0.714 | 0.457 | Returns | Returns the sink file. |
| 71 | `Summary_180` | ✓ |  | 0.081 | 0.714 | 0.256 | DOCUMENT ME! | The end column |
| 72 | `Summary_186` | ✓ |  | 0.890 | 0.714 | 0.960 | Try to get the primary  java.net.InetAddress of the primary  | Try to get the primary  java.net.InetAddress of the primary  |
| 73 | `Summary_48` | ✗(漏检) |  | 0.814 | 0.716 | 0.989 | Adds a menu item to the bar containing SafeHtml, that will f | Adds a menu item to the bar containing SafeHtml, that will f |
| 74 | `Summary_108` | ✗(漏检) |  | 0.884 | 0.729 | 0.934 | Evaluate a PLAIN login challenge, returning the a result str | Evaluate a PLAIN login challenge, returning the a result str |
| 75 | `Summary_134` | ✓ |  | 0.092 | 0.751 | 0.362 | DOCUMENT ME! | Returns the tree authoring path. |
| 76 | `Summary_128` | ✓ |  | 0.132 | 0.759 | 0.636 | Returns | Returns the roll cycle. |
| 77 | `Summary_114` | ✓ |  | 0.669 | 0.777 | 0.904 | Converts the given object into a JSON AST. | Converts the given object into a JSON string. |
| 78 | `Summary_98` | ✓ |  | 0.212 | 0.798 | 0.551 | DOCUMENT ME! | Returns the replication directory. |
| 79 | `Summary_14` | ✓ |  | 0.403 | 0.803 | 0.755 | Build a Ravioli client | Build a Lob |
| 80 | `Summary_102` | ✓ |  | 0.266 | 0.803 | 0.968 | DOCUMENT ME! | Gets the backup directory. |
| 81 | `Summary_190` | ✓ |  | 0.266 | 0.803 | 0.718 | DOCUMENT ME! | Returns the RCML directory. |
| 82 | `Summary_2` | ✓ |  | 0.795 | 0.870 | 0.898 | Marshal the aggregator values of to a JSONArray that will la | Marshal the aggregator values of to a byte array that will l |
| 83 | `Summary_42` | ✓ | ✓ | 1.000 | 0.958 | 0.998 | Expr : left.endsWith(right) (ignore case) | Expr : left.endsWith(right) |
| 84 | `Summary_10` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Returns the providers that are bound to the same location as | Returns the providers that are bound to the same location as |
| 85 | `Summary_22` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Return the list of module prefixes that are defined for this | Return the list of module prefixes that are defined for this |
| 86 | `Summary_28` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Unsubscribes the resource from this channel, if it exists. | Unsubscribes the resource from this repo, if it exists. |
| 87 | `Summary_32` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | Create an IType for an IASTName. | Create an IType for an IASTDeclarator. |
| 88 | `Summary_34` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Returns a List containing all the child nodes of this node. | Returns a Vector containing all the child nodes of this node |
| 89 | `Summary_38` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | This method initializes jTextArea | This method initializes ZapTextArea |
| 90 | `Summary_50` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | Get the specific column's ContextColumn object. | Get the specific column's ColumnDescriptor object. |
| 91 | `Summary_83` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Get the global configuration table name including the correc | Get the global configuration table name including the correc |
| 92 | `Summary_87` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Obtains a ISTextExpert instance for processing structured te | Obtains a IStructuredTextExpert instance for processing stru |
| 93 | `Summary_96` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | Return the list of Cassandra instances ordered by position o | Return the set of Cassandra instances. |
| 94 | `Summary_118` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Removes the content source from this channel, if it exists. | Removes the content source from this repo, if it exists. |
| 95 | `Summary_120` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Returns the meta object for the containment reference '  org | Returns the meta object for the attribute ' org.eclipse.myly |
| 96 | `Summary_124` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | First authenticates the AuthenticationToken argument, and if | First authenticates the AuthenticationToken argument, and if |
| 97 | `Summary_130` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | Build a DruidDimensionsLoader. | Build a DimensionValueLoadTask. |
| 98 | `Summary_152` | ✓ |  | 1.000 | 1.000 | 1.000 | Creates a  UserAdapter if there is more than one profile on  | Creates a UserSpinnerAdapter if there is more than one profi |
| 99 | `Summary_154` | ✓ |  | 1.000 | 1.000 | 0.999 | Returns  TwitterTokenStream to tokenize a text. | Returns TokenStream to tokenize a text. |
| 100 | `Summary_197` | ✓ |  | 0.562 | 1.000 | 0.981 | Return the  org.atmosphere.cpr.MetaBroadcaster | Return the DefaultMetaBroadcaster |

---

## 逐样本详情

### [3/100] `Summary_4`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1524 |
| SARI | 0.1061 |
| GLEU | 0.2037 |
| METEOR | 0.4118 |
| xMatch | ✗ |

**原注释 (source)**
```
Create an instance based on current maven profile (as defined by  -Pit).
```

**标准注释 (ground truth)**
```
Creates an instance based on current maven profile (as defined by  -Pit).
```

**生成注释 (generated)**
```
Create an instance based on MongoAssertions configuration.
```

**当前代码 (new_code)**
```java
  static MongoDatabasePolicy create() {
    final MongoClient client;
    if (MongoAssertions.useMongo()) {
      // use to real client (connects to mongo)
      client = new MongoClient();
    } else if (MongoAssertions.useFongo()) {
      // in-memory DB (fake Mongo)
      client = new Fongo(MongoDatabasePolicy.class.getSimpleName()).getMongo();
    } else {
      throw new UnsupportedOperationException("I can only connect to Mongo or Fongo instances");
    }

    return new MongoDatabasePolicy(client);
  }


```

**变更前代码 (old_code)**
```java
  static MongoDatabaseRule create() {
    final MongoClient client;
    if (MongoAssertions.useMongo()) {
      // use to real client (connects to mongo)
      client = new MongoClient();
    } else if (MongoAssertions.useFongo()) {
      // in-memory DB (fake Mongo)
      client = new Fongo(MongoDatabaseRule.class.getSimpleName()).getMongo();
    } else {
      throw new UnsupportedOperationException("I can only connect to Mongo or Fongo instances");
    }

    return new MongoDatabaseRule(client);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,14 +1,14 @@
-static MongoDatabaseRule create() {

+static MongoDatabasePolicy create() {

     final MongoClient client;

     if (MongoAssertions.useMongo()) {

       // use to real client (connects to mongo)

       client = new MongoClient();

     } else if (MongoAssertions.useFongo()) {

       // in-memory DB (fake Mongo)

-      client = new Fongo(MongoDatabaseRule.class.getSimpleName()).getMongo();

+      client = new Fongo(MongoDatabasePolicy.class.getSimpleName()).getMongo();

     } else {

       throw new UnsupportedOperationException("I can only connect to Mongo or Fongo instances");

     }

 

-    return new MongoDatabaseRule(client);

+    return new MongoDatabasePolicy(client);

   }
```

---

### [95/100] `Summary_192`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1650 |
| SARI | 0.1245 |
| GLEU | 0.2097 |
| METEOR | 0.4927 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns an error, because querys could't add new records to the database.
```

**标准注释 (ground truth)**
```
Returns an error, because it is not possible to add a record to a query.
```

**生成注释 (generated)**
```
Throws an error, because querys could't add new records to the database.
```

**当前代码 (new_code)**
```java
    @Override
    public void createRecord(DBRecord rec, Connection conn)
    {
        throw new NotImplementedException(this, "createRecord");
    }


```

**变更前代码 (old_code)**
```java
    @Override
    public boolean createRecord(DBRecord rec, Connection conn)
    {
        return error(Errors.NotImplemented, "addRecord");
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
 @Override

-    public boolean createRecord(DBRecord rec, Connection conn)

+    public void createRecord(DBRecord rec, Connection conn)

     {

-        return error(Errors.NotImplemented, "addRecord");

+        throw new NotImplementedException(this, "createRecord");

     }
```

---

### [46/100] `Summary_92`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0527 |
| SARI | 0.1857 |
| GLEU | 0.1471 |
| METEOR | 0.2083 |
| xMatch | ✗ |

**原注释 (source)**
```
Get the parent cuboid really on the spanning tree.
```

**标准注释 (ground truth)**
```
Get the parent cuboid rely on the spanning tree.
```

**生成注释 (generated)**
```
Get the best match cuboid.
```

**当前代码 (new_code)**
```java
    public long findBestMatchCuboid(long cuboid) {
        return findBestMatchCuboid1(cuboid);
    }

```

**变更前代码 (old_code)**
```java
    public long findBestMatchCuboid(long child) {
        long parent = getOnTreeParent(child);
        while (parent > 0) {
            if (cubeDesc.getAllCuboids().contains(parent)) {
                break;
            }
            parent = getOnTreeParent(parent);
        }

        if (parent <= 0) {
            throw new IllegalStateException("Can't find valid parent for Cuboid " + child);
        }
        return parent;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,14 +1,3 @@
-public long findBestMatchCuboid(long child) {

-        long parent = getOnTreeParent(child);

-        while (parent > 0) {

-            if (cubeDesc.getAllCuboids().contains(parent)) {

-                break;

-            }

-            parent = getOnTreeParent(parent);

-        }

-

-        if (parent <= 0) {

-            throw new IllegalStateException("Can't find valid parent for Cuboid " + child);

-        }

-        return parent;

+public long findBestMatchCuboid(long cuboid) {

+        return findBestMatchCuboid1(cuboid);

     }
```

---

### [47/100] `Summary_94`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0073 |
| SARI | 0.1917 |
| GLEU | 0.0455 |
| METEOR | 0.1190 |
| xMatch | ✗ |

**原注释 (source)**
```
String representation of the signature.
```

**标准注释 (ground truth)**
```
Get a string representation of this member, using the '#' separator for class members.
```

**生成注释 (generated)**
```
String format of the signature.
```

**当前代码 (new_code)**
```java
    @Override
    public String toString() {
        if (stringRep == null) {
            stringRep = toString(true);
        }
    	return stringRep;
    }


```

**变更前代码 (old_code)**
```java
    public String toString(boolean altMemberSep) {
        StringBuffer s = new StringBuffer();
        if ( className != null ) {
            s.append(className);
        }
        if (memberName != null) {
            if ( className != null ) {            	
                s.append(altMemberSep ? ALT_MEMBER_SEPARATOR : '.');
            }
            s.append(memberName);
        }
        if ( descriptor != null && (className == null || memberName != null) ) {
            s.append(descriptor);
        }
        return s.toString();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,16 +1,7 @@
-public String toString(boolean altMemberSep) {

-        StringBuffer s = new StringBuffer();

-        if ( className != null ) {

-            s.append(className);

+@Override

+    public String toString() {

+        if (stringRep == null) {

+            stringRep = toString(true);

         }

-        if (memberName != null) {

-            if ( className != null ) {            	

-                s.append(altMemberSep ? ALT_MEMBER_SEPARATOR : '.');

-            }

-            s.append(memberName);

-        }

-        if ( descriptor != null && (className == null || memberName != null) ) {

-            s.append(descriptor);

-        }

-        return s.toString();

+    	return stringRep;

     }
```

---

### [100/100] `Summary_204`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5002 |
| SARI | 0.2220 |
| GLEU | 0.5135 |
| METEOR | 0.8849 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns the encoding used to send and receive lines from the IRC server, or null if not set.
```

**标准注释 (ground truth)**
```
Returns the encoding used to send and receive lines from the IRC server.
```

**生成注释 (generated)**
```
Returns the Charset used to send and receive lines from the IRC server, or null if not set.
```

**当前代码 (new_code)**
```java
	public Charset getEncoding() {
		return _charset;
	}


```

**变更前代码 (old_code)**
```java
	public String getEncoding() {
		return _charset;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public String getEncoding() {

+public Charset getEncoding() {

 		return _charset;

 	}
```

---

### [23/100] `Summary_44`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4183 |
| SARI | 0.2694 |
| GLEU | 0.4571 |
| METEOR | 0.6683 |
| xMatch | ✗ |

**原注释 (source)**
```
The  #add(Object...) method uses Java variable-length arguments to pass a row of values.
```

**标准注释 (ground truth)**
```
The  #addRow(Object...) method uses Java variable-length arguments to pass a row of values.
```

**生成注释 (generated)**
```
The addSingleCol(Object value) method uses an Object array to pass a row of values.
```

**当前代码 (new_code)**
```java
  public RowSetBuilder addSingleCol(Object value) {
    return addRow(new Object[] { value });
  }

```

**变更前代码 (old_code)**
```java
  public RowSetBuilder addSingleCol(Object value) {
    return add(new Object[] { value });
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public RowSetBuilder addSingleCol(Object value) {

-    return add(new Object[] { value });

+    return addRow(new Object[] { value });

   }
```

---

### [55/100] `Summary_110`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1453 |
| SARI | 0.2734 |
| GLEU | 0.2303 |
| METEOR | 0.3704 |
| xMatch | ✗ |

**原注释 (source)**
```
Return XML schema for the specified type, suitable for insertion into the &lt;types&gt; element of a WSDL document.
```

**标准注释 (ground truth)**
```
Return XML schema for the specified type, suitable for insertion into the &lt;types&gt; element of a WSDL document, or underneath an &lt;element&gt; or &lt;attribute&gt; declaration.
```

**生成注释 (generated)**
```
Return null for the specified type, unsuitable for insertion into the <types> element of a WSDL document.
```

**当前代码 (new_code)**
```java
    public Element writeSchema(Class javaType, Types types) throws Exception {
        return null;
    }


```

**变更前代码 (old_code)**
```java
    public boolean writeSchema(Types types) throws Exception {
        return false;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean writeSchema(Types types) throws Exception {

-        return false;

+public Element writeSchema(Class javaType, Types types) throws Exception {

+        return null;

     }
```

---

### [73/100] `Summary_146`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7357 |
| SARI | 0.2960 |
| GLEU | 0.7385 |
| METEOR | 0.9439 |
| xMatch | ✗ |

**原注释 (source)**
```
Converts a value from its logical format (BigDecimal) to its encoded format - a struct containing the scale of the number and a binary representation of the number.
```

**标准注释 (ground truth)**
```
Converts a value from its logical format to its encoded format - a struct containing the scale of the number and a binary representation of the number.
```

**生成注释 (generated)**
```
Delegates the conversion of a value from its logical format (BigDecimal) to its encoded format - a struct containing the scale of the number and a binary representation of the number.
```

**当前代码 (new_code)**
```java
    public static Struct fromLogical(Schema schema, SpecialValueDecimal value) {
        return fromLogical(schema, value.getDecimalValue().orElse(null));
    }

```

**变更前代码 (old_code)**
```java
    public static Struct fromLogical(Schema schema, SpecialValueDecimal value) {
        Struct result = new Struct(schema);
        final BigDecimal decimalValue = value.getDecimalValue().orElse(null);
        assert decimalValue != null : "Unable to encode special value";
        result.put(VALUE_FIELD, decimalValue.unscaledValue().toByteArray());
        result.put(SCALE_FIELD, decimalValue.scale());
        return result;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,3 @@
 public static Struct fromLogical(Schema schema, SpecialValueDecimal value) {

-        Struct result = new Struct(schema);

-        final BigDecimal decimalValue = value.getDecimalValue().orElse(null);

-        assert decimalValue != null : "Unable to encode special value";

-        result.put(VALUE_FIELD, decimalValue.unscaledValue().toByteArray());

-        result.put(SCALE_FIELD, decimalValue.scale());

-        return result;

+        return fromLogical(schema, value.getDecimalValue().orElse(null));

     }
```

---

### [38/100] `Summary_75`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0446 |
| SARI | 0.3144 |
| GLEU | 0.0882 |
| METEOR | 0.4076 |
| xMatch | ✗ |

**原注释 (source)**
```
Loads the  JBossWebSocketHandler using reflection as it imports container specific classes.
```

**标准注释 (ground truth)**
```
Loads the  JBossWebSocketHandler u
```

**生成注释 (generated)**
```
Instantiates the JBossWebSocketHandler as it imports container specific classes.
```

**当前代码 (new_code)**
```java
    private HttpEventServlet newWebSocketHandler(AtmosphereConfig config) {
        try {
            return new JBossWebSocketHandler(config);
        } catch (Exception e) {
            logger.error("Cannot instantiate JBossWebSocketHandler. Websocket events will not be handled.", e);
        }
        
        return null;
    }

```

**变更前代码 (old_code)**
```java
    private HttpEventServlet newWebSocketHandler(AtmosphereConfig config) {
        try {
            Class<?> clazz = getClass().getClassLoader().loadClass(WEB_SOCKET_HANDLER);
            Constructor<?> ctor = clazz.getDeclaredConstructor(new Class[] {AtmosphereConfig.class});
            return HttpEventServlet.class.cast(ctor.newInstance(config));
        } catch (Exception e) {
            logger.error("Cannot instantiate JBossWebSocketHandler. Websocket events will not be handled.", e);
        }
        
        return null;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,6 @@
 private HttpEventServlet newWebSocketHandler(AtmosphereConfig config) {

         try {

-            Class<?> clazz = getClass().getClassLoader().loadClass(WEB_SOCKET_HANDLER);

-            Constructor<?> ctor = clazz.getDeclaredConstructor(new Class[] {AtmosphereConfig.class});

-            return HttpEventServlet.class.cast(ctor.newInstance(config));

+            return new JBossWebSocketHandler(config);

         } catch (Exception e) {

             logger.error("Cannot instantiate JBossWebSocketHandler. Websocket events will not be handled.", e);

         }

```

---

### [21/100] `Summary_40`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.0132 |
| SARI | 0.3452 |
| GLEU | 0.0185 |
| METEOR | 0.0407 |
| xMatch | ✗ |

**原注释 (source)**
```
Determines if a specified set of columns from a specified relational expression are unique.
```

**标准注释 (ground truth)**
```
Returns the  BuiltInMetadata.ColumnUniqueness#areColumnsUnique(BitSet, boolean) statistic.
```

**生成注释 (generated)**
```
Determines if a specified set of columns from a specified relational expression are unique.
```

**当前代码 (new_code)**
```java
  public static Boolean areColumnsUnique(RelNode rel, BitSet columns) {
    final BuiltInMetadata.ColumnUniqueness metadata =
        rel.metadata(BuiltInMetadata.ColumnUniqueness.class);
    return metadata.areColumnsUnique(columns, false);
  }

```

**变更前代码 (old_code)**
```java
  public static Boolean areColumnsUnique(RelNode rel, BitSet columns) {
    return (Boolean) rel.getCluster().getMetadataProvider().getRelMetadata(
        rel,
        "areColumnsUnique",
        new Object[]{columns, false});
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,5 @@
 public static Boolean areColumnsUnique(RelNode rel, BitSet columns) {

-    return (Boolean) rel.getCluster().getMetadataProvider().getRelMetadata(

-        rel,

-        "areColumnsUnique",

-        new Object[]{columns, false});

+    final BuiltInMetadata.ColumnUniqueness metadata =

+        rel.metadata(BuiltInMetadata.ColumnUniqueness.class);

+    return metadata.areColumnsUnique(columns, false);

   }
```

---

### [50/100] `Summary_100`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0189 |
| SARI | 0.3485 |
| GLEU | 0.0263 |
| METEOR | 0.0543 |
| xMatch | ✗ |

**原注释 (source)**
```
Get entry data, read directly from internal data structure.
```

**标准注释 (ground truth)**
```
Returns the value stored at the specified key.
```

**生成注释 (generated)**
```
Get entry data, read directly from internal data structure.
```

**当前代码 (new_code)**
```java
    public String getValue(String key) throws NotFoundException, NotLeaderException {
        if (cluster.getLocalRole() != Role.LEADER) {
            throw new NotLeaderException();
        }
        if (!entries.containsKey(key)) {
            throw new NotFoundException();
        }
        String value = entries.get(key);
        logger.info(String.format("Get key %s: %s", key, value));
        return value;
    }


```

**变更前代码 (old_code)**
```java
    public String getValue(String entryId) throws RecordNotFoundException {
        if (!entries.containsKey(entryId)) {
            throw new RecordNotFoundException();
        }
        return entries.get(entryId);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,11 @@
-public String getValue(String entryId) throws RecordNotFoundException {

-        if (!entries.containsKey(entryId)) {

-            throw new RecordNotFoundException();

+public String getValue(String key) throws NotFoundException, NotLeaderException {

+        if (cluster.getLocalRole() != Role.LEADER) {

+            throw new NotLeaderException();

         }

-        return entries.get(entryId);

+        if (!entries.containsKey(key)) {

+            throw new NotFoundException();

+        }

+        String value = entries.get(key);

+        logger.info(String.format("Get key %s: %s", key, value));

+        return value;

     }
```

---

### [74/100] `Summary_150`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5728 |
| SARI | 0.3509 |
| GLEU | 0.5814 |
| METEOR | 0.8220 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns the providers that have at least one common ISO 3166 code and are of the given type.
```

**标准注释 (ground truth)**
```
Returns the providers that have at least one common ISO 3166 code and are of the given contextWrappableAs.
```

**生成注释 (generated)**
```
Returns the providers that have at least one common ISO 3166 code and whose context is wrappable as the given type token.
```

**当前代码 (new_code)**
```java
   public static Iterable<ProviderMetadata> collocatedWith(ProviderMetadata providerMetadata,
            TypeToken<? extends Wrapper> contextWrappableAs) {
      return filter(all(), Predicates.and(ProviderPredicates.intersectingIso3166Code(providerMetadata),
               ProviderPredicates.contextWrappableAs(contextWrappableAs)));
   }


```

**变更前代码 (old_code)**
```java
   public static Iterable<ProviderMetadata<?, ?, ?, ?>> collocatedWith(ProviderMetadata<?, ?, ?, ?> providerMetadata,
         ApiType type) {
      return filter(all(),
            Predicates.and(ProviderPredicates.intersectingIso3166Code(providerMetadata), ProviderPredicates.type(type)));
   }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public static Iterable<ProviderMetadata<?, ?, ?, ?>> collocatedWith(ProviderMetadata<?, ?, ?, ?> providerMetadata,

-         ApiType type) {

-      return filter(all(),

-            Predicates.and(ProviderPredicates.intersectingIso3166Code(providerMetadata), ProviderPredicates.type(type)));

+public static Iterable<ProviderMetadata> collocatedWith(ProviderMetadata providerMetadata,

+            TypeToken<? extends Wrapper> contextWrappableAs) {

+      return filter(all(), Predicates.and(ProviderPredicates.intersectingIso3166Code(providerMetadata),

+               ProviderPredicates.contextWrappableAs(contextWrappableAs)));

    }
```

---

### [35/100] `Summary_69`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.0251 |
| SARI | 0.3611 |
| GLEU | 0.0588 |
| METEOR | 0.1818 |
| xMatch | ✗ |

**原注释 (source)**
```
Ensure that correct implementation is used for the component.
```

**标准注释 (ground truth)**
```
Update generic component features.
```

**生成注释 (generated)**
```
Ensure that correct implementation is used for the component.
```

**当前代码 (new_code)**
```java
	public boolean updateComponent(Widget component, UIDL uidl,
			boolean manageCaption) {

		// Switch to correct implementation if neede
		if (!widgetFactory.isCorrectImplementation(component, uidl)) {
			Layout parent = getParentLayout(component);
			if (parent != null) {
				Widget w = widgetFactory.createWidget(uidl);
				registerPaintable(uidl.getId(), (Paintable) w);
				parent.replaceChildComponent(component, w);
				((Paintable) w).updateFromUIDL(uidl, this);
				return true;
			}
		}

		// Set captions
		// TODO Manage Error messages
		if (manageCaption) {
			Layout parent = getParentLayout(component);
			if (parent != null)
				parent.updateCaption(component, uidl);
		}

		// Visibility, Disabling and read-only status
		if (component instanceof FocusWidget)
			((FocusWidget) component).setEnabled(!uidl
					.getBooleanAttribute("disabled"));
		boolean visible = !uidl.getBooleanAttribute("invisible");
		component.setVisible(visible);
		if (!visible)
// ... (truncated)
```

**变更前代码 (old_code)**
```java
	public boolean updateComponent(Widget component, UIDL uidl,
			boolean manageCaption) {

		if (manageCaption) {
			Layout parent = getParentLayout(component);
			if (parent != null)
				parent.updateCaption(component, uidl);
		}
		
		boolean visible = !uidl.getBooleanAttribute("invisible");
		component.setVisible(visible);
		if (!visible) return true;
		
		if (widgetFactory.isCorrectImplementation(component, uidl))
			return false;
		Layout parent = getParentLayout(component);
		if (parent == null)
			return false;
		Widget w = widgetFactory.createWidget(uidl);
		registerPaintable(uidl.getId(), (Paintable) w);
		parent.replaceChildComponent(component, w);
		((Paintable) w).updateFromUIDL(uidl, this);

		return true;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,25 +1,34 @@
 public boolean updateComponent(Widget component, UIDL uidl,

 			boolean manageCaption) {

 

+		// Switch to correct implementation if neede

+		if (!widgetFactory.isCorrectImplementation(component, uidl)) {

+			Layout parent = getParentLayout(component);

+			if (parent != null) {

+				Widget w = widgetFactory.createWidget(uidl);

+				registerPaintable(uidl.getId(), (Paintable) w);

+				parent.replaceChildComponent(component, w);

+				((Paintable) w).updateFromUIDL(uidl, this);

+				return true;

+			}

+		}

+

+		// Set captions

+		// TODO Manage Error messages

 		if (manageCaption) {

 			Layout parent = getParentLayout(component);

 			if (parent != null)

 				parent.updateCaption(component, uidl);

 		}

-		

+

+		// Visibility, Disabling and read-only status

+		if (component instanceof FocusWidget)

+			((FocusWidget) component).setEnabled(!uidl

+					.getBooleanAttribute("disabled"));

 		boolean visible = !uidl.getBooleanAttribute("invisible");

 		component.setVisible(visible);

-		if (!visible) return true;

-		

-		if (widgetFactory.isCorrectImplementation(component, uidl))

-			return false;

-		Layout parent = getParentLayout(component);

-		if (parent == null)

-			return false;

```

---

### [77/100] `Summary_156`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0224 |
| SARI | 0.3652 |
| GLEU | 0.0526 |
| METEOR | 0.1980 |
| xMatch | ✗ |

**原注释 (source)**
```
Gets sentry role objects for a given groupName from the persistence layer
```

**标准注释 (ground truth)**
```
Return set of roles corresponding to the groups provided.
```

**生成注释 (generated)**
```
Gets sentry role objects for given groups from the persistence layer
```

**当前代码 (new_code)**
```java
  public Set<TSentryRole> getTSentryRolesByGroupName(final Set<String> groupNames,
                                                     final boolean checkAllGroups) throws Exception {
    if (groupNames.isEmpty()) {
      return Collections.emptySet();
    }

    return tm.executeTransaction(
            new TransactionBlock<Set<TSentryRole>>() {
              @Override
              public Set<TSentryRole> execute(PersistenceManager pm) throws Exception {

                pm.setDetachAllOnCommit(false); // No need to detach objects

                // Pre-allocate large sets for role names and results.
                // roleNames is used to avoid adding the same role mutiple times into
                // result. The result is set, but comparisons between TSentryRole objects
                // is more expensive then String comparisons.
                Set<String> roleNames = new HashSet<>(1024);
                Set<TSentryRole> result = new HashSet<>(1024);

                for(String group: groupNames) {
                  if (group == null) {
                    // Special case - return all roles
                    List<MSentryRole> roles = getAllRoles(pm);
                    for (MSentryRole role: roles) {
                      result.add(convertToTSentryRole(role));
                    }
                    return result;
                  }

// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public Set<TSentryRole> getTSentryRolesByGroupName(Set<String> groupNames,
      boolean checkAllGroups) throws Exception {
    Set<MSentryRole> roleSet = Sets.newHashSet();
    for (String groupName : groupNames) {
      try {
        roleSet.addAll(getMSentryRolesByGroupName(groupName));
      } catch (SentryNoSuchObjectException e) {
        // if we are checking for all the given groups, then continue searching
        if (!checkAllGroups) {
          throw e;
        }
      }
    }
    return convertToTSentryRoles(roleSet);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,15 +1,53 @@
-public Set<TSentryRole> getTSentryRolesByGroupName(Set<String> groupNames,

-      boolean checkAllGroups) throws Exception {

-    Set<MSentryRole> roleSet = Sets.newHashSet();

-    for (String groupName : groupNames) {

-      try {

-        roleSet.addAll(getMSentryRolesByGroupName(groupName));

-      } catch (SentryNoSuchObjectException e) {

-        // if we are checking for all the given groups, then continue searching

-        if (!checkAllGroups) {

-          throw e;

-        }

-      }

+public Set<TSentryRole> getTSentryRolesByGroupName(final Set<String> groupNames,

+                                                     final boolean checkAllGroups) throws Exception {

+    if (groupNames.isEmpty()) {

+      return Collections.emptySet();

     }

-    return convertToTSentryRoles(roleSet);

+

+    return tm.executeTransaction(

+            new TransactionBlock<Set<TSentryRole>>() {

+              @Override

+              public Set<TSentryRole> execute(PersistenceManager pm) throws Exception {

+

+                pm.setDetachAllOnCommit(false); // No need to detach objects

+

+                // Pre-allocate large sets for role names and results.

+                // roleNames is used to avoid adding the same role mutiple times into

+                // result. The result is set, but comparisons between TSentryRole objects

+                // is more expensive then String comparisons.

+                Set<String> roleNames = new HashSet<>(1024);

+                Set<TSentryRole> result = new HashSet<>(1024);

+

+                for(String group: groupNames) {

+                  if (group == null) {

+                    // Special case - return all roles

+                    List<MSentryRole> roles = getAllRoles(pm);

```

---

### [5/100] `Summary_8`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4276 |
| SARI | 0.3824 |
| GLEU | 0.4651 |
| METEOR | 0.6694 |
| xMatch | ✗ |

**原注释 (source)**
```
Provides a list containing four set, each containing projects to be displayed on the project view for projects using the parameterized trigger plugin under 'Subprojects'. 
```

**标准注释 (ground truth)**
```
Provides a SubProjectData object containing four set, each containing projects to be displayed on the project view under 'Subprojects' section. 
```

**生成注释 (generated)**
```
Provides a SubProjectData object to be displayed on the project view for projects using the parameterized trigger plugin under 'Subprojects'.
```

**当前代码 (new_code)**
```java
    public SubProjectData getProjectInfo(AbstractProject context) {

        SubProjectData subProjectData = new SubProjectData();

        iterateBuilds(context, projects, subProjectData);

        // We don't want to show a project twice
        subProjectData.getTriggered().removeAll(subProjectData.getDynamic());
        subProjectData.getTriggered().removeAll(subProjectData.getFixed());

        return subProjectData;
    }


```

**变更前代码 (old_code)**
```java
    public List<Set<?>> getProjectInfo(AbstractProject context) {

        Comparator customComparator = new Comparator<AbstractProject>() {
            public int compare(AbstractProject abstractProject1, AbstractProject abstractProject2) {
                return abstractProject1.getFullName().compareTo(abstractProject2.getFullName());
            }
        };

        Set<AbstractProject> dynamicProject = new TreeSet<AbstractProject>(customComparator);
        Set<AbstractProject> staticProject = new TreeSet<AbstractProject>(customComparator);
        Set<AbstractProject> triggeredProject = new TreeSet<AbstractProject>(customComparator);
        Set<String> unresolvedProject = new TreeSet<String>();

        iterateBuilds(context, projects, dynamicProject, staticProject, triggeredProject, unresolvedProject);

        // We don't want to show a project twice
        triggeredProject.removeAll(dynamicProject);
        triggeredProject.removeAll(staticProject);

        return Arrays.asList(staticProject, dynamicProject, triggeredProject, unresolvedProject);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,21 +1,12 @@
-public List<Set<?>> getProjectInfo(AbstractProject context) {

+public SubProjectData getProjectInfo(AbstractProject context) {

 

-        Comparator customComparator = new Comparator<AbstractProject>() {

-            public int compare(AbstractProject abstractProject1, AbstractProject abstractProject2) {

-                return abstractProject1.getFullName().compareTo(abstractProject2.getFullName());

-            }

-        };

+        SubProjectData subProjectData = new SubProjectData();

 

-        Set<AbstractProject> dynamicProject = new TreeSet<AbstractProject>(customComparator);

-        Set<AbstractProject> staticProject = new TreeSet<AbstractProject>(customComparator);

-        Set<AbstractProject> triggeredProject = new TreeSet<AbstractProject>(customComparator);

-        Set<String> unresolvedProject = new TreeSet<String>();

-

-        iterateBuilds(context, projects, dynamicProject, staticProject, triggeredProject, unresolvedProject);

+        iterateBuilds(context, projects, subProjectData);

 

         // We don't want to show a project twice

-        triggeredProject.removeAll(dynamicProject);

-        triggeredProject.removeAll(staticProject);

+        subProjectData.getTriggered().removeAll(subProjectData.getDynamic());

+        subProjectData.getTriggered().removeAll(subProjectData.getFixed());

 

-        return Arrays.asList(staticProject, dynamicProject, triggeredProject, unresolvedProject);

+        return subProjectData;

     }
```

---

### [37/100] `Summary_73`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1375 |
| SARI | 0.3826 |
| GLEU | 0.2941 |
| METEOR | 0.6181 |
| xMatch | ✗ |

**原注释 (source)**
```
Encodes a value in a canonical serialized string format, for use in a URL query parameter.
```

**标准注释 (ground truth)**
```
Encodes a value for use in a URL.
```

**生成注释 (generated)**
```
Encodes a value in a canonical serialized string format.
```

**当前代码 (new_code)**
```java
	public static String encodeValue(Value value) {
		return NTriplesUtil.toNTriplesString(value);
	}


```

**变更前代码 (old_code)**
```java
	public static String encodeValue(Value value) {
		if (value instanceof BNode) {
			// SES-2129 special treatment of blank node names to avoid problems with round-tripping.
			return "_:" + ((BNode)value).getID();
		}
		
		// for everything else we just use N-Triples serialization.
		return NTriplesUtil.toNTriplesString(value);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,3 @@
 public static String encodeValue(Value value) {

-		if (value instanceof BNode) {

-			// SES-2129 special treatment of blank node names to avoid problems with round-tripping.

-			return "_:" + ((BNode)value).getID();

-		}

-		

-		// for everything else we just use N-Triples serialization.

 		return NTriplesUtil.toNTriplesString(value);

 	}
```

---

### [34/100] `Summary_67`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7718 |
| SARI | 0.3952 |
| GLEU | 0.7778 |
| METEOR | 0.8830 |
| xMatch | ✗ |

**原注释 (source)**
```
If a Schema contains a reference to an other Schema with '$ref', returns the referenced Schema or the actual Schema in the other cases.
```

**标准注释 (ground truth)**
```
If a Schema contains a reference to an other Schema with '$ref', returns the referenced Schema if it is found or the actual Schema in the other cases.
```

**生成注释 (generated)**
```
If a Schema contains a reference to an other Schema with '$ref' and resolved, returns the referenced Schema or the actual Schema in the other cases.
```

**当前代码 (new_code)**
```java
    public static Schema getReferencedSchema(OpenAPI openAPI, Schema schema) {
        if (schema != null && StringUtils.isNotEmpty(schema.get$ref())) {
            String name = getSimpleRef(schema.get$ref());
            Schema referencedSchema = getSchema(openAPI, name);
            if(referencedSchema != null) {
                return referencedSchema;
            }
        }
        return schema;
    }

```

**变更前代码 (old_code)**
```java
    public static Schema getReferencedSchema(OpenAPI openAPI, Schema schema) {
        if (schema != null && StringUtils.isNotEmpty(schema.get$ref())) {
            String name = getSimpleRef(schema.get$ref());
            return getSchema(openAPI, name);
        }
        return schema;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,10 @@
 public static Schema getReferencedSchema(OpenAPI openAPI, Schema schema) {

         if (schema != null && StringUtils.isNotEmpty(schema.get$ref())) {

             String name = getSimpleRef(schema.get$ref());

-            return getSchema(openAPI, name);

+            Schema referencedSchema = getSchema(openAPI, name);

+            if(referencedSchema != null) {

+                return referencedSchema;

+            }

         }

         return schema;

     }
```

---

### [7/100] `Summary_12`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0192 |
| SARI | 0.3958 |
| GLEU | 0.0526 |
| METEOR | 0.1442 |
| xMatch | ✗ |

**原注释 (source)**
```
Only the views are mirrored.
```

**标准注释 (ground truth)**
```
Returns true if the compare viewer is mirrored, i.e.
```

**生成注释 (generated)**
```
The views are mirrored.
```

**当前代码 (new_code)**
```java
	public boolean isMirrored() {
		if (!fMirroringEnabled)
			return false;
		Object property = getProperty(MIRRORED);
		return property instanceof Boolean && (Boolean) property;
	}


```

**变更前代码 (old_code)**
```java
	public boolean isMirrored() {
		Object property = getProperty(MIRRORED);
		return property instanceof Boolean && (Boolean) property;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,6 @@
 public boolean isMirrored() {

+		if (!fMirroringEnabled)

+			return false;

 		Object property = getProperty(MIRRORED);

 		return property instanceof Boolean && (Boolean) property;

 	}
```

---

### [27/100] `Summary_52`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0474 |
| SARI | 0.3985 |
| GLEU | 0.1316 |
| METEOR | 0.2410 |
| xMatch | ✗ |

**原注释 (source)**
```
Create a CoreMap representing a sentence from this protocol buffer.
```

**标准注释 (ground truth)**
```
Create a CoreLabel from its serialized counterpart.
```

**生成注释 (generated)**
```
Create a CoreMap representing a word from this protocol buffer.
```

**当前代码 (new_code)**
```java
  protected CoreLabel fromProto(CoreNLPProtos.Token proto) {
    CoreLabel word = new CoreLabel();
    // Required fields
    word.setWord(proto.getWord());
    // Optional fields
    if (proto.hasPos()) { word.setTag(proto.getPos()); }
    if (proto.hasValue()) { word.setValue(proto.getValue()); }
    if (proto.hasCategory()) { word.setCategory(proto.getCategory()); }
    if (proto.hasBefore()) { word.setBefore(proto.getBefore()); }
    if (proto.hasAfter()) { word.setAfter(proto.getAfter()); }
    if (proto.hasOriginalText()) { word.setOriginalText(proto.getOriginalText()); }
    if (proto.hasNer()) { word.setNER(proto.getNer()); }
    if (proto.hasLemma()) { word.setLemma(proto.getLemma()); }
    if (proto.hasBeginChar()) { word.setBeginPosition(proto.getBeginChar()); }
    if (proto.hasEndChar()) { word.setEndPosition(proto.getEndChar()); }
    if (proto.hasSpeaker()) { word.set(SpeakerAnnotation.class, proto.getSpeaker()); }
    if (proto.hasUtterance()) { word.set(UtteranceAnnotation.class, proto.getUtterance()); }
    if (proto.hasBeginIndex()) { word.set(BeginIndexAnnotation.class, proto.getBeginIndex()); }
    if (proto.hasEndIndex()) { word.set(EndIndexAnnotation.class, proto.getEndIndex()); }
    if (proto.hasTokenBeginIndex()) { word.set(TokenBeginAnnotation.class, proto.getTokenBeginIndex()); }
    if (proto.hasTokenEndIndex()) { word.set(TokenEndAnnotation.class, proto.getTokenEndIndex()); }
    if (proto.hasNormalizedNER()) { word.set(NormalizedNamedEntityTagAnnotation.class, proto.getNormalizedNER()); }
    if (proto.hasTimexValue()) { word.set(TimexAnnotation.class, fromProto(proto.getTimexValue())); }
    if (proto.hasHasXmlContext() && proto.getHasXmlContext()) { word.set(XmlContextAnnotation.class, proto.getXmlContextList()); }
    if (proto.hasCorefClusterID()) { word.set(CorefClusterIdAnnotation.class, proto.getCorefClusterID()); }
    if (proto.hasAnswer()) { word.set(AnswerAnnotation.class, proto.getAnswer()); }
    // Non-default annotators
    if (proto.hasGender()) { word.set(GenderAnnotation.class, proto.getGender()); }
    if (proto.hasTrueCase()) { word.set(TrueCaseAnnotation.class, proto.getTrueCase()); }
    if (proto.hasTrueCaseText()) { word.set(TrueCaseTextAnnotation.class, proto.getTrueCaseText()); }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  protected CoreMap fromProto(CoreNLPProtos.Sentence proto) {
    CoreMap sentence = new ArrayCoreMap();
    // Required fields
    sentence.set(TokenBeginAnnotation.class, proto.getTokenOffsetBegin());
    sentence.set(TokenEndAnnotation.class, proto.getTokenOffsetEnd());
    // Optional fields
    if (proto.hasSentenceIndex()) { sentence.set(SentenceIndexAnnotation.class, proto.getSentenceIndex()); }
    if (proto.hasCharacterOffsetBegin()) { sentence.set(CharacterOffsetBeginAnnotation.class, proto.getCharacterOffsetBegin()); }
    if (proto.hasCharacterOffsetEnd()) { sentence.set(CharacterOffsetEndAnnotation.class, proto.getCharacterOffsetEnd()); }
    if (proto.hasParseTree()) { sentence.set(TreeAnnotation.class, fromProto(proto.getParseTree())); }
    // Non-default fields
    if (proto.hasHasRelationAnnotations() && proto.getHasRelationAnnotations()) {
      // set entities
      List<EntityMention> entities = new ArrayList<EntityMention>();
      for (CoreNLPProtos.Entity entity : proto.getEntityList()) { entities.add(fromProto(entity, sentence)); }
      sentence.set(EntityMentionsAnnotation.class, entities);
      // set relations
      List<RelationMention> relations = new ArrayList<RelationMention>();
      for (CoreNLPProtos.Relation relation : proto.getRelationList()) { relations.add(fromProto(relation, sentence)); }
      sentence.set(RelationMentionsAnnotation.class, relations);
    }
    // Return
    return sentence;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,24 +1,33 @@
-protected CoreMap fromProto(CoreNLPProtos.Sentence proto) {

-    CoreMap sentence = new ArrayCoreMap();

+protected CoreLabel fromProto(CoreNLPProtos.Token proto) {

+    CoreLabel word = new CoreLabel();

     // Required fields

-    sentence.set(TokenBeginAnnotation.class, proto.getTokenOffsetBegin());

-    sentence.set(TokenEndAnnotation.class, proto.getTokenOffsetEnd());

+    word.setWord(proto.getWord());

     // Optional fields

-    if (proto.hasSentenceIndex()) { sentence.set(SentenceIndexAnnotation.class, proto.getSentenceIndex()); }

-    if (proto.hasCharacterOffsetBegin()) { sentence.set(CharacterOffsetBeginAnnotation.class, proto.getCharacterOffsetBegin()); }

-    if (proto.hasCharacterOffsetEnd()) { sentence.set(CharacterOffsetEndAnnotation.class, proto.getCharacterOffsetEnd()); }

-    if (proto.hasParseTree()) { sentence.set(TreeAnnotation.class, fromProto(proto.getParseTree())); }

-    // Non-default fields

-    if (proto.hasHasRelationAnnotations() && proto.getHasRelationAnnotations()) {

-      // set entities

-      List<EntityMention> entities = new ArrayList<EntityMention>();

-      for (CoreNLPProtos.Entity entity : proto.getEntityList()) { entities.add(fromProto(entity, sentence)); }

-      sentence.set(EntityMentionsAnnotation.class, entities);

-      // set relations

-      List<RelationMention> relations = new ArrayList<RelationMention>();

-      for (CoreNLPProtos.Relation relation : proto.getRelationList()) { relations.add(fromProto(relation, sentence)); }

-      sentence.set(RelationMentionsAnnotation.class, relations);

-    }

+    if (proto.hasPos()) { word.setTag(proto.getPos()); }

+    if (proto.hasValue()) { word.setValue(proto.getValue()); }

+    if (proto.hasCategory()) { word.setCategory(proto.getCategory()); }

+    if (proto.hasBefore()) { word.setBefore(proto.getBefore()); }

+    if (proto.hasAfter()) { word.setAfter(proto.getAfter()); }

+    if (proto.hasOriginalText()) { word.setOriginalText(proto.getOriginalText()); }

+    if (proto.hasNer()) { word.setNER(proto.getNer()); }

+    if (proto.hasLemma()) { word.setLemma(proto.getLemma()); }

+    if (proto.hasBeginChar()) { word.setBeginPosition(proto.getBeginChar()); }

+    if (proto.hasEndChar()) { word.setEndPosition(proto.getEndChar()); }

+    if (proto.hasSpeaker()) { word.set(SpeakerAnnotation.class, proto.getSpeaker()); }

+    if (proto.hasUtterance()) { word.set(UtteranceAnnotation.class, proto.getUtterance()); }

+    if (proto.hasBeginIndex()) { word.set(BeginIndexAnnotation.class, proto.getBeginIndex()); }

```

---

### [71/100] `Summary_142`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4555 |
| SARI | 0.4108 |
| GLEU | 0.4828 |
| METEOR | 0.6048 |
| xMatch | ✗ |

**原注释 (source)**
```
All Paths are 'tagged' in swagger with the final entity type name in the path.
```

**标准注释 (ground truth)**
```
All Paths are 'tagged' in swagger with the root entity name in the path.
```

**生成注释 (generated)**
```
All Paths are 'tagged' in swagger with a name.
```

**当前代码 (new_code)**
```java
        private String getTag() {
            if (lineage.isEmpty()) {
                return name;
            } else {
                return lineage.get(0).getName();
            }
        }


```

**变更前代码 (old_code)**
```java
        private String getTag() {
            return dictionary.getJsonAliasFor(type);
        }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,7 @@
 private String getTag() {

-            return dictionary.getJsonAliasFor(type);

+            if (lineage.isEmpty()) {

+                return name;

+            } else {

+                return lineage.get(0).getName();

+            }

         }
```

---

### [28/100] `Summary_54`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0307 |
| SARI | 0.4111 |
| GLEU | 0.0800 |
| METEOR | 0.2355 |
| xMatch | ✗ |

**原注释 (source)**
```
Checks if a flag is set.
```

**标准注释 (ground truth)**
```
Returns  true if any of the flags supplied in the argument are set.
```

**生成注释 (generated)**
```
Checks if a flag mask is set.
```

**当前代码 (new_code)**
```java
    public boolean isFlagSet(int flagsToCheck) {
        return isFlagSet(flags, flagsToCheck);
    }


```

**变更前代码 (old_code)**
```java
    public boolean isFlagSet(int flag) {
        return (flags & flag) != 0;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean isFlagSet(int flag) {

-        return (flags & flag) != 0;

+public boolean isFlagSet(int flagsToCheck) {

+        return isFlagSet(flags, flagsToCheck);

     }
```

---

### [61/100] `Summary_122`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0455 |
| SARI | 0.4333 |
| GLEU | 0.1667 |
| METEOR | 0.7339 |
| xMatch | ✗ |

**原注释 (source)**
```
Return a String to recreate the GRANTs given for the passed table.
```

**标准注释 (ground truth)**
```
Return the GRANTs for the given table
```

**生成注释 (generated)**
```
Return a Collection<TableGrant> of the GRANTs given for the passed table.
```

**当前代码 (new_code)**
```java
	public Collection<TableGrant> getTableGrants(TableIdentifier table)
	{
		Collection<TableGrant> result = new HashSet<TableGrant>();
		ResultSet rs = null;
		try
		{
			TableIdentifier tbl = table.createCopy();
			tbl.adjustCase(this.dbConnection);
			rs = this.metaData.getTablePrivileges(tbl.getCatalog(), tbl.getSchema(), tbl.getTableName());
			while (rs.next())
			{
				String from = rs.getString(4);
				String to = rs.getString(5);
				String what = rs.getString(6);
				boolean grantable = StringUtil.stringToBool(rs.getString(7));
				TableGrant grant = new TableGrant(to, what, grantable);
				result.add(grant);
			}
		}
		catch (Exception e)
		{
			LogMgr.logError("DbMetadata.getTableGrants()", "Error when retrieving table privileges",e);
		}
		finally
		{
			try { rs.close(); } catch (Throwable th) {}
		}
		return result;
	}

// ... (truncated)
```

**变更前代码 (old_code)**
```java
	public DataStore getTableGrants(TableIdentifier table)
	{
		String[] columns = new String[] { "TABLENAME", "GRANTOR", "GRANTEE", "PRIVILEGE", "GRANTABLE" };
		int[] colTypes = new int[] { Types.VARCHAR, Types.VARCHAR, Types.VARCHAR, Types.VARCHAR, Types.VARCHAR };
		DataStore result = new DataStore(columns, colTypes);
		ResultSet rs = null;
		try
		{
			TableIdentifier tbl = table.createCopy();
			tbl.adjustCase(this.dbConnection);
			rs = this.metaData.getTablePrivileges(tbl.getCatalog(), tbl.getSchema(), tbl.getTableName());
			while (rs.next())
			{
				int row = result.addRow();
				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_OBJECT_NAME, rs.getString(3));
				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_GRANTOR, rs.getString(4));
				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_GRANTEE, rs.getString(5));
				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_PRIV, rs.getString(6));
				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_GRANTABLE, rs.getString(7));
			}
		}
		catch (Exception e)
		{
			LogMgr.logError("DbMetadata.getTableGrants()", "Error when retrieving table privileges",e);
			result.reset();
		}
		finally
		{
			try { rs.close(); } catch (Throwable th) {}
		}
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,6 @@
-public DataStore getTableGrants(TableIdentifier table)

+public Collection<TableGrant> getTableGrants(TableIdentifier table)

 	{

-		String[] columns = new String[] { "TABLENAME", "GRANTOR", "GRANTEE", "PRIVILEGE", "GRANTABLE" };

-		int[] colTypes = new int[] { Types.VARCHAR, Types.VARCHAR, Types.VARCHAR, Types.VARCHAR, Types.VARCHAR };

-		DataStore result = new DataStore(columns, colTypes);

+		Collection<TableGrant> result = new HashSet<TableGrant>();

 		ResultSet rs = null;

 		try

 		{

@@ -11,18 +9,17 @@
 			rs = this.metaData.getTablePrivileges(tbl.getCatalog(), tbl.getSchema(), tbl.getTableName());

 			while (rs.next())

 			{

-				int row = result.addRow();

-				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_OBJECT_NAME, rs.getString(3));

-				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_GRANTOR, rs.getString(4));

-				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_GRANTEE, rs.getString(5));

-				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_PRIV, rs.getString(6));

-				result.setValue(row, COLUMN_IDX_TABLE_GRANTS_GRANTABLE, rs.getString(7));

+				String from = rs.getString(4);

+				String to = rs.getString(5);

+				String what = rs.getString(6);

+				boolean grantable = StringUtil.stringToBool(rs.getString(7));

+				TableGrant grant = new TableGrant(to, what, grantable);

+				result.add(grant);

 			}

 		}

 		catch (Exception e)

 		{

 			LogMgr.logError("DbMetadata.getTableGrants()", "Error when retrieving table privileges",e);

-			result.reset();

 		}

 		finally

 		{

```

---

### [13/100] `Summary_24`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5663 |
| SARI | 0.4442 |
| GLEU | 0.5877 |
| METEOR | 0.6711 |
| xMatch | ✗ |

**原注释 (source)**
```
Check if the Elasticsearch  Node is connected and that the cluster health status is not  ClusterHealthStatus#RED.
```

**标准注释 (ground truth)**
```
Check if the Elasticsearch  Node is connected and that the cluster health status is not  ClusterHealthStatus#RED and that the  org.graylog2.indexer.Deflector#isUp() deflector is up.
```

**生成注释 (generated)**
```
Check if the Elasticsearch Node is connected, deflector is up, and that the cluster health status is not ClusterHealthStatus#RED.
```

**当前代码 (new_code)**
```java
    public boolean isConnectedAndHealthy() {
        Map<String, DiscoveryNode> nodeMap = nodes.get();
        if (nodeMap == null || nodeMap.isEmpty()) {
            return false;
        }
        if (!deflector.isUp()) {
            return false;
        }
        try {
            return getHealth() != ClusterHealthStatus.RED;
        } catch (ElasticsearchException e) {
            LOG.trace("Couldn't determine Elasticsearch health properly", e);
            return false;
        }
    }


```

**变更前代码 (old_code)**
```java
    public boolean isConnectedAndHealthy() {
        try {
            return getHealth() != ClusterHealthStatus.RED;
        } catch (ElasticsearchException e) {
            LOG.trace("Couldn't determine Elasticsearch health properly", e);
            return false;
        }
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,11 @@
 public boolean isConnectedAndHealthy() {

+        Map<String, DiscoveryNode> nodeMap = nodes.get();

+        if (nodeMap == null || nodeMap.isEmpty()) {

+            return false;

+        }

+        if (!deflector.isUp()) {

+            return false;

+        }

         try {

             return getHealth() != ClusterHealthStatus.RED;

         } catch (ElasticsearchException e) {

```

---

### [72/100] `Summary_144`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1674 |
| SARI | 0.4452 |
| GLEU | 0.2400 |
| METEOR | 0.2256 |
| xMatch | ✗ |

**原注释 (source)**
```
Gets the element for the method corresponding to this invocation.
```

**标准注释 (ground truth)**
```
Gets the element for the declaration corresponding to this use of an element.
```

**生成注释 (generated)**
```
Gets the element for this expression.
```

**当前代码 (new_code)**
```java
    public static final Element elementFromUse(ExpressionTree node) {
        return InternalUtils.symbol(node);
    }


```

**变更前代码 (old_code)**
```java
    public static final ExecutableElement elementFromUse(MethodInvocationTree node) {
        return (ExecutableElement)TreeInfo.symbol((JCTree)node.getMethodSelect());
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static final ExecutableElement elementFromUse(MethodInvocationTree node) {

-        return (ExecutableElement)TreeInfo.symbol((JCTree)node.getMethodSelect());

+public static final Element elementFromUse(ExpressionTree node) {

+        return InternalUtils.symbol(node);

     }
```

---

### [16/100] `Summary_30`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0363 |
| SARI | 0.4493 |
| GLEU | 0.1200 |
| METEOR | 0.3353 |
| xMatch | ✗ |

**原注释 (source)**
```
Checks if a flag is set.
```

**标准注释 (ground truth)**
```
Returns  true if any of the flags supplied in the argument are set.
```

**生成注释 (generated)**
```
Checks if any flag is set.
```

**当前代码 (new_code)**
```java
    public boolean isFlagSet(int flagsToCheck) {
        return (flags & flagsToCheck) != 0;
    }


```

**变更前代码 (old_code)**
```java
    public boolean isFlagSet(int flag) {
        return (flags & flag) != 0;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean isFlagSet(int flag) {

-        return (flags & flag) != 0;

+public boolean isFlagSet(int flagsToCheck) {

+        return (flags & flagsToCheck) != 0;

     }
```

---

### [1/100] `Summary_0`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0487 |
| SARI | 0.4500 |
| GLEU | 0.0556 |
| METEOR | 0.0862 |
| xMatch | ✗ |

**原注释 (source)**
```
Creates elastic node as single member of a cluster.
```

**标准注释 (ground truth)**
```
Creates an instance with existing settings
```

**生成注释 (generated)**
```
Creates elastic node.
```

**当前代码 (new_code)**
```java
  private static EmbeddedElasticsearchNode create(Settings settings) {
    // ensure PainlessPlugin is installed or otherwise scripted fields would not work
    Node node = new LocalNode(settings, Arrays.asList(Netty4Plugin.class, PainlessPlugin.class));
    return new EmbeddedElasticsearchNode(node);
  }

```

**变更前代码 (old_code)**
```java
  public static EmbeddedElasticsearchNode create() {
    File data = Files.createTempDir();
    data.deleteOnExit();
    File home = Files.createTempDir();
    home.deleteOnExit();

    Settings settings = Settings.builder()
        .put("node.name", "fake-elastic")
        .put("path.home", home.getAbsolutePath())
        .put("path.data", data.getAbsolutePath())
        .put("http.type", "netty4")
        .put("network.host", "localhost")
        .build();

    return create(settings);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,16 +1,5 @@
-public static EmbeddedElasticsearchNode create() {

-    File data = Files.createTempDir();

-    data.deleteOnExit();

-    File home = Files.createTempDir();

-    home.deleteOnExit();

-

-    Settings settings = Settings.builder()

-        .put("node.name", "fake-elastic")

-        .put("path.home", home.getAbsolutePath())

-        .put("path.data", data.getAbsolutePath())

-        .put("http.type", "netty4")

-        .put("network.host", "localhost")

-        .build();

-

-    return create(settings);

+private static EmbeddedElasticsearchNode create(Settings settings) {

+    // ensure PainlessPlugin is installed or otherwise scripted fields would not work

+    Node node = new LocalNode(settings, Arrays.asList(Netty4Plugin.class, PainlessPlugin.class));

+    return new EmbeddedElasticsearchNode(node);

   }
```

---

### [41/100] `Summary_81`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.1535 |
| SARI | 0.4718 |
| GLEU | 0.3529 |
| METEOR | 0.8201 |
| xMatch | ✗ |

**原注释 (source)**
```
Installs a list of  RemotePackage and their dependent packages.
```

**标准注释 (ground truth)**
```
Installs a  RemotePackage and its dependent packages.
```

**生成注释 (generated)**
```
Installs a list of  RemotePackage and their dependent packages.
```

**当前代码 (new_code)**
```java
    private boolean installRemotePackages(
            @NonNull List<RemotePackage> requestPackages,
            @NonNull RepoManager repoManager,
            @NonNull Downloader downloader,
            @NonNull ProgressIndicator progress) {

        List<RemotePackage> remotePackages =
                InstallerUtil.computeRequiredPackages(
                        requestPackages, repoManager.getPackages(), progress);

        if (remotePackages == null) {
            return false;
        }

        for (RemotePackage p : remotePackages) {
            if (p.getLicense() != null && !p.getLicense().checkAccepted(
                    repoManager.getLocalPath(), mSdkHandler.getFileOp())) {
                progress.setText(
                        "The license for package " + p.getDisplayName() + " was not accepted. "
                                + "Please install this package through Android Studio SDK "
                                + "Manager.");
                return false;
            }

            Installer installer = SdkInstallerUtil
                    .findBestInstallerFactory(p, mSdkHandler)
                    .createInstaller(p, repoManager, downloader, mSdkHandler.getFileOp());
            boolean result = installer.prepare(progress)
                    && installer.complete(progress);

// ... (truncated)
```

**变更前代码 (old_code)**
```java
    private Map<RemotePackage, InstallResultType> installRemotePackages(
            @NonNull List<RemotePackage> requestPackages,
            @NonNull RepoManager repoManager,
            @NonNull Downloader downloader,
            @NonNull ProgressIndicator progress) {

        List<RemotePackage> remotePackages =
                InstallerUtil.computeRequiredPackages(
                        requestPackages, repoManager.getPackages(), progress);
        Map<RemotePackage, InstallResultType> installResults = new HashMap<>();

        if (remotePackages == null) {
            requestPackages.forEach(p -> installResults.put(p, InstallResultType.INSTALL_FAIL));

        } else {
            for (RemotePackage p : remotePackages) {
                if (p.getLicense() != null && !p.getLicense()
                        .checkAccepted(repoManager.getLocalPath(), mSdkHandler.getFileOp())) {
                    progress.setText(
                            "The license for package " + p.getDisplayName() + " was not accepted. "
                                    + "Please install this package through Android Studio SDK "
                                    + "Manager.");
                    installResults.put(p, InstallResultType.LICENSE_FAIL);
                } else {
                    Installer installer = SdkInstallerUtil
                            .findBestInstallerFactory(p, mSdkHandler)
                            .createInstaller(p, repoManager, downloader, mSdkHandler.getFileOp());
                    if (installer.prepare(progress) && installer.complete(progress)) {
                        installResults.put(p, InstallResultType.SUCCESS);
                    } else {
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-private Map<RemotePackage, InstallResultType> installRemotePackages(

+private boolean installRemotePackages(

             @NonNull List<RemotePackage> requestPackages,

             @NonNull RepoManager repoManager,

             @NonNull Downloader downloader,

@@ -7,31 +7,31 @@
         List<RemotePackage> remotePackages =

                 InstallerUtil.computeRequiredPackages(

                         requestPackages, repoManager.getPackages(), progress);

-        Map<RemotePackage, InstallResultType> installResults = new HashMap<>();

 

         if (remotePackages == null) {

-            requestPackages.forEach(p -> installResults.put(p, InstallResultType.INSTALL_FAIL));

+            return false;

+        }

 

-        } else {

-            for (RemotePackage p : remotePackages) {

-                if (p.getLicense() != null && !p.getLicense()

-                        .checkAccepted(repoManager.getLocalPath(), mSdkHandler.getFileOp())) {

-                    progress.setText(

-                            "The license for package " + p.getDisplayName() + " was not accepted. "

-                                    + "Please install this package through Android Studio SDK "

-                                    + "Manager.");

-                    installResults.put(p, InstallResultType.LICENSE_FAIL);

-                } else {

-                    Installer installer = SdkInstallerUtil

-                            .findBestInstallerFactory(p, mSdkHandler)

-                            .createInstaller(p, repoManager, downloader, mSdkHandler.getFileOp());

-                    if (installer.prepare(progress) && installer.complete(progress)) {

-                        installResults.put(p, InstallResultType.SUCCESS);

-                    } else {

-                        installResults.put(p, InstallResultType.INSTALL_FAIL);

-                    }

-                }

+        for (RemotePackage p : remotePackages) {

+            if (p.getLicense() != null && !p.getLicense().checkAccepted(

```

---

### [52/100] `Summary_104`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.0773 |
| SARI | 0.4742 |
| GLEU | 0.1818 |
| METEOR | 0.5357 |
| xMatch | ✗ |

**原注释 (source)**
```
Creates a renderscript allocation from a bitmap
```

**标准注释 (ground truth)**
```
Creates an Allocation from a  android.graphics.Bitmap.
```

**生成注释 (generated)**
```
Creates a renderscript allocation from a bitmap
```

**当前代码 (new_code)**
```java
    static public Allocation createFromBitmap(RenderScript rs, Bitmap b,
                                              MipmapControl mips,
                                              int usage) {
        if (rs.isNative) {
            RenderScriptThunker rst = (RenderScriptThunker)rs;
            return AllocationThunker.createFromBitmap(rst, b, mips, usage);
        }
        rs.validate();

        // WAR undocumented color formats
        if (b.getConfig() == null) {
            if ((usage & USAGE_SHARED) != 0) {
                throw new RSIllegalArgumentException("USAGE_SHARED cannot be used with a Bitmap that has a null config.");
            }
            Bitmap newBitmap = Bitmap.createBitmap(b.getWidth(), b.getHeight(), Bitmap.Config.ARGB_8888);
            Canvas c = new Canvas(newBitmap);
            c.drawBitmap(b, 0, 0, null);
            return createFromBitmap(rs, newBitmap, mips, usage);
        }

        Type t = typeFromBitmap(rs, b, mips);

        // enable optimized bitmap path only with no mipmap and script-only usage
        if (mips == MipmapControl.MIPMAP_NONE &&
            t.getElement().isCompatible(Element.RGBA_8888(rs)) &&
            usage == (USAGE_SHARED | USAGE_SCRIPT)) {
            int id = rs.nAllocationCreateBitmapBackedAllocation(t.getID(rs), mips.mID, b, usage);
            if (id == 0) {
                throw new RSRuntimeException("Load failed.");
            }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    static public Allocation createFromBitmap(RenderScript rs, Bitmap b,
                                              MipmapControl mips,
                                              int usage) {
        rs.validate();
        Type t = typeFromBitmap(rs, b, mips);

        int id = rs.nAllocationCreateFromBitmap(t.getID(rs), mips.mID, b, usage);
        if (id == 0) {
            throw new RSRuntimeException("Load failed.");
        }
        return new Allocation(id, rs, t, usage);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,40 @@
 static public Allocation createFromBitmap(RenderScript rs, Bitmap b,

                                               MipmapControl mips,

                                               int usage) {

+        if (rs.isNative) {

+            RenderScriptThunker rst = (RenderScriptThunker)rs;

+            return AllocationThunker.createFromBitmap(rst, b, mips, usage);

+        }

         rs.validate();

+

+        // WAR undocumented color formats

+        if (b.getConfig() == null) {

+            if ((usage & USAGE_SHARED) != 0) {

+                throw new RSIllegalArgumentException("USAGE_SHARED cannot be used with a Bitmap that has a null config.");

+            }

+            Bitmap newBitmap = Bitmap.createBitmap(b.getWidth(), b.getHeight(), Bitmap.Config.ARGB_8888);

+            Canvas c = new Canvas(newBitmap);

+            c.drawBitmap(b, 0, 0, null);

+            return createFromBitmap(rs, newBitmap, mips, usage);

+        }

+

         Type t = typeFromBitmap(rs, b, mips);

+

+        // enable optimized bitmap path only with no mipmap and script-only usage

+        if (mips == MipmapControl.MIPMAP_NONE &&

+            t.getElement().isCompatible(Element.RGBA_8888(rs)) &&

+            usage == (USAGE_SHARED | USAGE_SCRIPT)) {

+            int id = rs.nAllocationCreateBitmapBackedAllocation(t.getID(rs), mips.mID, b, usage);

+            if (id == 0) {

+                throw new RSRuntimeException("Load failed.");

+            }

+

+            // keep a reference to the Bitmap around to prevent GC

+            Allocation alloc = new Allocation(id, rs, t, usage);

+            alloc.setBitmap(b);

+            return alloc;

+        }

+

```

---

### [33/100] `Summary_65`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4903 |
| SARI | 0.4769 |
| GLEU | 0.5238 |
| METEOR | 0.7486 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns all currently displayed sentences in plain text form.
```

**标准注释 (ground truth)**
```
Returns all currently displayed sentences in string buffer, plain text form
```

**生成注释 (generated)**
```
Returns all currently displayed sentences in plain text buffer.
```

**当前代码 (new_code)**
```java
  public StringBuffer getMatchedSentences() {
    StringBuffer sb = new StringBuffer();
    for(int i = 0; i < list.getModel().getSize(); i++) {
      String t = ((TreeFromFile) list.getModel().getElementAt(i)).getLabel().getText();
      sb.append(t);
      sb.append("\n");
    }
    return sb;
  }


```

**变更前代码 (old_code)**
```java
  public String getMatchedSentences() {
    StringBuilder sb = new StringBuilder();
    for (int i = 0, sz = list.getModel().getSize(); i < sz; i++) {
      String t = ((TreeFromFile) list.getModel().getElementAt(i)).getLabel().getText();
      sb.append(t);
      sb.append("\n");
    }
    return sb.toString();
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,9 @@
-public String getMatchedSentences() {

-    StringBuilder sb = new StringBuilder();

-    for (int i = 0, sz = list.getModel().getSize(); i < sz; i++) {

+public StringBuffer getMatchedSentences() {

+    StringBuffer sb = new StringBuffer();

+    for(int i = 0; i < list.getModel().getSize(); i++) {

       String t = ((TreeFromFile) list.getModel().getElementAt(i)).getLabel().getText();

       sb.append(t);

       sb.append("\n");

     }

-    return sb.toString();

+    return sb;

   }
```

---

### [96/100] `Summary_194`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.0418 |
| SARI | 0.4931 |
| GLEU | 0.0882 |
| METEOR | 0.3099 |
| xMatch | ✗ |

**原注释 (source)**
```
Checks if toolitem is selected
```

**标准注释 (ground truth)**
```
Finds out whether specified  ToolItem is selected or not.
```

**生成注释 (generated)**
```
Checks if toolitem is selected
```

**当前代码 (new_code)**
```java
	public boolean isSelected(final ToolItem toolItem) {
		boolean selectionState = Display.syncExec(new ResultRunnable<Boolean>() {
			@Override
			public Boolean run() {
					return toolItem.getSelection(); 
			}
		});
		return selectionState;
	}


```

**变更前代码 (old_code)**
```java
	public boolean isSelected(final ToolItem w) {
		boolean selectionState = Display.syncExec(new ResultRunnable<Boolean>() {
			@Override
			public Boolean run() {
					return w.getSelection(); 
			}
		});
		return selectionState;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,8 @@
-public boolean isSelected(final ToolItem w) {

+public boolean isSelected(final ToolItem toolItem) {

 		boolean selectionState = Display.syncExec(new ResultRunnable<Boolean>() {

 			@Override

 			public Boolean run() {

-					return w.getSelection(); 

+					return toolItem.getSelection(); 

 			}

 		});

 		return selectionState;

```

---

### [98/100] `Summary_199`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7918 |
| SARI | 0.5217 |
| GLEU | 0.7982 |
| METEOR | 0.9272 |
| xMatch | ✗ |

**原注释 (source)**
```
Convert an object that may or may not be a JSONArray or JSONObject into its JSON string representation, handling the case where it is neither in a graceful way.
```

**标准注释 (ground truth)**
```
Convert an object that may or may not be a JsonElement into its JSON string representation, handling the case where it is neither in a graceful way.
```

**生成注释 (generated)**
```
Convert an object that may or may not be a JSON type into its JSON string representation, handling the case where it is neither in a serialized way.
```

**当前代码 (new_code)**
```java
  public String convert(Object object) {
    if (object == null) {
      return null;
    }

    try {
      JsonElement json = convertObject(object);
      return new GsonBuilder().serializeNulls().create().toJson(json);
    } catch (Exception e) {
      throw new WebDriverException("Unable to convert: " + object, e);
    }
  }

```

**变更前代码 (old_code)**
```java
  public String convert(Object object) {
    if (object == null) {
      return null;
    }

    try {
      Object converted = convertObject(object, MAX_DEPTH);
      if (converted instanceof JSONObject
          || converted instanceof JSONArray
          || converted instanceof String
          || converted instanceof Number) {
        return converted.toString();
      }

      return String.valueOf(object);
    } catch (Exception e) {
      throw new WebDriverException("Unable to convert: " + object, e);
    }
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -4,15 +4,8 @@
     }

 

     try {

-      Object converted = convertObject(object, MAX_DEPTH);

-      if (converted instanceof JSONObject

-          || converted instanceof JSONArray

-          || converted instanceof String

-          || converted instanceof Number) {

-        return converted.toString();

-      }

-

-      return String.valueOf(object);

+      JsonElement json = convertObject(object);

+      return new GsonBuilder().serializeNulls().create().toJson(json);

     } catch (Exception e) {

       throw new WebDriverException("Unable to convert: " + object, e);

     }

```

---

### [81/100] `Summary_164`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3976 |
| SARI | 0.5270 |
| GLEU | 0.6000 |
| METEOR | 0.7361 |
| xMatch | ✗ |

**原注释 (source)**
```
Invoke the proprietary  CometSupport
```

**标准注释 (ground truth)**
```
Invoke the proprietary  AsyncSupport
```

**生成注释 (generated)**
```
Invoke the proprietary  CometSupport
```

**当前代码 (new_code)**
```java
    public Action doCometSupport(AtmosphereRequest req, AtmosphereResponse res) throws IOException, ServletException {
        req.setAttribute(BROADCASTER_FACTORY, broadcasterFactory);
        req.setAttribute(PROPERTY_USE_STREAM, useStreamForFlushingComments);
        req.setAttribute(BROADCASTER_CLASS, broadcasterClassName);
        req.setAttribute(ATMOSPHERE_CONFIG, config);

        Action a = null;
        try {
            if ((config.getInitParameter(ALLOW_QUERYSTRING_AS_REQUEST) != null
                    || (isIECandidate(req) || req.getParameter(HeaderConfig.JSONP_CALLBACK_NAME) != null))
                    && req.getAttribute(WebSocket.WEBSOCKET_SUSPEND) == null) {

                Map<String, String> headers = configureQueryStringAsRequest(req);
                String body = headers.remove(ATMOSPHERE_POST_BODY);
                if (body != null && body.isEmpty()) {
                    body = null;
                }

                req.headers(headers)
                   .method(body != null && req.getMethod().equalsIgnoreCase("GET") ? "POST" : req.getMethod());

                if (body != null) {
                   req.body(body);
                }

                a = asyncSupport.service(req, res);
            } else {
                return asyncSupport.service(req, res);
            }
        } catch (IllegalStateException ex) {
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public Action doCometSupport(AtmosphereRequest req, AtmosphereResponse res) throws IOException, ServletException {
        req.setAttribute(BROADCASTER_FACTORY, broadcasterFactory);
        req.setAttribute(PROPERTY_USE_STREAM, useStreamForFlushingComments);
        req.setAttribute(BROADCASTER_CLASS, broadcasterClassName);
        req.setAttribute(ATMOSPHERE_CONFIG, config);

        Action a = null;
        try {
            if ((config.getInitParameter(ALLOW_QUERYSTRING_AS_REQUEST) != null
                    || (isIECandidate(req) || req.getParameter(HeaderConfig.JSONP_CALLBACK_NAME) != null))
                    && req.getAttribute(WebSocket.WEBSOCKET_SUSPEND) == null) {

                Map<String, String> headers = configureQueryStringAsRequest(req);
                String body = headers.remove(ATMOSPHERE_POST_BODY);
                if (body != null && body.isEmpty()) {
                    body = null;
                }

                req.headers(headers)
                   .method(body != null && req.getMethod().equalsIgnoreCase("GET") ? "POST" : req.getMethod());

                if (body != null) {
                   req.body(body);
                }

                a = cometSupport.service(req, res);
            } else {
                return cometSupport.service(req, res);
            }
        } catch (IllegalStateException ex) {
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -23,20 +23,20 @@
                    req.body(body);

                 }

 

-                a = cometSupport.service(req, res);

+                a = asyncSupport.service(req, res);

             } else {

-                return cometSupport.service(req, res);

+                return asyncSupport.service(req, res);

             }

         } catch (IllegalStateException ex) {

             if (ex.getMessage() != null && (ex.getMessage().startsWith("Tomcat failed") || ex.getMessage().startsWith("JBoss failed") )) {

                 if (!isFilter) {

-                    logger.warn("Failed using comet support: {}, error: {} Is the Nio or Apr Connector enabled?", cometSupport.getClass().getName(),

+                    logger.warn("Failed using comet support: {}, error: {} Is the Nio or Apr Connector enabled?", asyncSupport.getClass().getName(),

                             ex.getMessage());

                     logger.warn("Using BlockingIOCometSupport.");

                 }

                 logger.trace(ex.getMessage(), ex);

 

-                cometSupport = new BlockingIOCometSupport(config);

+                asyncSupport = new BlockingIOCometSupport(config);

                 doCometSupport(req, res);

             } else {

                 logger.error("AtmosphereServlet exception", ex);

```

---

### [79/100] `Summary_160`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3365 |
| SARI | 0.5310 |
| GLEU | 0.3519 |
| METEOR | 0.6069 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns collection containing all existing Simons matching the pattern (can be  null).
```

**标准注释 (ground truth)**
```
Returns collection containing all existing Simons accepted by specified  SimonFilter.
```

**生成注释 (generated)**
```
Returns collection containing all existing Simons matching the filter (can be null).
```

**当前代码 (new_code)**
```java
	public static Collection<Simon> getSimons(SimonFilter simonFilter) {
		return manager.getSimons(simonFilter);
	}


```

**变更前代码 (old_code)**
```java
	public static Collection<Simon> getSimons(SimonPattern pattern) {
		return manager.getSimons(pattern);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static Collection<Simon> getSimons(SimonPattern pattern) {

-		return manager.getSimons(pattern);

+public static Collection<Simon> getSimons(SimonFilter simonFilter) {

+		return manager.getSimons(simonFilter);

 	}
```

---

### [9/100] `Summary_16`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3552 |
| SARI | 0.5421 |
| GLEU | 0.3889 |
| METEOR | 0.5894 |
| xMatch | ✗ |

**原注释 (source)**
```
Create a web page using the given template,  SecurityContext and model data.
```

**标准注释 (ground truth)**
```
Create the web page using the given template and  SecurityContext after authentication is done.
```

**生成注释 (generated)**
```
Create a web page using the given template, SecurityContext.
```

**当前代码 (new_code)**
```java
  public static Viewable create(final boolean authEnabled, final String templateName, final SecurityContext sc) {
    return new ViewableWithPermissions(authEnabled, templateName, sc, true, null);
  }

```

**变更前代码 (old_code)**
```java
  public static Viewable create(final String templateName, final SecurityContext sc, final Object model) {
    return new ViewableWithPermissions(templateName, sc, true, model);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static Viewable create(final String templateName, final SecurityContext sc, final Object model) {

-    return new ViewableWithPermissions(templateName, sc, true, model);

+public static Viewable create(final boolean authEnabled, final String templateName, final SecurityContext sc) {

+    return new ViewableWithPermissions(authEnabled, templateName, sc, true, null);

   }
```

---

### [66/100] `Summary_132`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4704 |
| SARI | 0.5508 |
| GLEU | 0.4783 |
| METEOR | 0.6560 |
| xMatch | ✗ |

**原注释 (source)**
```
prepares an url-encoded HTTP queryString containing the group/job and the options.
```

**标准注释 (ground truth)**
```
prepare the  HttpClient's queryString containing the group/job and the options.
```

**生成注释 (generated)**
```
prepares an array of name-value pairs containing the group/job and the options.
```

**当前代码 (new_code)**
```java
    private NameValuePair[] prepareQueryString(String groupPath, String jobName, Properties options) {
        List<NameValuePair> queryString = new ArrayList<NameValuePair>();

        queryString.add(new NameValuePair("groupPath", groupPath));
        queryString.add(new NameValuePair("jobName", jobName));

        if (options != null) {
            for (Entry<Object, Object> option : options.entrySet()) {
                queryString.add(new NameValuePair("extra.command.option." + option.getKey(),
                                                  String.valueOf(option.getValue())));
            }
        }

        return queryString.toArray(new NameValuePair[queryString.size()]);
    }


```

**变更前代码 (old_code)**
```java
    private String prepareQueryString(String groupPath, String jobName, Properties options) {
        List<NameValuePair> parameters = new ArrayList<NameValuePair>();

        parameters.add(new BasicNameValuePair("groupPath", groupPath));
        parameters.add(new BasicNameValuePair("jobName", jobName));

        if (options != null) {
            for (Entry<Object, Object> option : options.entrySet()) {
                parameters.add(new BasicNameValuePair("extra.command.option." + option.getKey(),
                                                      String.valueOf(option.getValue())));
            }
        }

        return URLEncodedUtils.format(parameters, HTTP.UTF_8);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,15 +1,15 @@
-private String prepareQueryString(String groupPath, String jobName, Properties options) {

-        List<NameValuePair> parameters = new ArrayList<NameValuePair>();

+private NameValuePair[] prepareQueryString(String groupPath, String jobName, Properties options) {

+        List<NameValuePair> queryString = new ArrayList<NameValuePair>();

 

-        parameters.add(new BasicNameValuePair("groupPath", groupPath));

-        parameters.add(new BasicNameValuePair("jobName", jobName));

+        queryString.add(new NameValuePair("groupPath", groupPath));

+        queryString.add(new NameValuePair("jobName", jobName));

 

         if (options != null) {

             for (Entry<Object, Object> option : options.entrySet()) {

-                parameters.add(new BasicNameValuePair("extra.command.option." + option.getKey(),

-                                                      String.valueOf(option.getValue())));

+                queryString.add(new NameValuePair("extra.command.option." + option.getKey(),

+                                                  String.valueOf(option.getValue())));

             }

         }

 

-        return URLEncodedUtils.format(parameters, HTTP.UTF_8);

+        return queryString.toArray(new NameValuePair[queryString.size()]);

     }
```

---

### [85/100] `Summary_172`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.2272 |
| SARI | 0.5542 |
| GLEU | 0.3000 |
| METEOR | 0.8721 |
| xMatch | ✗ |

**原注释 (source)**
```
Helper method to return the constant string for a  CstInsn in human form.
```

**标准注释 (ground truth)**
```
Helper method to return a constant string.
```

**生成注释 (generated)**
```
Helper method to return the constant string for a  CstInsn in human form.
```

**当前代码 (new_code)**
```java
    protected static String cstString(DalvInsn insn) {
        CstInsn ci = (CstInsn) insn;
        Constant cst = ci.getConstant();

        return cst.toHuman();
    }


```

**变更前代码 (old_code)**
```java
    protected static String cstString(DalvInsn insn) {
        CstInsn ci = (CstInsn) insn;
        Constant cst = ci.getConstant();

        return cst instanceof CstString ? ((CstString) cst).toQuoted() : cst.toHuman();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -2,5 +2,5 @@
         CstInsn ci = (CstInsn) insn;

         Constant cst = ci.getConstant();

 

-        return cst instanceof CstString ? ((CstString) cst).toQuoted() : cst.toHuman();

+        return cst.toHuman();

     }
```

---

### [53/100] `Summary_106`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5266 |
| SARI | 0.5646 |
| GLEU | 0.5870 |
| METEOR | 0.8376 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns the sibling on the right of the end of given  Treepath.
```

**标准注释 (ground truth)**
```
Returns the sibling on the left of the bottom of given  Treepath.
```

**生成注释 (generated)**
```
Returns the sibling on the right of the end of given  Treepath.
```

**当前代码 (new_code)**
```java
  public static Treepath getNextSibling( Treepath treepath ) {
    if( treepath.getHeight() < 2 ) {
      throw new IllegalArgumentException( "Treepath must have minimum height of 2" ) ;
    }
    final Tree treeToMove = treepath.getBottom() ;
    final Tree parent = treepath.getTreeAtHeight( 1 ) ;
    for( int i = 0 ; i < parent.getChildCount() - 1 ; i++ ) {
      final Tree child = parent.getChildAt( i ) ;
      if( child == treeToMove ) {
        return Treepath.create( treepath.getParent(), parent.getChildAt( i + 1 ) ) ;
      }
    }
    throw new IllegalArgumentException( "No next sibling" ) ;
  }


```

**变更前代码 (old_code)**
```java
  public static Treepath getNextSibling( Treepath treepath ) {
    throw new UnsupportedOperationException( "getNextSibling" ) ;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,14 @@
 public static Treepath getNextSibling( Treepath treepath ) {

-    throw new UnsupportedOperationException( "getNextSibling" ) ;

+    if( treepath.getHeight() < 2 ) {

+      throw new IllegalArgumentException( "Treepath must have minimum height of 2" ) ;

+    }

+    final Tree treeToMove = treepath.getBottom() ;

+    final Tree parent = treepath.getTreeAtHeight( 1 ) ;

+    for( int i = 0 ; i < parent.getChildCount() - 1 ; i++ ) {

+      final Tree child = parent.getChildAt( i ) ;

+      if( child == treeToMove ) {

+        return Treepath.create( treepath.getParent(), parent.getChildAt( i + 1 ) ) ;

+      }

+    }

+    throw new IllegalArgumentException( "No next sibling" ) ;

   }
```

---

### [30/100] `Summary_58`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5703 |
| SARI | 0.5753 |
| GLEU | 0.5926 |
| METEOR | 0.8308 |
| xMatch | ✗ |

**原注释 (source)**
```
Creates and returns a new comparison object for the SQL "in" operator.
```

**标准注释 (ground truth)**
```
Creates and returns an expression for the SQL "in" operator.
```

**生成注释 (generated)**
```
Creates and returns a new comparison object for the SQL "in" operator.
```

**当前代码 (new_code)**
```java
    public final DBCompareColExpr in(Collection<?> values)
    {
        if (values==null || values.isEmpty())
            return cmp(DBCmpType.EQUAL, null);
        // create expression
        return cmp(DBCmpType.IN, values);
    }


```

**变更前代码 (old_code)**
```java
    public DBCompareColExpr in(Object value)
    {
        return cmp(DBCmpType.IN, listToArray(value));
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,7 @@
-public DBCompareColExpr in(Object value)

+public final DBCompareColExpr in(Collection<?> values)

     {

-        return cmp(DBCmpType.IN, listToArray(value));

+        if (values==null || values.isEmpty())

+            return cmp(DBCmpType.EQUAL, null);

+        // create expression

+        return cmp(DBCmpType.IN, values);

     }
```

---

### [40/100] `Summary_79`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5510 |
| SARI | 0.5834 |
| GLEU | 0.5952 |
| METEOR | 0.8290 |
| xMatch | ✗ |

**原注释 (source)**
```
Does this time interval contain the specified time interval completely.
```

**标准注释 (ground truth)**
```
Does this time interval contain or equal the specified time interval.
```

**生成注释 (generated)**
```
Does this time interval contain the specified time interval completely.
```

**当前代码 (new_code)**
```java
    public boolean contains(ReadableInterval interval) {
        if (interval == null) {
            return containsNow();
        }
        long otherStart = interval.getStartMillis();
        long otherEnd = interval.getEndMillis();
        long thisStart = getStartMillis();
        long thisEnd = getEndMillis();
        return (thisStart <= otherStart && otherStart < thisEnd && otherEnd <= thisEnd) ||
            (thisStart == otherStart && thisEnd == otherEnd);
    }

```

**变更前代码 (old_code)**
```java
    public boolean contains(ReadableInterval interval) {
        if (interval == null) {
            return containsNow();
        }
        long otherStart = interval.getStartMillis();
        long otherEnd = interval.getEndMillis();
        long thisStart = getStartMillis();
        long thisEnd = getEndMillis();
        return (otherStart >= thisStart && otherStart < thisEnd && otherEnd <= thisEnd);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -6,5 +6,6 @@
         long otherEnd = interval.getEndMillis();

         long thisStart = getStartMillis();

         long thisEnd = getEndMillis();

-        return (otherStart >= thisStart && otherStart < thisEnd && otherEnd <= thisEnd);

+        return (thisStart <= otherStart && otherStart < thisEnd && otherEnd <= thisEnd) ||

+            (thisStart == otherStart && thisEnd == otherEnd);

     }
```

---

### [90/100] `Summary_182`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5342 |
| SARI | 0.5855 |
| GLEU | 0.5882 |
| METEOR | 0.8018 |
| xMatch | ✗ |

**原注释 (source)**
```
Tests if the editor is in word-wrap mode.
```

**标准注释 (ground truth)**
```
Tests if the text area is in word-wrap mode.
```

**生成注释 (generated)**
```
Tests if the editor is in word-wrap mode.
```

**当前代码 (new_code)**
```java
    public boolean isWordwrap() {
        return wordwrap;
    }


```

**变更前代码 (old_code)**
```java
    @Override
    public boolean isWordwrap() {
        // TODO implement here once the API from TextField is removed
        return super.isWordwrap();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,3 @@
-@Override

-    public boolean isWordwrap() {

-        // TODO implement here once the API from TextField is removed

-        return super.isWordwrap();

+public boolean isWordwrap() {

+        return wordwrap;

     }
```

---

### [88/100] `Summary_178`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4373 |
| SARI | 0.5863 |
| GLEU | 0.4565 |
| METEOR | 0.6424 |
| xMatch | ✗ |

**原注释 (source)**
```
Create and return a new Field instance that that is a copy of this field but that uses the supplied predicate during  Field#validate(Configuration, Consumer).
```

**标准注释 (ground truth)**
```
Create and return a new Field instance that is a copy of this field but that in addition to  #validator() existing validation the supplied validation function(s) are also used.
```

**生成注释 (generated)**
```
Create and return a new Field instance that that is a copy of this field but that uses the supplied validator during Field#validate(Configuration, Consumer).
```

**当前代码 (new_code)**
```java
    public Field withValidation(Validator... validators) {
        Validator actualValidator = validator;
        for (Validator validator : validators) {
            if (validator != null) actualValidator = validator.and(actualValidator);
        }
        return new Field(name(), displayName(), type(), width(), description(), importance(), dependents,
                defaultValueGenerator, actualValidator, recommender);
    }

```

**变更前代码 (old_code)**
```java
    public Field withValidation(Predicate<String>... predicates) {
        return new Field(name(), description(), defaultValueGenerator, (config, field, problems) -> {
            String value = config.getString(field);
            for (Predicate<String> predicate : predicates) {
                if (predicate != null) {
                    try {
                        if (!predicate.test(value)) {
                            problems.accept("The " + field.name() + " value '" + value + "' is not valid");
                            return 1;
                        }
                    } catch (Throwable t) {
                        problems.accept("The " + field.name() + " value '" + value + "' is not allowed: " + t.getMessage());
                        return 1;
                    }
                }
            }
            return 0;
        });
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,19 +1,8 @@
-public Field withValidation(Predicate<String>... predicates) {

-        return new Field(name(), description(), defaultValueGenerator, (config, field, problems) -> {

-            String value = config.getString(field);

-            for (Predicate<String> predicate : predicates) {

-                if (predicate != null) {

-                    try {

-                        if (!predicate.test(value)) {

-                            problems.accept("The " + field.name() + " value '" + value + "' is not valid");

-                            return 1;

-                        }

-                    } catch (Throwable t) {

-                        problems.accept("The " + field.name() + " value '" + value + "' is not allowed: " + t.getMessage());

-                        return 1;

-                    }

-                }

-            }

-            return 0;

-        });

+public Field withValidation(Validator... validators) {

+        Validator actualValidator = validator;

+        for (Validator validator : validators) {

+            if (validator != null) actualValidator = validator.and(actualValidator);

+        }

+        return new Field(name(), displayName(), type(), width(), description(), importance(), dependents,

+                defaultValueGenerator, actualValidator, recommender);

     }
```

---

### [56/100] `Summary_112`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5153 |
| SARI | 0.5959 |
| GLEU | 0.5370 |
| METEOR | 0.7206 |
| xMatch | ✗ |

**原注释 (source)**
```
Looks up a field with a given name and if found returns its ordinal.
```

**标准注释 (ground truth)**
```
Looks up a field with a given name, returning null if not found.
```

**生成注释 (generated)**
```
Looks up a field with a given name and if found returns the field.
```

**当前代码 (new_code)**
```java
    public static RelDataTypeField lookupField(
        final RelDataType rowType,
        String columnName)
    {
        final RelDataTypeField [] fields = rowType.getFields();
        for (int i = 0; i < fields.length; i++) {
            RelDataTypeField field = fields[i];
            if (field.getName().equals(columnName)) {
                return field;
            }
        }
        return null;
    }


```

**变更前代码 (old_code)**
```java
    public static int lookupField(
        final RelDataType rowType,
        String columnName)
    {
        final RelDataTypeField [] fields = rowType.getFields();
        for (int i = 0; i < fields.length; i++) {
            RelDataTypeField field = fields[i];
            if (field.getName().equals(columnName)) {
                return i;
            }
        }
        return -1;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public static int lookupField(

+public static RelDataTypeField lookupField(

         final RelDataType rowType,

         String columnName)

     {

@@ -6,8 +6,8 @@
         for (int i = 0; i < fields.length; i++) {

             RelDataTypeField field = fields[i];

             if (field.getName().equals(columnName)) {

-                return i;

+                return field;

             }

         }

-        return -1;

+        return null;

     }
```

---

### [84/100] `Summary_170`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3792 |
| SARI | 0.5977 |
| GLEU | 0.4194 |
| METEOR | 0.6016 |
| xMatch | ✗ |

**原注释 (source)**
```
Given a URL, attempt to infer and return the hostname from the URL.
```

**标准注释 (ground truth)**
```
Given a URL, attempt to return the host portion (not including the port).
```

**生成注释 (generated)**
```
Given a URL, attempt to infer and return the host from the URL.
```

**当前代码 (new_code)**
```java
   public static String getHostFromUrl(String url)
   {
      String authority = getAuthorityFromUrl(url);
      
      // no port
      int idx = authority.indexOf(":");
      if (idx == -1)
         return authority;
      
      // port, return only the portion preceding the port
      return authority.substring(0, idx);
   }

```

**变更前代码 (old_code)**
```java
   public static String getHostFromUrl(String url)
   {
      // no work to do
      if (url.indexOf('/') == -1)
         return url;
      
      // presume no protocol; if present, skip those slashes
      int slashes = 0;
      if (url.contains("://"))
         slashes += 2;
      
      // split on slashes and return first component
      String[] parts = url.split("/");
      if (parts.length < slashes)
         return url;
      return parts[slashes];
   }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,17 +1,12 @@
 public static String getHostFromUrl(String url)

    {

-      // no work to do

-      if (url.indexOf('/') == -1)

-         return url;

+      String authority = getAuthorityFromUrl(url);

       

-      // presume no protocol; if present, skip those slashes

-      int slashes = 0;

-      if (url.contains("://"))

-         slashes += 2;

+      // no port

+      int idx = authority.indexOf(":");

+      if (idx == -1)

+         return authority;

       

-      // split on slashes and return first component

-      String[] parts = url.split("/");

-      if (parts.length < slashes)

-         return url;

-      return parts[slashes];

+      // port, return only the portion preceding the port

+      return authority.substring(0, idx);

    }
```

---

### [87/100] `Summary_176`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3656 |
| SARI | 0.6027 |
| GLEU | 0.4231 |
| METEOR | 0.9132 |
| xMatch | ✗ |

**原注释 (source)**
```
Gets an integer value of the request method.
```

**标准注释 (ground truth)**
```
Gets the request method.
```

**生成注释 (generated)**
```
Gets a Method of the request method.
```

**当前代码 (new_code)**
```java
    public Method getMethod() {
        return method;
    }


```

**变更前代码 (old_code)**
```java
    public int getMethod() {
        return method;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public int getMethod() {

+public Method getMethod() {

         return method;

     }
```

---

### [31/100] `Summary_61`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5877 |
| SARI | 0.6132 |
| GLEU | 0.6316 |
| METEOR | 0.8862 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns all currently displayed sentences in string buffer, plain text form
```

**标准注释 (ground truth)**
```
Returns all currently displayed sentences in plain text form.
```

**生成注释 (generated)**
```
Returns all currently displayed sentences in string, plain text form
```

**当前代码 (new_code)**
```java
  public String getMatchedSentences() {
    StringBuilder sb = new StringBuilder();
    for (int i = 0, sz = list.getModel().getSize(); i < sz; i++) {
      String t = list.getModel().getElementAt(i).getLabel().getText();
      sb.append(t);
      sb.append("\n");
    }
    return sb.toString();
  }


```

**变更前代码 (old_code)**
```java
  public StringBuffer getMatchedSentences() {
    StringBuffer sb = new StringBuffer();
    for(int i = 0; i < list.getModel().getSize(); i++) {
      String t = ((TreeFromFile) list.getModel().getElementAt(i)).getLabel().getText();
      sb.append(t);
      sb.append("\n");
    }
    return sb;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,9 @@
-public StringBuffer getMatchedSentences() {

-    StringBuffer sb = new StringBuffer();

-    for(int i = 0; i < list.getModel().getSize(); i++) {

-      String t = ((TreeFromFile) list.getModel().getElementAt(i)).getLabel().getText();

+public String getMatchedSentences() {

+    StringBuilder sb = new StringBuilder();

+    for (int i = 0, sz = list.getModel().getSize(); i < sz; i++) {

+      String t = list.getModel().getElementAt(i).getLabel().getText();

       sb.append(t);

       sb.append("\n");

     }

-    return sb;

+    return sb.toString();

   }
```

---

### [43/100] `Summary_85`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.7064 |
| SARI | 0.6161 |
| GLEU | 0.7111 |
| METEOR | 0.7913 |
| xMatch | ✗ |

**原注释 (source)**
```
Gets the total number of bytes uploaded by this uploader or  0 for direct uploads when the content length is not known.
```

**标准注释 (ground truth)**
```
Gets the total number of bytes the server received so far or  0 for direct uploads when the content length is not known.
```

**生成注释 (generated)**
```
Gets the total number of bytes uploaded by this uploader or  0 for direct uploads when the content length is not known.
```

**当前代码 (new_code)**
```java
  @Deprecated
  public long getNumBytesUploaded() {
    return totalBytesServerReceived;
  }


```

**变更前代码 (old_code)**
```java
  public long getNumBytesUploaded() {
    return bytesUploaded;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,4 @@
-public long getNumBytesUploaded() {

-    return bytesUploaded;

+@Deprecated

+  public long getNumBytesUploaded() {

+    return totalBytesServerReceived;

   }
```

---

### [39/100] `Summary_77`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4374 |
| SARI | 0.6161 |
| GLEU | 0.4524 |
| METEOR | 0.5425 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns the common base directory between a current base directory and a given file.
```

**标准注释 (ground truth)**
```
Returns the common base directory between the passed file1 and file2.
```

**生成注释 (generated)**
```
Returns the common base directory between two files.
```

**当前代码 (new_code)**
```java
    File getBaseDir(final File file1, final File file2) {
        if (file1 == null || file2 == null) {
            return null;
        }
        final Iterator bases = getParents(file1).iterator();
        final Iterator fileParents = getParents(file2.getAbsoluteFile()).iterator();
        File result = null;
        while (bases.hasNext() && fileParents.hasNext()) {
            File next = (File) bases.next();
            if (next.equals(fileParents.next())) {
                result = next;
            } else {
                break;
            }
        }
        return result;
    }


```

**变更前代码 (old_code)**
```java
    File getBaseDir(File base, File file) {
        if (base == null) {
            return file.getParentFile().getAbsoluteFile();
        } else {
            Iterator bases = getParents(base).iterator();
            Iterator fileParents = getParents(file.getAbsoluteFile()).iterator();
            File result = null;
            while (bases.hasNext() && fileParents.hasNext()) {
                File next = (File) bases.next();
                if (next.equals(fileParents.next())) {
                    result = next;
                } else {
                    break;
                }
            }
            return result;
        }
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,18 +1,17 @@
-File getBaseDir(File base, File file) {

-        if (base == null) {

-            return file.getParentFile().getAbsoluteFile();

-        } else {

-            Iterator bases = getParents(base).iterator();

-            Iterator fileParents = getParents(file.getAbsoluteFile()).iterator();

-            File result = null;

-            while (bases.hasNext() && fileParents.hasNext()) {

-                File next = (File) bases.next();

-                if (next.equals(fileParents.next())) {

-                    result = next;

-                } else {

-                    break;

-                }

+File getBaseDir(final File file1, final File file2) {

+        if (file1 == null || file2 == null) {

+            return null;

+        }

+        final Iterator bases = getParents(file1).iterator();

+        final Iterator fileParents = getParents(file2.getAbsoluteFile()).iterator();

+        File result = null;

+        while (bases.hasNext() && fileParents.hasNext()) {

+            File next = (File) bases.next();

+            if (next.equals(fileParents.next())) {

+                result = next;

+            } else {

+                break;

             }

-            return result;

         }

+        return result;

     }
```

---

### [19/100] `Summary_36`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.7012 |
| SARI | 0.6188 |
| GLEU | 0.7037 |
| METEOR | 0.9070 |
| xMatch | ✗ |

**原注释 (source)**
```
Method that get's left and right incoming batch and produce the output batch.
```

**标准注释 (ground truth)**
```
Gets the left and right incoming batch and produce the output batch.
```

**生成注释 (generated)**
```
Method that get's left and right incoming batch and produce the output batch.
```

**当前代码 (new_code)**
```java
  public IterOutcome innerNext() {

    if (hasRemainderForLeftJoin) { // if set that means there is spill over from previous left batch and no
      // corresponding right rows and it is left join scenario
      allocateVectors();

      boolean hasMoreRows = !handleRemainingLeftRows();
      if (leftUpstream == EMIT || hasMoreRows) {
        logger.debug("Sending current output batch with EMIT outcome since left is received with EMIT and is fully " +
          "consumed now in output batch");
        hasRemainderForLeftJoin = hasMoreRows;
        finalizeOutputContainer();
        return (leftUpstream == EMIT) ? EMIT : OK;
      } else {
        // release memory for previous left batch
        leftJoinIndex = -1;
        VectorAccessibleUtilities.clear(left);
      }
    }

    // We don't do anything special on FIRST state. Process left batch first and then right batch if need be
    IterOutcome childOutcome = processLeftBatch();
    logger.debug("Received left batch with outcome {}", childOutcome);

    if (processLeftBatchInFuture && hasRemainderForLeftJoin) {
      finalizeOutputContainer();
      hasRemainderForLeftJoin = false;
      return OK;
    }

// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public IterOutcome innerNext() {

    if (hasRemainderForLeftJoin) { // if set that means there is spill over from previous left batch and no
      // corresponding right rows and it is left join scenario
      allocateVectors();

      boolean hasMoreRows = !handleRemainingLeftRows();
      if (leftUpstream == EMIT || hasMoreRows) {
        logger.debug("Sending current output batch with EMIT outcome since left is received with EMIT and is fully " +
          "consumed now in output batch");
        hasRemainderForLeftJoin = hasMoreRows;
        finalizeOutputContainer();
        return (leftUpstream == EMIT) ? EMIT : OK;
      } else {
        // release memory for previous left batch
        leftJoinIndex = -1;
        VectorAccessibleUtilities.clear(left);
      }
    }

    // We don't do anything special on FIRST state. Process left batch first and then right batch if need be
    IterOutcome childOutcome = processLeftBatch();
    logger.debug("Received left batch with outcome {}", childOutcome);

    if (processLeftBatchInFuture && hasRemainderForLeftJoin) {
      finalizeOutputContainer();
      hasRemainderForLeftJoin = false;
      return OK;
    }

// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -58,8 +58,8 @@
     // If OK_NEW_SCHEMA is seen only on non empty left batch but not on right batch, then we should setup schema in

     // output container based on new left schema and old right schema. If schema change failed then return STOP

     // downstream

-    if (leftUpstream == OK_NEW_SCHEMA && !handleSchemaChange()) {

-      return STOP;

+    if (leftUpstream == OK_NEW_SCHEMA) {

+      handleSchemaChange();

     }

 

     // Setup the references of left, right and outgoing container in generated operator

```

---

### [45/100] `Summary_89`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.7911 |
| SARI | 0.6279 |
| GLEU | 0.8043 |
| METEOR | 0.9209 |
| xMatch | ✗ |

**原注释 (source)**
```
Create and return a new feature service with the default server URL.
```

**标准注释 (ground truth)**
```
Create and return a new feature service with the default endpoint URL.
```

**生成注释 (generated)**
```
Create and return a new feature service with the default server URL.
```

**当前代码 (new_code)**
```java
    public FeatureService createFeatureService() {
        return createFeatureService(defaultEndpointUrl);
    }


```

**变更前代码 (old_code)**
```java
    public FeatureService createFeatureService() {
        return createFeatureService(defaultServerUrl);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public FeatureService createFeatureService() {

-        return createFeatureService(defaultServerUrl);

+        return createFeatureService(defaultEndpointUrl);

     }
```

---

### [24/100] `Summary_46`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.6801 |
| SARI | 0.6360 |
| GLEU | 0.6905 |
| METEOR | 0.8441 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns if this query should buffer before emitting results.
```

**标准注释 (ground truth)**
```
Returns if this query should buffer before emitting the final results.
```

**生成注释 (generated)**
```
Returns if this query should buffer before emitting results.
```

**当前代码 (new_code)**
```java
    public boolean shouldBuffer() {
        Window window = runningQuery.getQuery().getWindow();
        boolean noWindow =  window == null;
        // Only buffer if there is no window (including Raw) or if it's a record based window.
        return noWindow || !window.isTimeBased();
    }


```

**变更前代码 (old_code)**
```java
    public boolean shouldBuffer() {
        Window window = runningQuery.getQuery().getWindow();
        boolean noWindow = window == null;
        // If it's a RAW query without a window, it should be buffered if and only if it timed out. This means that the
        // query is not yet done. So this tells the driver to buffer the query to wait for more potential results.
        if (noWindow && isRaw()) {
            return runningQuery.isTimedOut();
        }
        // No window (and not raw) is a duration based query => do buffer. Otherwise, buffer if the window is time based.
        return noWindow || window.isTimeBased();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,6 @@
 public boolean shouldBuffer() {

         Window window = runningQuery.getQuery().getWindow();

-        boolean noWindow = window == null;

-        // If it's a RAW query without a window, it should be buffered if and only if it timed out. This means that the

-        // query is not yet done. So this tells the driver to buffer the query to wait for more potential results.

-        if (noWindow && isRaw()) {

-            return runningQuery.isTimedOut();

-        }

-        // No window (and not raw) is a duration based query => do buffer. Otherwise, buffer if the window is time based.

-        return noWindow || window.isTimeBased();

+        boolean noWindow =  window == null;

+        // Only buffer if there is no window (including Raw) or if it's a record based window.

+        return noWindow || !window.isTimeBased();

     }
```

---

### [82/100] `Summary_166`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.8371 |
| SARI | 0.6370 |
| GLEU | 0.8448 |
| METEOR | 0.9364 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns the ScopeContext for the MODULE scope that will be associated with this deployment unit.
```

**标准注释 (ground truth)**
```
Returns the ScopeContainer for the MODULE scope that will be associated with this deployment unit.
```

**生成注释 (generated)**
```
Returns the ScopeContext for the MODULE scope that will be associated with this deployment unit.
```

**当前代码 (new_code)**
```java
    public ScopeContainer getModuleScope() {
        return moduleScope;
    }


```

**变更前代码 (old_code)**
```java
    public ScopeContext getModuleScope() {
        return moduleScope;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public ScopeContext getModuleScope() {

+public ScopeContainer getModuleScope() {

         return moduleScope;

     }
```

---

### [11/100] `Summary_20`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5133 |
| SARI | 0.6416 |
| GLEU | 0.5667 |
| METEOR | 0.7687 |
| xMatch | ✗ |

**原注释 (source)**
```
Add a tag to the set of filters
```

**标准注释 (ground truth)**
```
Add a tagId to the set of filters.
```

**生成注释 (generated)**
```
Add a tag ID to the set of filters
```

**当前代码 (new_code)**
```java
    public boolean add(String tagId, String category) {
        return isCategoryValid(category) && mSelectedTopics.add(tagId);
    }


```

**变更前代码 (old_code)**
```java
    public boolean add(Tag tag) {
        return isCategoryValid(tag.getCategory()) && mSelectedTopics.add(tag);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean add(Tag tag) {

-        return isCategoryValid(tag.getCategory()) && mSelectedTopics.add(tag);

+public boolean add(String tagId, String category) {

+        return isCategoryValid(category) && mSelectedTopics.add(tagId);

     }
```

---

### [10/100] `Summary_18`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.2078 |
| SARI | 0.6418 |
| GLEU | 0.3427 |
| METEOR | 0.4319 |
| xMatch | ✗ |

**原注释 (source)**
```
Return XML schema for the specified type, suitable for insertion into the  element of a WSDL document.
```

**标准注释 (ground truth)**
```
Return XML schema for the specified type, suitable for insertion into the &lt;types&gt; element of a WSDL document, or underneath an &lt;element&gt; or &lt;attribute&gt; declaration.
```

**生成注释 (generated)**
```
Return XML schema for the specified type, suitable for insertion into the  element of a WSDL document.
```

**当前代码 (new_code)**
```java
    public Element writeSchema(Class javaType, Types types) throws Exception {
        // Let the caller generate WSDL if this is not a SimpleType
        if (!SimpleType.class.isAssignableFrom(javaType))
            return null;

        // ComplexType representation of SimpleType bean class
        Element complexType = types.createElement("complexType");
        types.writeSchemaElement(xmlType, complexType);
        complexType.setAttribute("name", xmlType.getLocalPart());

        // Produce simpleContent extending base type.
        Element simpleContent = types.createElement("simpleContent");
        complexType.appendChild(simpleContent);
        Element extension = types.createElement("extension");
        simpleContent.appendChild(extension);

        // Get the base type from the "value" element of the bean
        String base = "string";
        for (int i=0; i<propertyDescriptor.length; i++) {
            String propName = propertyDescriptor[i].getName();
            if (!propName.equals("value")) {
                if (typeDesc != null) {
                    FieldDesc field = typeDesc.getFieldByName(propName);
                    if (field != null) {
                        if (field.isElement()) {
                            // throw?
                        }
                        QName qname = field.getXmlName();
                        if (qname == null) {
                            // Use the default...
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public boolean writeSchema(Types types) throws Exception {
        // Let the caller generate WSDL if this is not a SimpleType
        if (!SimpleType.class.isAssignableFrom(javaType))
            return false;

        // ComplexType representation of SimpleType bean class
        Element complexType = types.createElement("complexType");
        types.writeSchemaElement(xmlType, complexType);
        complexType.setAttribute("name", xmlType.getLocalPart());

        // Produce simpleContent extending base type.
        Element simpleContent = types.createElement("simpleContent");
        complexType.appendChild(simpleContent);
        Element extension = types.createElement("extension");
        simpleContent.appendChild(extension);

        // Get the base type from the "value" element of the bean
        String base = "string";
        for (int i=0; i<propertyDescriptor.length; i++) {
            String propName = propertyDescriptor[i].getName();
            if (!propName.equals("value")) {
                if (typeDesc != null) {
                    FieldDesc field = typeDesc.getFieldByName(propName);
                    if (field != null) {
                        if (field.isElement()) {
                            // throw?
                        }
                        QName qname = field.getXmlName();
                        if (qname == null) {
                            // Use the default...
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,7 @@
-public boolean writeSchema(Types types) throws Exception {

+public Element writeSchema(Class javaType, Types types) throws Exception {

         // Let the caller generate WSDL if this is not a SimpleType

         if (!SimpleType.class.isAssignableFrom(javaType))

-            return false;

+            return null;

 

         // ComplexType representation of SimpleType bean class

         Element complexType = types.createElement("complexType");

@@ -28,7 +28,6 @@
                         QName qname = field.getXmlName();

                         if (qname == null) {

                             // Use the default...

-                            propName = propName;

                             qname = new QName("", propName);

                         }

 

@@ -44,9 +43,9 @@
 

                         // write attribute element

                         // TODO the attribute name needs to be preserved from the XML

-                        String elementType = types.writeType(fieldType);

                         Element elem = types.createAttributeElement(propName,

-                                elementType,

+                                fieldType,

+                                field.getXmlType(),

                                 false,

                                 extension.getOwnerDocument());

                         extension.appendChild(elem);

@@ -67,6 +66,6 @@
         }

 

         // done

-        return true;

+        return complexType;

 

     }
```

---

### [91/100] `Summary_184`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.8213 |
| SARI | 0.6564 |
| GLEU | 0.8254 |
| METEOR | 0.8891 |
| xMatch | ✗ |

**原注释 (source)**
```
If a ApiResponse contains a reference to an other ApiResponse with '$ref', returns the referenced ApiResponse or the actual ApiResponse in the other cases.
```

**标准注释 (ground truth)**
```
If a ApiResponse contains a reference to an other ApiResponse with '$ref', returns the referenced ApiResponse if it is found or the actual ApiResponse in the other cases.
```

**生成注释 (generated)**
```
If a ApiResponse contains a reference to an other ApiResponse with '$ref', returns the referenced ApiResponse or the actual ApiResponse in the other cases.
```

**当前代码 (new_code)**
```java
    public static ApiResponse getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) {
        if (apiResponse != null && StringUtils.isNotEmpty(apiResponse.get$ref())) {
            String name = getSimpleRef(apiResponse.get$ref());
            ApiResponse referencedApiResponse = getApiResponse(openAPI, name);
            if(referencedApiResponse != null) {
                return referencedApiResponse;
            }
        }
        return apiResponse;
    }

```

**变更前代码 (old_code)**
```java
    public static ApiResponse getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) {
        if (apiResponse != null && StringUtils.isNotEmpty(apiResponse.get$ref())) {
            String name = getSimpleRef(apiResponse.get$ref());
            return getApiResponse(openAPI, name);
        }
        return apiResponse;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,10 @@
 public static ApiResponse getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) {

         if (apiResponse != null && StringUtils.isNotEmpty(apiResponse.get$ref())) {

             String name = getSimpleRef(apiResponse.get$ref());

-            return getApiResponse(openAPI, name);

+            ApiResponse referencedApiResponse = getApiResponse(openAPI, name);

+            if(referencedApiResponse != null) {

+                return referencedApiResponse;

+            }

         }

         return apiResponse;

     }
```

---

### [83/100] `Summary_168`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.6126 |
| SARI | 0.6611 |
| GLEU | 0.6304 |
| METEOR | 0.7104 |
| xMatch | ✗ |

**原注释 (source)**
```
Expects principal of the format primary/instance@REALM.
```

**标准注释 (ground truth)**
```
Expects principal of the format primary/instance@REALM or primary@REALM.
```

**生成注释 (generated)**
```
Expects principal of the format primary/instance@REALM.
```

**当前代码 (new_code)**
```java
  public static String[] splitPrincipalIntoParts(final String principal) {
    final String[] components = principal.split("[/@]");
    checkState(components.length < 4);
    checkState(components.length > 1);
    checkNotNull(components[0]);
    checkNotNull(components[1]);

    if (components.length == 2) {
      return new String[] { components[0], "", components[1] };
    } else {
      checkNotNull(components[2]);
      return components;
    }
  }

```

**变更前代码 (old_code)**
```java
  public static String[] splitPrincipalIntoParts(final String principal) {
    final String[] components = principal.split("[/@]");
    checkState(components.length == 3);
    checkNotNull(components[0]);
    checkNotNull(components[1]);
    checkNotNull(components[2]);
    return components;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,14 @@
 public static String[] splitPrincipalIntoParts(final String principal) {

     final String[] components = principal.split("[/@]");

-    checkState(components.length == 3);

+    checkState(components.length < 4);

+    checkState(components.length > 1);

     checkNotNull(components[0]);

     checkNotNull(components[1]);

-    checkNotNull(components[2]);

-    return components;

+

+    if (components.length == 2) {

+      return new String[] { components[0], "", components[1] };

+    } else {

+      checkNotNull(components[2]);

+      return components;

+    }

   }
```

---

### [14/100] `Summary_26`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7048 |
| SARI | 0.6667 |
| GLEU | 0.7200 |
| METEOR | 0.8613 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns true if, the lockClient is keeping the lock for the lockPath
```

**标准注释 (ground truth)**
```
Returns true if, the job server is keeping the lock for the lockPath
```

**生成注释 (generated)**
```
Returns true if, the serverName is keeping the lock for the lockPath
```

**当前代码 (new_code)**
```java

    private boolean isKeepLock(String serverName, String lockPath) {
        try {
            if (zkClient.checkExists().forPath(lockPath) != null) {
                byte[] data = zkClient.getData().forPath(lockPath);
                String lockServerName = new String(data, Charset.forName("UTF-8"));
                return lockServerName.equalsIgnoreCase(serverName);
            }
        } catch (Exception e) {
            logger.error("fail to get the serverName for the path: " + lockPath, e);
        }
        return false;
    }


```

**变更前代码 (old_code)**
```java

    private boolean isKeepLock(String lockClient, String lockPath) {
        try {
            if (zkClient.checkExists().forPath(lockPath) != null) {
                byte[] data = zkClient.getData().forPath(lockPath);
                String lockServerName = new String(data, Charset.forName("UTF-8"));
                return lockServerName.equalsIgnoreCase(lockClient);
            }
        } catch (Exception e) {
            logger.error("fail to get the lockClient for the path: " + lockPath, e);
        }
        return false;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,12 +1,12 @@
-private boolean isKeepLock(String lockClient, String lockPath) {

+private boolean isKeepLock(String serverName, String lockPath) {

         try {

             if (zkClient.checkExists().forPath(lockPath) != null) {

                 byte[] data = zkClient.getData().forPath(lockPath);

                 String lockServerName = new String(data, Charset.forName("UTF-8"));

-                return lockServerName.equalsIgnoreCase(lockClient);

+                return lockServerName.equalsIgnoreCase(serverName);

             }

         } catch (Exception e) {

-            logger.error("fail to get the lockClient for the path: " + lockPath, e);

+            logger.error("fail to get the serverName for the path: " + lockPath, e);

         }

         return false;

     }
```

---

### [32/100] `Summary_63`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0000 |
| SARI | 0.6667 |
| GLEU | 0.0000 |
| METEOR | 0.0000 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Returns a list of links for a HTTP connection
```

**生成注释 (generated)**
```
Handles HTML.
```

**当前代码 (new_code)**
```java
    public static List handleHTML(HttpURLConnection httpCon) throws IOException {
        ContentHandler handler = new HTMLHandler();
        handler.parse(httpCon.getInputStream());

        if (handler.getRobotFollow()) {
            List links = handler.getLinks();
            return links;
        }

        return null;
    }


```

**变更前代码 (old_code)**
```java
    public static java.util.List handleHTML(HttpURLConnection httpCon)
        throws java.io.IOException {
        ContentHandler handler = new HTMLHandler();
        handler.parse(httpCon.getInputStream());

        if (handler.getRobotFollow()) {
            java.util.List links = handler.getLinks();

            return links;
        }

        return null;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,9 @@
-public static java.util.List handleHTML(HttpURLConnection httpCon)

-        throws java.io.IOException {

+public static List handleHTML(HttpURLConnection httpCon) throws IOException {

         ContentHandler handler = new HTMLHandler();

         handler.parse(httpCon.getInputStream());

 

         if (handler.getRobotFollow()) {

-            java.util.List links = handler.getLinks();

-

+            List links = handler.getLinks();

             return links;

         }

 

```

---

### [36/100] `Summary_71`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8091 |
| SARI | 0.6667 |
| GLEU | 0.8200 |
| METEOR | 0.9269 |
| xMatch | ✗ |

**原注释 (source)**
```
Return the GraphItem representing the second (target) node in the edge.
```

**标准注释 (ground truth)**
```
Return the VisualItem representing the second (target) node in the edge.
```

**生成注释 (generated)**
```
Return the Node representing the second (target) node in the edge.
```

**当前代码 (new_code)**
```java
	public Node getSecondNode() {
		return m_node2;
	} //


```

**变更前代码 (old_code)**
```java
	public NodeItem getSecondNode() {
		return m_node2;
	} //

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public NodeItem getSecondNode() {

+public Node getSecondNode() {

 		return m_node2;

 	} //
```

---

### [70/100] `Summary_140`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0351 |
| SARI | 0.6667 |
| GLEU | 0.1400 |
| METEOR | 0.1538 |
| xMatch | ✗ |

**原注释 (source)**
```
Allocate a bitmap with the specified width and height.
```

**标准注释 (ground truth)**
```
Allocate a bitmap that has a backing memory allocacation of 'size' bytes.
```

**生成注释 (generated)**
```
Allocate a bitmap.
```

**当前代码 (new_code)**
```java
  @Override
  protected Bitmap alloc(int size) {
    return Bitmap.createBitmap(
        1,
        (int) Math.ceil(size / (double) BitmapUtil.RGB_565_BYTES_PER_PIXEL),
        Bitmap.Config.RGB_565);
  }


```

**变更前代码 (old_code)**
```java
  @Override
  protected Bitmap alloc(int size) {
    return Bitmap.createBitmap(1, size, Bitmaps.BITMAP_CONFIG);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,7 @@
 @Override

   protected Bitmap alloc(int size) {

-    return Bitmap.createBitmap(1, size, Bitmaps.BITMAP_CONFIG);

+    return Bitmap.createBitmap(

+        1,

+        (int) Math.ceil(size / (double) BitmapUtil.RGB_565_BYTES_PER_PIXEL),

+        Bitmap.Config.RGB_565);

   }
```

---

### [80/100] `Summary_162`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7825 |
| SARI | 0.6667 |
| GLEU | 0.8000 |
| METEOR | 0.9269 |
| xMatch | ✗ |

**原注释 (source)**
```
Looks up a specific revision based on some SCM-specific set of permissible syntaxes.
```

**标准注释 (ground truth)**
```
Looks up a specific thingName based on some SCM-specific set of permissible syntaxes.
```

**生成注释 (generated)**
```
Looks up a specific thing based on some SCM-specific set of permissible syntaxes.
```

**当前代码 (new_code)**
```java
    @CheckForNull
    public final SCMRevision fetch(@NonNull String thingName, @CheckForNull TaskListener listener)
            throws IOException, InterruptedException {
        return retrieve(thingName, defaultListener(listener));
    }


```

**变更前代码 (old_code)**
```java
    @CheckForNull
    public final SCMRevision fetch(@NonNull String revision, @CheckForNull TaskListener listener)
            throws IOException, InterruptedException {
        return retrieve(revision, defaultListener(listener));
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
 @CheckForNull

-    public final SCMRevision fetch(@NonNull String revision, @CheckForNull TaskListener listener)

+    public final SCMRevision fetch(@NonNull String thingName, @CheckForNull TaskListener listener)

             throws IOException, InterruptedException {

-        return retrieve(revision, defaultListener(listener));

+        return retrieve(thingName, defaultListener(listener));

     }
```

---

### [99/100] `Summary_201`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7533 |
| SARI | 0.6667 |
| GLEU | 0.7593 |
| METEOR | 0.8709 |
| xMatch | ✗ |

**原注释 (source)**
```
Parse a signature, with or without classname, with or without descriptor.
```

**标准注释 (ground truth)**
```
Parse a member ID, with or without classname, with or without descriptor.
```

**生成注释 (generated)**
```
Parse a memberID, with or without classname, with or without descriptor.
```

**当前代码 (new_code)**
```java
    public static MemberID parse(String memberID) {
        return parse(memberID, false, AppInfo.getSingleton().getClassPath());
    }


```

**变更前代码 (old_code)**
```java
    public static MemberID parse(String signature) {
        return parse(signature, false, AppInfo.getSingleton().getClassPath());
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static MemberID parse(String signature) {

-        return parse(signature, false, AppInfo.getSingleton().getClassPath());

+public static MemberID parse(String memberID) {

+        return parse(memberID, false, AppInfo.getSingleton().getClassPath());

     }
```

---

### [86/100] `Summary_174`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.6340 |
| SARI | 0.6732 |
| GLEU | 0.6667 |
| METEOR | 0.9765 |
| xMatch | ✗ |

**原注释 (source)**
```
Does this time interval contain or equal the specified time interval.
```

**标准注释 (ground truth)**
```
Does this time interval contain the specified time interval.
```

**生成注释 (generated)**
```
Does this time interval contain or equal the specified time interval.
```

**当前代码 (new_code)**
```java
    public boolean contains(ReadableInterval interval) {
        if (interval == null) {
            return containsNow();
        }
        long otherStart = interval.getStartMillis();
        long otherEnd = interval.getEndMillis();
        long thisStart = getStartMillis();
        long thisEnd = getEndMillis();
        return (thisStart <= otherStart && otherStart < thisEnd && otherEnd <= thisEnd);
    }

```

**变更前代码 (old_code)**
```java
    public boolean contains(ReadableInterval interval) {
        if (interval == null) {
            return containsNow();
        }
        long otherStart = interval.getStartMillis();
        long otherEnd = interval.getEndMillis();
        long thisStart = getStartMillis();
        long thisEnd = getEndMillis();
        return (thisStart <= otherStart && otherStart < thisEnd && otherEnd <= thisEnd) ||
            (thisStart == otherStart && thisEnd == otherEnd);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -6,6 +6,5 @@
         long otherEnd = interval.getEndMillis();

         long thisStart = getStartMillis();

         long thisEnd = getEndMillis();

-        return (thisStart <= otherStart && otherStart < thisEnd && otherEnd <= thisEnd) ||

-            (thisStart == otherStart && thisEnd == otherEnd);

+        return (thisStart <= otherStart && otherStart < thisEnd && otherEnd <= thisEnd);

     }
```

---

### [78/100] `Summary_158`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5946 |
| SARI | 0.6743 |
| GLEU | 0.6538 |
| METEOR | 0.8648 |
| xMatch | ✗ |

**原注释 (source)**
```
Create DrillFileSystem for given proxyUserName, configuration and stats.
```

**标准注释 (ground truth)**
```
Create DrillFileSystem for given proxyUserName and configuration.
```

**生成注释 (generated)**
```
Create DrillFileSystem for given proxyUserName, configuration.
```

**当前代码 (new_code)**
```java
  public static DrillFileSystem createFileSystem(String proxyUserName, Configuration fsConf) {
    return createFileSystem(createProxyUgi(proxyUserName), fsConf, null);
  }

```

**变更前代码 (old_code)**
```java
  public static DrillFileSystem createFileSystem(String proxyUserName, Configuration fsConf, OperatorStats stats) {
    return createFileSystem(createProxyUgi(proxyUserName), fsConf, stats);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static DrillFileSystem createFileSystem(String proxyUserName, Configuration fsConf, OperatorStats stats) {

-    return createFileSystem(createProxyUgi(proxyUserName), fsConf, stats);

+public static DrillFileSystem createFileSystem(String proxyUserName, Configuration fsConf) {

+    return createFileSystem(createProxyUgi(proxyUserName), fsConf, null);

   }
```

---

### [93/100] `Summary_188`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.6316 |
| SARI | 0.6749 |
| GLEU | 0.6429 |
| METEOR | 0.9624 |
| xMatch | ✗ |

**原注释 (source)**
```
Removes a converter from the set of converters, by index.
```

**标准注释 (ground truth)**
```
Removes a converter from the set of converters.
```

**生成注释 (generated)**
```
Removes a converter from the set of converters, by index.
```

**当前代码 (new_code)**
```java
    public DurationConverter removeDurationConverter(DurationConverter converter)
            throws SecurityException {
        
        checkAlterDurationConverters();
        if (converter == null) {
            return null;
        }
        DurationConverter[] removed = new DurationConverter[1];
        iDurationConverters = iDurationConverters.remove(converter, removed);
        return removed[0];
    }

```

**变更前代码 (old_code)**
```java
    public DurationConverter removeDurationConverter(int index) throws SecurityException {
        checkAlterDurationConverters();
        DurationConverter[] removed = new DurationConverter[1];
        iDurationConverters = iDurationConverters.remove(index, removed);
        return removed[0];
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,11 @@
-public DurationConverter removeDurationConverter(int index) throws SecurityException {

+public DurationConverter removeDurationConverter(DurationConverter converter)

+            throws SecurityException {

+        

         checkAlterDurationConverters();

+        if (converter == null) {

+            return null;

+        }

         DurationConverter[] removed = new DurationConverter[1];

-        iDurationConverters = iDurationConverters.remove(index, removed);

+        iDurationConverters = iDurationConverters.remove(converter, removed);

         return removed[0];

     }
```

---

### [58/100] `Summary_116`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0000 |
| SARI | 0.6818 |
| GLEU | 0.0000 |
| METEOR | 0.1333 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Get the list of src attributes for images
```

**生成注释 (generated)**
```
The image sources
```

**当前代码 (new_code)**
```java
    public ArrayList getImageSrcs() {
        return this.img_src;
    }


```

**变更前代码 (old_code)**
```java
    public ArrayList getImageSrcs() {
        return img_src;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public ArrayList getImageSrcs() {

-        return img_src;

+        return this.img_src;

     }
```

---

### [69/100] `Summary_138`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0440 |
| SARI | 0.6818 |
| GLEU | 0.0556 |
| METEOR | 0.3178 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Get a list of all links
```

**生成注释 (generated)**
```
Returns all link HREFs.
```

**当前代码 (new_code)**
```java
    public ArrayList getAllLinkHRefs() {
        return this.link_href_all;
    }


```

**变更前代码 (old_code)**
```java
    public ArrayList getAllLinkHRefs() {
        return link_href_all;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public ArrayList getAllLinkHRefs() {

-        return link_href_all;

+        return this.link_href_all;

     }
```

---

### [29/100] `Summary_56`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.6606 |
| SARI | 0.6827 |
| GLEU | 0.7000 |
| METEOR | 0.8819 |
| xMatch | ✗ |

**原注释 (source)**
```
Parses a Specification out of the query string.
```

**标准注释 (ground truth)**
```
Parses a Query out of the query string.
```

**生成注释 (generated)**
```
Parses a Specification out of the query string.
```

**当前代码 (new_code)**
```java
    public static Query parse(String queryString, BulletConfig config) {
        Query query = GSON.fromJson(queryString, Query.class);
        query.configure(config);
        return query;
    }


```

**变更前代码 (old_code)**
```java
    public static Specification parse(String queryString, BulletConfig config) {
        Specification specification = GSON.fromJson(queryString, Specification.class);
        specification.configure(config);
        return specification;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public static Specification parse(String queryString, BulletConfig config) {

-        Specification specification = GSON.fromJson(queryString, Specification.class);

-        specification.configure(config);

-        return specification;

+public static Query parse(String queryString, BulletConfig config) {

+        Query query = GSON.fromJson(queryString, Query.class);

+        query.configure(config);

+        return query;

     }
```

---

### [63/100] `Summary_126`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4854 |
| SARI | 0.6852 |
| GLEU | 0.5128 |
| METEOR | 0.6361 |
| xMatch | ✗ |

**原注释 (source)**
```
Make fully qualified URI based on the default file system Scheme and Authority
```

**标准注释 (ground truth)**
```
Make fully qualified URI if Scheme and/or Authority is missing, based on the default file system Scheme and Authority.
```

**生成注释 (generated)**
```
Make fully qualified URI or null based on the default file system Scheme and Authority
```

**当前代码 (new_code)**
```java
  private static URI makeFullQualifiedURI(String uriName) throws IOException {
    Path uriPath = new Path(uriName);
    if (isNormalized(uriName) && uriPath.isUriPathAbsolute()) {
      // add scheme and/or authority if either is missing
      if ((uriPath.toUri().getScheme() == null || uriPath.toUri().getAuthority() == null)) {
        URI defaultUri = FileSystem.getDefaultUri(CONF);
        uriPath = uriPath.makeQualified(defaultUri, uriPath);
      }
      return uriPath.toUri();
    } else { // relative URI path is unacceptable
      return null;
    }
  }


```

**变更前代码 (old_code)**
```java
  private static URI makeFullQualifiedURI(String uriName) throws IOException, URISyntaxException {
    Path uriPath = new Path(uriName);

    if (uriPath.isAbsoluteAndSchemeAuthorityNull()) {

      URI defaultUri = FileSystem.getDefaultUri(CONF);
      uriPath = uriPath.makeQualified(defaultUri, uriPath);
      return uriPath.toUri();
    }

    return new URI(uriName);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,12 +1,13 @@
-private static URI makeFullQualifiedURI(String uriName) throws IOException, URISyntaxException {

+private static URI makeFullQualifiedURI(String uriName) throws IOException {

     Path uriPath = new Path(uriName);

-

-    if (uriPath.isAbsoluteAndSchemeAuthorityNull()) {

-

-      URI defaultUri = FileSystem.getDefaultUri(CONF);

-      uriPath = uriPath.makeQualified(defaultUri, uriPath);

+    if (isNormalized(uriName) && uriPath.isUriPathAbsolute()) {

+      // add scheme and/or authority if either is missing

+      if ((uriPath.toUri().getScheme() == null || uriPath.toUri().getAuthority() == null)) {

+        URI defaultUri = FileSystem.getDefaultUri(CONF);

+        uriPath = uriPath.makeQualified(defaultUri, uriPath);

+      }

       return uriPath.toUri();

+    } else { // relative URI path is unacceptable

+      return null;

     }

-

-    return new URI(uriName);

   }
```

---

### [68/100] `Summary_136`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0803 |
| SARI | 0.6875 |
| GLEU | 0.1000 |
| METEOR | 0.4688 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Generate a parse exception
```

**生成注释 (generated)**
```
Generates a ParseException.
```

**当前代码 (new_code)**
```java
    final public ParseException generateParseException() {
        this.jj_expentries.removeAllElements();

        boolean[] la1tokens = new boolean[27];

        for (int i = 0; i < 27; i++) {
            la1tokens[i] = false;
        }

        if (this.jj_kind >= 0) {
            la1tokens[this.jj_kind] = true;
            this.jj_kind = -1;
        }

        for (int i = 0; i < 13; i++) {
            if (this.jj_la1[i] == this.jj_gen) {
                for (int j = 0; j < 32; j++) {
                    if ((this.jj_la1_0[i] & (1 << j)) != 0) {
                        la1tokens[j] = true;
                    }
                }
            }
        }

        for (int i = 0; i < 27; i++) {
            if (la1tokens[i]) {
                this.jj_expentry = new int[1];
                this.jj_expentry[0] = i;
                this.jj_expentries.addElement(this.jj_expentry);
            }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    final public ParseException generateParseException() {
        jj_expentries.removeAllElements();

        boolean[] la1tokens = new boolean[27];

        for (int i = 0; i < 27; i++) {
            la1tokens[i] = false;
        }

        if (jj_kind >= 0) {
            la1tokens[jj_kind] = true;
            jj_kind = -1;
        }

        for (int i = 0; i < 13; i++) {
            if (jj_la1[i] == jj_gen) {
                for (int j = 0; j < 32; j++) {
                    if ((jj_la1_0[i] & (1 << j)) != 0) {
                        la1tokens[j] = true;
                    }
                }
            }
        }

        for (int i = 0; i < 27; i++) {
            if (la1tokens[i]) {
                jj_expentry = new int[1];
                jj_expentry[0] = i;
                jj_expentries.addElement(jj_expentry);
            }
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
 final public ParseException generateParseException() {

-        jj_expentries.removeAllElements();

+        this.jj_expentries.removeAllElements();

 

         boolean[] la1tokens = new boolean[27];

 

@@ -7,15 +7,15 @@
             la1tokens[i] = false;

         }

 

-        if (jj_kind >= 0) {

-            la1tokens[jj_kind] = true;

-            jj_kind = -1;

+        if (this.jj_kind >= 0) {

+            la1tokens[this.jj_kind] = true;

+            this.jj_kind = -1;

         }

 

         for (int i = 0; i < 13; i++) {

-            if (jj_la1[i] == jj_gen) {

+            if (this.jj_la1[i] == this.jj_gen) {

                 for (int j = 0; j < 32; j++) {

-                    if ((jj_la1_0[i] & (1 << j)) != 0) {

+                    if ((this.jj_la1_0[i] & (1 << j)) != 0) {

                         la1tokens[j] = true;

                     }

                 }

@@ -24,21 +24,21 @@
 

         for (int i = 0; i < 27; i++) {

             if (la1tokens[i]) {

-                jj_expentry = new int[1];

-                jj_expentry[0] = i;

-                jj_expentries.addElement(jj_expentry);

+                this.jj_expentry = new int[1];

+                this.jj_expentry[0] = i;

+                this.jj_expentries.addElement(this.jj_expentry);

```

---

### [4/100] `Summary_6`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1136 |
| SARI | 0.7143 |
| GLEU | 0.2143 |
| METEOR | 0.4573 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns
```

**标准注释 (ground truth)**
```
Returns the queue directory
```

**生成注释 (generated)**
```
Returns the sink file.
```

**当前代码 (new_code)**
```java
	public File getSinkFile() {
		return queue.file();
	}


```

**变更前代码 (old_code)**
```java
	public File getSinkFile() {
		return sinkFile;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public File getSinkFile() {

-		return sinkFile;

+		return queue.file();

 	}
```

---

### [89/100] `Summary_180`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0814 |
| SARI | 0.7143 |
| GLEU | 0.1000 |
| METEOR | 0.2564 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Get the column position
```

**生成注释 (generated)**
```
The end column
```

**当前代码 (new_code)**
```java
    public final int getEndColumn() {
        return this.bufcolumn[this.bufpos];
    }


```

**变更前代码 (old_code)**
```java
    public final int getEndColumn() {
        return bufcolumn[bufpos];
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public final int getEndColumn() {

-        return bufcolumn[bufpos];

+        return this.bufcolumn[this.bufpos];

     }
```

---

### [92/100] `Summary_186`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8895 |
| SARI | 0.7143 |
| GLEU | 0.8936 |
| METEOR | 0.9597 |
| xMatch | ✗ |

**原注释 (source)**
```
Try to get the primary  java.net.InetAddress of the primary network interface with fallback to the local loopback address (usually  127.0.0.1 or  ::1.
```

**标准注释 (ground truth)**
```
Try to get the primary  InetAddress of the primary network interface with fallback to the local loopback address (usually  127.0.0.1 or  ::1.
```

**生成注释 (generated)**
```
Try to get the primary  java.net.InetAddress of the primary network interface with fallback to the local loopback address (usually  127.0.0.1 or  ::1.
```

**当前代码 (new_code)**
```java
    public static InetAddress guessPrimaryNetworkAddress(boolean preferIPv4) throws SocketException {
        final Enumeration<NetworkInterface> interfaces = NetworkInterface.getNetworkInterfaces();

        if (interfaces != null) {
            for (NetworkInterface interf : Collections.list(interfaces)) {
                if (!interf.isLoopback() && interf.isUp()) {
                    // Interface is not loopback and up. Try to get the first address.
                    for (InetAddress addr : Collections.list(interf.getInetAddresses())) {
                        if (preferIPv4 && addr instanceof Inet4Address) {
                            return addr;
                        }
                        if (!preferIPv4 && addr instanceof Inet6Address) {
                            return addr;
                        }
                    }
                }
            }
        }

        return InetAddress.getLoopbackAddress();
    }


```

**变更前代码 (old_code)**
```java
    public static InetAddress guessPrimaryNetworkAddress() throws SocketException {
        final Enumeration<NetworkInterface> interfaces = NetworkInterface.getNetworkInterfaces();

        if (interfaces != null) {
            for (NetworkInterface interf : Collections.list(interfaces)) {
                if (!interf.isLoopback() && interf.isUp()) {
                    // Interface is not loopback and up. Try to get the first address.
                    for (InetAddress addr : Collections.list(interf.getInetAddresses())) {
                        if (addr instanceof Inet4Address) {
                            return addr;
                        }
                    }
                }
            }
        }

        return InetAddress.getLoopbackAddress();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public static InetAddress guessPrimaryNetworkAddress() throws SocketException {

+public static InetAddress guessPrimaryNetworkAddress(boolean preferIPv4) throws SocketException {

         final Enumeration<NetworkInterface> interfaces = NetworkInterface.getNetworkInterfaces();

 

         if (interfaces != null) {

@@ -6,7 +6,10 @@
                 if (!interf.isLoopback() && interf.isUp()) {

                     // Interface is not loopback and up. Try to get the first address.

                     for (InetAddress addr : Collections.list(interf.getInetAddresses())) {

-                        if (addr instanceof Inet4Address) {

+                        if (preferIPv4 && addr instanceof Inet4Address) {

+                            return addr;

+                        }

+                        if (!preferIPv4 && addr instanceof Inet6Address) {

                             return addr;

                         }

                     }

```

---

### [25/100] `Summary_48`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.8137 |
| SARI | 0.7156 |
| GLEU | 0.8205 |
| METEOR | 0.9890 |
| xMatch | ✗ |

**原注释 (source)**
```
Adds a menu item to the bar containing SafeHtml, that will fire the given command when it is selected.
```

**标准注释 (ground truth)**
```
Adds a menu item to the bar, that will fire the given command when it is selected.
```

**生成注释 (generated)**
```
Adds a menu item to the bar containing SafeHtml, that will fire the given command when it is selected.
```

**当前代码 (new_code)**
```java
  public MenuItem addItem(String text, boolean asHTML, Command cmd) {
    return addItem(new MenuItem(text, asHTML, cmd));
  }

```

**变更前代码 (old_code)**
```java
  public MenuItem addItem(SafeHtml html, ScheduledCommand cmd) {
    return addItem(new MenuItem(html, Roles.getMenuitemRole(), false, cmd));
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public MenuItem addItem(SafeHtml html, ScheduledCommand cmd) {

-    return addItem(new MenuItem(html, Roles.getMenuitemRole(), false, cmd));

+public MenuItem addItem(String text, boolean asHTML, Command cmd) {

+    return addItem(new MenuItem(text, asHTML, cmd));

   }
```

---

### [54/100] `Summary_108`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.8844 |
| SARI | 0.7292 |
| GLEU | 0.8871 |
| METEOR | 0.9338 |
| xMatch | ✗ |

**原注释 (source)**
```
Evaluate a PLAIN login challenge, returning the a result string that should satisfy the clallenge.
```

**标准注释 (ground truth)**
```
Evaluate a PLAIN login challenge, returning the a result string that should satisfy the challenge.
```

**生成注释 (generated)**
```
Evaluate a PLAIN login challenge, returning the a result string that should satisfy the clallenge.
```

**当前代码 (new_code)**
```java
    public byte[] evaluateChallenge(byte[] challenge) throws MessagingException {
        try {

            String result = "\0"+username+"\0"+password;

            if(authzid != null && authzid.length() > 0) {
                result = authzid+result;
            }

            complete = true;
            return result.getBytes("UTF-8");

        } catch (UnsupportedEncodingException e) {
            // got an error, fail this
            throw new MessagingException("Invalid encoding");
        }
    }


```

**变更前代码 (old_code)**
```java
    public byte[] evaluateChallenge(byte[] challenge) throws MessagingException {
        try {
            // get the username and password in an UTF-8 encoding to create the
            // token
            byte[] userBytes = username.getBytes("UTF-8");
            byte[] passBytes = password.getBytes("UTF-8");

            // our token has two copies of the username, one copy of the
            // password, and nulls
            // between
            byte[] tokenBytes = new byte[(userBytes.length * 2) + passBytes.length + 2];

            System.arraycopy(userBytes, 0, tokenBytes, 0, userBytes.length);
            System.arraycopy(userBytes, 0, tokenBytes, userBytes.length + 1, userBytes.length);
            System.arraycopy(passBytes, 0, tokenBytes, (userBytes.length * 2) + 2, passBytes.length);

            complete = true;
            return tokenBytes;

        } catch (UnsupportedEncodingException e) {
            // got an error, fail this
            throw new MessagingException("Invalid encoding");
        }
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,21 +1,14 @@
 public byte[] evaluateChallenge(byte[] challenge) throws MessagingException {

         try {

-            // get the username and password in an UTF-8 encoding to create the

-            // token

-            byte[] userBytes = username.getBytes("UTF-8");

-            byte[] passBytes = password.getBytes("UTF-8");

 

-            // our token has two copies of the username, one copy of the

-            // password, and nulls

-            // between

-            byte[] tokenBytes = new byte[(userBytes.length * 2) + passBytes.length + 2];

+            String result = "\0"+username+"\0"+password;

 

-            System.arraycopy(userBytes, 0, tokenBytes, 0, userBytes.length);

-            System.arraycopy(userBytes, 0, tokenBytes, userBytes.length + 1, userBytes.length);

-            System.arraycopy(passBytes, 0, tokenBytes, (userBytes.length * 2) + 2, passBytes.length);

+            if(authzid != null && authzid.length() > 0) {

+                result = authzid+result;

+            }

 

             complete = true;

-            return tokenBytes;

+            return result.getBytes("UTF-8");

 

         } catch (UnsupportedEncodingException e) {

             // got an error, fail this

```

---

### [67/100] `Summary_134`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0919 |
| SARI | 0.7513 |
| GLEU | 0.2727 |
| METEOR | 0.3623 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Returns the path to the authoring tree
```

**生成注释 (generated)**
```
Returns the tree authoring path.
```

**当前代码 (new_code)**
```java
    public String getTreeAuthoringPath() {
        return this.treeAuthoringPath;
    }


```

**变更前代码 (old_code)**
```java
    public String getTreeAuthoringPath() {
        return treeAuthoringPath;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public String getTreeAuthoringPath() {

-        return treeAuthoringPath;

+        return this.treeAuthoringPath;

     }
```

---

### [64/100] `Summary_128`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1316 |
| SARI | 0.7593 |
| GLEU | 0.3333 |
| METEOR | 0.6356 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns
```

**标准注释 (ground truth)**
```
Returns the queue file roll cycle
```

**生成注释 (generated)**
```
Returns the roll cycle.
```

**当前代码 (new_code)**
```java
	public RollCycle getRollCycle() {
		return queue.rollCycle();
	}


```

**变更前代码 (old_code)**
```java
	public RollCycle getRollCycle() {
		return rollCycle;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public RollCycle getRollCycle() {

-		return rollCycle;

+		return queue.rollCycle();

 	}
```

---

### [57/100] `Summary_114`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6690 |
| SARI | 0.7768 |
| GLEU | 0.7059 |
| METEOR | 0.9041 |
| xMatch | ✗ |

**原注释 (source)**
```
Converts the given object into a JSON AST.
```

**标准注释 (ground truth)**
```
Converts the given object into a canonical JSON string.
```

**生成注释 (generated)**
```
Converts the given object into a JSON string.
```

**当前代码 (new_code)**
```java
    public static String asJson(Object object) throws IOException {
        return JSON.writeValueAsString(object);
    }


```

**变更前代码 (old_code)**
```java
    public static JsonNode asJson(Object object) throws IOException {
        return JSON.writeValueAsTree(object);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static JsonNode asJson(Object object) throws IOException {

-        return JSON.writeValueAsTree(object);

+public static String asJson(Object object) throws IOException {

+        return JSON.writeValueAsString(object);

     }
```

---

### [49/100] `Summary_98`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2120 |
| SARI | 0.7981 |
| GLEU | 0.3636 |
| METEOR | 0.5515 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Returns the path to the replication directory
```

**生成注释 (generated)**
```
Returns the replication directory.
```

**当前代码 (new_code)**
```java
    public String getReplicationDirectory() {
        return this.replicationDirectory;
    }


```

**变更前代码 (old_code)**
```java
    public String getReplicationDirectory() {
        return replicationDirectory;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public String getReplicationDirectory() {

-        return replicationDirectory;

+        return this.replicationDirectory;

     }
```

---

### [8/100] `Summary_14`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4029 |
| SARI | 0.8028 |
| GLEU | 0.6000 |
| METEOR | 0.7550 |
| xMatch | ✗ |

**原注释 (source)**
```
Build a Ravioli client
```

**标准注释 (ground truth)**
```
Build a Lob client
```

**生成注释 (generated)**
```
Build a Lob
```

**当前代码 (new_code)**
```java
        public Lob build() {
            return new Lob(this);
        }


```

**变更前代码 (old_code)**
```java
        public Ravioli build() {
            return new Ravioli(this);
        }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public Ravioli build() {

-            return new Ravioli(this);

+public Lob build() {

+            return new Lob(this);

         }
```

---

### [51/100] `Summary_102`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2659 |
| SARI | 0.8032 |
| GLEU | 0.4286 |
| METEOR | 0.9680 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Get the backup directory
```

**生成注释 (generated)**
```
Gets the backup directory.
```

**当前代码 (new_code)**
```java
    public String getBackupDirectory() {
        return this.backupDirectory;
    }


```

**变更前代码 (old_code)**
```java
    public String getBackupDirectory() {
        return backupDirectory;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public String getBackupDirectory() {

-        return backupDirectory;

+        return this.backupDirectory;

     }
```

---

### [94/100] `Summary_190`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2659 |
| SARI | 0.8032 |
| GLEU | 0.4286 |
| METEOR | 0.7182 |
| xMatch | ✗ |

**原注释 (source)**
```
DOCUMENT ME!
```

**标准注释 (ground truth)**
```
Get the RCML directory
```

**生成注释 (generated)**
```
Returns the RCML directory.
```

**当前代码 (new_code)**
```java
    public String getRCMLDirectory() {
        return this.rcmlDirectory;
    }


```

**变更前代码 (old_code)**
```java
    public String getRCMLDirectory() {
        return rcmlDirectory;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public String getRCMLDirectory() {

-        return rcmlDirectory;

+        return this.rcmlDirectory;

     }
```

---

### [2/100] `Summary_2`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7947 |
| SARI | 0.8700 |
| GLEU | 0.8000 |
| METEOR | 0.8984 |
| xMatch | ✗ |

**原注释 (source)**
```
Marshal the aggregator values of to a JSONArray that will later be aggregated by master.
```

**标准注释 (ground truth)**
```
Marshal the aggregator values of the worker to a byte array that will later be aggregated by master.
```

**生成注释 (generated)**
```
Marshal the aggregator values of to a byte array that will later be aggregated by master.
```

**当前代码 (new_code)**
```java
  private byte[] marshalAggregatorValues(long superstep) {
    if (superstep == INPUT_SUPERSTEP) {
      return new byte[0];
    }

    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
    DataOutputStream output = new DataOutputStream(outputStream);
    for (Entry<String, AggregatorWrapper<Writable>> entry :
        getAggregatorMap().entrySet()) {
      if (entry.getValue().isChanged()) {
        try {
          output.writeUTF(entry.getKey());
          entry.getValue().getCurrentAggregatedValue().write(output);
        } catch (IOException e) {
          throw new IllegalStateException("Failed to marshall aggregator " +
              "with IOException " + entry.getKey(), e);
        }
      }
    }

    if (LOG.isInfoEnabled()) {
      LOG.info(
          "marshalAggregatorValues: Finished assembling aggregator values");
    }
    return outputStream.toByteArray();
  }


```

**变更前代码 (old_code)**
```java
  private JSONArray marshalAggregatorValues(long superstep) {
    JSONArray aggregatorArray = new JSONArray();
    if ((superstep == INPUT_SUPERSTEP) || (aggregatorInUse.size() == 0)) {
      return aggregatorArray;
    }

    for (String name : aggregatorInUse) {
      try {
        Aggregator<Writable> aggregator = getAggregatorMap().get(name);
        ByteArrayOutputStream outputStream =
            new ByteArrayOutputStream();
        DataOutput output = new DataOutputStream(outputStream);
        aggregator.getAggregatedValue().write(output);

        JSONObject aggregatorObj = new JSONObject();
        aggregatorObj.put(AGGREGATOR_NAME_KEY, name);
        aggregatorObj.put(AGGREGATOR_CLASS_NAME_KEY,
            aggregator.getClass().getName());
        aggregatorObj.put(
            AGGREGATOR_VALUE_KEY,
            Base64.encodeBytes(outputStream.toByteArray()));
        aggregatorArray.put(aggregatorObj);
        if (LOG.isInfoEnabled()) {
          LOG.info("marshalAggregatorValues: " +
              "Found aggregatorObj " +
              aggregatorObj + ", value (" +
              aggregator.getAggregatedValue() + ")");
        }
      } catch (JSONException e) {
        throw new IllegalStateException("Failed to marshall aggregator " +
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,44 +1,26 @@
-private JSONArray marshalAggregatorValues(long superstep) {

-    JSONArray aggregatorArray = new JSONArray();

-    if ((superstep == INPUT_SUPERSTEP) || (aggregatorInUse.size() == 0)) {

-      return aggregatorArray;

+private byte[] marshalAggregatorValues(long superstep) {

+    if (superstep == INPUT_SUPERSTEP) {

+      return new byte[0];

     }

 

-    for (String name : aggregatorInUse) {

-      try {

-        Aggregator<Writable> aggregator = getAggregatorMap().get(name);

-        ByteArrayOutputStream outputStream =

-            new ByteArrayOutputStream();

-        DataOutput output = new DataOutputStream(outputStream);

-        aggregator.getAggregatedValue().write(output);

-

-        JSONObject aggregatorObj = new JSONObject();

-        aggregatorObj.put(AGGREGATOR_NAME_KEY, name);

-        aggregatorObj.put(AGGREGATOR_CLASS_NAME_KEY,

-            aggregator.getClass().getName());

-        aggregatorObj.put(

-            AGGREGATOR_VALUE_KEY,

-            Base64.encodeBytes(outputStream.toByteArray()));

-        aggregatorArray.put(aggregatorObj);

-        if (LOG.isInfoEnabled()) {

-          LOG.info("marshalAggregatorValues: " +

-              "Found aggregatorObj " +

-              aggregatorObj + ", value (" +

-              aggregator.getAggregatedValue() + ")");

+    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();

+    DataOutputStream output = new DataOutputStream(outputStream);

+    for (Entry<String, AggregatorWrapper<Writable>> entry :

+        getAggregatorMap().entrySet()) {

+      if (entry.getValue().isChanged()) {

+        try {

+          output.writeUTF(entry.getKey());

```

---

### [22/100] `Summary_42`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9583 |
| GLEU | 1.0000 |
| METEOR | 0.9977 |
| xMatch | ✓ |

**原注释 (source)**
```
Expr : left.endsWith(right) (ignore case)
```

**标准注释 (ground truth)**
```
Expr : left.endsWith(right)
```

**生成注释 (generated)**
```
Expr : left.endsWith(right)
```

**当前代码 (new_code)**
```java
    public static EBoolean endsWith(Expr<String> left, String right) {
        return operationFactory.createBoolean(Ops.ENDSWITH, left, exprFactory
                .createConstant(right));
    }

```

**变更前代码 (old_code)**
```java
    public static EBoolean endsWith(Expr<String> left, String right, boolean caseSensitive) {
        if (caseSensitive){
            return endsWith(left, right);            
        }else{
            return operationFactory.createBoolean(Ops.ENDSWITH_IC, left, exprFactory.createConstant(right));
        }                
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,4 @@
-public static EBoolean endsWith(Expr<String> left, String right, boolean caseSensitive) {

-        if (caseSensitive){

-            return endsWith(left, right);            

-        }else{

-            return operationFactory.createBoolean(Ops.ENDSWITH_IC, left, exprFactory.createConstant(right));

-        }                

+public static EBoolean endsWith(Expr<String> left, String right) {

+        return operationFactory.createBoolean(Ops.ENDSWITH, left, exprFactory

+                .createConstant(right));

     }
```

---

### [6/100] `Summary_10`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 1.0000 |
| xMatch | ✓ |

**原注释 (source)**
```
Returns the providers that are bound to the same location as the given ISO 3166 code and of the given type.
```

**标准注释 (ground truth)**
```
Returns the providers that are bound to the same location as the given ISO 3166 code and of the given contextWrappableAs.
```

**生成注释 (generated)**
```
Returns the providers that are bound to the same location as the given ISO 3166 code and of the given contextWrappableAs.
```

**当前代码 (new_code)**
```java
   public static Iterable<ProviderMetadata> boundedByIso3166Code(String iso3166Code,
            TypeToken<? extends Wrapper> contextWrappableAs) {
      return filter(all(), Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates
               .contextWrappableAs(contextWrappableAs)));
   }


```

**变更前代码 (old_code)**
```java
   public static Iterable<ProviderMetadata<?, ?, ?, ?>> boundedByIso3166Code(String iso3166Code, ApiType type) {
      return filter(all(),
            Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates.type(type)));
   }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,5 @@
-public static Iterable<ProviderMetadata<?, ?, ?, ?>> boundedByIso3166Code(String iso3166Code, ApiType type) {

-      return filter(all(),

-            Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates.type(type)));

+public static Iterable<ProviderMetadata> boundedByIso3166Code(String iso3166Code,

+            TypeToken<? extends Wrapper> contextWrappableAs) {

+      return filter(all(), Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates

+               .contextWrappableAs(contextWrappableAs)));

    }
```

---

### [12/100] `Summary_22`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9998 |
| xMatch | ✓ |

**原注释 (source)**
```
Return the list of module prefixes that are defined for this web application, creating it if necessary.
```

**标准注释 (ground truth)**
```
Return the list of module prefixes that are defined for this web application.
```

**生成注释 (generated)**
```
Return the list of module prefixes that are defined for this web application.
```

**当前代码 (new_code)**
```java
    public static String[] getModulePrefixes(ServletContext context) {
        return (String[]) context.getAttribute(Globals.MODULE_PREFIXES_KEY);
    }


```

**变更前代码 (old_code)**
```java
    public synchronized static String[] getModulePrefixes(ServletContext context) {
        // TODO Move prefix list initialization to ActionServlet.init() and unsynchronize
        // this method in Struts 1.2 
        
        String prefixes[] = (String[]) context.getAttribute(PREFIXES_KEY);
        if (prefixes != null) {
            return (prefixes);
        }

        ArrayList list = new ArrayList();
        Enumeration names = context.getAttributeNames();
        while (names.hasMoreElements()) {
            String name = (String) names.nextElement();
            if (!name.startsWith(Globals.MODULE_KEY)) {
                continue;
            }
            String prefix = name.substring(Globals.MODULE_KEY.length());
            if (prefix.length() > 0) {
                list.add(prefix);
            }
        }
        prefixes = (String[]) list.toArray(new String[list.size()]);
        context.setAttribute(PREFIXES_KEY, prefixes);
        return (prefixes);

    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,26 +1,3 @@
-public synchronized static String[] getModulePrefixes(ServletContext context) {

-        // TODO Move prefix list initialization to ActionServlet.init() and unsynchronize

-        // this method in Struts 1.2 

-        

-        String prefixes[] = (String[]) context.getAttribute(PREFIXES_KEY);

-        if (prefixes != null) {

-            return (prefixes);

-        }

-

-        ArrayList list = new ArrayList();

-        Enumeration names = context.getAttributeNames();

-        while (names.hasMoreElements()) {

-            String name = (String) names.nextElement();

-            if (!name.startsWith(Globals.MODULE_KEY)) {

-                continue;

-            }

-            String prefix = name.substring(Globals.MODULE_KEY.length());

-            if (prefix.length() > 0) {

-                list.add(prefix);

-            }

-        }

-        prefixes = (String[]) list.toArray(new String[list.size()]);

-        context.setAttribute(PREFIXES_KEY, prefixes);

-        return (prefixes);

-

+public static String[] getModulePrefixes(ServletContext context) {

+        return (String[]) context.getAttribute(Globals.MODULE_PREFIXES_KEY);

     }
```

---

### [15/100] `Summary_28`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9996 |
| xMatch | ✓ |

**原注释 (source)**
```
Unsubscribes the resource from this channel, if it exists.
```

**标准注释 (ground truth)**
```
Unsubscribes the resource from this repo, if it exists.
```

**生成注释 (generated)**
```
Unsubscribes the resource from this repo, if it exists.
```

**当前代码 (new_code)**
```java
    public ResourceRepo removeResource(Resource resource) {
        if ((this.resourceRepos == null) || (resource == null)) {
            return null;
        }

        ResourceRepo doomed = null;

        for (ResourceRepo rc : this.resourceRepos) {
            if (resource.equals(rc.getResourceRepoPK().getResource())) {
                doomed = rc;
                break;
            }
        }

        if (doomed != null) {
            this.resourceRepos.remove(doomed);
        }

        return doomed;
    }


```

**变更前代码 (old_code)**
```java
    public ResourceChannel removeResource(Resource resource) {
        if ((this.resourceChannels == null) || (resource == null)) {
            return null;
        }

        ResourceChannel doomed = null;

        for (ResourceChannel rc : this.resourceChannels) {
            if (resource.equals(rc.getResourceChannelPK().getResource())) {
                doomed = rc;
                break;
            }
        }

        if (doomed != null) {
            this.resourceChannels.remove(doomed);
        }

        return doomed;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,19 +1,19 @@
-public ResourceChannel removeResource(Resource resource) {

-        if ((this.resourceChannels == null) || (resource == null)) {

+public ResourceRepo removeResource(Resource resource) {

+        if ((this.resourceRepos == null) || (resource == null)) {

             return null;

         }

 

-        ResourceChannel doomed = null;

+        ResourceRepo doomed = null;

 

-        for (ResourceChannel rc : this.resourceChannels) {

-            if (resource.equals(rc.getResourceChannelPK().getResource())) {

+        for (ResourceRepo rc : this.resourceRepos) {

+            if (resource.equals(rc.getResourceRepoPK().getResource())) {

                 doomed = rc;

                 break;

             }

         }

 

         if (doomed != null) {

-            this.resourceChannels.remove(doomed);

+            this.resourceRepos.remove(doomed);

         }

 

         return doomed;

```

---

### [17/100] `Summary_32`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9985 |
| xMatch | ✓ |

**原注释 (source)**
```
Create an IType for an IASTName.
```

**标准注释 (ground truth)**
```
Create an IType for an IASTDeclarator.
```

**生成注释 (generated)**
```
Create an IType for an IASTDeclarator.
```

**当前代码 (new_code)**
```java
	public static IType createType(IASTDeclarator declarator) {
	    IASTDeclSpecifier declSpec = null;
		
		IASTNode node = declarator.getParent();
		while( node instanceof IASTDeclarator ){
			declarator = (IASTDeclarator) node;
			node = node.getParent();
		}
		
		if( node instanceof IASTParameterDeclaration )
			declSpec = ((IASTParameterDeclaration) node).getDeclSpecifier();
		else if( node instanceof IASTSimpleDeclaration )
			declSpec = ((IASTSimpleDeclaration)node).getDeclSpecifier();
		else if( node instanceof IASTFunctionDefinition )
			declSpec = ((IASTFunctionDefinition)node).getDeclSpecifier();
		else if( node instanceof IASTTypeId )
		    declSpec = ((IASTTypeId)node).getDeclSpecifier();
	
		boolean isParameter = ( node instanceof IASTParameterDeclaration || node.getParent() instanceof ICASTKnRFunctionDeclarator ); 
		
		IType type = null;
		
		//C99 6.7.5.3-12 The storage class specifier for a parameter declaration is ignored unless the declared parameter is one of the 
		//members of the parameter type list for a function definition.
		if( isParameter && node.getParent().getParent() instanceof IASTFunctionDefinition ){
		    type = createBaseType( declSpec );
		} else {
		    type = createType( declSpec );
		}
		
// ... (truncated)
```

**变更前代码 (old_code)**
```java
	public static IType createType(IASTName name) {
		if (!(name.getParent() instanceof IASTDeclarator)) return null;
		
	    IASTDeclSpecifier declSpec = null;
		IASTDeclarator declarator = (IASTDeclarator) name.getParent();
		
		IASTNode node = declarator.getParent();
		while( node instanceof IASTDeclarator ){
			declarator = (IASTDeclarator) node;
			node = node.getParent();
		}
		
		if( node instanceof IASTParameterDeclaration )
			declSpec = ((IASTParameterDeclaration) node).getDeclSpecifier();
		else if( node instanceof IASTSimpleDeclaration )
			declSpec = ((IASTSimpleDeclaration)node).getDeclSpecifier();
		else if( node instanceof IASTFunctionDefinition )
			declSpec = ((IASTFunctionDefinition)node).getDeclSpecifier();
		else if( node instanceof IASTTypeId )
		    declSpec = ((IASTTypeId)node).getDeclSpecifier();
	
		boolean isParameter = ( node instanceof IASTParameterDeclaration || node.getParent() instanceof ICASTKnRFunctionDeclarator ); 
		
		IType type = null;
		
		//C99 6.7.5.3-12 The storage class specifier for a parameter declaration is ignored unless the declared parameter is one of the 
		//members of the parameter type list for a function definition.
		if( isParameter && node.getParent().getParent() instanceof IASTFunctionDefinition ){
		    type = createBaseType( declSpec );
		} else {
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,5 @@
-public static IType createType(IASTName name) {

-		if (!(name.getParent() instanceof IASTDeclarator)) return null;

-		

+public static IType createType(IASTDeclarator declarator) {

 	    IASTDeclSpecifier declSpec = null;

-		IASTDeclarator declarator = (IASTDeclarator) name.getParent();

 		

 		IASTNode node = declarator.getParent();

 		while( node instanceof IASTDeclarator ){

```

---

### [18/100] `Summary_34`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9997 |
| xMatch | ✓ |

**原注释 (source)**
```
Returns a List containing all the child nodes of this node.
```

**标准注释 (ground truth)**
```
Returns a Vector containing all the child nodes of this node.
```

**生成注释 (generated)**
```
Returns a Vector containing all the child nodes of this node.
```

**当前代码 (new_code)**
```java
    protected final Vector getContents() {
        return _contents;
    }


```

**变更前代码 (old_code)**
```java
    protected final List<SyntaxTreeNode> getContents() {
        return _contents;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-protected final List<SyntaxTreeNode> getContents() {

+protected final Vector getContents() {

         return _contents;

     }
```

---

### [20/100] `Summary_38`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9922 |
| xMatch | ✓ |

**原注释 (source)**
```
This method initializes jTextArea
```

**标准注释 (ground truth)**
```
This method initializes ZapTextArea
```

**生成注释 (generated)**
```
This method initializes ZapTextArea
```

**当前代码 (new_code)**
```java
    private ZapTextArea getTxtSkipURL() {
        if (txtSkipURL == null) {
            txtSkipURL = new ZapTextArea();
            txtSkipURL.setFont(new java.awt.Font("Default", java.awt.Font.PLAIN, 11));
    	    if (Model.getSingleton().getOptionsParam().getViewParam().getWmUiHandlingOption() == 0) {
    	    	txtSkipURL.setSize(new java.awt.Dimension(290,52));
    	    }
        }
        return txtSkipURL;
    }

```

**变更前代码 (old_code)**
```java
    private JTextArea getTxtSkipURL() {
        if (txtSkipURL == null) {
            txtSkipURL = new JTextArea();
            txtSkipURL.setFont(new java.awt.Font("Default", java.awt.Font.PLAIN, 11));
    	    if (Model.getSingleton().getOptionsParam().getViewParam().getWmUiHandlingOption() == 0) {
    	    	txtSkipURL.setSize(new java.awt.Dimension(290,52));
    	    }
        }
        return txtSkipURL;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
-private JTextArea getTxtSkipURL() {

+private ZapTextArea getTxtSkipURL() {

         if (txtSkipURL == null) {

-            txtSkipURL = new JTextArea();

+            txtSkipURL = new ZapTextArea();

             txtSkipURL.setFont(new java.awt.Font("Default", java.awt.Font.PLAIN, 11));

     	    if (Model.getSingleton().getOptionsParam().getViewParam().getWmUiHandlingOption() == 0) {

     	    	txtSkipURL.setSize(new java.awt.Dimension(290,52));

```

---

### [26/100] `Summary_50`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9990 |
| xMatch | ✓ |

**原注释 (source)**
```
Get the specific column's ContextColumn object.
```

**标准注释 (ground truth)**
```
Get the specific column's ColumnDescriptor object.
```

**生成注释 (generated)**
```
Get the specific column's ColumnDescriptor object.
```

**当前代码 (new_code)**
```java
	private ColumnDescriptor getColumn(int columnIndex) {
		Tree tree = viewer.getTree();
		TreeColumn column = tree.getColumn(columnIndex);
		ColumnDescriptor descriptor = (ColumnDescriptor) column.getData();
		return descriptor;
	}


```

**变更前代码 (old_code)**
```java
	private ColumnDescriptor getColumn(int columnIndex) {
		Tree tree = viewer.getTree();
		TreeColumn column = tree.getColumn(columnIndex);
		ColumnDescriptor context = (ColumnDescriptor) column.getData();
		return context;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
 private ColumnDescriptor getColumn(int columnIndex) {

 		Tree tree = viewer.getTree();

 		TreeColumn column = tree.getColumn(columnIndex);

-		ColumnDescriptor context = (ColumnDescriptor) column.getData();

-		return context;

+		ColumnDescriptor descriptor = (ColumnDescriptor) column.getData();

+		return descriptor;

 	}
```

---

### [42/100] `Summary_83`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9995 |
| xMatch | ✓ |

**原注释 (source)**
```
Get the global configuration table name including the correct escaped schema
```

**标准注释 (ground truth)**
```
Get the global configuration table name including the correct schema
```

**生成注释 (generated)**
```
Get the global configuration table name including the correct schema
```

**当前代码 (new_code)**
```java
    private String getConfigurationTable(Connection con) {
        try {
            if (StorageManager.getStorageImpl(con.getMetaData().getDatabaseProductName()).requiresConfigSchema()) {
                if (DatabaseConst.getConfigSchema().endsWith("."))
                    return DatabaseConst.getConfigSchema() + TBL_GLOBAL_CONFIG;
                else
                    return DatabaseConst.getConfigSchema() + "." + TBL_GLOBAL_CONFIG;
            }
        } catch (SQLException e) {
            LOG.warn(e);
        }
        return TBL_GLOBAL_CONFIG;
    }


```

**变更前代码 (old_code)**
```java
    private String getConfigurationTable(Connection con) {
        try {
            if (StorageManager.getStorageImpl(con.getMetaData().getDatabaseProductName()).escapeSchema())
                return "\"" + DatabaseConst.getConfigSchema() + "\"." + TBL_GLOBAL_CONFIG;
        } catch (SQLException e) {
            LOG.warn(e);
        }
        return DatabaseConst.getConfigSchema() + "." + TBL_GLOBAL_CONFIG;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,13 @@
 private String getConfigurationTable(Connection con) {

         try {

-            if (StorageManager.getStorageImpl(con.getMetaData().getDatabaseProductName()).escapeSchema())

-                return "\"" + DatabaseConst.getConfigSchema() + "\"." + TBL_GLOBAL_CONFIG;

+            if (StorageManager.getStorageImpl(con.getMetaData().getDatabaseProductName()).requiresConfigSchema()) {

+                if (DatabaseConst.getConfigSchema().endsWith("."))

+                    return DatabaseConst.getConfigSchema() + TBL_GLOBAL_CONFIG;

+                else

+                    return DatabaseConst.getConfigSchema() + "." + TBL_GLOBAL_CONFIG;

+            }

         } catch (SQLException e) {

             LOG.warn(e);

         }

-        return DatabaseConst.getConfigSchema() + "." + TBL_GLOBAL_CONFIG;

+        return TBL_GLOBAL_CONFIG;

     }
```

---

### [44/100] `Summary_87`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9999 |
| xMatch | ✓ |

**原注释 (source)**
```
Obtains a ISTextExpert instance for processing structured text with the specified type handler and the specified environment.
```

**标准注释 (ground truth)**
```
Obtains a IStructuredTextExpert instance for processing structured text with the specified type handler and the specified environment.
```

**生成注释 (generated)**
```
Obtains a IStructuredTextExpert instance for processing structured text with the specified type handler and the specified environment.
```

**当前代码 (new_code)**
```java
	static public IStructuredTextExpert getStatefulExpert(StructuredTextTypeHandler handler, StructuredTextEnvironment environment) {
		if (environment == null)
			environment = StructuredTextEnvironment.DEFAULT;
		return new StructuredTextImpl(handler, environment, true);
	}


```

**变更前代码 (old_code)**
```java
	static public ISTextExpert getStatefulExpert(STextTypeHandler handler, STextEnvironment environment) {
		if (environment == null)
			environment = STextEnvironment.DEFAULT;
		return new STextImpl(handler, environment, true);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-static public ISTextExpert getStatefulExpert(STextTypeHandler handler, STextEnvironment environment) {

+static public IStructuredTextExpert getStatefulExpert(StructuredTextTypeHandler handler, StructuredTextEnvironment environment) {

 		if (environment == null)

-			environment = STextEnvironment.DEFAULT;

-		return new STextImpl(handler, environment, true);

+			environment = StructuredTextEnvironment.DEFAULT;

+		return new StructuredTextImpl(handler, environment, true);

 	}
```

---

### [48/100] `Summary_96`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9985 |
| xMatch | ✓ |

**原注释 (source)**
```
Return the list of Cassandra instances ordered by position on ring, indicated by token.
```

**标准注释 (ground truth)**
```
Return the set of Cassandra instances.
```

**生成注释 (generated)**
```
Return the set of Cassandra instances.
```

**当前代码 (new_code)**
```java
  @GET
  public Set<CassandraInstance> findAll() {
    return service.findAll();
  }


```

**变更前代码 (old_code)**
```java
  @GET
  public List<CassandraInstance> findAll() {
    return service.findAll();
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
 @GET

-  public List<CassandraInstance> findAll() {

+  public Set<CassandraInstance> findAll() {

     return service.findAll();

   }
```

---

### [59/100] `Summary_118`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9997 |
| xMatch | ✓ |

**原注释 (source)**
```
Removes the content source from this channel, if it exists.
```

**标准注释 (ground truth)**
```
Removes the content source from this repo, if it exists.
```

**生成注释 (generated)**
```
Removes the content source from this repo, if it exists.
```

**当前代码 (new_code)**
```java
    public RepoContentSource removeContentSource(ContentSource contentSource) {
        if ((this.repoContentSources == null) || (contentSource == null)) {
            return null;
        }

        RepoContentSource doomed = null;

        for (RepoContentSource ccs : this.repoContentSources) {
            if (contentSource.equals(ccs.getRepoContentSourcePK().getContentSource())) {
                doomed = ccs;
                break;
            }
        }

        if (doomed != null) {
            this.repoContentSources.remove(doomed);
        }

        return doomed;
    }


```

**变更前代码 (old_code)**
```java
    public ChannelContentSource removeContentSource(ContentSource contentSource) {
        if ((this.channelContentSources == null) || (contentSource == null)) {
            return null;
        }

        ChannelContentSource doomed = null;

        for (ChannelContentSource ccs : this.channelContentSources) {
            if (contentSource.equals(ccs.getChannelContentSourcePK().getContentSource())) {
                doomed = ccs;
                break;
            }
        }

        if (doomed != null) {
            this.channelContentSources.remove(doomed);
        }

        return doomed;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,19 +1,19 @@
-public ChannelContentSource removeContentSource(ContentSource contentSource) {

-        if ((this.channelContentSources == null) || (contentSource == null)) {

+public RepoContentSource removeContentSource(ContentSource contentSource) {

+        if ((this.repoContentSources == null) || (contentSource == null)) {

             return null;

         }

 

-        ChannelContentSource doomed = null;

+        RepoContentSource doomed = null;

 

-        for (ChannelContentSource ccs : this.channelContentSources) {

-            if (contentSource.equals(ccs.getChannelContentSourcePK().getContentSource())) {

+        for (RepoContentSource ccs : this.repoContentSources) {

+            if (contentSource.equals(ccs.getRepoContentSourcePK().getContentSource())) {

                 doomed = ccs;

                 break;

             }

         }

 

         if (doomed != null) {

-            this.channelContentSources.remove(doomed);

+            this.repoContentSources.remove(doomed);

         }

 

         return doomed;

```

---

### [60/100] `Summary_120`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9998 |
| xMatch | ✓ |

**原注释 (source)**
```
Returns the meta object for the containment reference '  org.eclipse.mylyn.reviews.core.model.IChange#getState State'.
```

**标准注释 (ground truth)**
```
Returns the meta object for the attribute ' org.eclipse.mylyn.reviews.core.model.IChange#getState State'.
```

**生成注释 (generated)**
```
Returns the meta object for the attribute ' org.eclipse.mylyn.reviews.core.model.IChange#getState State'.
```

**当前代码 (new_code)**
```java
	public EAttribute getChange_State() {
		return (EAttribute) changeEClass.getEStructuralFeatures().get(5);
	}


```

**变更前代码 (old_code)**
```java
	public EReference getChange_State() {
		return (EReference) changeEClass.getEStructuralFeatures().get(5);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public EReference getChange_State() {

-		return (EReference) changeEClass.getEStructuralFeatures().get(5);

+public EAttribute getChange_State() {

+		return (EAttribute) changeEClass.getEStructuralFeatures().get(5);

 	}
```

---

### [62/100] `Summary_124`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9999 |
| xMatch | ✓ |

**原注释 (source)**
```
First authenticates the AuthenticationToken argument, and if successful, constructs a SecurityContext instance representing the authenticated account's identity.
```

**标准注释 (ground truth)**
```
First authenticates the AuthenticationToken argument, and if successful, constructs a Subject instance representing the authenticated account's identity.
```

**生成注释 (generated)**
```
First authenticates the AuthenticationToken argument, and if successful, constructs a Subject instance representing the authenticated account's identity.
```

**当前代码 (new_code)**
```java
    public Subject login(AuthenticationToken token) throws AuthenticationException {
        Account account;
        try {
            account = authenticate(token);
            rememberMeSuccessfulLogin(token, account);
        } catch (AuthenticationException ae) {
            rememberMeFailedLogin(token, ae);
            throw ae; //propagate
        }
        Subject secCtx = createSubject(token, account);
        assertCreation(secCtx);
        bind(secCtx);
        return secCtx;
    }


```

**变更前代码 (old_code)**
```java
    public SecurityContext login(AuthenticationToken token) throws AuthenticationException {
        Account account;
        try {
            account = authenticate(token);
            rememberMeSuccessfulLogin(token, account);
        } catch (AuthenticationException ae) {
            rememberMeFailedLogin(token, ae);
            throw ae; //propagate
        }
        SecurityContext secCtx = createSecurityContext(token, account);
        assertCreation(secCtx);
        bind(secCtx);
        return secCtx;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public SecurityContext login(AuthenticationToken token) throws AuthenticationException {

+public Subject login(AuthenticationToken token) throws AuthenticationException {

         Account account;

         try {

             account = authenticate(token);

@@ -7,7 +7,7 @@
             rememberMeFailedLogin(token, ae);

             throw ae; //propagate

         }

-        SecurityContext secCtx = createSecurityContext(token, account);

+        Subject secCtx = createSubject(token, account);

         assertCreation(secCtx);

         bind(secCtx);

         return secCtx;

```

---

### [65/100] `Summary_130`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9922 |
| xMatch | ✓ |

**原注释 (source)**
```
Build a DruidDimensionsLoader.
```

**标准注释 (ground truth)**
```
Build a DimensionValueLoadTask.
```

**生成注释 (generated)**
```
Build a DimensionValueLoadTask.
```

**当前代码 (new_code)**
```java
    protected DimensionValueLoadTask buildDruidDimensionsLoader(
            DruidWebService webService,
            PhysicalTableDictionary physicalTableDictionary,
            DimensionDictionary dimensionDictionary
    ) {
        DruidDimensionValueLoader druidDimensionRowProvider = new DruidDimensionValueLoader(
                physicalTableDictionary,
                dimensionDictionary,
                webService
        );
        return new DimensionValueLoadTask(Collections.singletonList(druidDimensionRowProvider));
    }


```

**变更前代码 (old_code)**
```java
    protected DruidDimensionsLoader buildDruidDimensionsLoader(
            DruidWebService webService,
            PhysicalTableDictionary physicalTableDictionary,
            DimensionDictionary dimensionDictionary
    ) {
        return new DruidDimensionsLoader(
                physicalTableDictionary,
                dimensionDictionary,
                webService
        );
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,12 @@
-protected DruidDimensionsLoader buildDruidDimensionsLoader(

+protected DimensionValueLoadTask buildDruidDimensionsLoader(

             DruidWebService webService,

             PhysicalTableDictionary physicalTableDictionary,

             DimensionDictionary dimensionDictionary

     ) {

-        return new DruidDimensionsLoader(

+        DruidDimensionValueLoader druidDimensionRowProvider = new DruidDimensionValueLoader(

                 physicalTableDictionary,

                 dimensionDictionary,

                 webService

         );

+        return new DimensionValueLoadTask(Collections.singletonList(druidDimensionRowProvider));

     }
```

---

### [75/100] `Summary_152`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9998 |
| xMatch | ✗ |

**原注释 (source)**
```
Creates a  UserAdapter if there is more than one profile on the device.
```

**标准注释 (ground truth)**
```
Creates a  UserSpinnerAdapter if there is more than one profile on the device.
```

**生成注释 (generated)**
```
Creates a UserSpinnerAdapter if there is more than one profile on the device.
```

**当前代码 (new_code)**
```java
    public static UserSpinnerAdapter createUserSpinnerAdapter(UserManager userManager,
            Context context) {
        List<UserHandle> userProfiles = userManager.getUserProfiles();
        if (userProfiles.size() < 2) {
            return null;
        }

        UserHandle myUserHandle = new UserHandle(UserHandle.myUserId());
        // The first option should be the current profile
        userProfiles.remove(myUserHandle);
        userProfiles.add(0, myUserHandle);

        ArrayList<UserDetails> userDetails = new ArrayList<UserDetails>(userProfiles.size());
        final int count = userProfiles.size();
        for (int i = 0; i < count; i++) {
            userDetails.add(new UserDetails(userProfiles.get(i), userManager, context));
        }
        return new UserSpinnerAdapter(context, userDetails);
    }


```

**变更前代码 (old_code)**
```java
    public static UserAdapter createUserSpinnerAdapter(UserManager userManager,
            Context context) {
        List<UserHandle> userProfiles = userManager.getUserProfiles();
        if (userProfiles.size() < 2) {
            return null;
        }

        UserHandle myUserHandle = new UserHandle(UserHandle.myUserId());
        // The first option should be the current profile
        userProfiles.remove(myUserHandle);
        userProfiles.add(0, myUserHandle);

        return createUserAdapter(userManager, context, userProfiles);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public static UserAdapter createUserSpinnerAdapter(UserManager userManager,

+public static UserSpinnerAdapter createUserSpinnerAdapter(UserManager userManager,

             Context context) {

         List<UserHandle> userProfiles = userManager.getUserProfiles();

         if (userProfiles.size() < 2) {

@@ -10,5 +10,10 @@
         userProfiles.remove(myUserHandle);

         userProfiles.add(0, myUserHandle);

 

-        return createUserAdapter(userManager, context, userProfiles);

+        ArrayList<UserDetails> userDetails = new ArrayList<UserDetails>(userProfiles.size());

+        final int count = userProfiles.size();

+        for (int i = 0; i < count; i++) {

+            userDetails.add(new UserDetails(userProfiles.get(i), userManager, context));

+        }

+        return new UserSpinnerAdapter(context, userDetails);

     }
```

---

### [76/100] `Summary_154`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9985 |
| xMatch | ✗ |

**原注释 (source)**
```
Returns  TwitterTokenStream to tokenize a text.
```

**标准注释 (ground truth)**
```
Returns  TokenStream to tokenize a text.
```

**生成注释 (generated)**
```
Returns TokenStream to tokenize a text.
```

**当前代码 (new_code)**
```java
  public TokenStream getDefaultTokenStream() {
    return tokenizationStream;
  }


```

**变更前代码 (old_code)**
```java
  public TwitterTokenStream getDefaultTokenStream() {
    return tokenizationStream;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public TwitterTokenStream getDefaultTokenStream() {

+public TokenStream getDefaultTokenStream() {

     return tokenizationStream;

   }
```

---

### [97/100] `Summary_197`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5623 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9815 |
| xMatch | ✗ |

**原注释 (source)**
```
Return the  org.atmosphere.cpr.MetaBroadcaster
```

**标准注释 (ground truth)**
```
Return the  DefaultMetaBroadcaster
```

**生成注释 (generated)**
```
Return the DefaultMetaBroadcaster
```

**当前代码 (new_code)**
```java
    public static DefaultMetaBroadcaster metaBroadcaster() {
        return metaBroadcaster;
    }


```

**变更前代码 (old_code)**
```java
    public static MetaBroadcaster metaBroadcaster() {
        return metaBroadcaster;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static MetaBroadcaster metaBroadcaster() {

+public static DefaultMetaBroadcaster metaBroadcaster() {

         return metaBroadcaster;

     }
```

---

