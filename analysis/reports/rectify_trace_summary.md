# Rectifier 逐样本追踪报告

## 汇总指标

- **xMatch (%)**: 24.0
- **BLEU-4**: 0.5355
- **GLEU**: 0.5702
- **Meteor**: 0.6966
- **SARI**: 0.6701
- **Samples_Evaluated**: 50

## 汇总一览（按 SARI 升序，最差排前）

| # | ID | 检测到 | xMatch | BLEU-4 | SARI | METEOR | 原注释(前60) | 生成(前60) |
|---|---|---|---|---|---|---|---|---|
| 1 | `Summary_92` | ✓ |  | 0.053 | 0.186 | 0.208 | Get the parent cuboid really on the spanning tree. | Get the best match cuboid. |
| 2 | `Summary_4` | ✓ |  | 0.652 | 0.263 | 0.871 | Create an instance based on current maven profile (as define | Create an instance based on current MongoAssertions (as defi |
| 3 | `Summary_58` | ✓ |  | 0.367 | 0.308 | 0.795 | Creates and returns a new comparison object for the SQL "in" | Creates and returns a new comparison object for the SQL "in" |
| 4 | `Summary_40` | ✗(漏检) |  | 0.013 | 0.345 | 0.041 | Determines if a specified set of columns from a specified re | Determines if a specified set of columns from a specified re |
| 5 | `Summary_100` | ✓ |  | 0.019 | 0.348 | 0.054 | Get entry data, read directly from internal data structure. | Get entry data, read directly from internal data structure. |
| 6 | `Summary_69` | ✗(漏检) |  | 0.025 | 0.361 | 0.182 | Ensure that correct implementation is used for the component | Ensure that correct implementation is used for the component |
| 7 | `Summary_73` | ✓ |  | 0.137 | 0.383 | 0.618 | Encodes a value in a canonical serialized string format, for | Encodes a value in a canonical serialized string format. |
| 8 | `Summary_44` | ✓ |  | 0.731 | 0.422 | 0.897 | The  #add(Object...) method uses Java variable-length argume | The #addSingleCol(Object) method uses Java variable-length a |
| 9 | `Summary_75` | ✓ |  | 0.093 | 0.429 | 0.626 | Loads the  JBossWebSocketHandler using reflection as it impo | Loads the JBossWebSocketHandler directly as it imports conta |
| 10 | `Summary_0` | ✓ |  | 0.049 | 0.450 | 0.086 | Creates elastic node as single member of a cluster. | Creates elastic node. |
| 11 | `Summary_65` | ✓ |  | 0.437 | 0.464 | 0.591 | Returns all currently displayed sentences in plain text form | Returns all currently displayed sentences in StringBuffer fo |
| 12 | `Summary_52` | ✓ |  | 0.106 | 0.466 | 0.301 | Create a CoreMap representing a sentence from this protocol  | Create a CoreLabel representing a token from this protocol b |
| 13 | `Summary_81` | ✓ |  | 0.154 | 0.472 | 0.820 | Installs a list of  RemotePackage and their dependent packag | Installs a list of RemotePackage and their dependent package |
| 14 | `Summary_94` | ✓ |  | 0.017 | 0.520 | 0.264 | String representation of the signature. | String representation of the cached signature. |
| 15 | `Summary_12` | ✓ |  | 0.023 | 0.542 | 0.190 | Only the views are mirrored. | Only the mirroring is enabled. |
| 16 | `Summary_16` | ✓ |  | 0.355 | 0.542 | 0.589 | Create a web page using the given template,  SecurityContext | Create a web page using the given template, SecurityContext. |
| 17 | `Summary_8` | ✓ |  | 0.552 | 0.570 | 0.824 | Provides a list containing four set, each containing project | Provides a list containing four set, each containing project |
| 18 | `Summary_79` | ✗(漏检) |  | 0.551 | 0.583 | 0.829 | Does this time interval contain the specified time interval  | Does this time interval contain the specified time interval  |
| 19 | `Summary_61` | ✓ |  | 0.531 | 0.613 | 0.878 | Returns all currently displayed sentences in string buffer,  | Returns all currently displayed sentences in string builder, |
| 20 | `Summary_85` | ✓ |  | 0.706 | 0.616 | 0.791 | Gets the total number of bytes uploaded by this uploader or  | Gets the total number of bytes uploaded by this uploader or  |
| 21 | `Summary_77` | ✓ |  | 0.437 | 0.616 | 0.542 | Returns the common base directory between a current base dir | Returns the common base directory between two files. |
| 22 | `Summary_36` | ✗(漏检) |  | 0.701 | 0.619 | 0.907 | Method that get's left and right incoming batch and produce  | Method that get's left and right incoming batch and produce  |
| 23 | `Summary_46` | ✓ |  | 0.680 | 0.636 | 0.844 | Returns if this query should buffer before emitting results. | Returns if this query should buffer before emitting results. |
| 24 | `Summary_42` | ✓ |  | 0.517 | 0.637 | 0.799 | Expr : left.endsWith(right) (ignore case) | Expr : left.endsWith(right) (case sensitive) |
| 25 | `Summary_18` | ✗(漏检) |  | 0.208 | 0.642 | 0.432 | Return XML schema for the specified type, suitable for inser | Return XML schema for the specified type, suitable for inser |
| 26 | `Summary_48` | ✓ |  | 0.774 | 0.656 | 0.984 | Adds a menu item to the bar containing SafeHtml, that will f | Adds a menu item to the bar containing String text, that wil |
| 27 | `Summary_67` | ✗(漏检) |  | 0.821 | 0.656 | 0.889 | If a Schema contains a reference to an other Schema with '$r | If a Schema contains a reference to an other Schema with '$r |
| 28 | `Summary_24` | ✗(漏检) |  | 0.536 | 0.659 | 0.575 | Check if the Elasticsearch  Node is connected and that the c | Check if the Elasticsearch  Node is connected and that the c |
| 29 | `Summary_26` | ✓ |  | 0.705 | 0.667 | 0.861 | Returns true if, the lockClient is keeping the lock for the  | Returns true if, the serverName is keeping the lock for the  |
| 30 | `Summary_71` | ✓ |  | 0.809 | 0.667 | 0.927 | Return the GraphItem representing the second (target) node i | Return the Node representing the second (target) node in the |
| 31 | `Summary_63` | ✓ |  | 0.017 | 0.675 | 0.108 | DOCUMENT ME! | Process HTML content and return links if robot follow is all |
| 32 | `Summary_30` | ✓ |  | 0.061 | 0.676 | 0.338 | Checks if a flag is set. | Checks if flags are set. |
| 33 | `Summary_54` | ✓ |  | 0.061 | 0.676 | 0.338 | Checks if a flag is set. | Checks if flags are set. |
| 34 | `Summary_6` | ✓ |  | 0.092 | 0.745 | 0.594 | Returns | Returns the file from the queue. |
| 35 | `Summary_28` | ✓ |  | 0.893 | 0.798 | 0.909 | Unsubscribes the resource from this channel, if it exists. | Removes the resource from this repo, if it exists. |
| 36 | `Summary_98` | ✓ |  | 0.212 | 0.798 | 0.551 | DOCUMENT ME! | Returns the replication directory. |
| 37 | `Summary_2` | ✓ |  | 0.795 | 0.870 | 0.898 | Marshal the aggregator values of to a JSONArray that will la | Marshal the aggregator values of to a byte array that will l |
| 38 | `Summary_20` | ✓ |  | 0.882 | 0.932 | 0.898 | Add a tag to the set of filters | Add a tagId to the set of filters |
| 39 | `Summary_10` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Returns the providers that are bound to the same location as | Returns the providers that are bound to the same location as |
| 40 | `Summary_14` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | Build a Ravioli client | Build a Lob client |
| 41 | `Summary_22` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Return the list of module prefixes that are defined for this | Return the list of module prefixes that are defined for this |
| 42 | `Summary_32` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | Create an IType for an IASTName. | Create an IType for an IASTDeclarator. |
| 43 | `Summary_34` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Returns a List containing all the child nodes of this node. | Returns a Vector containing all the child nodes of this node |
| 44 | `Summary_38` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | This method initializes jTextArea | This method initializes ZapTextArea |
| 45 | `Summary_50` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | Get the specific column's ContextColumn object. | Get the specific column's ColumnDescriptor object. |
| 46 | `Summary_56` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | Parses a Specification out of the query string. | Parses a Query out of the query string. |
| 47 | `Summary_83` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Get the global configuration table name including the correc | Get the global configuration table name including the correc |
| 48 | `Summary_87` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Obtains a ISTextExpert instance for processing structured te | Obtains a IStructuredTextExpert instance for processing stru |
| 49 | `Summary_89` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | Create and return a new feature service with the default ser | Create and return a new feature service with the default end |
| 50 | `Summary_96` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | Return the list of Cassandra instances ordered by position o | Return the set of Cassandra instances. |

---

## 逐样本详情

### [46/50] `Summary_92`

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

**代码片段**
```java
    public long findBestMatchCuboid(long cuboid) {
        return findBestMatchCuboid1(cuboid);
    }

```

---

### [3/50] `Summary_4`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6515 |
| SARI | 0.2626 |
| GLEU | 0.6667 |
| METEOR | 0.8709 |
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
Create an instance based on current MongoAssertions (as defined by -Pit).
```

**代码片段**
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

---

### [30/50] `Summary_58`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3671 |
| SARI | 0.3077 |
| GLEU | 0.3919 |
| METEOR | 0.7948 |
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
Creates and returns a new comparison object for the SQL "in" operator with a collection of values.
```

**代码片段**
```java
    public final DBCompareColExpr in(Collection<?> values)
    {
        if (values==null || values.isEmpty())
            return cmp(DBCmpType.EQUAL, null);
        // create expression
        return cmp(DBCmpType.IN, values);
    }


```

---

### [21/50] `Summary_40`

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

**代码片段**
```java
  public static Boolean areColumnsUnique(RelNode rel, BitSet columns) {
    final BuiltInMetadata.ColumnUniqueness metadata =
        rel.metadata(BuiltInMetadata.ColumnUniqueness.class);
    return metadata.areColumnsUnique(columns, false);
  }

```

---

### [50/50] `Summary_100`

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

**代码片段**
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

---

### [35/50] `Summary_69`

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

**代码片段**
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

---

### [37/50] `Summary_73`

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

**代码片段**
```java
	public static String encodeValue(Value value) {
		return NTriplesUtil.toNTriplesString(value);
	}


```

---

### [23/50] `Summary_44`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7309 |
| SARI | 0.4216 |
| GLEU | 0.7429 |
| METEOR | 0.8970 |
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
The #addSingleCol(Object) method uses Java variable-length arguments to pass a row of values.
```

**代码片段**
```java
  public RowSetBuilder addSingleCol(Object value) {
    return addRow(new Object[] { value });
  }

```

---

### [38/50] `Summary_75`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0933 |
| SARI | 0.4289 |
| GLEU | 0.1579 |
| METEOR | 0.6265 |
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
Loads the JBossWebSocketHandler directly as it imports container specific classes.
```

**代码片段**
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

---

### [1/50] `Summary_0`

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

**代码片段**
```java
  private static EmbeddedElasticsearchNode create(Settings settings) {
    // ensure PainlessPlugin is installed or otherwise scripted fields would not work
    Node node = new LocalNode(settings, Arrays.asList(Netty4Plugin.class, PainlessPlugin.class));
    return new EmbeddedElasticsearchNode(node);
  }

```

---

### [33/50] `Summary_65`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4374 |
| SARI | 0.4637 |
| GLEU | 0.4524 |
| METEOR | 0.5913 |
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
Returns all currently displayed sentences in StringBuffer form.
```

**代码片段**
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

---

### [27/50] `Summary_52`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1060 |
| SARI | 0.4662 |
| GLEU | 0.2105 |
| METEOR | 0.3012 |
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
Create a CoreLabel representing a token from this protocol buffer.
```

**代码片段**
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

---

### [41/50] `Summary_81`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
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
Installs a list of RemotePackage and their dependent packages.
```

**代码片段**
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

---

### [47/50] `Summary_94`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0173 |
| SARI | 0.5202 |
| GLEU | 0.0758 |
| METEOR | 0.2639 |
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
String representation of the cached signature.
```

**代码片段**
```java
    @Override
    public String toString() {
        if (stringRep == null) {
            stringRep = toString(true);
        }
    	return stringRep;
    }


```

---

### [7/50] `Summary_12`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0234 |
| SARI | 0.5417 |
| GLEU | 0.0789 |
| METEOR | 0.1905 |
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
Only the mirroring is enabled.
```

**代码片段**
```java
	public boolean isMirrored() {
		if (!fMirroringEnabled)
			return false;
		Object property = getProperty(MIRRORED);
		return property instanceof Boolean && (Boolean) property;
	}


```

---

### [9/50] `Summary_16`

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

**代码片段**
```java
  public static Viewable create(final boolean authEnabled, final String templateName, final SecurityContext sc) {
    return new ViewableWithPermissions(authEnabled, templateName, sc, true, null);
  }

```

---

### [5/50] `Summary_8`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5524 |
| SARI | 0.5698 |
| GLEU | 0.5660 |
| METEOR | 0.8238 |
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
Provides a list containing four set, each containing projects to be displayed on the project view for projects using the parameterized trigger plugin under 'Subprojects'.
```

**代码片段**
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

---

### [40/50] `Summary_79`

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

**代码片段**
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

---

### [31/50] `Summary_61`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5311 |
| SARI | 0.6132 |
| GLEU | 0.5714 |
| METEOR | 0.8775 |
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
Returns all currently displayed sentences in string builder, plain text form
```

**代码片段**
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

---

### [43/50] `Summary_85`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
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
Gets the total number of bytes uploaded by this uploader or 0 for direct uploads when the content length is not known.
```

**代码片段**
```java
  @Deprecated
  public long getNumBytesUploaded() {
    return totalBytesServerReceived;
  }


```

---

### [39/50] `Summary_77`

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

**代码片段**
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

---

### [19/50] `Summary_36`

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

**代码片段**
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

---

### [24/50] `Summary_46`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
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

**代码片段**
```java
    public boolean shouldBuffer() {
        Window window = runningQuery.getQuery().getWindow();
        boolean noWindow =  window == null;
        // Only buffer if there is no window (including Raw) or if it's a record based window.
        return noWindow || !window.isTimeBased();
    }


```

---

### [22/50] `Summary_42`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5170 |
| SARI | 0.6367 |
| GLEU | 0.5294 |
| METEOR | 0.7986 |
| xMatch | ✗ |

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
Expr : left.endsWith(right) (case sensitive)
```

**代码片段**
```java
    public static EBoolean endsWith(Expr<String> left, String right) {
        return operationFactory.createBoolean(Ops.ENDSWITH, left, exprFactory
                .createConstant(right));
    }

```

---

### [10/50] `Summary_18`

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

**代码片段**
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

---

### [25/50] `Summary_48`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7739 |
| SARI | 0.6563 |
| GLEU | 0.7805 |
| METEOR | 0.9839 |
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
Adds a menu item to the bar containing String text, that will fire the given command when it is selected.
```

**代码片段**
```java
  public MenuItem addItem(String text, boolean asHTML, Command cmd) {
    return addItem(new MenuItem(text, asHTML, cmd));
  }

```

---

### [34/50] `Summary_67`

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
If a Schema contains a reference to an other Schema with '$ref', returns the referenced Schema or the actual Schema in the other cases.
```

**标准注释 (ground truth)**
```
If a Schema contains a reference to an other Schema with '$ref', returns the referenced Schema if it is found or the actual Schema in the other cases.
```

**生成注释 (generated)**
```
If a Schema contains a reference to an other Schema with '$ref', returns the referenced Schema or the actual Schema in the other cases.
```

**代码片段**
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

---

### [13/50] `Summary_24`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5355 |
| SARI | 0.6591 |
| GLEU | 0.5877 |
| METEOR | 0.5746 |
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
Check if the Elasticsearch  Node is connected and that the cluster health status is not  ClusterHealthStatus#RED.
```

**代码片段**
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

---

### [14/50] `Summary_26`

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

**代码片段**
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

---

### [36/50] `Summary_71`

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

**代码片段**
```java
	public Node getSecondNode() {
		return m_node2;
	} //


```

---

### [32/50] `Summary_63`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0170 |
| SARI | 0.6750 |
| GLEU | 0.0238 |
| METEOR | 0.1075 |
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
Process HTML content and return links if robot follow is allowed.
```

**代码片段**
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

---

### [16/50] `Summary_30`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0605 |
| SARI | 0.6763 |
| GLEU | 0.1600 |
| METEOR | 0.3379 |
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
Checks if flags are set.
```

**代码片段**
```java
    public boolean isFlagSet(int flagsToCheck) {
        return (flags & flagsToCheck) != 0;
    }


```

---

### [28/50] `Summary_54`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0605 |
| SARI | 0.6763 |
| GLEU | 0.1600 |
| METEOR | 0.3379 |
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
Checks if flags are set.
```

**代码片段**
```java
    public boolean isFlagSet(int flagsToCheck) {
        return isFlagSet(flags, flagsToCheck);
    }


```

---

### [4/50] `Summary_6`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0919 |
| SARI | 0.7454 |
| GLEU | 0.2273 |
| METEOR | 0.5943 |
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
Returns the file from the queue.
```

**代码片段**
```java
	public File getSinkFile() {
		return queue.file();
	}


```

---

### [15/50] `Summary_28`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8932 |
| SARI | 0.7980 |
| GLEU | 0.8947 |
| METEOR | 0.9086 |
| xMatch | ✗ |

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
Removes the resource from this repo, if it exists.
```

**代码片段**
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

---

### [49/50] `Summary_98`

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

**代码片段**
```java
    public String getReplicationDirectory() {
        return this.replicationDirectory;
    }


```

---

### [2/50] `Summary_2`

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

**代码片段**
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

---

### [11/50] `Summary_20`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8825 |
| SARI | 0.9317 |
| GLEU | 0.8667 |
| METEOR | 0.8980 |
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
Add a tagId to the set of filters
```

**代码片段**
```java
    public boolean add(String tagId, String category) {
        return isCategoryValid(category) && mSelectedTopics.add(tagId);
    }


```

---

### [6/50] `Summary_10`

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

**代码片段**
```java
   public static Iterable<ProviderMetadata> boundedByIso3166Code(String iso3166Code,
            TypeToken<? extends Wrapper> contextWrappableAs) {
      return filter(all(), Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates
               .contextWrappableAs(contextWrappableAs)));
   }


```

---

### [8/50] `Summary_14`

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
Build a Ravioli client
```

**标准注释 (ground truth)**
```
Build a Lob client
```

**生成注释 (generated)**
```
Build a Lob client
```

**代码片段**
```java
        public Lob build() {
            return new Lob(this);
        }


```

---

### [12/50] `Summary_22`

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

**代码片段**
```java
    public static String[] getModulePrefixes(ServletContext context) {
        return (String[]) context.getAttribute(Globals.MODULE_PREFIXES_KEY);
    }


```

---

### [17/50] `Summary_32`

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

**代码片段**
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

---

### [18/50] `Summary_34`

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

**代码片段**
```java
    protected final Vector getContents() {
        return _contents;
    }


```

---

### [20/50] `Summary_38`

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

**代码片段**
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

---

### [26/50] `Summary_50`

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

**代码片段**
```java
	private ColumnDescriptor getColumn(int columnIndex) {
		Tree tree = viewer.getTree();
		TreeColumn column = tree.getColumn(columnIndex);
		ColumnDescriptor descriptor = (ColumnDescriptor) column.getData();
		return descriptor;
	}


```

---

### [29/50] `Summary_56`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9993 |
| xMatch | ✓ |

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
Parses a Query out of the query string.
```

**代码片段**
```java
    public static Query parse(String queryString, BulletConfig config) {
        Query query = GSON.fromJson(queryString, Query.class);
        query.configure(config);
        return query;
    }


```

---

### [42/50] `Summary_83`

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

**代码片段**
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

---

### [44/50] `Summary_87`

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

**代码片段**
```java
	static public IStructuredTextExpert getStatefulExpert(StructuredTextTypeHandler handler, StructuredTextEnvironment environment) {
		if (environment == null)
			environment = StructuredTextEnvironment.DEFAULT;
		return new StructuredTextImpl(handler, environment, true);
	}


```

---

### [45/50] `Summary_89`

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
Create and return a new feature service with the default server URL.
```

**标准注释 (ground truth)**
```
Create and return a new feature service with the default endpoint URL.
```

**生成注释 (generated)**
```
Create and return a new feature service with the default endpoint URL.
```

**代码片段**
```java
    public FeatureService createFeatureService() {
        return createFeatureService(defaultEndpointUrl);
    }


```

---

### [48/50] `Summary_96`

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

**代码片段**
```java
  @GET
  public Set<CassandraInstance> findAll() {
    return service.findAll();
  }


```

---

