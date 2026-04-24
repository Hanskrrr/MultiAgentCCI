# Rectifier 逐样本追踪报告

## 汇总指标

- **xMatch (%)**: 25.0
- **BLEU-4**: 0.5283
- **GLEU**: 0.5971
- **Meteor**: 0.7491
- **SARI**: 0.6529
- **Samples_Evaluated**: 52

## 汇总一览（按 SARI 升序，最差排前）

| # | ID | 检测到 | xMatch | BLEU-4 | SARI | METEOR | 原注释(前60) | 生成(前60) |
|---|---|---|---|---|---|---|---|---|
| 1 | `Return_58` | ✓ |  | 0.292 | 0.145 | 0.638 | @return true if the example is compatible with the mode of t | @return true if the example is compatible with the provided  |
| 2 | `Return_24` | ✓ |  | 0.178 | 0.160 | 0.852 | @return new background color based on the supplied foregroun | @return new Color object based on the supplied foreground co |
| 3 | `Return_64` | ✓ |  | 0.066 | 0.210 | 0.428 | @return when the work has ben accepted. | @return the accepted time. |
| 4 | `Return_20` | ✓ |  | 0.240 | 0.228 | 0.625 | @return javax.swing.JTextField | @return ZapTextArea |
| 5 | `Return_42` | ✓ |  | 0.240 | 0.228 | 0.625 | @return javax.swing.JTextField | @return ZapTextArea |
| 6 | `Return_98` | ✓ |  | 0.240 | 0.228 | 0.625 | @return javax.swing.JMenuItem | @return ZapMenuItem |
| 7 | `Return_30` | ✓ |  | 0.538 | 0.247 | 0.673 | @return the value of this attribute if this attribute is pre | @return the value of this attribute if this attribute is pre |
| 8 | `Return_76` | ✓ |  | 0.071 | 0.250 | 0.272 | @return A List of Sentence of TaggedWord | @return A List of ArrayList of TaggedWord |
| 9 | `Return_92` | ✓ |  | 0.410 | 0.444 | 0.533 | @return Object value of the property - or null | @return Object value of the property - or throws IllegalArgu |
| 10 | `Return_16` | ✓ |  | 0.123 | 0.444 | 0.258 | @return Whether is successful to set the task completed. If  | @return Whether is successful to set the task completed. If  |
| 11 | `Return_18` | ✗(漏检) |  | 0.202 | 0.470 | 0.701 | @return A SqlParser object. | @return A SqlParser object. |
| 12 | `Return_2` | ✓ |  | 0.408 | 0.474 | 0.613 | @return The string representation as a comma-separated list  | @return The string representation. |
| 13 | `Return_66` | ✓ |  | 0.839 | 0.481 | 0.944 | @return The name of the main character of a user. Returns nu | @return The JSONObject of the main character of a user. Retu |
| 14 | `Return_88` | ✗(漏检) |  | 0.146 | 0.483 | 0.647 | @return total count | @return total count |
| 15 | `Return_34` | ✓ |  | 0.073 | 0.505 | 0.370 | @return an <code>Iterator</code> | @return a Group[] |
| 16 | `Return_40` | ✓ |  | 0.040 | 0.508 | 0.670 | @return a <code>File<code> value | @return a <code>String<code> value |
| 17 | `Return_90` | ✗(漏检) |  | 0.339 | 0.520 | 0.782 | @return an option of the first object of the iteration | @return an option of the first object of the iteration |
| 18 | `Return_94` | ✓ |  | 0.267 | 0.537 | 0.620 | @return true if we have enough data to decode the PI frame f | @return NUM if we have enough data to decode the PI frame fu |
| 19 | `Return_48` | ✗(漏检) |  | 0.512 | 0.588 | 0.853 | @return URL with query params | @return URL with query params |
| 20 | `Return_46` | ✓ |  | 0.103 | 0.593 | 0.654 | @return the parsed Test Suite or null if no Test Suite was f | @return the parsed Test Suites or empty list if no Test Suit |
| 21 | `Return_8` | ✓ |  | 0.513 | 0.610 | 0.865 | @return Host name and port, as a string. | @return Host name, as a string. |
| 22 | `Return_56` | ✓ |  | 0.655 | 0.612 | 0.829 | @return The maximum query evaluation time, in milliseconds. | @return The maximum query evaluation time, in milliseconds. |
| 23 | `Return_14` | ✓ |  | 0.024 | 0.617 | 0.219 | @return the {@link Cursor} backing this SquidCursor | @return the {@link ICursor} backing this SquidCursor |
| 24 | `Return_62` | ✓ |  | 0.477 | 0.627 | 0.668 | @return Get method or null if none found. | @return Get method or null if none found. |
| 25 | `Return_84` | ✓ |  | 0.639 | 0.633 | 0.672 | @return the extension handler used by this SVGGraphics2D ins | @return the extension handler used by this generatorContext  |
| 26 | `Return_86` | ✗(漏检) |  | 0.362 | 0.643 | 0.555 | @return {@link CacheStatisticsImpl}. | @return {@link CacheStatisticsImpl}. |
| 27 | `Return_102` | ✗(漏检) |  | 0.408 | 0.647 | 0.585 | @return A read-only view of the additionalHttpHeaders. | @return A read-only view of the additionalHttpHeaders. |
| 28 | `Return_22` | ✓ |  | 0.661 | 0.664 | 0.910 | @return a List of the combined {@link BulletRecord} so far.  | @return a Clip of the combined {@link BulletRecord} so far.  |
| 29 | `Return_26` | ✓ |  | 0.595 | 0.667 | 0.865 | @return ProjectRel corresponding to the right child | @return Project corresponding to the right child |
| 30 | `Return_54` | ✗(漏检) |  | 0.651 | 0.667 | 0.721 | @return true if habit has reminder | @return true if habit has reminder |
| 31 | `Return_60` | ✓ |  | 0.165 | 0.667 | 0.661 | @return the extended FluentPipeline | @return the extended GremlinPipeline<S, Map<String, Object>> |
| 32 | `Return_74` | ✗(漏检) |  | 0.534 | 0.702 | 0.979 | @return the ObjectName for the given exchange on the test Vi | @return the ObjectName for the given exchange on the test Vi |
| 33 | `Return_32` | ✓ |  | 0.285 | 0.724 | 0.443 | @return the ID of the last baseline build. | @return the ID of the last baseline build before the specifi |
| 34 | `Return_12` | ✓ |  | 0.925 | 0.730 | 0.993 | @return <code>true</code> if the button is visible and Popup | @return <code>true</code> if the button is visible. |
| 35 | `Return_68` | ✓ |  | 0.240 | 0.750 | 0.625 | @return ping host | @return this |
| 36 | `Return_50` | ✓ |  | 0.419 | 0.760 | 0.485 | @return The {@link CmdLineOptionInstance}s which failed vali | @return The {@link CmdLineOptionValidator.Result}s which fai |
| 37 | `Return_0` | ✓ |  | 0.749 | 0.798 | 0.920 | @return an open input stream, or null if no suitable output  | @return a generated output file, or null if no suitable outp |
| 38 | `Return_4` | ✓ |  | 0.606 | 0.828 | 0.632 | @return an instance of the specified class | @return an instance of the specified class or null if creati |
| 39 | `Return_96` | ✓ |  | 0.670 | 0.865 | 0.989 | @return This same sentence, but with the default properties  | @return A new Sentence instance with the default properties  |
| 40 | `Return_6` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return {@code TokenStream} to tokenize the text | @return {@code TwitterTokenStream} to tokenize the text |
| 41 | `Return_10` | ✓ | ✓ | 1.000 | 1.000 | 0.996 | @return the ApplicationConfig object | @return the ModuleConfig object |
| 42 | `Return_28` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | @return a Line | @return an AudioInputStream |
| 43 | `Return_36` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return a list of jobs which had never been started if timeo | @return a list of jobs which had never been started if timeo |
| 44 | `Return_38` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return An Enumeration of all child nodes of this node. | @return An Iterator of all child nodes of this node. |
| 45 | `Return_44` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return A {@link Hashtable} representation of a {@link Workf | @return A {@link HashMap} representation of a {@link Workflo |
| 46 | `Return_52` | ✓ | ✓ | 0.562 | 1.000 | 0.981 | @return ModuleClassLoader | @return ModuleJarClassLoader |
| 47 | `Return_70` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return a StyleSheetProcessingInstruction if target is "xml- | @return a SVGStyleSheetProcessingInstruction if target is "x |
| 48 | `Return_72` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | @return the id_category | @return the id |
| 49 | `Return_78` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return the char[] | @return the union of the char[]s |
| 50 | `Return_80` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return a new feature service with the default server URL | @return a new feature service with the default endpoint URL |
| 51 | `Return_82` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | @return the HornetQConnectionFactory | @return the ActiveMQConnectionFactory |
| 52 | `Return_100` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @return the associated {@link HttpServletRequest} | @return the associated {@link AtmosphereRequest} |

---

## 逐样本详情

### [30/52] `Return_58`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2917 |
| SARI | 0.1448 |
| GLEU | 0.3696 |
| METEOR | 0.6379 |
| xMatch | ✗ |

**原注释 (source)**
```
@return true if the example is compatible with the mode of the currently active editor
```

**标准注释 (ground truth)**
```
@return true if compatible with the Mode of the currently active editor
```

**生成注释 (generated)**
```
@return true if the example is compatible with the provided mode
```

**代码片段**
```java
  static public boolean isCompatible(Mode mode, StringDict props) {
    String currentIdentifier = mode.getIdentifier();
    StringList compatibleList = parseModeList(props);
    if (compatibleList.size() == 0) {
      if (mode.requireExampleCompatibility()) {
        // for p5js (and maybe Python), examples must specify that they work
        return false;
      }
      // if no Mode specified, assume compatible everywhere
      return true;
    }
    return compatibleList.hasValue(currentIdentifier);
  }

```

---

### [13/52] `Return_24`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1783 |
| SARI | 0.1604 |
| GLEU | 0.3947 |
| METEOR | 0.8520 |
| xMatch | ✗ |

**原注释 (source)**
```
@return new background color based on the supplied foreground color
```

**标准注释 (ground truth)**
```
@return new background color based on the foreground color
```

**生成注释 (generated)**
```
@return new Color object based on the supplied foreground color
```

**代码片段**
```java
private Color invertBgColor() {
    if (currentColor_.defaultColor()) {
        if (!inverted_)
            clazzes_.add(INVERSE_BG_STYLE);
        return new Color();
    } else if (currentColor_.isExtended()) {
        clazzes_.add(Color.clazzForColorIndex(currentColor_.code(), true));
        return new Color(true, currentColor_.code());
    } else if (currentColor_.code() >= FOREGROUND_MIN && currentColor_.code() <= FOREGROUND_MAX) {
        int newBg = currentColor_.code() + (BACKGROUND_MIN - FOREGROUND_MIN);
        clazzes_.add(BACKGROUND_STYLE + Integer.toString(newBg - BACKGROUND_MIN));
        return new Color(false, newBg);
    } else {
        int newBg = currentColor_.code() + (BACKGROUND_INTENSE_MIN - FOREGROUND_INTENSE_MIN);
        clazzes_.add(BACKGROUND_STYLE + Integer.toString(newBg + NUM - BACKGROUND_INTENSE_MIN));
        return new Color(false, newBg);
    }
}
```

---

### [33/52] `Return_64`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0658 |
| SARI | 0.2099 |
| GLEU | 0.2000 |
| METEOR | 0.4276 |
| xMatch | ✗ |

**原注释 (source)**
```
@return when the work has ben accepted.
```

**标准注释 (ground truth)**
```
@return When the work has been accepted.
```

**生成注释 (generated)**
```
@return the accepted time.
```

**代码片段**
```java
public synchronized long getAcceptedTime() {
    return acceptedTime;
}
```

---

### [11/52] `Return_20`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2403 |
| SARI | 0.2278 |
| GLEU | 0.5000 |
| METEOR | 0.6250 |
| xMatch | ✗ |

**原注释 (source)**
```
@return javax.swing.JTextField
```

**标准注释 (ground truth)**
```
@return javax.swing.ZapTextArea
```

**生成注释 (generated)**
```
@return ZapTextArea
```

**代码片段**
```java
	private ZapTextArea getTxtEncode() {
		if (txtEncode == null) {
			txtEncode = new ZapTextArea();
			txtEncode.setLineWrap(true);
			txtEncode.setFont(new java.awt.Font("Courier New", java.awt.Font.PLAIN, 12));
			txtEncode.addMouseListener(new java.awt.event.MouseAdapter() {   
				public void mousePressed(java.awt.event.MouseEvent e) {    
	          		if ((e.getModifiers() & InputEvent.BUTTON3_MASK) != 0) {  // right mouse button
	            		view.getPopupMenu().show(e.getComponent(), e.getX(), e.getY());
	            	}
				} 

			
			});

		}
		return txtEncode;
	}

```

---

### [22/52] `Return_42`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2403 |
| SARI | 0.2278 |
| GLEU | 0.5000 |
| METEOR | 0.6250 |
| xMatch | ✗ |

**原注释 (source)**
```
@return javax.swing.JTextField
```

**标准注释 (ground truth)**
```
@return javax.swing.ZapTextArea
```

**生成注释 (generated)**
```
@return ZapTextArea
```

**代码片段**
```java
	private ZapTextArea getTxtDecode() {
		if (txtDecode == null) {
			txtDecode = new ZapTextArea();
			txtDecode.setLineWrap(true);
			txtDecode.setFont(new java.awt.Font("Courier New", java.awt.Font.PLAIN, 12));
		}
		return txtDecode;
	}

```

---

### [50/52] `Return_98`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2403 |
| SARI | 0.2278 |
| GLEU | 0.5000 |
| METEOR | 0.6250 |
| xMatch | ✗ |

**原注释 (source)**
```
@return javax.swing.JMenuItem
```

**标准注释 (ground truth)**
```
@return javax.swing.ZapMenuItem
```

**生成注释 (generated)**
```
@return ZapMenuItem
```

**代码片段**
```java
	private ZapMenuItem getMenuHelpAbout() {
		if (menuHelpAbout == null) {
			menuHelpAbout = new ZapMenuItem("menu.help.about");
			menuHelpAbout.addActionListener(new java.awt.event.ActionListener() { 
				@Override
				public void actionPerformed(java.awt.event.ActionEvent e) {    
					AboutDialog dialog = new AboutDialog(View.getSingleton().getMainFrame(), true);
					dialog.setVisible(true);
				}
			});

		}
		return menuHelpAbout;
	}

```

---

### [16/52] `Return_30`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5382 |
| SARI | 0.2472 |
| GLEU | 0.5714 |
| METEOR | 0.6727 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the value of this attribute if this attribute is present in the map. Otherwise {@link #getDefaultValue()}
```

**标准注释 (ground truth)**
```
@return the value of this attribute if this attribute is present in the extracted map. Otherwise {@link #getDefaultValue()}
```

**生成注释 (generated)**
```
@return the value of this attribute if this attribute is present in the map. Otherwise null
```

**代码片段**
```java
public double get(WithAttributes withAttributes) {
    return withAttributes.getAttributes().get(this);
}
```

---

### [39/52] `Return_76`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0710 |
| SARI | 0.2504 |
| GLEU | 0.1809 |
| METEOR | 0.2724 |
| xMatch | ✗ |

**原注释 (source)**
```
@return A List of Sentence of TaggedWord
```

**标准注释 (ground truth)**
```
@return A List of Sentence of TaggedWord (final generification cannot be listed due to lack of complete generification of super classes)
```

**生成注释 (generated)**
```
@return A List of ArrayList of TaggedWord
```

**代码片段**
```java
  public List<ArrayList<TaggedWord>> process(List<? extends List<? extends HasWord>> sentences) {
    List<ArrayList<TaggedWord>> taggedSentences = new ArrayList<ArrayList<TaggedWord>>();

    TestSentence testSentence = new TestSentence(this);
    for (List<? extends HasWord> sentence : sentences) {
      taggedSentences.add(testSentence.tagSentence(sentence, false));
    }
    return taggedSentences;
  }

```

---

### [47/52] `Return_92`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4102 |
| SARI | 0.4435 |
| GLEU | 0.4259 |
| METEOR | 0.5335 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Object value of the property - or null
```

**标准注释 (ground truth)**
```
@return Object value of the property or null if the property is not set
```

**生成注释 (generated)**
```
@return Object value of the property - or throws IllegalArgumentException
```

**代码片段**
```java
public Object getProperty(String name) {
    if (name == null || !isPropertySupported(name))
        throw new IllegalArgumentException();
    return callProperties.get(name);
}
```

---

### [9/52] `Return_16`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1234 |
| SARI | 0.4438 |
| GLEU | 0.1584 |
| METEOR | 0.2583 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Whether is successful to set the task completed. If the  path not exist will be false; If the length of the file in  path is not equal to  totalBytes will be false; If the task with  url and  path is downloading will be false. Otherwise will be true.
```

**标准注释 (ground truth)**
```
@return Whether is successful to update all tasks' status to the Filedownloader Engine. If one task atom among them is not match the Rules in  com.liulishuo.filedownloader.services.FileDownloadMgr#obtainCompletedTaskModel(String, String, long) will receive false, and non of them would be updated to DB.
```

**生成注释 (generated)**
```
@return Whether is successful to set the task completed. If the taskAtomList is empty will be false; If any task in taskAtomList is downloading will be false; If any task in taskAtomList is not completed will be false. Otherwise will be true.
```

**代码片段**
```java
    public boolean setTaskCompleted(List<FileDownloadTaskAtom> taskAtomList) {
        return FileDownloadServiceProxy.getImpl().setTaskCompleted(taskAtomList);
    }

```

---

### [10/52] `Return_18`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.2021 |
| SARI | 0.4698 |
| GLEU | 0.3333 |
| METEOR | 0.7011 |
| xMatch | ✗ |

**原注释 (source)**
```
@return A SqlParser object.
```

**标准注释 (ground truth)**
```
@return A parser
```

**生成注释 (generated)**
```
@return A SqlParser object.
```

**代码片段**
```java
  public static SqlParser create(String sql, Config config) {
    SqlAbstractParserImpl parser =
        config.parserFactory().getParser(new StringReader(sql));

    return new SqlParser(sql, parser, config);
  }

```

---

### [2/52] `Return_2`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4083 |
| SARI | 0.4736 |
| GLEU | 0.4412 |
| METEOR | 0.6134 |
| xMatch | ✗ |

**原注释 (source)**
```
@return The string representation as a comma-separated list of simple annotation names.
```

**标准注释 (ground truth)**
```
@return The string representation as a comma-separated list.
```

**生成注释 (generated)**
```
@return The string representation.
```

**代码片段**
```java
@Override
public String toString() {
    return annotations.toString();
}
```

---

### [34/52] `Return_66`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8394 |
| SARI | 0.4813 |
| GLEU | 0.8485 |
| METEOR | 0.9437 |
| xMatch | ✗ |

**原注释 (source)**
```
@return The name of the main character of a user. Returns null if not found.
```

**标准注释 (ground truth)**
```
@return The region/realm/name of the main character of a user. Returns null if not found.
```

**生成注释 (generated)**
```
@return The JSONObject of the main character of a user. Returns null if not found.
```

**代码片段**
```java
public JSONObject getMainCharacterForUserInGuild(User user, Guild guild) {
    JSONObject character = null;
    HttpUrl url = new HttpUrl.Builder().scheme(STR).host(getBot().getBotSettings().getProperty(STR)).addPathSegments(STR + user.getId() + STR + guild.getId()).build();
    Request request = new Request.Builder().url(url).build();
    try {
        Response response = client.newCall(request).execute();
        JSONObject jsonObject = new JSONObject(response.body().source());
        character = jsonObject.length() > NUM ? jsonObject : null;
    } catch (IOException e) {
        e.printStackTrace();
    }
    return character;
}
```

---

### [45/52] `Return_88`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.1457 |
| SARI | 0.4833 |
| GLEU | 0.3333 |
| METEOR | 0.6466 |
| xMatch | ✗ |

**原注释 (source)**
```
@return total count
```

**标准注释 (ground truth)**
```
@return int, total count
```

**生成注释 (generated)**
```
@return total count
```

**代码片段**
```java
@Transactional(readOnly = true)
@Override
public int getAllCount(final String currentUser, final Set<String> userRoles, EphesoftUser ephesoftUser) {
    return batchInstanceDao.getAllCount(currentUser, userRoles, ephesoftUser);
}
```

---

### [18/52] `Return_34`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0731 |
| SARI | 0.5053 |
| GLEU | 0.1364 |
| METEOR | 0.3704 |
| xMatch | ✗ |

**原注释 (source)**
```
@return an <code>Iterator</code>
```

**标准注释 (ground truth)**
```
@return an array of groups.
```

**生成注释 (generated)**
```
@return a Group[]
```

**代码片段**
```java
public Group[] getGroups() {
    Item[] items = super.getItems();
    Group[] groups = new Group[items.length];
    for (int i = NUM; i < groups.length; i++) {
        groups[i] = (Group) items[i];
    }
    return groups;
}
```

---

### [21/52] `Return_40`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0399 |
| SARI | 0.5083 |
| GLEU | 0.0789 |
| METEOR | 0.6696 |
| xMatch | ✗ |

**原注释 (source)**
```
@return a <code>File<code> value
```

**标准注释 (ground truth)**
```
@return A string.
```

**生成注释 (generated)**
```
@return a <code>String<code> value
```

**代码片段**
```java
public String getDocumentPath() {
    if (this.path == null) {
        final Document doc = getDocument();
        try {
            this.path = doc != null ? doc.getPath() : getPublication().getDocumentBuilder().getLocator(this.factory, this.webappUrl).getPath();
        } catch (final Exception e) {
            throw new RuntimeException(e);
        }
    }
    return this.path;
}
```

---

### [46/52] `Return_90`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.3393 |
| SARI | 0.5197 |
| GLEU | 0.4211 |
| METEOR | 0.7823 |
| xMatch | ✗ |

**原注释 (source)**
```
@return an option of the first object of the iteration
```

**标准注释 (ground truth)**
```
@return an Optional containing the first object of this Iterable
```

**生成注释 (generated)**
```
@return an option of the first object of the iteration
```

**代码片段**
```java
@Override
public Optional<TYPE> first() {
    Iterator<TYPE> resultIterator = first(NUM).iterator();
    return resultIterator.hasNext() ? Optional.of(resultIterator.next()) : Optional.empty();
}
```

---

### [48/52] `Return_94`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2669 |
| SARI | 0.5365 |
| GLEU | 0.2872 |
| METEOR | 0.6203 |
| xMatch | ✗ |

**原注释 (source)**
```
@return true if we have enough data to decode the PI frame fully, false if more data is required
```

**标准注释 (ground truth)**
```
@return number of extra octets of data required data to decode the PI frame fully
```

**生成注释 (generated)**
```
@return NUM if we have enough data to decode the PI frame fully, NUM - in.remaining() if more data is required
```

**代码片段**
```java
public int decodable(QpidByteBuffer in) {
    return (in.remaining() >= NUM) ? NUM : NUM - in.remaining();
}
```

---

### [25/52] `Return_48`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5115 |
| SARI | 0.5880 |
| GLEU | 0.5909 |
| METEOR | 0.8535 |
| xMatch | ✗ |

**原注释 (source)**
```
@return URL with query params
```

**标准注释 (ground truth)**
```
@return URL with appended query params
```

**生成注释 (generated)**
```
@return URL with query params
```

**代码片段**
```java
@SuppressWarnings(STR)
public static String append(final String url, final Map<String, ?> params) {
    if (params == null || params.isEmpty())
        return url;
    final StringBuilder result = new StringBuilder(url);
    int firstColon = url.indexOf(STR);
    int lastSlash = url.lastIndexOf(STR);
    if (firstColon + NUM == lastSlash)
        result.append(STR);
    result.append(STR);
    Entry<String, ?> entry;
    Object value;
    Iterator<?> iterator = params.entrySet().iterator();
    entry = (Entry<String, ?>) iterator.next();
    result.append(entry.getKey());
    result.append(STR);
    value = entry.getValue();
    if (value != null)
        result.append(value);
    while (iterator.hasNext()) {
        result.append(STR);
        entry = (Entry<String, ?>) iterator.next();
        result.append(entry.getKey());
        result.append(STR);
        value = entry.getValue();
        if (value != null)
            result.append(value);
    }
    return result.toString();
}
```

---

### [24/52] `Return_46`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1027 |
| SARI | 0.5932 |
| GLEU | 0.2568 |
| METEOR | 0.6536 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the parsed Test Suite or null if no Test Suite was found.
```

**标准注释 (ground truth)**
```
@return a linked list with parsed Test Suites. An empty list of no test suites were found.
```

**生成注释 (generated)**
```
@return the parsed Test Suites or empty list if no Test Suites were found.
```

**代码片段**
```java
public List<TestSuite> getSuite() {
    return this.testSuites;
}
```

---

### [5/52] `Return_8`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5133 |
| SARI | 0.6104 |
| GLEU | 0.5667 |
| METEOR | 0.8655 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Host name and port, as a string.
```

**标准注释 (ground truth)**
```
@return The host, as a string.
```

**生成注释 (generated)**
```
@return Host name, as a string.
```

**代码片段**
```java
public static String getHostFromUrl(String url) {
    String authority = getAuthorityFromUrl(url);
    int idx = authority.indexOf(STR);
    if (idx == -NUM)
        return authority;
    return authority.substring(NUM, idx);
}
```

---

### [29/52] `Return_56`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6552 |
| SARI | 0.6121 |
| GLEU | 0.6667 |
| METEOR | 0.8290 |
| xMatch | ✗ |

**原注释 (source)**
```
@return The maximum query evaluation time, in milliseconds.
```

**标准注释 (ground truth)**
```
@return The maximum query evaluation time, measured in seconds.
```

**生成注释 (generated)**
```
@return The maximum query evaluation time, in milliseconds.
```

**代码片段**
```java
public int getMaxQueryTime() {
    return maxQueryTime;
}
```

---

### [8/52] `Return_14`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0241 |
| SARI | 0.6169 |
| GLEU | 0.1881 |
| METEOR | 0.2189 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the {@link Cursor} backing this SquidCursor
```

**标准注释 (ground truth)**
```
@return the {@link ICursor} backing this SquidCursor. If you are on Android and you need to pass this object across process boundaries, and if this SquidCursor was obtained from a SquidDatabase, you can safely cast the object returned by this method to an Android cursor
```

**生成注释 (generated)**
```
@return the {@link ICursor} backing this SquidCursor
```

**代码片段**
```java
public ICursor getCursor() {
    return cursor;
}
```

---

### [32/52] `Return_62`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4765 |
| SARI | 0.6271 |
| GLEU | 0.5185 |
| METEOR | 0.6676 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Get method or null if none found.
```

**标准注释 (ground truth)**
```
@return Get method or null (or throws IllegalArgumentException) if none found.
```

**生成注释 (generated)**
```
@return Get method or null if none found.
```

**代码片段**
```java
public static Method findGetMethod(Field field, boolean throwExceptions) throws IllegalArgumentException {
    Method fieldGetMethod;
    if (Locale.ENGLISH.equals(Locale.getDefault())) {
        fieldGetMethod = findMethodFromNames(field, true, throwExceptions, methodFromField(field, STR, null), methodFromField(field, STR, null));
    } else {
        fieldGetMethod = findMethodFromNames(field, true, throwExceptions, methodFromField(field, STR, null), methodFromField(field, STR, Locale.ENGLISH), methodFromField(field, STR, null), methodFromField(field, STR, Locale.ENGLISH));
    }
    if (fieldGetMethod == null) {
        return null;
    }
    if (fieldGetMethod.getReturnType() != field.getType()) {
        if (throwExceptions) {
            throw new IllegalArgumentException(STR + fieldGetMethod.getName() + STR + field.getType());
        } else {
            return null;
        }
    }
    return fieldGetMethod;
}
```

---

### [43/52] `Return_84`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6389 |
| SARI | 0.6330 |
| GLEU | 0.6471 |
| METEOR | 0.6724 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the extension handler used by this SVGGraphics2D instance
```

**标准注释 (ground truth)**
```
@return the extension handler used by the DOMTreeManager.
```

**生成注释 (generated)**
```
@return the extension handler used by this generatorContext instance
```

**代码片段**
```java
public ExtensionHandler getExtensionHandler() {
    return generatorContext.getExtensionHandler();
}
```

---

### [44/52] `Return_86`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.3624 |
| SARI | 0.6434 |
| GLEU | 0.4259 |
| METEOR | 0.5551 |
| xMatch | ✗ |

**原注释 (source)**
```
@return {@link CacheStatisticsImpl}.
```

**标准注释 (ground truth)**
```
@return {@link CacheStatisticsImpl} or an empty statistics if not enabled.
```

**生成注释 (generated)**
```
@return {@link CacheStatisticsImpl}.
```

**代码片段**
```java
public CacheStatisticsImpl createCacheStatIfAbsent(String name) {
    CacheStatisticsImpl statistics = new CacheStatisticsImpl();
    CacheStatisticsImpl temp = this.statistics.putIfAbsent(name, statistics);
    if (temp != null) {
        statistics = temp;
    }
    return statistics;
}
```

---

### [52/52] `Return_102`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.4085 |
| SARI | 0.6471 |
| GLEU | 0.4655 |
| METEOR | 0.5850 |
| xMatch | ✗ |

**原注释 (source)**
```
@return A read-only view of the additionalHttpHeaders.
```

**标准注释 (ground truth)**
```
@return A read-only view of the additionalHttpHeaders, or null if none are set.
```

**生成注释 (generated)**
```
@return A read-only view of the additionalHttpHeaders.
```

**代码片段**
```java
public Map<String, String> getAdditionalHttpHeaders() {
    return additionalHttpHeaders == null ? null : Collections.unmodifiableMap(additionalHttpHeaders);
}
```

---

### [12/52] `Return_22`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6611 |
| SARI | 0.6642 |
| GLEU | 0.6866 |
| METEOR | 0.9095 |
| xMatch | ✗ |

**原注释 (source)**
```
@return a List of the combined {@link BulletRecord} so far. The List has a size that is at most the maximum specified by the {@link Aggregation}.
```

**标准注释 (ground truth)**
```
@return a {@link Clip} of the combined records so far. The records have a size that is at most the maximum specified by the {@link Aggregation}.
```

**生成注释 (generated)**
```
@return a Clip of the combined {@link BulletRecord} so far. The Clip has a size that is at most the maximum specified by the {@link Aggregation}.
```

**代码片段**
```java
@Override
public Clip getAggregation() {
    return Clip.of(aggregate);
}
```

---

### [14/52] `Return_26`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5946 |
| SARI | 0.6667 |
| GLEU | 0.6538 |
| METEOR | 0.8648 |
| xMatch | ✗ |

**原注释 (source)**
```
@return ProjectRel corresponding to the right child
```

**标准注释 (ground truth)**
```
@return LogicalProject corresponding to the right child
```

**生成注释 (generated)**
```
@return Project corresponding to the right child
```

**代码片段**
```java
  protected Project getRightChild(RelOptRuleCall call) {
    return call.rel(2);
  }

```

---

### [28/52] `Return_54`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.6514 |
| SARI | 0.6667 |
| GLEU | 0.6471 |
| METEOR | 0.7206 |
| xMatch | ✗ |

**原注释 (source)**
```
@return true if habit has reminder
```

**标准注释 (ground truth)**
```
@return true if habit has reminder, false otherwise
```

**生成注释 (generated)**
```
@return true if habit has reminder
```

**代码片段**
```java
public boolean hasReminder() {
    return reminder != null;
}
```

---

### [31/52] `Return_60`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1645 |
| SARI | 0.6667 |
| GLEU | 0.1852 |
| METEOR | 0.6615 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the extended FluentPipeline
```

**标准注释 (ground truth)**
```
@return the extended Pipeline
```

**生成注释 (generated)**
```
@return the extended GremlinPipeline<S, Map<String, Object>>
```

**代码片段**
```java
public GremlinPipeline<S, Map<String, Object>> map() {
    return this.add(new PropertyMapPipe());
}
```

---

### [38/52] `Return_74`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5344 |
| SARI | 0.7019 |
| GLEU | 0.5652 |
| METEOR | 0.9792 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the ObjectName for the given exchange on the test VirtualHost.
```

**标准注释 (ground truth)**
```
@return the ObjectName for the given Exchange on the VirtualHost
```

**生成注释 (generated)**
```
@return the ObjectName for the given exchange on the test VirtualHost.
```

**代码片段**
```java
@SuppressWarnings(STR)
public ObjectName getExchangeObjectName(String virtualHostName, String exchange) {
    AllObjects allObject = new AllObjects(_mbsc);
    allObject.querystring = STR + virtualHostName + STR + exchange + STR;
    Set<ObjectName> objectNames = allObject.returnObjects();
    _test.assertNotNull(STR, objectNames);
    _test.assertEquals(STR + exchange + STR, NUM, objectNames.size());
    ObjectName objectName = objectNames.iterator().next();
    _test.getLogger().info(STR + objectName);
    return objectName;
}
```

---

### [17/52] `Return_32`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2849 |
| SARI | 0.7243 |
| GLEU | 0.3679 |
| METEOR | 0.4428 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the ID of the last baseline build.
```

**标准注释 (ground truth)**
```
@return the ID of the last baseline build before the given date or <code>null</code> if none was run before it...
```

**生成注释 (generated)**
```
@return the ID of the last baseline build before the specified date.
```

**代码片段**
```java
public static String getLastBaselineBuild(String date) {
    if (BUILDS == null) {
        queryAllVariations(STR);
    }
    if (date == null)
        return LAST_BASELINE_BUILD;
    String lastBaselineBuild = null;
    for (int i = NUM; i < BUILDS_LENGTH; i++) {
        String build = BUILDS[i];
        if (build.startsWith(AbstractResults.VERSION_REF)) {
            String buildDate = build.substring(build.indexOf(STR) + NUM);
            if (buildDate.compareTo(date) < NUM) {
                if (lastBaselineBuild == null || build.compareTo(lastBaselineBuild) > NUM) {
                    lastBaselineBuild = build;
                }
            }
        }
    }
    return lastBaselineBuild;
}
```

---

### [7/52] `Return_12`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.9254 |
| SARI | 0.7300 |
| GLEU | 0.9259 |
| METEOR | 0.9927 |
| xMatch | ✗ |

**原注释 (source)**
```
@return <code>true</code> if the button is visible and Popup Menu is assigned.
```

**标准注释 (ground truth)**
```
@return <code>true</code> if the button is visible
```

**生成注释 (generated)**
```
@return <code>true</code> if the button is visible.
```

**代码片段**
```java
public boolean isButtonOverflowVisible() {
    return mIsButtonOverflowVisible;
}
```

---

### [35/52] `Return_68`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2403 |
| SARI | 0.7500 |
| GLEU | 0.5000 |
| METEOR | 0.6250 |
| xMatch | ✗ |

**原注释 (source)**
```
@return ping host
```

**标准注释 (ground truth)**
```
@return Builder
```

**生成注释 (generated)**
```
@return this
```

**代码片段**
```java
public Builder host(String host) {
    this.host = host;
    return this;
}
```

---

### [26/52] `Return_50`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4193 |
| SARI | 0.7603 |
| GLEU | 0.4429 |
| METEOR | 0.4848 |
| xMatch | ✗ |

**原注释 (source)**
```
@return The {@link CmdLineOptionInstance}s which failed validation.
```

**标准注释 (ground truth)**
```
@return The {@link CmdLineOptionValidator.Result}s generated when running {@link CmdLineOptionValidator}s.
```

**生成注释 (generated)**
```
@return The {@link CmdLineOptionValidator.Result}s which failed validation.
```

**代码片段**
```java
public static List<CmdLineOptionValidator.Result> validate(CmdLineArgs cmdLineArgs) {
    Validate.notNull(cmdLineArgs);
    List<CmdLineOptionValidator.Result> results = Lists.newArrayList();
    for (CmdLineOptionInstance optionInst : cmdLineArgs.getSpecifiedOptions()) {
        results.addAll(CmdLineUtils.validate(optionInst));
    }
    return results;
}
```

---

### [1/52] `Return_0`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7487 |
| SARI | 0.7976 |
| GLEU | 0.7593 |
| METEOR | 0.9203 |
| xMatch | ✗ |

**原注释 (source)**
```
@return an open input stream, or null if no suitable output was produced
```

**标准注释 (ground truth)**
```
@return the output file, or null if no suitable output was produced
```

**生成注释 (generated)**
```
@return a generated output file, or null if no suitable output was produced
```

**代码片段**
```java
public final File getGeneratedOutput() throws CurnException {
    return hasGeneratedOutput() ? outputFile : null;
}
```

---

### [3/52] `Return_4`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6059 |
| SARI | 0.8275 |
| GLEU | 0.6129 |
| METEOR | 0.6315 |
| xMatch | ✗ |

**原注释 (source)**
```
@return an instance of the specified class
```

**标准注释 (ground truth)**
```
@return an instance of the specified class or null if the class cannot be instantiated
```

**生成注释 (generated)**
```
@return an instance of the specified class or null if creation fails
```

**代码片段**
```java
    public AsyncSupport newCometSupport(final Class<? extends AsyncSupport> targetClass) {
        try {
            return (AsyncSupport) targetClass.getDeclaredConstructor(new Class[]{AtmosphereConfig.class})
                    .newInstance(config);
        } catch (final Exception e) {
            logger.warn("Failed to create AsyncSupport class: {}, error: {}", targetClass, e);
            return null; // All callers are expected to handle null return value
        }
    }

```

---

### [49/52] `Return_96`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6703 |
| SARI | 0.8646 |
| GLEU | 0.6957 |
| METEOR | 0.9894 |
| xMatch | ✗ |

**原注释 (source)**
```
@return This same sentence, but with the default properties swapped out.
```

**标准注释 (ground truth)**
```
@return A new sentence with the default properties swapped out.
```

**生成注释 (generated)**
```
@return A new Sentence instance with the default properties swapped out.
```

**代码片段**
```java
  public Sentence cased() {
    return new Sentence(this.docFn, impl.build(), Document.EMPTY_PROPS);
  }

```

---

### [4/52] `Return_6`

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
@return {@code TokenStream} to tokenize the text
```

**标准注释 (ground truth)**
```
@return {@code TwitterTokenStream} to tokenize the text
```

**生成注释 (generated)**
```
@return {@code TwitterTokenStream} to tokenize the text
```

**代码片段**
```java
public TwitterTokenStream getDefaultTokenStream() {
    return tokenizationStream;
}
```

---

### [6/52] `Return_10`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9960 |
| xMatch | ✓ |

**原注释 (source)**
```
@return the ApplicationConfig object
```

**标准注释 (ground truth)**
```
@return the ModuleConfig object
```

**生成注释 (generated)**
```
@return the ModuleConfig object
```

**代码片段**
```java
public static ModuleConfig getModuleConfig(HttpServletRequest request, ServletContext context) {
    ModuleConfig moduleConfig = (ModuleConfig) request.getAttribute(Globals.MODULE_KEY);
    if (moduleConfig == null) {
        moduleConfig = (ModuleConfig) context.getAttribute(Globals.MODULE_KEY);
    }
    return moduleConfig;
}
```

---

### [15/52] `Return_28`

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
@return a Line
```

**标准注释 (ground truth)**
```
@return an AudioInputStream
```

**生成注释 (generated)**
```
@return an AudioInputStream
```

**代码片段**
```java
public final AudioInputStream getSoundChallenge() {
    return this.challenge;
}
```

---

### [19/52] `Return_36`

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
@return a list of jobs which had never been started if timeout was reached, or null if that did not happen.
```

**标准注释 (ground truth)**
```
@return a list of jobs which had never been started if timeout was reached, or an empty list if that did not happen.
```

**生成注释 (generated)**
```
@return a list of jobs which had never been started if timeout was reached, or an empty list if that did not happen.
```

**代码片段**
```java
  public List<I> joinWithTimeout() {
    if (timeout < 0) {
      join();
      return new ArrayList<>();
    }
    // Make blocking calls to the last processes that are running
    if ( ! threadPool.isShutdown()) {
      try {
        List<I> leftover = null;
        int i;
        for (i = nThreads; i > 0; --i) {
          if (idleProcessors.poll(timeout, TimeUnit.MILLISECONDS) == null) {
            leftover = shutdownNow();
            break;
          }
        }
        // if the poll hit a timeout, retake the remaining processors
        // so join() can guarantee the threads are finished
        if (i > 0) {
          for ( ; i > leftover.size(); --i) {
            idleProcessors.take();
          }
          return leftover;
        } else {
          threadPool.shutdown();
          // Sanity check. The threadpool should be done after iterating over
          // the processors.
          threadPool.awaitTermination(10, TimeUnit.SECONDS);
        }
      } catch (InterruptedException e) {
// ... (truncated)
```

---

### [20/52] `Return_38`

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
@return An Enumeration of all child nodes of this node.
```

**标准注释 (ground truth)**
```
@return An Iterator of all child nodes of this node.
```

**生成注释 (generated)**
```
@return An Iterator of all child nodes of this node.
```

**代码片段**
```java
protected final Iterator<SyntaxTreeNode> elements() {
    return _contents.iterator();
}
```

---

### [23/52] `Return_44`

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
@return A {@link Hashtable} representation of a {@link WorkflowInstancePage}.
```

**标准注释 (ground truth)**
```
@return A {@link HashMap} representation of a {@link WorkflowInstancePage}.
```

**生成注释 (generated)**
```
@return A {@link HashMap} representation of a {@link WorkflowInstancePage}.
```

**代码片段**
```java
public static HashMap getXmlRpcWorkflowInstancePage(WorkflowInstancePage page) {
    HashMap pageHash = new HashMap();
    pageHash.put(STR, String.valueOf(page.getTotalPages()));
    pageHash.put(STR, String.valueOf(page.getPageNum()));
    pageHash.put(STR, String.valueOf(page.getPageSize()));
    pageHash.put(STR, getXmlRpcWorkflowInstances(page.getPageWorkflows()));
    return pageHash;
}
```

---

### [27/52] `Return_52`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5623 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9815 |
| xMatch | ✓ |

**原注释 (source)**
```
@return ModuleClassLoader
```

**标准注释 (ground truth)**
```
@return ModuleJarClassLoader
```

**生成注释 (generated)**
```
@return ModuleJarClassLoader
```

**代码片段**
```java
public ModuleJarClassLoader getLoader() {
    return loader;
}
```

---

### [36/52] `Return_70`

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
@return a StyleSheetProcessingInstruction if target is "xml-stylesheet" or a GenericProcessingInstruction otherwise.
```

**标准注释 (ground truth)**
```
@return a SVGStyleSheetProcessingInstruction if target is "xml-stylesheet" or a GenericProcessingInstruction otherwise.
```

**生成注释 (generated)**
```
@return a SVGStyleSheetProcessingInstruction if target is "xml-stylesheet" or a GenericProcessingInstruction otherwise.
```

**代码片段**
```java
public ProcessingInstruction createProcessingInstruction(String target, String data) throws DOMException {
    if (STR.equals(target)) {
        return new SVGStyleSheetProcessingInstruction(data, this, (StyleSheetFactory) getImplementation());
    }
    return new GenericProcessingInstruction(target, data, this);
}
```

---

### [37/52] `Return_72`

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
@return the id_category
```

**标准注释 (ground truth)**
```
@return the id
```

**生成注释 (generated)**
```
@return the id
```

**代码片段**
```java
public long getId() {
    return id;
}
```

---

### [40/52] `Return_78`

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
@return the char[]
```

**标准注释 (ground truth)**
```
@return the union of the char[]s
```

**生成注释 (generated)**
```
@return the union of the char[]s
```

**代码片段**
```java
public static char[] union(char[]... list) {
    StringBuilder sb = new StringBuilder();
    for (char[] characters : list) {
        for (int i = NUM; i < list.length; i++) {
            if (!contains(sb, characters[i]))
                sb.append(list[i]);
        }
    }
    char[] toReturn = new char[sb.length()];
    sb.getChars(NUM, sb.length(), toReturn, NUM);
    Arrays.sort(toReturn);
    return toReturn;
}
```

---

### [41/52] `Return_80`

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
@return a new feature service with the default server URL
```

**标准注释 (ground truth)**
```
@return a new feature service with the default endpoint URL
```

**生成注释 (generated)**
```
@return a new feature service with the default endpoint URL
```

**代码片段**
```java
public FeatureService createFeatureService() {
    return createFeatureService(defaultEndpointUrl);
}
```

---

### [42/52] `Return_82`

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
@return the HornetQConnectionFactory
```

**标准注释 (ground truth)**
```
@return the ActiveMQConnectionFactory
```

**生成注释 (generated)**
```
@return the ActiveMQConnectionFactory
```

**代码片段**
```java
public static ActiveMQConnectionFactory createConnectionFactoryWithoutHA(JMSFactoryType jmsFactoryType, final TransportConfiguration... transportConfigurations) {
    ActiveMQConnectionFactory factory = null;
    if (jmsFactoryType.equals(JMSFactoryType.CF)) {
        factory = new ActiveMQJMSConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.QUEUE_CF)) {
        factory = new ActiveMQQueueConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.TOPIC_CF)) {
        factory = new ActiveMQTopicConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.XA_CF)) {
        factory = new ActiveMQXAConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.QUEUE_XA_CF)) {
        factory = new ActiveMQXAQueueConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.TOPIC_XA_CF)) {
        factory = new ActiveMQXATopicConnectionFactory(false, transportConfigurations);
    }
    return factory;
}
```

---

### [51/52] `Return_100`

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
@return the associated {@link HttpServletRequest}
```

**标准注释 (ground truth)**
```
@return the associated {@link AtmosphereRequest}
```

**生成注释 (generated)**
```
@return the associated {@link AtmosphereRequest}
```

**代码片段**
```java
public AtmosphereRequest getRequest() {
    return atmosphereRequest;
}
```

---

