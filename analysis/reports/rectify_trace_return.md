# Rectifier 逐样本追踪报告

## 汇总指标

- **xMatch (%)**: 24.51
- **BLEU-4**: 0.5421
- **GLEU**: 0.5978
- **Meteor**: 0.7512
- **SARI**: 0.6659
- **Samples_Evaluated**: 102

## 汇总一览（按 SARI 升序，最差排前）

| # | ID | 检测到 | xMatch | BLEU-4 | SARI | METEOR | 原注释(前60) | 生成(前60) |
|---|---|---|---|---|---|---|---|---|
| 1 | `Return_178` | ✓ |  | 0.006 | 0.066 | 0.081 | @return {@link IServer} state | @return int state constants |
| 2 | `Return_158` | ✓ |  | 0.035 | 0.113 | 0.204 | @return the version | @return a function that processes version information |
| 3 | `Return_58` | ✓ |  | 0.292 | 0.145 | 0.638 | @return true if the example is compatible with the mode of t | @return true if the example is compatible with the given mod |
| 4 | `Return_188` | ✓ |  | 0.105 | 0.160 | 0.712 | @return Iterator of all derived types | @return List of all derived types |
| 5 | `Return_20` | ✓ |  | 0.240 | 0.228 | 0.625 | @return javax.swing.JTextField | @return ZapTextArea |
| 6 | `Return_42` | ✓ |  | 0.240 | 0.228 | 0.625 | @return javax.swing.JTextField | @return ZapTextArea |
| 7 | `Return_98` | ✓ |  | 0.240 | 0.228 | 0.625 | @return javax.swing.JMenuItem | @return ZapMenuItem |
| 8 | `Return_30` | ✓ |  | 0.538 | 0.247 | 0.673 | @return the value of this attribute if this attribute is pre | @return the value of this attribute if this attribute is pre |
| 9 | `Return_148` | ✓ |  | 0.538 | 0.247 | 0.673 | @return the value of this attribute if this attribute is pre | @return the value of this attribute if this attribute is pre |
| 10 | `Return_76` | ✓ |  | 0.071 | 0.250 | 0.272 | @return A List of Sentence of TaggedWord | @return A List of ArrayList of TaggedWord |
| 11 | `Return_124` | ✓ |  | 0.077 | 0.258 | 0.419 | @return menu placed under specified control | @return controlMenu placed under specified control |
| 12 | `Return_194` | ✓ |  | 0.348 | 0.295 | 0.493 | @return true: can launch bundle, false: otherwise | @return true: can launch bundle, true: otherwise |
| 13 | `Return_168` | ✓ |  | 0.530 | 0.332 | 0.733 | @return the converted value, or null if the conversion could | @return the converted value, or null if the data is null and |
| 14 | `Return_186` | ✓ |  | 0.066 | 0.354 | 0.303 | @return <false> if the first result is an update count, <tru | @return <false> if the result queue is empty, <true> if it's |
| 15 | `Return_2` | ✓ |  | 0.418 | 0.381 | 0.516 | @return The string representation as a comma-separated list  | @return The string representation of the annotations. |
| 16 | `Return_144` | ✗(漏检) |  | 0.038 | 0.392 | 0.266 | @return boolean Returns a boolean to indicate whether the op | @return boolean Returns a boolean to indicate whether the op |
| 17 | `Return_108` | ✓ |  | 0.070 | 0.394 | 0.268 | @return Value between 1 and 16,777,215 | @return Value between 1 and 16,777,215 |
| 18 | `Return_16` | ✓ |  | 0.115 | 0.436 | 0.224 | @return Whether is successful to set the task completed. If  | @return Whether is successful to set the task completed. If  |
| 19 | `Return_190` | ✓ |  | 0.072 | 0.451 | 0.344 | @return the value for the init parameter if defined | @return the value for the init parameter if defined, or null |
| 20 | `Return_202` | ✓ |  | 0.486 | 0.460 | 0.756 | @return  true if regex string is found a given number of tim | @return true if text is found at least the given number of t |
| 21 | `Return_134` | ✓ |  | 0.197 | 0.467 | 0.383 | @return A list of all of the names that have already been us | @return A set of all of the names that have already been use |
| 22 | `Return_18` | ✗(漏检) |  | 0.202 | 0.470 | 0.701 | @return A SqlParser object. | @return A SqlParser object. |
| 23 | `Return_126` | ✓ |  | 0.020 | 0.471 | 0.319 | @return uri with properties on | @return uri with properties on string |
| 24 | `Return_66` | ✓ |  | 0.839 | 0.481 | 0.944 | @return The name of the main character of a user. Returns nu | @return The JSONObject of the main character of a user. Retu |
| 25 | `Return_88` | ✗(漏检) |  | 0.146 | 0.483 | 0.647 | @return total count | @return total count |
| 26 | `Return_192` | ✗(漏检) |  | 0.110 | 0.496 | 0.580 | @return current Estimated rotation we are at | @return current Estimated rotation we are at |
| 27 | `Return_34` | ✓ |  | 0.073 | 0.505 | 0.370 | @return an <code>Iterator</code> | @return a Group[] |
| 28 | `Return_184` | ✓ |  | 0.239 | 0.508 | 0.653 | @return the list of init params defined in web.xml or applic | @return the value of the init param defined in web.xml or ap |
| 29 | `Return_40` | ✓ |  | 0.040 | 0.508 | 0.670 | @return a <code>File<code> value | @return a <code>String<code> value |
| 30 | `Return_90` | ✗(漏检) |  | 0.339 | 0.520 | 0.782 | @return an option of the first object of the iteration | @return an option of the first object of the iteration |
| 31 | `Return_122` | ✗(漏检) |  | 0.275 | 0.525 | 0.841 | @return a grapql language ast  Value | @return a grapql language ast  Value |
| 32 | `Return_130` | ✓ |  | 0.145 | 0.527 | 0.377 | @return the aggregationCount | @return the aggregationCount.longValue() |
| 33 | `Return_94` | ✓ |  | 0.267 | 0.537 | 0.620 | @return true if we have enough data to decode the PI frame f | @return NUM if we have enough data to decode the PI frame fu |
| 34 | `Return_46` | ✓ |  | 0.092 | 0.561 | 0.558 | @return the parsed Test Suite or null if no Test Suite was f | @return the parsed Test Suites or null if no Test Suites wer |
| 35 | `Return_92` | ✓ |  | 0.382 | 0.582 | 0.709 | @return Object value of the property - or null | @return Object value of the property - or IllegalArgumentExc |
| 36 | `Return_136` | ✓ |  | 0.564 | 0.584 | 0.784 | @return true if this authentication realm "understands" how  | @return true if this authentication realm "understands" how  |
| 37 | `Return_156` | ✓ |  | 0.120 | 0.604 | 0.800 | @return contactId, if not found INVALID_ID is returned | @return List of contactIds, if not found empty list is retur |
| 38 | `Return_104` | ✗(漏检) |  | 0.707 | 0.609 | 0.865 | @return the {@link AsyncAppenderBase} | @return the {@link AsyncAppenderBase} |
| 39 | `Return_8` | ✓ |  | 0.513 | 0.610 | 0.865 | @return Host name and port, as a string. | @return Host name, as a string. |
| 40 | `Return_56` | ✓ |  | 0.655 | 0.612 | 0.829 | @return The maximum query evaluation time, in milliseconds. | @return The maximum query evaluation time, in milliseconds. |
| 41 | `Return_14` | ✓ |  | 0.024 | 0.617 | 0.219 | @return the {@link Cursor} backing this SquidCursor | @return the {@link ICursor} backing this SquidCursor |
| 42 | `Return_166` | ✓ |  | 0.334 | 0.626 | 0.738 | @return the converted value, or null if the conversion could | @return the converted value, or null if the data is null and |
| 43 | `Return_62` | ✓ |  | 0.477 | 0.627 | 0.668 | @return Get method or null if none found. | @return Get method or null if none found. |
| 44 | `Return_84` | ✓ |  | 0.639 | 0.633 | 0.672 | @return the extension handler used by this SVGGraphics2D ins | @return the extension handler used by this generatorContext  |
| 45 | `Return_152` | ✓ |  | 0.726 | 0.638 | 0.777 | @return returns all axis mapped to an ImmutableMap | @return returns all axis mapped to an unmodifiableMap |
| 46 | `Return_86` | ✗(漏检) |  | 0.362 | 0.643 | 0.555 | @return {@link CacheStatisticsImpl}. | @return {@link CacheStatisticsImpl}. |
| 47 | `Return_102` | ✗(漏检) |  | 0.408 | 0.647 | 0.585 | @return A read-only view of the additionalHttpHeaders. | @return A read-only view of the additionalHttpHeaders. |
| 48 | `Return_146` | ✗(漏检) |  | 0.580 | 0.652 | 0.657 | @return The index of the specified element in the model's it | @return The index of the specified element in the model's it |
| 49 | `Return_114` | ✓ |  | 0.500 | 0.653 | 0.893 | @return the list of initial <code>ServiceReference</code> ob | @return the list of initial <code>ServiceReference</code> ob |
| 50 | `Return_140` | ✗(漏检) |  | 0.862 | 0.658 | 0.877 | @return Opaque string handle for this terminal instance, or  | @return Opaque string handle for this terminal instance, or  |
| 51 | `Return_128` | ✓ |  | 0.817 | 0.660 | 0.891 | @return Map {@link IBuildConfiguration} -> {@link Incrementa | @return Map {@link IBuildConfiguration} -> {@link Incrementa |
| 52 | `Return_22` | ✓ |  | 0.661 | 0.664 | 0.910 | @return a List of the combined {@link BulletRecord} so far.  | @return a Clip of the combined {@link BulletRecord} so far.  |
| 53 | `Return_26` | ✓ |  | 0.595 | 0.667 | 0.865 | @return ProjectRel corresponding to the right child | @return Project corresponding to the right child |
| 54 | `Return_54` | ✗(漏检) |  | 0.651 | 0.667 | 0.721 | @return true if habit has reminder | @return true if habit has reminder |
| 55 | `Return_60` | ✓ |  | 0.165 | 0.667 | 0.661 | @return the extended FluentPipeline | @return the extended GremlinPipeline<S, Map<String, Object>> |
| 56 | `Return_142` | ✓ |  | 0.861 | 0.667 | 0.954 | @return the annotation type string, or null if the supplied  | @return the annotation type, or null if the supplied destina |
| 57 | `Return_150` | ✗(漏检) |  | 0.535 | 0.667 | 0.623 | @return Window to show in the portlet | @return Window to show in the portlet |
| 58 | `Return_160` | ✓ |  | 0.574 | 0.667 | 0.660 | @return  true if we are currently paused. The caller might b | @return true if we are currently paused. The caller might be |
| 59 | `Return_162` | ✓ |  | 0.254 | 0.667 | 0.949 | @return the invoking thread's contention manager | @return the static contention manager |
| 60 | `Return_110` | ✓ |  | 0.077 | 0.678 | 0.594 | @return 42. | @return the calculated hash value. |
| 61 | `Return_64` | ✓ |  | 0.519 | 0.698 | 0.973 | @return when the work has ben accepted. | @return the time when the work has been accepted. |
| 62 | `Return_24` | ✓ |  | 0.742 | 0.700 | 0.986 | @return new background color based on the supplied foregroun | @return new background color based on the supplied foregroun |
| 63 | `Return_74` | ✗(漏检) |  | 0.534 | 0.702 | 0.979 | @return the ObjectName for the given exchange on the test Vi | @return the ObjectName for the given exchange on the test Vi |
| 64 | `Return_32` | ✓ |  | 0.285 | 0.724 | 0.443 | @return the ID of the last baseline build. | @return the ID of the last baseline build before the specifi |
| 65 | `Return_12` | ✓ |  | 0.925 | 0.730 | 0.993 | @return <code>true</code> if the button is visible and Popup | @return <code>true</code> if the button is visible. |
| 66 | `Return_68` | ✓ |  | 0.240 | 0.750 | 0.625 | @return ping host | @return this |
| 67 | `Return_106` | ✓ |  | 0.411 | 0.754 | 0.651 | @return the wireType | @return the queue wireType() |
| 68 | `Return_50` | ✓ |  | 0.419 | 0.760 | 0.485 | @return The {@link CmdLineOptionInstance}s which failed vali | @return The {@link CmdLineOptionValidator.Result}s which fai |
| 69 | `Return_132` | ✓ |  | 0.745 | 0.783 | 1.000 | @return Whether the segments matches (in sense of "be mergab | @return Whether the Ways matches (in sense of "be mergable") |
| 70 | `Return_0` | ✓ |  | 0.749 | 0.798 | 0.920 | @return an open input stream, or null if no suitable output  | @return a generated output file, or null if no suitable outp |
| 71 | `Return_170` | ✓ |  | 0.530 | 0.801 | 0.942 | @return A {@link RepositoryMethodMetadataInitializer} corres | @return A {@link RepositoryMethodMetadata} corresponding to  |
| 72 | `Return_174` | ✓ |  | 0.742 | 0.812 | 0.905 | @return The mouse cursor y position | @return The mouse cursor y position or -NUM if unknown |
| 73 | `Return_4` | ✓ |  | 0.606 | 0.828 | 0.632 | @return an instance of the specified class | @return an instance of the specified class or null if creati |
| 74 | `Return_96` | ✓ |  | 0.670 | 0.865 | 0.989 | @return This same sentence, but with the default properties  | @return A new Sentence instance with the default properties  |
| 75 | `Return_120` | ✓ | ✓ | 1.000 | 0.917 | 1.000 | @return an aggregated Account instance representing account  | @return an aggregated AuthenticationInfo instance representi |
| 76 | `Return_164` | ✓ |  | 0.663 | 0.946 | 0.949 | @return One of the following application running states: {@l | @return One of the following application running states: {@l |
| 77 | `Return_138` | ✓ |  | 0.581 | 0.962 | 0.988 | @return The naemspace URI mapped to the prefix. | @return The namespace URI mapped to the prefix. |
| 78 | `Return_6` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return {@code TokenStream} to tokenize the text | @return {@code TwitterTokenStream} to tokenize the text |
| 79 | `Return_10` | ✓ | ✓ | 1.000 | 1.000 | 0.996 | @return the ApplicationConfig object | @return the ModuleConfig object |
| 80 | `Return_28` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | @return a Line | @return an AudioInputStream |
| 81 | `Return_36` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return a list of jobs which had never been started if timeo | @return a list of jobs which had never been started if timeo |
| 82 | `Return_38` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return An Enumeration of all child nodes of this node. | @return An Iterator of all child nodes of this node. |
| 83 | `Return_44` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return A {@link Hashtable} representation of a {@link Workf | @return A {@link HashMap} representation of a {@link Workflo |
| 84 | `Return_48` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @return URL with query params | @return URL with appended query params |
| 85 | `Return_52` | ✓ | ✓ | 0.562 | 1.000 | 0.981 | @return ModuleClassLoader | @return ModuleJarClassLoader |
| 86 | `Return_70` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return a StyleSheetProcessingInstruction if target is "xml- | @return a SVGStyleSheetProcessingInstruction if target is "x |
| 87 | `Return_72` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | @return the id_category | @return the id |
| 88 | `Return_78` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return the char[] | @return the union of the char[]s |
| 89 | `Return_80` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return a new feature service with the default server URL | @return a new feature service with the default endpoint URL |
| 90 | `Return_82` | ✓ | ✓ | 1.000 | 1.000 | 0.992 | @return the HornetQConnectionFactory | @return the ActiveMQConnectionFactory |
| 91 | `Return_100` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @return the associated {@link HttpServletRequest} | @return the associated {@link AtmosphereRequest} |
| 92 | `Return_112` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return the ScopeContext for the MODULE scope that will be a | @return the ScopeContainer for the MODULE scope that will be |
| 93 | `Return_116` | ✓ |  | 0.815 | 1.000 | 1.000 | @return StringBuffer filled with the penn treebank forms of  | @return String filled with the penn treebank forms of all tr |
| 94 | `Return_118` | ✓ | ✓ | 1.000 | 1.000 | 0.996 | @return the new PartitionMetaData | @return the new PartitionTemplate |
| 95 | `Return_154` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return WSDL <code>Document</code> | @return WSDL <code>Definition</code> |
| 96 | `Return_172` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return A {@link Hashtable} representation of a {@link Workf | @return A {@link HashMap} representation of a {@link Workflo |
| 97 | `Return_176` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @return the list of Cassandra instances | @return the set of Cassandra instances |
| 98 | `Return_180` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @return string array of misspelt words | @return string array of misspelled words |
| 99 | `Return_182` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return a {@link UserSpinnerAdapter} or null if there is onl | @return a {@link UserAdapter} or null if there is only one p |
| 100 | `Return_196` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return the GraphItem located at the given point, if any | @return the VisualItem located at the given point, if any |
| 101 | `Return_198` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @return a new variation service with the default server URL | @return a new variation service with the default endpoint UR |
| 102 | `Return_200` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @return A {@link Ravioli} | @return A {@link Lob} |

---

## 逐样本详情

### [90/102] `Return_178`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0063 |
| SARI | 0.0663 |
| GLEU | 0.0541 |
| METEOR | 0.0811 |
| xMatch | ✗ |

**原注释 (source)**
```
@return {@link IServer} state
```

**标准注释 (ground truth)**
```
@return {@link IServer} state of the application based on the application running state in the Cloud
```

**生成注释 (generated)**
```
@return int state constants
```

**当前代码 (new_code)**
```java
public synchronized int getState() {
    if (this.application != null && this.application.getState() == AppState.STOPPED) {
        return IServer.STATE_STOPPED;
    }
    InstanceState instanceState = getRunState();
    if (instanceState != null) {
        switch(instanceState) {
            case RUNNING:
                return IServer.STATE_STARTED;
            case STARTING:
                return IServer.STATE_STARTING;
            case DOWN:
                return IServer.STATE_STOPPED;
        }
    }
    return IServer.STATE_UNKNOWN;
}
```

**变更前代码 (old_code)**
```java
public synchronized int getState() {
    if (application != null) {
        AppState state = application.getState();
        switch(state) {
            case STARTED:
                return IServer.STATE_STARTED;
            case UPDATING:
                return IServer.STATE_STARTING;
            case STOPPED:
                return IServer.STATE_STOPPED;
        }
    }
    return IServer.STATE_UNKNOWN;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,12 +1,15 @@
 public synchronized int getState() {

-    if (application != null) {

-        AppState state = application.getState();

-        switch(state) {

-            case STARTED:

+    if (this.application != null && this.application.getState() == AppState.STOPPED) {

+        return IServer.STATE_STOPPED;

+    }

+    InstanceState instanceState = getRunState();

+    if (instanceState != null) {

+        switch(instanceState) {

+            case RUNNING:

                 return IServer.STATE_STARTED;

-            case UPDATING:

+            case STARTING:

                 return IServer.STATE_STARTING;

-            case STOPPED:

+            case DOWN:

                 return IServer.STATE_STOPPED;

         }

     }

```

---

### [80/102] `Return_158`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0348 |
| SARI | 0.1131 |
| GLEU | 0.0870 |
| METEOR | 0.2044 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the version
```

**标准注释 (ground truth)**
```
@return the version or null if the version cannot be determined
```

**生成注释 (generated)**
```
@return a function that processes version information
```

**当前代码 (new_code)**
```java
public static Function<String, String> osVersion() {
    return new Function<String, String>() {

        @Override
        public String apply(final String description) {
            OsFamily family = osFamily().apply(description);
            if (Objects.equal(family, OsFamily.CENTOS))
                return parseVersion(description, CENTOS);
            else if (Objects.equal(family, OsFamily.DEBIAN))
                return parseVersion(description, DEBIAN);
            else if (Objects.equal(family, OsFamily.FEDORA))
                return parseVersion(description, FEDORA);
            else if (Objects.equal(family, OsFamily.RHEL))
                return parseVersion(description, RHEL);
            else if (Objects.equal(family, OsFamily.UBUNTU))
                return parseVersion(description, UBUNTU);
            else if (Objects.equal(family, OsFamily.WINDOWS))
                return parseVersion(description, WINDOWS);
            else if (Objects.equal(family, OsFamily.CLOUD_LINUX))
                return parseVersion(description, CLOUD_LINUX);
            return null;
        }
    };
}
```

**变更前代码 (old_code)**
```java
public static Function<ProductItem, String> osVersion() {
    return new Function<ProductItem, String>() {

        @Override
        public String apply(ProductItem productItem) {
            checkNotNull(productItem, STR);
            final String description = productItem.getDescription();
            OsFamily family = osFamily().apply(productItem);
            if (family.equals(OsFamily.CENTOS))
                return parseVersion(description, CENTOS);
            else if (family.equals(OsFamily.DEBIAN))
                return parseVersion(description, DEBIAN);
            else if (family.equals(OsFamily.FEDORA))
                return parseVersion(description, FEDORA);
            else if (family.equals(OsFamily.RHEL))
                return parseVersion(description, RHEL);
            else if (family.equals(OsFamily.UBUNTU))
                return parseVersion(description, UBUNTU);
            else if (family.equals(OsFamily.WINDOWS))
                return parseVersion(description, WINDOWS);
            else if (family.equals(OsFamily.CLOUD_LINUX))
                return parseVersion(description, CLOUD_LINUX);
            else
                throw new NoSuchElementException(STR + productItem);
        }
    };
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,27 +1,24 @@
-public static Function<ProductItem, String> osVersion() {

-    return new Function<ProductItem, String>() {

+public static Function<String, String> osVersion() {

+    return new Function<String, String>() {

 

         @Override

-        public String apply(ProductItem productItem) {

-            checkNotNull(productItem, STR);

-            final String description = productItem.getDescription();

-            OsFamily family = osFamily().apply(productItem);

-            if (family.equals(OsFamily.CENTOS))

+        public String apply(final String description) {

+            OsFamily family = osFamily().apply(description);

+            if (Objects.equal(family, OsFamily.CENTOS))

                 return parseVersion(description, CENTOS);

-            else if (family.equals(OsFamily.DEBIAN))

+            else if (Objects.equal(family, OsFamily.DEBIAN))

                 return parseVersion(description, DEBIAN);

-            else if (family.equals(OsFamily.FEDORA))

+            else if (Objects.equal(family, OsFamily.FEDORA))

                 return parseVersion(description, FEDORA);

-            else if (family.equals(OsFamily.RHEL))

+            else if (Objects.equal(family, OsFamily.RHEL))

                 return parseVersion(description, RHEL);

-            else if (family.equals(OsFamily.UBUNTU))

+            else if (Objects.equal(family, OsFamily.UBUNTU))

                 return parseVersion(description, UBUNTU);

-            else if (family.equals(OsFamily.WINDOWS))

+            else if (Objects.equal(family, OsFamily.WINDOWS))

                 return parseVersion(description, WINDOWS);

-            else if (family.equals(OsFamily.CLOUD_LINUX))

+            else if (Objects.equal(family, OsFamily.CLOUD_LINUX))

                 return parseVersion(description, CLOUD_LINUX);

-            else

-                throw new NoSuchElementException(STR + productItem);

+            return null;

         }

```

---

### [30/102] `Return_58`

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
@return true if the example is compatible with the given mode
```

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
  static public boolean isCompatible(Base base, StringDict props) {
    Mode mode = base.getActiveEditor().getMode();
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
    for (String c : compatibleList) {
      if (c.equals(currentIdentifier)) {
        return true;
      }
    }
    return false;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,4 @@
-static public boolean isCompatible(Base base, StringDict props) {

-    Mode mode = base.getActiveEditor().getMode();

+static public boolean isCompatible(Mode mode, StringDict props) {

     String currentIdentifier = mode.getIdentifier();

     StringList compatibleList = parseModeList(props);

     if (compatibleList.size() == 0) {

@@ -10,10 +9,5 @@
       // if no Mode specified, assume compatible everywhere

       return true;

     }

-    for (String c : compatibleList) {

-      if (c.equals(currentIdentifier)) {

-        return true;

-      }

-    }

-    return false;

+    return compatibleList.hasValue(currentIdentifier);

   }
```

---

### [95/102] `Return_188`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1049 |
| SARI | 0.1603 |
| GLEU | 0.3462 |
| METEOR | 0.7120 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Iterator of all derived types
```

**标准注释 (ground truth)**
```
@return Iterator of all directly derived types
```

**生成注释 (generated)**
```
@return List of all derived types
```

**当前代码 (new_code)**
```java
public List<FxType> getDerivedTypes() {
    return Collections.unmodifiableList(derivedTypes);
}
```

**变更前代码 (old_code)**
```java
public List<FxType> getDerivedTypes() {
    return derivedTypes;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public List<FxType> getDerivedTypes() {

-    return derivedTypes;

+    return Collections.unmodifiableList(derivedTypes);

 }
```

---

### [11/102] `Return_20`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
	private JTextArea getTxtEncode() {
		if (txtEncode == null) {
			txtEncode = new JTextArea();
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

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
-private JTextArea getTxtEncode() {

+private ZapTextArea getTxtEncode() {

 		if (txtEncode == null) {

-			txtEncode = new JTextArea();

+			txtEncode = new ZapTextArea();

 			txtEncode.setLineWrap(true);

 			txtEncode.setFont(new java.awt.Font("Courier New", java.awt.Font.PLAIN, 12));

 			txtEncode.addMouseListener(new java.awt.event.MouseAdapter() {   

```

---

### [22/102] `Return_42`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
	private JTextArea getTxtDecode() {
		if (txtDecode == null) {
			txtDecode = new JTextArea();
			txtDecode.setLineWrap(true);
			txtDecode.setFont(new java.awt.Font("Courier New", java.awt.Font.PLAIN, 12));
		}
		return txtDecode;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
-private JTextArea getTxtDecode() {

+private ZapTextArea getTxtDecode() {

 		if (txtDecode == null) {

-			txtDecode = new JTextArea();

+			txtDecode = new ZapTextArea();

 			txtDecode.setLineWrap(true);

 			txtDecode.setFont(new java.awt.Font("Courier New", java.awt.Font.PLAIN, 12));

 		}

```

---

### [50/102] `Return_98`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
	private JMenuItem getMenuHelpAbout() {
		if (menuHelpAbout == null) {
			menuHelpAbout = new JMenuItem();
			// ZAP: Rebrand
			menuHelpAbout.setText(Constant.messages.getString("menu.help.about")); // ZAP: i18n
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

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,16 +1,11 @@
-private JMenuItem getMenuHelpAbout() {

+private ZapMenuItem getMenuHelpAbout() {

 		if (menuHelpAbout == null) {

-			menuHelpAbout = new JMenuItem();

-			// ZAP: Rebrand

-			menuHelpAbout.setText(Constant.messages.getString("menu.help.about")); // ZAP: i18n

+			menuHelpAbout = new ZapMenuItem("menu.help.about");

 			menuHelpAbout.addActionListener(new java.awt.event.ActionListener() { 

-

 				@Override

 				public void actionPerformed(java.awt.event.ActionEvent e) {    

-

 					AboutDialog dialog = new AboutDialog(View.getSingleton().getMainFrame(), true);

 					dialog.setVisible(true);

-					

 				}

 			});

 

```

---

### [16/102] `Return_30`

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

**当前代码 (new_code)**
```java
public double get(WithAttributes withAttributes) {
    return withAttributes.getAttributes().get(this);
}
```

**变更前代码 (old_code)**
```java
public double get(WithAttributes attributes) {
    return attributes.getAttributes().get(this);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public double get(WithAttributes attributes) {

-    return attributes.getAttributes().get(this);

+public double get(WithAttributes withAttributes) {

+    return withAttributes.getAttributes().get(this);

 }
```

---

### [75/102] `Return_148`

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
@return the value of this attribute if this attribute is present in the map. Otherwise 0
```

**当前代码 (new_code)**
```java
public long get(WithAttributes withAttributes) {
    return withAttributes.getAttributes().get(this);
}
```

**变更前代码 (old_code)**
```java
public long get(WithAttributes attributes) {
    return attributes.getAttributes().get(this);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public long get(WithAttributes attributes) {

-    return attributes.getAttributes().get(this);

+public long get(WithAttributes withAttributes) {

+    return withAttributes.getAttributes().get(this);

 }
```

---

### [39/102] `Return_76`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
  public List<List<TaggedWord>> process(List<? extends List<? extends HasWord>> sentences) {
    List<List<TaggedWord>> taggedSentences = Generics.newArrayList();

    TestSentence testSentence = new TestSentence(this);
    for (List<? extends HasWord> sentence : sentences) {
      taggedSentences.add(testSentence.tagSentence(sentence, false));
    }
    return taggedSentences;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public List<List<TaggedWord>> process(List<? extends List<? extends HasWord>> sentences) {

-    List<List<TaggedWord>> taggedSentences = Generics.newArrayList();

+public List<ArrayList<TaggedWord>> process(List<? extends List<? extends HasWord>> sentences) {

+    List<ArrayList<TaggedWord>> taggedSentences = new ArrayList<ArrayList<TaggedWord>>();

 

     TestSentence testSentence = new TestSentence(this);

     for (List<? extends HasWord> sentence : sentences) {

```

---

### [63/102] `Return_124`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0773 |
| SARI | 0.2583 |
| GLEU | 0.1818 |
| METEOR | 0.4189 |
| xMatch | ✗ |

**原注释 (source)**
```
@return menu placed under specified control
```

**标准注释 (ground truth)**
```
@return menu of given control
```

**生成注释 (generated)**
```
@return controlMenu placed under specified control
```

**当前代码 (new_code)**
```java
public Menu getControlMenu(final Control c) {
    Menu controlMenu = ControlHandler.getInstance().getMenu(c);
    if (controlMenu == null) {
        throw new CoreLayerException(c.getClass() + STR);
    }
    return controlMenu;
}
```

**变更前代码 (old_code)**
```java
public Menu getControlMenu(final Control c) {
    Menu menu = Display.syncExec(new ResultRunnable<Menu>() {

        @Override
        public Menu run() {
            Menu m = c.getMenu();
            return m;
        }
    });
    if (menu == null) {
        throw new CoreLayerException(c.getClass() + STR);
    }
    return menu;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,14 +1,7 @@
 public Menu getControlMenu(final Control c) {

-    Menu menu = Display.syncExec(new ResultRunnable<Menu>() {

-

-        @Override

-        public Menu run() {

-            Menu m = c.getMenu();

-            return m;

-        }

-    });

-    if (menu == null) {

+    Menu controlMenu = ControlHandler.getInstance().getMenu(c);

+    if (controlMenu == null) {

         throw new CoreLayerException(c.getClass() + STR);

     }

-    return menu;

+    return controlMenu;

 }
```

---

### [98/102] `Return_194`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3479 |
| SARI | 0.2951 |
| GLEU | 0.3913 |
| METEOR | 0.4932 |
| xMatch | ✗ |

**原注释 (source)**
```
@return true: can launch bundle, false: otherwise
```

**标准注释 (ground truth)**
```
@return true: can load the bundle, false: cannot
```

**生成注释 (generated)**
```
@return true: can launch bundle, true: otherwise
```

**当前代码 (new_code)**
```java
public boolean preloadBundle(Bundle bundle) {
    return true;
}
```

**变更前代码 (old_code)**
```java
public boolean preloadBundle(Bundle bundle) {
    return false;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public boolean preloadBundle(Bundle bundle) {

-    return false;

+    return true;

 }
```

---

### [85/102] `Return_168`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5296 |
| SARI | 0.3323 |
| GLEU | 0.5405 |
| METEOR | 0.7333 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the converted value, or null if the conversion could not be made
```

**标准注释 (ground truth)**
```
@return the converted value, or null if the conversion could not be made and the column allows nulls
```

**生成注释 (generated)**
```
@return the converted value, or null if the data is null and the column is optional
```

**当前代码 (new_code)**
```java
    protected Object convertNumeric(Column column, Field fieldDefn, Object data) {
        if (data == null) {
            data = fieldDefn.schema().defaultValue();
        }
        if (data == null) {
            if (column.isOptional()) return null;
            return new BigDecimal(0);
        }
        BigDecimal decimal = null;
        if (data instanceof BigDecimal)
            decimal = (BigDecimal) data;
        else if (data instanceof Boolean)
            decimal = new BigDecimal(((Boolean) data).booleanValue() ? 1 : 0);
        else if (data instanceof Short)
            decimal = new BigDecimal(((Short) data).intValue());
        else if (data instanceof Integer)
            decimal = new BigDecimal(((Integer) data).intValue());
        else if (data instanceof Long)
            decimal = BigDecimal.valueOf(((Long) data).longValue());
        else if (data instanceof Float)
            decimal = BigDecimal.valueOf(((Float) data).doubleValue());
        else if (data instanceof Double)
            decimal = BigDecimal.valueOf(((Double) data).doubleValue());
        else {
            return handleUnknownData(column, fieldDefn, data);
        }
        return decimal;
    }

```

**变更前代码 (old_code)**
```java
    protected Object convertNumeric(Column column, Field fieldDefn, Object data) {
        if (data == null) return null;
        BigDecimal decimal = null;
        if (data instanceof BigDecimal)
            decimal = (BigDecimal) data;
        else if (data instanceof Boolean)
            decimal = new BigDecimal(((Boolean) data).booleanValue() ? 1 : 0);
        else if (data instanceof Short)
            decimal = new BigDecimal(((Short) data).intValue());
        else if (data instanceof Integer)
            decimal = new BigDecimal(((Integer) data).intValue());
        else if (data instanceof Long)
            decimal = BigDecimal.valueOf(((Long) data).longValue());
        else if (data instanceof Float)
            decimal = BigDecimal.valueOf(((Float) data).doubleValue());
        else if (data instanceof Double)
            decimal = BigDecimal.valueOf(((Double) data).doubleValue());
        else {
            return handleUnknownData(column, fieldDefn, data);
        }
        return decimal;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,11 @@
 protected Object convertNumeric(Column column, Field fieldDefn, Object data) {

-        if (data == null) return null;

+        if (data == null) {

+            data = fieldDefn.schema().defaultValue();

+        }

+        if (data == null) {

+            if (column.isOptional()) return null;

+            return new BigDecimal(0);

+        }

         BigDecimal decimal = null;

         if (data instanceof BigDecimal)

             decimal = (BigDecimal) data;

```

---

### [94/102] `Return_186`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0659 |
| SARI | 0.3544 |
| GLEU | 0.1744 |
| METEOR | 0.3025 |
| xMatch | ✗ |

**原注释 (source)**
```
@return <false> if the first result is an update count, <true> if it's a <code>ResultSet</code>
```

**标准注释 (ground truth)**
```
@return <code>true</code> if there are any results, <code>false</code> otherwise
```

**生成注释 (generated)**
```
@return <false> if the result queue is empty, <true> if it's not empty
```

**当前代码 (new_code)**
```java
private boolean processResults(boolean returnKeys, boolean update) throws SQLException {
    if (!resultQueue.isEmpty()) {
        throw new IllegalStateException(STR);
    }
    while (!tds.isEndOfResponse()) {
        if (!tds.getMoreResults()) {
            if (tds.isUpdateCount()) {
                if (update && connection.isLastUpdateCount()) {
                    resultQueue.clear();
                }
                resultQueue.addLast(new Integer(tds.getUpdateCount()));
            }
        } else {
            if (returnKeys) {
                if (tds.getNextRow()) {
                    genKeyResultSet = new CachedResultSet(this, tds.getColumns(), tds.getRowData());
                }
            } else {
                if (update && resultQueue.isEmpty()) {
                    throw new SQLException(Messages.get(STR), STR);
                }
                resultQueue.add(new JtdsResultSet(this, ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY, tds.getColumns()));
                break;
            }
        }
    }
    return !resultQueue.isEmpty();
}
```

**变更前代码 (old_code)**
```java
private boolean processResults(boolean returnKeys, boolean update) throws SQLException {
    while (!tds.isEndOfResponse()) {
        if (!tds.getMoreResults()) {
            if (tds.isUpdateCount()) {
                if (update && connection.isLastUpdateCount()) {
                    resultQueue.clear();
                }
                resultQueue.addLast(new Integer(tds.getUpdateCount()));
            }
        } else {
            if (returnKeys) {
                if (tds.getNextRow()) {
                    genKeyResultSet = new CachedResultSet(this, tds.getColumns(), tds.getRowData());
                }
            } else {
                if (update && resultQueue.isEmpty()) {
                    throw new SQLException(Messages.get(STR), STR);
                }
                JtdsResultSet rs = new JtdsResultSet(this, ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY, tds.getColumns(), false);
                if (resultQueue.isEmpty()) {
                    currentResult = rs;
                    return true;
                } else {
                    resultQueue.add(rs);
                    return false;
                }
            }
        }
    }
    return false;
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,7 @@
 private boolean processResults(boolean returnKeys, boolean update) throws SQLException {

+    if (!resultQueue.isEmpty()) {

+        throw new IllegalStateException(STR);

+    }

     while (!tds.isEndOfResponse()) {

         if (!tds.getMoreResults()) {

             if (tds.isUpdateCount()) {

@@ -16,16 +19,10 @@
                 if (update && resultQueue.isEmpty()) {

                     throw new SQLException(Messages.get(STR), STR);

                 }

-                JtdsResultSet rs = new JtdsResultSet(this, ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY, tds.getColumns(), false);

-                if (resultQueue.isEmpty()) {

-                    currentResult = rs;

-                    return true;

-                } else {

-                    resultQueue.add(rs);

-                    return false;

-                }

+                resultQueue.add(new JtdsResultSet(this, ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY, tds.getColumns()));

+                break;

             }

         }

     }

-    return false;

+    return !resultQueue.isEmpty();

 }
```

---

### [2/102] `Return_2`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4180 |
| SARI | 0.3806 |
| GLEU | 0.4412 |
| METEOR | 0.5163 |
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
@return The string representation of the annotations.
```

**当前代码 (new_code)**
```java
@Override
public String toString() {
    return annotations.toString();
}
```

**变更前代码 (old_code)**
```java
@Override
public String toString() {
    List<String> l = new LinkedList<>();
    for (AnnotationMirror a : annotations) {
        DeclaredType annoType = a.getAnnotationType();
        TypeElement elm = (TypeElement) annoType.asElement();
        l.add(elm.getSimpleName().toString());
    }
    String s = l.toString();
    return s.substring(NUM, s.length() - NUM);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,4 @@
 @Override

 public String toString() {

-    List<String> l = new LinkedList<>();

-    for (AnnotationMirror a : annotations) {

-        DeclaredType annoType = a.getAnnotationType();

-        TypeElement elm = (TypeElement) annoType.asElement();

-        l.add(elm.getSimpleName().toString());

-    }

-    String s = l.toString();

-    return s.substring(NUM, s.length() - NUM);

+    return annotations.toString();

 }
```

---

### [73/102] `Return_144`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.0380 |
| SARI | 0.3915 |
| GLEU | 0.1200 |
| METEOR | 0.2657 |
| xMatch | ✗ |

**原注释 (source)**
```
@return boolean Returns a boolean to indicate whether the operation was successful.
```

**标准注释 (ground truth)**
```
@return True if the set of filters was modified by this call.
```

**生成注释 (generated)**
```
@return boolean Returns a boolean to indicate whether the operation was successful.
```

**当前代码 (new_code)**
```java
public boolean remove(Tag tag) {
    return mSelectedTopics.remove(tag);
}
```

**变更前代码 (old_code)**
```java
public boolean remove(String tagId, String category) {
    return isCategoryValid(category) && mSelectedTopics.remove(tagId);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean remove(String tagId, String category) {

-    return isCategoryValid(category) && mSelectedTopics.remove(tagId);

+public boolean remove(Tag tag) {

+    return mSelectedTopics.remove(tag);

 }
```

---

### [55/102] `Return_108`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0699 |
| SARI | 0.3942 |
| GLEU | 0.1364 |
| METEOR | 0.2679 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Value between 1 and 16,777,215
```

**标准注释 (ground truth)**
```
@return position relative to home.
```

**生成注释 (generated)**
```
@return Value between 1 and 16,777,215
```

**当前代码 (new_code)**
```java
public int getPosition() {
    return currentPosition;
}
```

**变更前代码 (old_code)**
```java
public int getPosition() {
    return this.currentPosition;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public int getPosition() {

-    return this.currentPosition;

+    return currentPosition;

 }
```

---

### [9/102] `Return_16`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1149 |
| SARI | 0.4359 |
| GLEU | 0.1456 |
| METEOR | 0.2242 |
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
@return Whether is successful to set the task completed. If the taskAtomList is null or empty will be false; If any task in the list is already completed will be false; If any task in the list is currently downloading will be false. Otherwise will be true.
```

**当前代码 (new_code)**
```java
    public boolean setTaskCompleted(List<FileDownloadTaskAtom> taskAtomList) {
        return FileDownloadServiceProxy.getImpl().setTaskCompleted(taskAtomList);
    }

```

**变更前代码 (old_code)**
```java
    public boolean setTaskCompleted(String url, String path, long totalBytes) {
        return FileDownloadServiceProxy.getImpl().setTaskCompleted(url, path, totalBytes);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean setTaskCompleted(String url, String path, long totalBytes) {

-        return FileDownloadServiceProxy.getImpl().setTaskCompleted(url, path, totalBytes);

+public boolean setTaskCompleted(List<FileDownloadTaskAtom> taskAtomList) {

+        return FileDownloadServiceProxy.getImpl().setTaskCompleted(taskAtomList);

     }
```

---

### [96/102] `Return_190`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0724 |
| SARI | 0.4505 |
| GLEU | 0.1552 |
| METEOR | 0.3439 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the value for the init parameter if defined
```

**标准注释 (ground truth)**
```
@return the list of init params defined in web.xml or application.xml
```

**生成注释 (generated)**
```
@return the value for the init parameter if defined, or null if not defined
```

**当前代码 (new_code)**
```java
    public String getInitParameter(String name) {
        try {
            return framework.getServletConfig().getInitParameter(name);
        } catch (Throwable ex) {
            // Don't fail if Tomcat crash on startup with an NPE
            return null;
        }
    }

```

**变更前代码 (old_code)**
```java
    public String getInitParameter(String name) {
        try {
        	String value=framework.getServletConfig().getInitParameter(name);
        	if(value==null && useServletContextParameters) {
        		value=framework.getServletContext().getInitParameter(name);
        	}
        	return value;
        } catch (Throwable ex) {
            // Don't fail if Tomcat crash on startup with an NPE
            return null;
        }
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,10 +1,6 @@
 public String getInitParameter(String name) {

         try {

-        	String value=framework.getServletConfig().getInitParameter(name);

-        	if(value==null && useServletContextParameters) {

-        		value=framework.getServletContext().getInitParameter(name);

-        	}

-        	return value;

+            return framework.getServletConfig().getInitParameter(name);

         } catch (Throwable ex) {

             // Don't fail if Tomcat crash on startup with an NPE

             return null;

```

---

### [102/102] `Return_202`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4864 |
| SARI | 0.4598 |
| GLEU | 0.5244 |
| METEOR | 0.7561 |
| xMatch | ✗ |

**原注释 (source)**
```
@return  true if regex string is found a given number of times and  false if the regex string is not found
```

**标准注释 (ground truth)**
```
@return  true if text string is found a given number of times and  false if the text string is not found
```

**生成注释 (generated)**
```
@return true if text is found at least the given number of times and false if not found
```

**当前代码 (new_code)**
```java
	public boolean searchText(String text, int minimumNumberOfMatches, boolean scroll) {
		return searcher.searchWithTimeoutFor(TextView.class, text, minimumNumberOfMatches, scroll);
	}

```

**变更前代码 (old_code)**
```java
	public boolean searchText(String regex, int expectedMinimumNumberOfMatches, boolean scroll) {
		return searcher.searchWithTimeoutFor(TextView.class, regex, expectedMinimumNumberOfMatches, scroll);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean searchText(String regex, int expectedMinimumNumberOfMatches, boolean scroll) {

-		return searcher.searchWithTimeoutFor(TextView.class, regex, expectedMinimumNumberOfMatches, scroll);

+public boolean searchText(String text, int minimumNumberOfMatches, boolean scroll) {

+		return searcher.searchWithTimeoutFor(TextView.class, text, minimumNumberOfMatches, scroll);

 	}
```

---

### [68/102] `Return_134`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1974 |
| SARI | 0.4667 |
| GLEU | 0.3060 |
| METEOR | 0.3827 |
| xMatch | ✗ |

**原注释 (source)**
```
@return A list of all of the names that have already been used.
```

**标准注释 (ground truth)**
```
@return An alphabetically sorted list of all of the names that have already been used. This list is not modifiable, but is backed by the real list and will stay updated.
```

**生成注释 (generated)**
```
@return A set of all of the names that have already been used.
```

**当前代码 (new_code)**
```java
public SortedSet<String> getUsedNames() {
    return Collections.unmodifiableSortedSet(mUsedNames);
}
```

**变更前代码 (old_code)**
```java
public SimpleArrayMap<String, String> getUsedNames() {
    return mUsedNames;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public SimpleArrayMap<String, String> getUsedNames() {

-    return mUsedNames;

+public SortedSet<String> getUsedNames() {

+    return Collections.unmodifiableSortedSet(mUsedNames);

 }
```

---

### [10/102] `Return_18`

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

**当前代码 (new_code)**
```java
  public static SqlParser create(String sql, Config config) {
    SqlAbstractParserImpl parser =
        config.parserFactory().getParser(new StringReader(sql));

    return new SqlParser(sql, parser, config);
  }

```

**变更前代码 (old_code)**
```java
  public static SqlParser create(String s) {
    return create(SqlParserImpl.FACTORY, s, Quoting.DOUBLE_QUOTE,
        Casing.TO_UPPER, Casing.UNCHANGED);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,6 @@
-public static SqlParser create(String s) {

-    return create(SqlParserImpl.FACTORY, s, Quoting.DOUBLE_QUOTE,

-        Casing.TO_UPPER, Casing.UNCHANGED);

+public static SqlParser create(String sql, Config config) {

+    SqlAbstractParserImpl parser =

+        config.parserFactory().getParser(new StringReader(sql));

+

+    return new SqlParser(sql, parser, config);

   }
```

---

### [64/102] `Return_126`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0199 |
| SARI | 0.4706 |
| GLEU | 0.0806 |
| METEOR | 0.3194 |
| xMatch | ✗ |

**原注释 (source)**
```
@return uri with properties on
```

**标准注释 (ground truth)**
```
@return a new String value that is the original URI with the added bean properties.
```

**生成注释 (generated)**
```
@return uri with properties on string
```

**当前代码 (new_code)**
```java
public static String addPropertiesToURI(URI uri, Map<String, String> properties) throws Exception {
    return addPropertiesToURI(uri.toString(), properties);
}
```

**变更前代码 (old_code)**
```java
public static String addPropertiesToURI(URI uri, Map<String, String> props) throws Exception {
    return addPropertiesToURI(uri.toString(), props);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static String addPropertiesToURI(URI uri, Map<String, String> props) throws Exception {

-    return addPropertiesToURI(uri.toString(), props);

+public static String addPropertiesToURI(URI uri, Map<String, String> properties) throws Exception {

+    return addPropertiesToURI(uri.toString(), properties);

 }
```

---

### [34/102] `Return_66`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public String getMainCharacterForUserInGuild(User user, Guild guild) {
    MongoCollection<Document> collection = getBot().getMongoDatabase().getCollection(MONGO_WOW_CHARACTERS_COLLECTION);
    Document document = collection.find(and(eq(STR, user.getId()), eq(STR, guild.getId()))).first();
    return document != null ? document.getString(STR) : null;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,13 @@
-public String getMainCharacterForUserInGuild(User user, Guild guild) {

-    MongoCollection<Document> collection = getBot().getMongoDatabase().getCollection(MONGO_WOW_CHARACTERS_COLLECTION);

-    Document document = collection.find(and(eq(STR, user.getId()), eq(STR, guild.getId()))).first();

-    return document != null ? document.getString(STR) : null;

+public JSONObject getMainCharacterForUserInGuild(User user, Guild guild) {

+    JSONObject character = null;

+    HttpUrl url = new HttpUrl.Builder().scheme(STR).host(getBot().getBotSettings().getProperty(STR)).addPathSegments(STR + user.getId() + STR + guild.getId()).build();

+    Request request = new Request.Builder().url(url).build();

+    try {

+        Response response = client.newCall(request).execute();

+        JSONObject jsonObject = new JSONObject(response.body().source());

+        character = jsonObject.length() > NUM ? jsonObject : null;

+    } catch (IOException e) {

+        e.printStackTrace();

+    }

+    return character;

 }
```

---

### [45/102] `Return_88`

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

**当前代码 (new_code)**
```java
@Transactional(readOnly = true)
@Override
public int getAllCount(final String currentUser, final Set<String> userRoles, EphesoftUser ephesoftUser) {
    return batchInstanceDao.getAllCount(currentUser, userRoles, ephesoftUser);
}
```

**变更前代码 (old_code)**
```java
@Transactional(readOnly = true)
@Override
public int getAllCount(final String currentUser, final Set<String> currentRole) {
    return batchInstanceDao.getAllCount(currentUser, currentRole);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
 @Transactional(readOnly = true)

 @Override

-public int getAllCount(final String currentUser, final Set<String> currentRole) {

-    return batchInstanceDao.getAllCount(currentUser, currentRole);

+public int getAllCount(final String currentUser, final Set<String> userRoles, EphesoftUser ephesoftUser) {

+    return batchInstanceDao.getAllCount(currentUser, userRoles, ephesoftUser);

 }
```

---

### [97/102] `Return_192`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.1097 |
| SARI | 0.4955 |
| GLEU | 0.2381 |
| METEOR | 0.5797 |
| xMatch | ✗ |

**原注释 (source)**
```
@return current Estimated rotation we are at
```

**标准注释 (ground truth)**
```
@return estimated rotation of where we are at in angles.
```

**生成注释 (generated)**
```
@return current Estimated rotation we are at
```

**当前代码 (new_code)**
```java
public int getEstimatedRotation() {
    if (!isRotating()) {
        return getRotation();
    }
    double timeSpent = (System.currentTimeMillis() - estimatedRotationStartTime) / NUM;
    int rotation = estimatedRotationStart + (int) (currentVelocity * timeSpent);
    if ((estimatedRotationStart < estimatedRotationEnd) != (estimatedRotationStart < rotation)) {
        rotation = estimatedRotationEnd;
    }
    double angle = (double) (rotation) / Settings.getHandlerRotation() * NUM;
    return (int) (Math.round(angle)) % NUM;
}
```

**变更前代码 (old_code)**
```java
public int getEstimatedRotation() {
    if (!isRotating()) {
        return getRotation();
    } else {
        double timeSpent = (System.currentTimeMillis() - startingTime) / NUM;
        int pos = currentStartingPoint + (int) (currentVelocity * timeSpent);
        double angle = (double) (pos) / Settings.getHandlerRotation() * NUM;
        return (int) (Math.round(angle)) % NUM;
    }
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,10 +1,12 @@
 public int getEstimatedRotation() {

     if (!isRotating()) {

         return getRotation();

-    } else {

-        double timeSpent = (System.currentTimeMillis() - startingTime) / NUM;

-        int pos = currentStartingPoint + (int) (currentVelocity * timeSpent);

-        double angle = (double) (pos) / Settings.getHandlerRotation() * NUM;

-        return (int) (Math.round(angle)) % NUM;

     }

+    double timeSpent = (System.currentTimeMillis() - estimatedRotationStartTime) / NUM;

+    int rotation = estimatedRotationStart + (int) (currentVelocity * timeSpent);

+    if ((estimatedRotationStart < estimatedRotationEnd) != (estimatedRotationStart < rotation)) {

+        rotation = estimatedRotationEnd;

+    }

+    double angle = (double) (rotation) / Settings.getHandlerRotation() * NUM;

+    return (int) (Math.round(angle)) % NUM;

 }
```

---

### [18/102] `Return_34`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public Iterator getGroups() {
    return super.getItems();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,8 @@
-public Iterator getGroups() {

-    return super.getItems();

+public Group[] getGroups() {

+    Item[] items = super.getItems();

+    Group[] groups = new Group[items.length];

+    for (int i = NUM; i < groups.length; i++) {

+        groups[i] = (Group) items[i];

+    }

+    return groups;

 }
```

---

### [93/102] `Return_184`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2390 |
| SARI | 0.5076 |
| GLEU | 0.3043 |
| METEOR | 0.6529 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the list of init params defined in web.xml or application.xml
```

**标准注释 (ground truth)**
```
@return the value for the init parameter if defined
```

**生成注释 (generated)**
```
@return the value of the init param defined in web.xml or application.xml
```

**当前代码 (new_code)**
```java
public String getInitParameter(String name) {
    try {
        String value = framework.getServletConfig().getInitParameter(name);
        if (value == null) {
            value = framework.getServletContext().getInitParameter(name);
        }
        return value;
    } catch (Throwable ex) {
        return null;
    }
}
```

**变更前代码 (old_code)**
```java
public String getInitParameter(String name) {
    try {
        return framework.getServletConfig().getInitParameter(name);
    } catch (Throwable ex) {
        return null;
    }
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,10 @@
 public String getInitParameter(String name) {

     try {

-        return framework.getServletConfig().getInitParameter(name);

+        String value = framework.getServletConfig().getInitParameter(name);

+        if (value == null) {

+            value = framework.getServletContext().getInitParameter(name);

+        }

+        return value;

     } catch (Throwable ex) {

         return null;

     }

```

---

### [21/102] `Return_40`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public String getDocumentPath() {
    return getPublication().getPathMapper().getPath(getDocument().getUUID(), getDocument().getLanguage());
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,11 @@
 public String getDocumentPath() {

-    return getPublication().getPathMapper().getPath(getDocument().getUUID(), getDocument().getLanguage());

+    if (this.path == null) {

+        final Document doc = getDocument();

+        try {

+            this.path = doc != null ? doc.getPath() : getPublication().getDocumentBuilder().getLocator(this.factory, this.webappUrl).getPath();

+        } catch (final Exception e) {

+            throw new RuntimeException(e);

+        }

+    }

+    return this.path;

 }
```

---

### [46/102] `Return_90`

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

**当前代码 (new_code)**
```java
@Override
public Optional<TYPE> first() {
    Iterator<TYPE> resultIterator = first(NUM).iterator();
    return resultIterator.hasNext() ? Optional.of(resultIterator.next()) : Optional.empty();
}
```

**变更前代码 (old_code)**
```java
@Override
public Optional<TYPE> first() {
    Optional result = Optional.empty();
    List<TYPE> list = first(NUM).asList();
    if (!list.isEmpty()) {
        result = Optional.of(list.get(NUM));
    }
    return result;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,5 @@
 @Override

 public Optional<TYPE> first() {

-    Optional result = Optional.empty();

-    List<TYPE> list = first(NUM).asList();

-    if (!list.isEmpty()) {

-        result = Optional.of(list.get(NUM));

-    }

-    return result;

+    Iterator<TYPE> resultIterator = first(NUM).iterator();

+    return resultIterator.hasNext() ? Optional.of(resultIterator.next()) : Optional.empty();

 }
```

---

### [62/102] `Return_122`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.2749 |
| SARI | 0.5245 |
| GLEU | 0.5455 |
| METEOR | 0.8413 |
| xMatch | ✗ |

**原注释 (source)**
```
@return a grapql language ast  Value
```

**标准注释 (ground truth)**
```
@return a graphql language ast  Value
```

**生成注释 (generated)**
```
@return a grapql language ast  Value
```

**当前代码 (new_code)**
```java
    public static Value astFromValue(Object value, GraphQLType type) {
        if (value == null) {
            return null;
        }

        if (isNonNull(type)) {
            return handleNonNull(value, (GraphQLNonNull) type);
        }

        // Convert JavaScript array to GraphQL list. If the GraphQLType is a list, but
        // the value is not an array, convert the value using the list's item type.
        if (isList(type)) {
            return handleList(value, (GraphQLList) type);
        }

        // Populate the fields of the input object by creating ASTs from each value
        // in the JavaScript object according to the fields in the input type.
        if (type instanceof GraphQLInputObjectType) {
            return handleInputObject(value, (GraphQLInputObjectType) type);
        }

        if (!(type instanceof GraphQLScalarType || type instanceof GraphQLEnumType)) {
            throw new AssertException("Must provide Input Type, cannot use: " + type.getClass());
        }

        // Since value is an internally represented value, it must be serialized
        // to an externally represented value before converting into an AST.
        final Object serialized = serialize(type, value);
        if (isNullish(serialized)) {
            return null;
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public static Value astFromValue(Object value, GraphQLType type) {
        if (value == null) {
            return null;
        }

        if (isNonNull(type)) {
            return handleNonNull(value, (GraphQLNonNull) type);
        }

        // Convert JavaScript array to GraphQL list. If the GraphQLType is a list, but
        // the value is not an array, convert the value using the list's item type.
        if (isList(type)) {
            return handleList(value, (GraphQLList) type);
        }

        // Populate the fields of the input object by creating ASTs from each value
        // in the JavaScript object according to the fields in the input type.
        if (type instanceof GraphQLInputObjectType) {
            return handleInputObject(value, (GraphQLInputObjectType) type);
        }

        if (!(type instanceof GraphQLScalarType || type instanceof GraphQLEnumType)) {
            throw new AssertException("Must provide Input Type, cannot use: " + type.getClass());
        }

        // Since value is an internally represented value, it must be serialized
        // to an externally represented value before converting into an AST.
        final Object serialized = serialize(type, value);
        if (isNullish(serialized)) {
            return null;
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -53,7 +53,7 @@
             }

 

             // String types are just strings but JSON'ised

-            return StringValue.newStringValue().value(jsonStringify(stringValue)).build();

+            return StringValue.newStringValue().value(stringValue).build();

         }

 

         throw new AssertException("'Cannot convert value to AST: " + serialized);

```

---

### [66/102] `Return_130`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1448 |
| SARI | 0.5270 |
| GLEU | 0.2308 |
| METEOR | 0.3775 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the aggregationCount
```

**标准注释 (ground truth)**
```
@return the total number of aggregation executions
```

**生成注释 (generated)**
```
@return the aggregationCount.longValue()
```

**当前代码 (new_code)**
```java
@ManagedAttribute(description = STR)
public long getAggregationCount() {
    return aggregationCount.longValue();
}
```

**变更前代码 (old_code)**
```java
public LongAdder getAggregationCount() {
    return aggregationCount;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,4 @@
-public LongAdder getAggregationCount() {

-    return aggregationCount;

+@ManagedAttribute(description = STR)

+public long getAggregationCount() {

+    return aggregationCount.longValue();

 }
```

---

### [48/102] `Return_94`

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

**当前代码 (new_code)**
```java
public int decodable(QpidByteBuffer in) {
    return (in.remaining() >= NUM) ? NUM : NUM - in.remaining();
}
```

**变更前代码 (old_code)**
```java
public boolean decodable(MarkableDataInput in) throws IOException {
    return (in.available() >= NUM);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean decodable(MarkableDataInput in) throws IOException {

-    return (in.available() >= NUM);

+public int decodable(QpidByteBuffer in) {

+    return (in.remaining() >= NUM) ? NUM : NUM - in.remaining();

 }
```

---

### [24/102] `Return_46`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0922 |
| SARI | 0.5608 |
| GLEU | 0.2162 |
| METEOR | 0.5584 |
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
@return the parsed Test Suites or null if no Test Suites were found.
```

**当前代码 (new_code)**
```java
public List<TestSuite> getSuite() {
    return this.testSuites;
}
```

**变更前代码 (old_code)**
```java
public TestSuite getSuite() {
    return this.testSuite;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public TestSuite getSuite() {

-    return this.testSuite;

+public List<TestSuite> getSuite() {

+    return this.testSuites;

 }
```

---

### [47/102] `Return_92`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3818 |
| SARI | 0.5817 |
| GLEU | 0.4242 |
| METEOR | 0.7087 |
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
@return Object value of the property - or IllegalArgumentException if name is null or property not supported
```

**当前代码 (new_code)**
```java
public Object getProperty(String name) {
    if (name == null || !isPropertySupported(name))
        throw new IllegalArgumentException();
    return callProperties.get(name);
}
```

**变更前代码 (old_code)**
```java
public Object getProperty(String name) {
    if (name != null)
        return callProperties.get(name);
    return null;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
 public Object getProperty(String name) {

-    if (name != null)

-        return callProperties.get(name);

-    return null;

+    if (name == null || !isPropertySupported(name))

+        throw new IllegalArgumentException();

+    return callProperties.get(name);

 }
```

---

### [69/102] `Return_136`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5642 |
| SARI | 0.5843 |
| GLEU | 0.5897 |
| METEOR | 0.7839 |
| xMatch | ✗ |

**原注释 (source)**
```
@return true if this authentication realm "understands" how to process submissions for the submitted token instances of the class, false otherwise.
```

**标准注释 (ground truth)**
```
@return true if this authentication realm can process the submitted token instance of the class, false otherwise.
```

**生成注释 (generated)**
```
@return true if this authentication realm "understands" how to process the submitted token instance, false otherwise.
```

**当前代码 (new_code)**
```java
public boolean supports(AuthenticationToken token) {
    if (log.isInfoEnabled()) {
        log.info(STR + STR);
    }
    return token != null && getAuthenticationTokenClass().isAssignableFrom(token.getClass());
}
```

**变更前代码 (old_code)**
```java
public boolean supports(Class tokenClass) {
    return getAuthenticationTokenClass().isAssignableFrom(tokenClass);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,6 @@
-public boolean supports(Class tokenClass) {

-    return getAuthenticationTokenClass().isAssignableFrom(tokenClass);

+public boolean supports(AuthenticationToken token) {

+    if (log.isInfoEnabled()) {

+        log.info(STR + STR);

+    }

+    return token != null && getAuthenticationTokenClass().isAssignableFrom(token.getClass());

 }
```

---

### [79/102] `Return_156`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1204 |
| SARI | 0.6038 |
| GLEU | 0.3043 |
| METEOR | 0.8000 |
| xMatch | ✗ |

**原注释 (source)**
```
@return contactId, if not found INVALID_ID is returned
```

**标准注释 (ground truth)**
```
@return list of contactIds, empty list if none was found
```

**生成注释 (generated)**
```
@return List of contactIds, if not found empty list is returned
```

**当前代码 (new_code)**
```java
private List<Long> getRcsRawContactIdFromPhoneNumber(String phoneNumber) {
    List<Long> contactsIds = new ArrayList<Long>();
    String[] projection = { Data.RAW_CONTACT_ID };
    String selection = Data.MIMETYPE + STR + Phone.NUMBER + STR;
    String[] selectionArgs = { MIMETYPE_NUMBER, phoneNumber };
    String sortOrder = Data.RAW_CONTACT_ID;
    Cursor cur = ctx.getContentResolver().query(Data.CONTENT_URI, projection, selection, selectionArgs, sortOrder);
    if (cur != null) {
        while (cur.moveToNext()) {
            long rcsRawContactId = cur.getLong(cur.getColumnIndex(Data.RAW_CONTACT_ID));
            contactsIds.add(rcsRawContactId);
        }
        cur.close();
    }
    return contactsIds;
}
```

**变更前代码 (old_code)**
```java
private long getRcsRawContactIdFromPhoneNumber(String phoneNumber) {
    String[] projection = { Data.RAW_CONTACT_ID };
    String selection = Data.MIMETYPE + STR + Phone.NUMBER + STR;
    String[] selectionArgs = { MIMETYPE_NUMBER, phoneNumber };
    String sortOrder = Data.RAW_CONTACT_ID;
    Cursor cur = ctx.getContentResolver().query(Data.CONTENT_URI, projection, selection, selectionArgs, sortOrder);
    if (cur != null) {
        while (cur.moveToNext()) {
            long rcsRawContactId = cur.getLong(cur.getColumnIndex(Data.RAW_CONTACT_ID));
            cur.close();
            return rcsRawContactId;
        }
        cur.close();
    }
    return INVALID_ID;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,5 @@
-private long getRcsRawContactIdFromPhoneNumber(String phoneNumber) {

+private List<Long> getRcsRawContactIdFromPhoneNumber(String phoneNumber) {

+    List<Long> contactsIds = new ArrayList<Long>();

     String[] projection = { Data.RAW_CONTACT_ID };

     String selection = Data.MIMETYPE + STR + Phone.NUMBER + STR;

     String[] selectionArgs = { MIMETYPE_NUMBER, phoneNumber };

@@ -7,10 +8,9 @@
     if (cur != null) {

         while (cur.moveToNext()) {

             long rcsRawContactId = cur.getLong(cur.getColumnIndex(Data.RAW_CONTACT_ID));

-            cur.close();

-            return rcsRawContactId;

+            contactsIds.add(rcsRawContactId);

         }

         cur.close();

     }

-    return INVALID_ID;

+    return contactsIds;

 }
```

---

### [53/102] `Return_104`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.7071 |
| SARI | 0.6089 |
| GLEU | 0.7308 |
| METEOR | 0.8648 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the {@link AsyncAppenderBase}
```

**标准注释 (ground truth)**
```
@return the {@link AsyncAppenderFactory}
```

**生成注释 (generated)**
```
@return the {@link AsyncAppenderBase}
```

**当前代码 (new_code)**
```java
@Override
public AsyncAppenderBase<IAccessEvent> build() {
    return new AsyncAppenderBase<IAccessEvent>() {

        @Override
        protected void preprocess(IAccessEvent event) {
            event.prepareForDeferredProcessing();
        }
    };
}
```

**变更前代码 (old_code)**
```java
@Override
public AsyncAppenderBase<IAccessEvent> build() {
    return new AsyncAppenderBase<IAccessEvent>();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,10 @@
 @Override

 public AsyncAppenderBase<IAccessEvent> build() {

-    return new AsyncAppenderBase<IAccessEvent>();

+    return new AsyncAppenderBase<IAccessEvent>() {

+

+        @Override

+        protected void preprocess(IAccessEvent event) {

+            event.prepareForDeferredProcessing();

+        }

+    };

 }
```

---

### [5/102] `Return_8`

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

**当前代码 (new_code)**
```java
public static String getHostFromUrl(String url) {
    String authority = getAuthorityFromUrl(url);
    int idx = authority.indexOf(STR);
    if (idx == -NUM)
        return authority;
    return authority.substring(NUM, idx);
}
```

**变更前代码 (old_code)**
```java
public static String getHostFromUrl(String url) {
    if (url.indexOf(STR) == -NUM)
        return url;
    int slashes = NUM;
    if (url.contains(STR))
        slashes += NUM;
    String[] parts = url.split(STR);
    if (parts.length < slashes)
        return url;
    return parts[slashes];
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,7 @@
 public static String getHostFromUrl(String url) {

-    if (url.indexOf(STR) == -NUM)

-        return url;

-    int slashes = NUM;

-    if (url.contains(STR))

-        slashes += NUM;

-    String[] parts = url.split(STR);

-    if (parts.length < slashes)

-        return url;

-    return parts[slashes];

+    String authority = getAuthorityFromUrl(url);

+    int idx = authority.indexOf(STR);

+    if (idx == -NUM)

+        return authority;

+    return authority.substring(NUM, idx);

 }
```

---

### [29/102] `Return_56`

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

**当前代码 (new_code)**
```java
public int getMaxQueryTime() {
    return maxQueryTime;
}
```

**变更前代码 (old_code)**
```java
public long getMaxQueryTime() {
    return maxQueryTime;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public long getMaxQueryTime() {

+public int getMaxQueryTime() {

     return maxQueryTime;

 }
```

---

### [8/102] `Return_14`

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

**当前代码 (new_code)**
```java
public ICursor getCursor() {
    return cursor;
}
```

**变更前代码 (old_code)**
```java
public Cursor getCursor() {
    return cursor;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public Cursor getCursor() {

+public ICursor getCursor() {

     return cursor;

 }
```

---

### [84/102] `Return_166`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3337 |
| SARI | 0.6260 |
| GLEU | 0.3391 |
| METEOR | 0.7381 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the converted value, or null if the conversion could not be made
```

**标准注释 (ground truth)**
```
@return the converted value, or null if the conversion could not be made and the column allows nulls
```

**生成注释 (generated)**
```
@return the converted value, or null if the data is null and the column is optional, or 0L if the data is null and the column is not optional, or the result of handleUnknownData if the conversion could not be made
```

**当前代码 (new_code)**
```java
    protected Object convertTimeToNanosPastMidnight(Column column, Field fieldDefn, Object data) {
        if (data == null) {
            data = fieldDefn.schema().defaultValue();
        }
        if (data == null) {
            if (column.isOptional()) return null;
            return 0L; // return epoch
        }
        try {
            return NanoTime.toNanoOfDay(data);
        } catch (IllegalArgumentException e) {
            return handleUnknownData(column, fieldDefn, data);
        }
    }

```

**变更前代码 (old_code)**
```java
    protected Object convertTimeToNanosPastMidnight(Column column, Field fieldDefn, Object data) {
        if ( data == null ) return null;
        try {
            return NanoTime.toNanoOfDay(data);
        } catch (IllegalArgumentException e) {
            return handleUnknownData(column, fieldDefn, data);
        }
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,11 @@
 protected Object convertTimeToNanosPastMidnight(Column column, Field fieldDefn, Object data) {

-        if ( data == null ) return null;

+        if (data == null) {

+            data = fieldDefn.schema().defaultValue();

+        }

+        if (data == null) {

+            if (column.isOptional()) return null;

+            return 0L; // return epoch

+        }

         try {

             return NanoTime.toNanoOfDay(data);

         } catch (IllegalArgumentException e) {

```

---

### [32/102] `Return_62`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public static Method findGetMethod(Field field, boolean throwExceptions) {
    String methodName = methodFromField(field, STR);
    Method fieldGetMethod;
    try {
        try {
            fieldGetMethod = field.getDeclaringClass().getMethod(methodName);
        } catch (NoSuchMethodException nsme) {
            if (field.getType() == Boolean.class || field.getType() == boolean.class) {
                methodName = methodFromField(field, STR);
                fieldGetMethod = field.getDeclaringClass().getMethod(methodName);
            } else {
                throw nsme;
            }
        }
    } catch (Exception e) {
        if (throwExceptions) {
            throw new IllegalArgumentException(STR + field);
        } else {
            return null;
        }
    }
    if (fieldGetMethod.getReturnType() != field.getType()) {
        if (throwExceptions) {
            throw new IllegalArgumentException(STR + methodName + STR + field.getType());
        } else {
            return null;
        }
    }
    return fieldGetMethod;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,27 +1,16 @@
-public static Method findGetMethod(Field field, boolean throwExceptions) {

-    String methodName = methodFromField(field, STR);

+public static Method findGetMethod(Field field, boolean throwExceptions) throws IllegalArgumentException {

     Method fieldGetMethod;

-    try {

-        try {

-            fieldGetMethod = field.getDeclaringClass().getMethod(methodName);

-        } catch (NoSuchMethodException nsme) {

-            if (field.getType() == Boolean.class || field.getType() == boolean.class) {

-                methodName = methodFromField(field, STR);

-                fieldGetMethod = field.getDeclaringClass().getMethod(methodName);

-            } else {

-                throw nsme;

-            }

-        }

-    } catch (Exception e) {

-        if (throwExceptions) {

-            throw new IllegalArgumentException(STR + field);

-        } else {

-            return null;

-        }

+    if (Locale.ENGLISH.equals(Locale.getDefault())) {

+        fieldGetMethod = findMethodFromNames(field, true, throwExceptions, methodFromField(field, STR, null), methodFromField(field, STR, null));

+    } else {

+        fieldGetMethod = findMethodFromNames(field, true, throwExceptions, methodFromField(field, STR, null), methodFromField(field, STR, Locale.ENGLISH), methodFromField(field, STR, null), methodFromField(field, STR, Locale.ENGLISH));

+    }

+    if (fieldGetMethod == null) {

+        return null;

     }

     if (fieldGetMethod.getReturnType() != field.getType()) {

         if (throwExceptions) {

-            throw new IllegalArgumentException(STR + methodName + STR + field.getType());

+            throw new IllegalArgumentException(STR + fieldGetMethod.getName() + STR + field.getType());

         } else {

             return null;

         }

```

---

### [43/102] `Return_84`

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

**当前代码 (new_code)**
```java
public ExtensionHandler getExtensionHandler() {
    return generatorContext.getExtensionHandler();
}
```

**变更前代码 (old_code)**
```java
public ExtensionHandler getExtensionHandler() {
    return extensionHandler;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public ExtensionHandler getExtensionHandler() {

-    return extensionHandler;

+    return generatorContext.getExtensionHandler();

 }
```

---

### [77/102] `Return_152`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7260 |
| SARI | 0.6379 |
| GLEU | 0.7333 |
| METEOR | 0.7766 |
| xMatch | ✗ |

**原注释 (source)**
```
@return returns all axis mapped to an ImmutableMap
```

**标准注释 (ground truth)**
```
@return returns all axis mapped to a Map
```

**生成注释 (generated)**
```
@return returns all axis mapped to an unmodifiableMap
```

**当前代码 (new_code)**
```java
public Map<String, Integer> parameters() {
    HashMap<String, Integer> values = new HashMap<>();
    values.put(STR, this.x);
    values.put(STR, this.y);
    values.put(STR, this.z);
    return Collections.unmodifiableMap(values);
}
```

**变更前代码 (old_code)**
```java
public ImmutableMap<String, Integer> parameters() {
    return ImmutableMap.of(STR, this.x, STR, this.y, STR, this.z);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,7 @@
-public ImmutableMap<String, Integer> parameters() {

-    return ImmutableMap.of(STR, this.x, STR, this.y, STR, this.z);

+public Map<String, Integer> parameters() {

+    HashMap<String, Integer> values = new HashMap<>();

+    values.put(STR, this.x);

+    values.put(STR, this.y);

+    values.put(STR, this.z);

+    return Collections.unmodifiableMap(values);

 }
```

---

### [44/102] `Return_86`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public CacheStatisticsImpl createCacheStatIfAbsent(String name) {
    if (!statistics.containsKey(name)) {
        statistics.putIfAbsent(name, new CacheStatisticsImpl());
    }
    return statistics.get(name);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,8 @@
 public CacheStatisticsImpl createCacheStatIfAbsent(String name) {

-    if (!statistics.containsKey(name)) {

-        statistics.putIfAbsent(name, new CacheStatisticsImpl());

+    CacheStatisticsImpl statistics = new CacheStatisticsImpl();

+    CacheStatisticsImpl temp = this.statistics.putIfAbsent(name, statistics);

+    if (temp != null) {

+        statistics = temp;

     }

-    return statistics.get(name);

+    return statistics;

 }
```

---

### [52/102] `Return_102`

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

**当前代码 (new_code)**
```java
public Map<String, String> getAdditionalHttpHeaders() {
    return additionalHttpHeaders == null ? null : Collections.unmodifiableMap(additionalHttpHeaders);
}
```

**变更前代码 (old_code)**
```java
public Map<String, String> getAdditionalHttpHeaders() {
    return Collections.unmodifiableMap(additionalHttpHeaders);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public Map<String, String> getAdditionalHttpHeaders() {

-    return Collections.unmodifiableMap(additionalHttpHeaders);

+    return additionalHttpHeaders == null ? null : Collections.unmodifiableMap(additionalHttpHeaders);

 }
```

---

### [74/102] `Return_146`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5803 |
| SARI | 0.6521 |
| GLEU | 0.6098 |
| METEOR | 0.6572 |
| xMatch | ✗ |

**原注释 (source)**
```
@return The index of the specified element in the model's item list.
```

**标准注释 (ground truth)**
```
@return The index of the specified element in the model's item list, or -1 if it wasn't found
```

**生成注释 (generated)**
```
@return The index of the specified element in the model's item list.
```

**当前代码 (new_code)**
```java
		public int getIndexOf(Object object) {
			int index = tableModel.getUsers().indexOf(object);
			if (index < 0 && customUsers != null)
				return ArrayUtils.indexOf(customUsers, object);
			return index;
		}

```

**变更前代码 (old_code)**
```java
		public int getIndexOf(Object object) {
			return tableModel.getUsers().indexOf(object);
		}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,6 @@
 public int getIndexOf(Object object) {

-			return tableModel.getUsers().indexOf(object);

+			int index = tableModel.getUsers().indexOf(object);

+			if (index < 0 && customUsers != null)

+				return ArrayUtils.indexOf(customUsers, object);

+			return index;

 		}
```

---

### [58/102] `Return_114`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5002 |
| SARI | 0.6530 |
| GLEU | 0.5135 |
| METEOR | 0.8927 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the list of initial <code>ServiceReference</code> objects.
```

**标准注释 (ground truth)**
```
@return The list of initial <code>ServiceReference</code>s.
```

**生成注释 (generated)**
```
@return the list of initial <code>ServiceReference</code> objects based on the className parameter.
```

**当前代码 (new_code)**
```java
private ServiceReference[] getInitialReferences(boolean trackAllServices, String className, String filterString) throws InvalidSyntaxException {
    if (trackAllServices) {
        return context.getAllServiceReferences(className, filterString);
    }
    return context.getServiceReferences(className, filterString);
}
```

**变更前代码 (old_code)**
```java
private ServiceReference[] getInitialReferences(boolean trackAllServices, String trackClass, String filterString) throws InvalidSyntaxException {
    if (trackAllServices) {
        return context.getAllServiceReferences(trackClass, filterString);
    } else {
        return context.getServiceReferences(trackClass, filterString);
    }
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,6 @@
-private ServiceReference[] getInitialReferences(boolean trackAllServices, String trackClass, String filterString) throws InvalidSyntaxException {

+private ServiceReference[] getInitialReferences(boolean trackAllServices, String className, String filterString) throws InvalidSyntaxException {

     if (trackAllServices) {

-        return context.getAllServiceReferences(trackClass, filterString);

-    } else {

-        return context.getServiceReferences(trackClass, filterString);

+        return context.getAllServiceReferences(className, filterString);

     }

+    return context.getServiceReferences(className, filterString);

 }
```

---

### [71/102] `Return_140`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.8624 |
| SARI | 0.6578 |
| GLEU | 0.8605 |
| METEOR | 0.8771 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Opaque string handle for this terminal instance, or null if terminal has never been attached to a process
```

**标准注释 (ground truth)**
```
@return Opaque string handle for this terminal instance, or null if terminal has never been attached to a server ConsoleProcess.
```

**生成注释 (generated)**
```
@return Opaque string handle for this terminal instance, or null if terminal has never been attached to a process
```

**当前代码 (new_code)**
```java
public String getHandle() {
    if (consoleProcess_ == null) {
        return terminalHandle_;
    }
    return consoleProcess_.getProcessInfo().getHandle();
}
```

**变更前代码 (old_code)**
```java
public String getHandle() {
    if (consoleProcess_ == null) {
        return terminalHandle_;
    }
    return consoleProcess_.getProcessInfo().getTerminalHandle();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -2,5 +2,5 @@
     if (consoleProcess_ == null) {

         return terminalHandle_;

     }

-    return consoleProcess_.getProcessInfo().getTerminalHandle();

+    return consoleProcess_.getProcessInfo().getHandle();

 }
```

---

### [65/102] `Return_128`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8173 |
| SARI | 0.6596 |
| GLEU | 0.8210 |
| METEOR | 0.8915 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Map {@link IBuildConfiguration} -> {@link IncrementalProjectBuilder} if this build command supports multiple configurations. Otherwise return the {@link IncrementalProjectBuilder} associated with this build command.
```

**标准注释 (ground truth)**
```
@return A copy of the internal map {@link IBuildConfiguration} -> {@link IncrementalProjectBuilder} if this build command supports multiple configurations. Otherwise return the {@link IncrementalProjectBuilder} associated with this build command.
```

**生成注释 (generated)**
```
@return Map {@link IBuildConfiguration} -> {@link IncrementalProjectBuilder} if this build command supports multiple configurations. Otherwise return the {@link IncrementalProjectBuilder} associated with this build command.
```

**当前代码 (new_code)**
```java
public Object getBuilders() {
    synchronized (builderLock) {
        if (supportsConfigs()) {
            return builders == null ? null : new HashMap<>(builders);
        }
        return builder;
    }
}
```

**变更前代码 (old_code)**
```java
public Object getBuilders() {
    synchronized (builderLock) {
        if (supportsConfigs())
            return builders;
        return builder;
    }
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,8 @@
 public Object getBuilders() {

     synchronized (builderLock) {

-        if (supportsConfigs())

-            return builders;

+        if (supportsConfigs()) {

+            return builders == null ? null : new HashMap<>(builders);

+        }

         return builder;

     }

 }
```

---

### [12/102] `Return_22`

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

**当前代码 (new_code)**
```java
@Override
public Clip getAggregation() {
    return Clip.of(aggregate);
}
```

**变更前代码 (old_code)**
```java
@Override
public List<BulletRecord> getAggregation() {
    return aggregate;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
 @Override

-public List<BulletRecord> getAggregation() {

-    return aggregate;

+public Clip getAggregation() {

+    return Clip.of(aggregate);

 }
```

---

### [14/102] `Return_26`

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

**当前代码 (new_code)**
```java
  protected Project getRightChild(RelOptRuleCall call) {
    return call.rel(2);
  }

```

**变更前代码 (old_code)**
```java
  protected ProjectRelBase getRightChild(RelOptRuleCall call) {
    return call.rel(2);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-protected ProjectRelBase getRightChild(RelOptRuleCall call) {

+protected Project getRightChild(RelOptRuleCall call) {

     return call.rel(2);

   }
```

---

### [28/102] `Return_54`

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

**当前代码 (new_code)**
```java
public boolean hasReminder() {
    return reminder != null;
}
```

**变更前代码 (old_code)**
```java
public boolean hasReminder() {
    return (reminderHour != null && reminderMin != null);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public boolean hasReminder() {

-    return (reminderHour != null && reminderMin != null);

+    return reminder != null;

 }
```

---

### [31/102] `Return_60`

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

**当前代码 (new_code)**
```java
public GremlinPipeline<S, Map<String, Object>> map() {
    return this.add(new PropertyMapPipe());
}
```

**变更前代码 (old_code)**
```java
public T map() {
    return this.add(new PropertyMapPipe());
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public T map() {

+public GremlinPipeline<S, Map<String, Object>> map() {

     return this.add(new PropertyMapPipe());

 }
```

---

### [72/102] `Return_142`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8606 |
| SARI | 0.6667 |
| GLEU | 0.8649 |
| METEOR | 0.9542 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the annotation type string, or null if the supplied destination is null or can't be classified
```

**标准注释 (ground truth)**
```
@return the annotation type value, or null if the supplied destination is null or can't be classified
```

**生成注释 (generated)**
```
@return the annotation type, or null if the supplied destination is null or can't be classified
```

**当前代码 (new_code)**
```java
private Object toTypeAnnotation(JmsDestination destination, boolean useByteValue) {
    if (destination == null) {
        return null;
    }
    if (useByteValue) {
        if (destination.isQueue()) {
            if (destination.isTemporary()) {
                return TEMP_QUEUE_TYPE;
            } else {
                return QUEUE_TYPE;
            }
        } else if (destination.isTopic()) {
            if (destination.isTemporary()) {
                return TEMP_TOPIC_TYPE;
            } else {
                return TOPIC_TYPE;
            }
        }
    } else {
        if (destination.isQueue()) {
            if (destination.isTemporary()) {
                return TEMP_QUEUE_ATTRIBUTES_STRING;
            } else {
                return QUEUE_ATTRIBUTES_STRING;
            }
        } else if (destination.isTopic()) {
            if (destination.isTemporary()) {
                return TEMP_TOPIC_ATTRIBUTES_STRING;
            } else {
                return TOPIC_ATTRIBUTES_STRING;
// ... (truncated)
```

**变更前代码 (old_code)**
```java
private String toTypeAnnotation(JmsDestination destination) {
    if (destination == null) {
        return null;
    }
    if (destination.isQueue()) {
        if (destination.isTemporary()) {
            return TEMP_QUEUE_ATTRIBUTES_STRING;
        } else {
            return QUEUE_ATTRIBUTES_STRING;
        }
    } else if (destination.isTopic()) {
        if (destination.isTemporary()) {
            return TEMP_TOPIC_ATTRIBUTES_STRING;
        } else {
            return TOPIC_ATTRIBUTES_STRING;
        }
    }
    return null;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,18 +1,34 @@
-private String toTypeAnnotation(JmsDestination destination) {

+private Object toTypeAnnotation(JmsDestination destination, boolean useByteValue) {

     if (destination == null) {

         return null;

     }

-    if (destination.isQueue()) {

-        if (destination.isTemporary()) {

-            return TEMP_QUEUE_ATTRIBUTES_STRING;

-        } else {

-            return QUEUE_ATTRIBUTES_STRING;

+    if (useByteValue) {

+        if (destination.isQueue()) {

+            if (destination.isTemporary()) {

+                return TEMP_QUEUE_TYPE;

+            } else {

+                return QUEUE_TYPE;

+            }

+        } else if (destination.isTopic()) {

+            if (destination.isTemporary()) {

+                return TEMP_TOPIC_TYPE;

+            } else {

+                return TOPIC_TYPE;

+            }

         }

-    } else if (destination.isTopic()) {

-        if (destination.isTemporary()) {

-            return TEMP_TOPIC_ATTRIBUTES_STRING;

-        } else {

-            return TOPIC_ATTRIBUTES_STRING;

+    } else {

+        if (destination.isQueue()) {

+            if (destination.isTemporary()) {

+                return TEMP_QUEUE_ATTRIBUTES_STRING;

+            } else {

+                return QUEUE_ATTRIBUTES_STRING;

+            }

+        } else if (destination.isTopic()) {

```

---

### [76/102] `Return_150`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.5353 |
| SARI | 0.6667 |
| GLEU | 0.5652 |
| METEOR | 0.6231 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Window to show in the portlet
```

**标准注释 (ground truth)**
```
@return Window to show in the portlet for the given portlet mode
```

**生成注释 (generated)**
```
@return Window to show in the portlet
```

**当前代码 (new_code)**
```java
protected Window getPortletWindow(PortletRequest request, Application application) {
    PortletMode mode = request.getPortletMode();
    Window window = application.getWindow(mode.toString());
    if (window != null) {
        return window;
    }
    return application.getMainWindow();
}
```

**变更前代码 (old_code)**
```java
protected Window getPortletWindow(PortletRequest request, Application application) {
    PortletMode mode = request.getPortletMode();
    if (PortletMode.VIEW.equals(mode)) {
        return application.getMainWindow();
    } else {
        Window window = application.getWindow(mode.toString());
        if (window != null) {
            return window;
        }
    }
    return application.getMainWindow();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,12 +1,8 @@
 protected Window getPortletWindow(PortletRequest request, Application application) {

     PortletMode mode = request.getPortletMode();

-    if (PortletMode.VIEW.equals(mode)) {

-        return application.getMainWindow();

-    } else {

-        Window window = application.getWindow(mode.toString());

-        if (window != null) {

-            return window;

-        }

+    Window window = application.getWindow(mode.toString());

+    if (window != null) {

+        return window;

     }

     return application.getMainWindow();

 }
```

---

### [81/102] `Return_160`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5738 |
| SARI | 0.6667 |
| GLEU | 0.6226 |
| METEOR | 0.6595 |
| xMatch | ✗ |

**原注释 (source)**
```
@return  true if we are currently paused. The caller might be able to skip some work
```

**标准注释 (ground truth)**
```
@return true if we are currently paused. The caller might be able to skip some work in that case since we will come back again.
```

**生成注释 (generated)**
```
@return true if we are currently paused. The caller might be able to skip some work
```

**当前代码 (new_code)**
```java
    private boolean waitUntilResume(Runnable run, boolean deletePreviousRunnables) {
        if (mPaused) {
            Log.i(TAG, "Deferring update until onResume");
            if (deletePreviousRunnables) {
                while (mBindOnResumeCallbacks.remove(run)) {
                }
            }
            mBindOnResumeCallbacks.add(run);
            return true;
        } else {
            return false;
        }
    }

```

**变更前代码 (old_code)**
```java
    private boolean waitUntilResume(Runnable run) {
        return waitUntilResume(run, false);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,13 @@
-private boolean waitUntilResume(Runnable run) {

-        return waitUntilResume(run, false);

+private boolean waitUntilResume(Runnable run, boolean deletePreviousRunnables) {

+        if (mPaused) {

+            Log.i(TAG, "Deferring update until onResume");

+            if (deletePreviousRunnables) {

+                while (mBindOnResumeCallbacks.remove(run)) {

+                }

+            }

+            mBindOnResumeCallbacks.add(run);

+            return true;

+        } else {

+            return false;

+        }

     }
```

---

### [82/102] `Return_162`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2541 |
| SARI | 0.6667 |
| GLEU | 0.5000 |
| METEOR | 0.9490 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the invoking thread's contention manager
```

**标准注释 (ground truth)**
```
@return the contention manager
```

**生成注释 (generated)**
```
@return the static contention manager
```

**当前代码 (new_code)**
```java
static public ContentionManager getContentionManager() {
    return cm;
}
```

**变更前代码 (old_code)**
```java
static public ContentionManager getContentionManager() {
    ThreadState threadState = BaseTask.getThreadState();
    return threadState.manager();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,3 @@
 static public ContentionManager getContentionManager() {

-    ThreadState threadState = BaseTask.getThreadState();

-    return threadState.manager();

+    return cm;

 }
```

---

### [56/102] `Return_110`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0773 |
| SARI | 0.6778 |
| GLEU | 0.1818 |
| METEOR | 0.5943 |
| xMatch | ✗ |

**原注释 (source)**
```
@return 42.
```

**标准注释 (ground truth)**
```
@return hash code
```

**生成注释 (generated)**
```
@return the calculated hash value.
```

**当前代码 (new_code)**
```java
@Override
public int hashCode() {
    int hash = NUM;
    hash = hash * NUM + Double.valueOf(getRank()).hashCode();
    hash = hash * NUM + mUrlDevice.hashCode();
    hash = hash * NUM + mPwsResult.hashCode();
    return hash;
}
```

**变更前代码 (old_code)**
```java
public int hashCode() {
    assert false : STR;
    return NUM;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,8 @@
+@Override

 public int hashCode() {

-    assert false : STR;

-    return NUM;

+    int hash = NUM;

+    hash = hash * NUM + Double.valueOf(getRank()).hashCode();

+    hash = hash * NUM + mUrlDevice.hashCode();

+    hash = hash * NUM + mPwsResult.hashCode();

+    return hash;

 }
```

---

### [33/102] `Return_64`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5193 |
| SARI | 0.6984 |
| GLEU | 0.5526 |
| METEOR | 0.9729 |
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
@return the time when the work has been accepted.
```

**当前代码 (new_code)**
```java
public synchronized long getAcceptedTime() {
    return acceptedTime;
}
```

**变更前代码 (old_code)**
```java
public synchronized long getAcceptedTime() {
    return m_acceptedTime;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public synchronized long getAcceptedTime() {

-    return m_acceptedTime;

+    return acceptedTime;

 }
```

---

### [13/102] `Return_24`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7419 |
| SARI | 0.7005 |
| GLEU | 0.7632 |
| METEOR | 0.9861 |
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
@return new background color based on the supplied foreground color
```

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
private int invertBgColor() {
    if (currentColor_.defaultColor()) {
        if (!inverted_)
            clazzes_.add(INVERSE_BG_STYLE);
        return Color.DEFAULT_COLOR;
    } else if (currentColor_.code() >= FOREGROUND_MIN && currentColor_.code() <= FOREGROUND_MAX) {
        int newBg = currentColor_.code() + (BACKGROUND_MIN - FOREGROUND_MIN);
        clazzes_.add(BACKGROUND_STYLE + Integer.toString(newBg - BACKGROUND_MIN));
        return newBg;
    } else {
        int newBg = currentColor_.code() + (BACKGROUND_INTENSE_MIN - FOREGROUND_INTENSE_MIN);
        clazzes_.add(BACKGROUND_STYLE + Integer.toString(newBg + NUM - BACKGROUND_INTENSE_MIN));
        return newBg;
    }
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,15 +1,18 @@
-private int invertBgColor() {

+private Color invertBgColor() {

     if (currentColor_.defaultColor()) {

         if (!inverted_)

             clazzes_.add(INVERSE_BG_STYLE);

-        return Color.DEFAULT_COLOR;

+        return new Color();

+    } else if (currentColor_.isExtended()) {

+        clazzes_.add(Color.clazzForColorIndex(currentColor_.code(), true));

+        return new Color(true, currentColor_.code());

     } else if (currentColor_.code() >= FOREGROUND_MIN && currentColor_.code() <= FOREGROUND_MAX) {

         int newBg = currentColor_.code() + (BACKGROUND_MIN - FOREGROUND_MIN);

         clazzes_.add(BACKGROUND_STYLE + Integer.toString(newBg - BACKGROUND_MIN));

-        return newBg;

+        return new Color(false, newBg);

     } else {

         int newBg = currentColor_.code() + (BACKGROUND_INTENSE_MIN - FOREGROUND_INTENSE_MIN);

         clazzes_.add(BACKGROUND_STYLE + Integer.toString(newBg + NUM - BACKGROUND_INTENSE_MIN));

-        return newBg;

+        return new Color(false, newBg);

     }

 }
```

---

### [38/102] `Return_74`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public ObjectName getExchangeObjectName(String virtualHostName, String exchange) {
    AllObjects allObject = new AllObjects(_mbsc);
    allObject.querystring = STR + virtualHostName + STR + exchange + STR;
    Set<ObjectName> objectNames = allObject.returnObjects();
    _test.assertNotNull(STR, objectNames);
    _test.assertEquals(STR + exchange + STR, NUM, objectNames.size());
    return objectNames.iterator().next();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,11 @@
+@SuppressWarnings(STR)

 public ObjectName getExchangeObjectName(String virtualHostName, String exchange) {

     AllObjects allObject = new AllObjects(_mbsc);

     allObject.querystring = STR + virtualHostName + STR + exchange + STR;

     Set<ObjectName> objectNames = allObject.returnObjects();

     _test.assertNotNull(STR, objectNames);

     _test.assertEquals(STR + exchange + STR, NUM, objectNames.size());

-    return objectNames.iterator().next();

+    ObjectName objectName = objectNames.iterator().next();

+    _test.getLogger().info(STR + objectName);

+    return objectName;

 }
```

---

### [17/102] `Return_32`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public static String getLastBaselineBuild() {
    if (BUILDS == null) {
        queryAllVariations(STR);
    }
    return LAST_BASELINE_BUILD;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,20 @@
-public static String getLastBaselineBuild() {

+public static String getLastBaselineBuild(String date) {

     if (BUILDS == null) {

         queryAllVariations(STR);

     }

-    return LAST_BASELINE_BUILD;

+    if (date == null)

+        return LAST_BASELINE_BUILD;

+    String lastBaselineBuild = null;

+    for (int i = NUM; i < BUILDS_LENGTH; i++) {

+        String build = BUILDS[i];

+        if (build.startsWith(AbstractResults.VERSION_REF)) {

+            String buildDate = build.substring(build.indexOf(STR) + NUM);

+            if (buildDate.compareTo(date) < NUM) {

+                if (lastBaselineBuild == null || build.compareTo(lastBaselineBuild) > NUM) {

+                    lastBaselineBuild = build;

+                }

+            }

+        }

+    }

+    return lastBaselineBuild;

 }
```

---

### [7/102] `Return_12`

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

**当前代码 (new_code)**
```java
public boolean isButtonOverflowVisible() {
    return mIsButtonOverflowVisible;
}
```

**变更前代码 (old_code)**
```java
public boolean isButtonOverflowVisible() {
    if (mPopupMenu == NO_POPUP_MENU && mCustomOverflowAnimation == null) {
        if (mIsButtonOverflowVisible)
            Log.w(STR, STR);
        return false;
    }
    return mIsButtonOverflowVisible;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,3 @@
 public boolean isButtonOverflowVisible() {

-    if (mPopupMenu == NO_POPUP_MENU && mCustomOverflowAnimation == null) {

-        if (mIsButtonOverflowVisible)

-            Log.w(STR, STR);

-        return false;

-    }

     return mIsButtonOverflowVisible;

 }
```

---

### [35/102] `Return_68`

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

**当前代码 (new_code)**
```java
public Builder host(String host) {
    this.host = host;
    return this;
}
```

**变更前代码 (old_code)**
```java
public static Builder host(final String host) {
    return builder().host(host);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,4 @@
-public static Builder host(final String host) {

-    return builder().host(host);

+public Builder host(String host) {

+    this.host = host;

+    return this;

 }
```

---

### [54/102] `Return_106`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4111 |
| SARI | 0.7540 |
| GLEU | 0.4545 |
| METEOR | 0.6506 |
| xMatch | ✗ |

**原注释 (source)**
```
@return the wireType
```

**标准注释 (ground truth)**
```
@return the queue wire type
```

**生成注释 (generated)**
```
@return the queue wireType()
```

**当前代码 (new_code)**
```java
public WireType getWireType() {
    return queue.wireType();
}
```

**变更前代码 (old_code)**
```java
public WireType getWireType() {
    return wireType;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public WireType getWireType() {

-    return wireType;

+    return queue.wireType();

 }
```

---

### [26/102] `Return_50`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public static Set<CmdLineOptionInstance> validate(CmdLineArgs cmdLineArgs) {
    Validate.notNull(cmdLineArgs);
    HashSet<CmdLineOptionInstance> optionsFailed = new HashSet<CmdLineOptionInstance>();
    for (CmdLineOptionInstance optionInst : cmdLineArgs.getSpecifiedOptions()) {
        if (!CmdLineUtils.validate(optionInst)) {
            optionsFailed.add(optionInst);
        }
    }
    return optionsFailed;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,10 +1,8 @@
-public static Set<CmdLineOptionInstance> validate(CmdLineArgs cmdLineArgs) {

+public static List<CmdLineOptionValidator.Result> validate(CmdLineArgs cmdLineArgs) {

     Validate.notNull(cmdLineArgs);

-    HashSet<CmdLineOptionInstance> optionsFailed = new HashSet<CmdLineOptionInstance>();

+    List<CmdLineOptionValidator.Result> results = Lists.newArrayList();

     for (CmdLineOptionInstance optionInst : cmdLineArgs.getSpecifiedOptions()) {

-        if (!CmdLineUtils.validate(optionInst)) {

-            optionsFailed.add(optionInst);

-        }

+        results.addAll(CmdLineUtils.validate(optionInst));

     }

-    return optionsFailed;

+    return results;

 }
```

---

### [67/102] `Return_132`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7448 |
| SARI | 0.7826 |
| GLEU | 0.7586 |
| METEOR | 0.9999 |
| xMatch | ✗ |

**原注释 (source)**
```
@return Whether the segments matches (in sense of "be mergable").
```

**标准注释 (ground truth)**
```
@return Whether the ways match (in sense of "be mergable").
```

**生成注释 (generated)**
```
@return Whether the Ways matches (in sense of "be mergable").
```

**当前代码 (new_code)**
```java
private boolean match(Way w1, Way w2) {
    if (w1.id == NUM || w2.id == NUM) {
        if (w1.nodes.size() != w2.nodes.size())
            return false;
        Iterator<Node> it = w1.nodes.iterator();
        for (Node n : w2.nodes) if (!match(n, it.next()))
            return false;
        return true;
    }
    return w1.id == w2.id;
}
```

**变更前代码 (old_code)**
```java
private boolean match(Segment ls1, Segment ls2) {
    if (ls1.id == ls2.id && ls1.id != NUM)
        return true;
    if (ls1.incomplete || ls2.incomplete)
        return false;
    return match(ls1.from, ls2.from) && match(ls1.to, ls2.to);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,11 @@
-private boolean match(Segment ls1, Segment ls2) {

-    if (ls1.id == ls2.id && ls1.id != NUM)

+private boolean match(Way w1, Way w2) {

+    if (w1.id == NUM || w2.id == NUM) {

+        if (w1.nodes.size() != w2.nodes.size())

+            return false;

+        Iterator<Node> it = w1.nodes.iterator();

+        for (Node n : w2.nodes) if (!match(n, it.next()))

+            return false;

         return true;

-    if (ls1.incomplete || ls2.incomplete)

-        return false;

-    return match(ls1.from, ls2.from) && match(ls1.to, ls2.to);

+    }

+    return w1.id == w2.id;

 }
```

---

### [1/102] `Return_0`

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

**当前代码 (new_code)**
```java
public final File getGeneratedOutput() throws CurnException {
    return hasGeneratedOutput() ? outputFile : null;
}
```

**变更前代码 (old_code)**
```java
public final InputStream getGeneratedOutput() throws CurnException {
    InputStream result = null;
    if (hasGeneratedOutput()) {
        try {
            result = new FileInputStream(outputFile);
        } catch (FileNotFoundException ex) {
            throw new CurnException(Curn.BUNDLE_NAME, STR, STR, new Object[] { outputFile }, ex);
        }
    }
    return result;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,3 @@
-public final InputStream getGeneratedOutput() throws CurnException {

-    InputStream result = null;

-    if (hasGeneratedOutput()) {

-        try {

-            result = new FileInputStream(outputFile);

-        } catch (FileNotFoundException ex) {

-            throw new CurnException(Curn.BUNDLE_NAME, STR, STR, new Object[] { outputFile }, ex);

-        }

-    }

-    return result;

+public final File getGeneratedOutput() throws CurnException {

+    return hasGeneratedOutput() ? outputFile : null;

 }
```

---

### [86/102] `Return_170`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5296 |
| SARI | 0.8013 |
| GLEU | 0.5400 |
| METEOR | 0.9422 |
| xMatch | ✗ |

**原注释 (source)**
```
@return A {@link RepositoryMethodMetadataInitializer} corresponding to the method parameter.
```

**标准注释 (ground truth)**
```
@return A {@link RepositoryMethodMetadata}.
```

**生成注释 (generated)**
```
@return A {@link RepositoryMethodMetadata} corresponding to the method parameter.
```

**当前代码 (new_code)**
```java
public RepositoryMethodMetadata lookupMethod(RepositoryMetadata repositoryMetadata, Method method) {
    return repositoryMetadata.getMethodsMetadata().get(method);
}
```

**变更前代码 (old_code)**
```java
public RepositoryMethodMetadata lookupMethod(Class<?> repoClass, Method method) {
    return lookupComponent(repoClass).getMethodsMetadata().get(method);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public RepositoryMethodMetadata lookupMethod(Class<?> repoClass, Method method) {

-    return lookupComponent(repoClass).getMethodsMetadata().get(method);

+public RepositoryMethodMetadata lookupMethod(RepositoryMetadata repositoryMetadata, Method method) {

+    return repositoryMetadata.getMethodsMetadata().get(method);

 }
```

---

### [88/102] `Return_174`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7419 |
| SARI | 0.8125 |
| GLEU | 0.7632 |
| METEOR | 0.9055 |
| xMatch | ✗ |

**原注释 (source)**
```
@return The mouse cursor y position
```

**标准注释 (ground truth)**
```
@return The mouse cursor y position or -1 if unknown
```

**生成注释 (generated)**
```
@return The mouse cursor y position or -NUM if unknown
```

**当前代码 (new_code)**
```java
public int getClientY() {
    if (null != details) {
        return details.getClientY();
    } else {
        return -NUM;
    }
}
```

**变更前代码 (old_code)**
```java
public int getClientY() {
    return details.getClientY();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,7 @@
 public int getClientY() {

-    return details.getClientY();

+    if (null != details) {

+        return details.getClientY();

+    } else {

+        return -NUM;

+    }

 }
```

---

### [3/102] `Return_4`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
    public AsyncSupport newCometSupport(final Class<? extends AsyncSupport> targetClass) {
        try {
            return (AsyncSupport) targetClass.getDeclaredConstructor(new Class[]{AtmosphereConfig.class})
                    .newInstance(config);
        } catch (final Exception e) {
            logger.error("Failed to create comet support class: {}, error: {}", targetClass, e);
            logger.error("Switching to BlockingIO");

            return new BlockingIOCometSupport(config);
        }
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -3,9 +3,7 @@
             return (AsyncSupport) targetClass.getDeclaredConstructor(new Class[]{AtmosphereConfig.class})

                     .newInstance(config);

         } catch (final Exception e) {

-            logger.error("Failed to create comet support class: {}, error: {}", targetClass, e);

-            logger.error("Switching to BlockingIO");

-

-            return new BlockingIOCometSupport(config);

+            logger.warn("Failed to create AsyncSupport class: {}, error: {}", targetClass, e);

+            return null; // All callers are expected to handle null return value

         }

     }
```

---

### [49/102] `Return_96`

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

**当前代码 (new_code)**
```java
  public Sentence cased() {
    return new Sentence(this.docFn, impl.build(), Document.EMPTY_PROPS);
  }

```

**变更前代码 (old_code)**
```java
  public Sentence cased() {
    this.defaultProps = Document.EMPTY_PROPS;
    return this;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,3 @@
 public Sentence cased() {

-    this.defaultProps = Document.EMPTY_PROPS;

-    return this;

+    return new Sentence(this.docFn, impl.build(), Document.EMPTY_PROPS);

   }
```

---

### [61/102] `Return_120`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9999 |
| xMatch | ✓ |

**原注释 (source)**
```
@return an aggregated Account instance representing account data across all the successfully consulted realms.
```

**标准注释 (ground truth)**
```
@return an aggregated AuthenticationInfo instance representing account data across all the successfully consulted realms.
```

**生成注释 (generated)**
```
@return an aggregated AuthenticationInfo instance representing account data across all the successfully consulted realms.
```

**当前代码 (new_code)**
```java
protected AuthenticationInfo doMultiRealmAuthentication(Collection<? extends Realm> realms, AuthenticationToken token) {
    ModularAuthenticationStrategy strategy = getModularAuthenticationStrategy();
    AuthenticationInfo aggregate = strategy.beforeAllAttempts(realms, token);
    if (log.isDebugEnabled()) {
        log.debug(STR + realms.size() + STR);
    }
    for (Realm realm : realms) {
        if (realm.supports(token)) {
            if (log.isDebugEnabled()) {
                log.debug(STR + token + STR + STR + realm + STR);
            }
            AuthenticationInfo info = null;
            Throwable t = null;
            try {
                info = realm.getAuthenticationInfo(token);
            } catch (Throwable throwable) {
                t = throwable;
                if (log.isTraceEnabled()) {
                    String msg = STR + realm + STR;
                    log.trace(msg, t);
                }
            }
            aggregate = strategy.afterAttempt(realm, token, info, aggregate, t);
        } else {
            if (log.isDebugEnabled()) {
                log.debug(STR + realm + STR + STR + token + STR);
            }
        }
    }
    aggregate = strategy.afterAllAttempts(token, aggregate);
// ... (truncated)
```

**变更前代码 (old_code)**
```java
protected Account doMultiRealmAuthentication(Collection<? extends Realm> realms, AuthenticationToken token) {
    ModularAuthenticationStrategy strategy = getModularAuthenticationStrategy();
    Account aggregate = strategy.beforeAllAttempts(realms, token);
    if (log.isDebugEnabled()) {
        log.debug(STR + realms.size() + STR);
    }
    for (Realm realm : realms) {
        if (realm.supports(token)) {
            if (log.isDebugEnabled()) {
                log.debug(STR + token + STR + STR + realm + STR);
            }
            aggregate = strategy.beforeAttempt(realm, token, aggregate);
            Account account = null;
            Throwable t = null;
            try {
                account = realm.getAccount(token);
            } catch (Throwable throwable) {
                t = throwable;
                if (log.isTraceEnabled()) {
                    String msg = STR + realm + STR;
                    log.trace(msg, t);
                }
            }
            aggregate = strategy.afterAttempt(realm, token, account, aggregate, t);
        } else {
            if (log.isDebugEnabled()) {
                log.debug(STR + realm + STR + STR + token + STR);
            }
        }
    }
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
-protected Account doMultiRealmAuthentication(Collection<? extends Realm> realms, AuthenticationToken token) {

+protected AuthenticationInfo doMultiRealmAuthentication(Collection<? extends Realm> realms, AuthenticationToken token) {

     ModularAuthenticationStrategy strategy = getModularAuthenticationStrategy();

-    Account aggregate = strategy.beforeAllAttempts(realms, token);

+    AuthenticationInfo aggregate = strategy.beforeAllAttempts(realms, token);

     if (log.isDebugEnabled()) {

         log.debug(STR + realms.size() + STR);

     }

@@ -9,11 +9,10 @@
             if (log.isDebugEnabled()) {

                 log.debug(STR + token + STR + STR + realm + STR);

             }

-            aggregate = strategy.beforeAttempt(realm, token, aggregate);

-            Account account = null;

+            AuthenticationInfo info = null;

             Throwable t = null;

             try {

-                account = realm.getAccount(token);

+                info = realm.getAuthenticationInfo(token);

             } catch (Throwable throwable) {

                 t = throwable;

                 if (log.isTraceEnabled()) {

@@ -21,7 +20,7 @@
                     log.trace(msg, t);

                 }

             }

-            aggregate = strategy.afterAttempt(realm, token, account, aggregate, t);

+            aggregate = strategy.afterAttempt(realm, token, info, aggregate, t);

         } else {

             if (log.isDebugEnabled()) {

                 log.debug(STR + realm + STR + STR + token + STR);

```

---

### [83/102] `Return_164`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6629 |
| SARI | 0.9461 |
| GLEU | 0.6632 |
| METEOR | 0.9492 |
| xMatch | ✗ |

**原注释 (source)**
```
@return One of the following application running states: {@link IServer#STATE_STARTED}, {@link IServer#STATE_STARTING}, {@link IServer#STATE_STOPPED}, {@link IServer#STATE_STOPPING}, {@link IServer#STATE_UNKNOWN}
```

**标准注释 (ground truth)**
```
@return One of the following application running states: {@link IServer#STATE_STARTED}, {@link IServer#STATE_STOPPED}, {@link IServer#STATE_UNKNOWN}
```

**生成注释 (generated)**
```
@return One of the following application running states: {@link IServer#STATE_STARTED}, {@link IServer#STATE_STARTING}, {@link IServer#STATE_STOPPED}, {@link IServer#STATE_STOPPING}, {@link IServer#STATE_UNKNOWN}
```

**当前代码 (new_code)**
```java
public int track(IProgressMonitor monitor) throws CoreException, OperationCanceledException {
    long currentTime = System.currentTimeMillis();
    long totalTime = currentTime + timeout;
    CloudFoundryServerBehaviour behaviour = cloudServer.getBehaviour();
    String appName = appModule.getDeployedApplicationName();
    printlnToConsole(NLS.bind(Messages.ApplicationInstanceStartingTracker_STARTING_TRACKING, appName), appModule);
    int state = IServer.STATE_UNKNOWN;
    while (state != IServer.STATE_STARTED && state != IServer.STATE_STOPPED && currentTime < totalTime) {
        if (monitor != null && monitor.isCanceled()) {
            String error = NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_CHECK_CANCELED, appName);
            printlnToConsole(error, appModule);
            throw new OperationCanceledException(error);
        }
        CloudApplication cloudApp = behaviour.getCloudApplication(appName, monitor);
        ApplicationStats applicationStats = behaviour.getApplicationStats(appName, monitor);
        if (cloudApp == null) {
            String error = NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_NOT_EXISTS, appName);
            printlnToConsole(error, appModule);
            throw CloudErrorUtil.toCoreException(error);
        } else {
            state = CloudFoundryApplicationModule.getCloudState(cloudApp, applicationStats);
            try {
                Thread.sleep(WAIT_TIME);
            } catch (InterruptedException e) {
            }
            currentTime = System.currentTimeMillis();
        }
    }
    String runningStateMessage = state == IServer.STATE_STARTED ? NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_IS_RUNNING, appName) : NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_IS_NOT_RUNNING, appName);
    printlnToConsole(runningStateMessage, appModule);
// ... (truncated)
```

**变更前代码 (old_code)**
```java
public int track(IProgressMonitor monitor) throws CoreException {
    long currentTime = System.currentTimeMillis();
    long totalTime = currentTime + timeout;
    CloudFoundryApplicationModule appModule = cloudServer.getBehaviour().updateModuleWithAllCloudInfo(appName, monitor);
    printlnToConsole(NLS.bind(Messages.ApplicationInstanceStartingTracker_STARTING_TRACKING, appName), appModule);
    int state = appModule.getState();
    while (state != IServer.STATE_STARTED && state != IServer.STATE_STOPPED && currentTime < totalTime) {
        appModule = cloudServer.getBehaviour().updateModuleWithAllCloudInfo(appName, monitor);
        if (appModule == null || appModule.getApplication() == null) {
            printlnToConsole(NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_NOT_EXISTS, appName), appModule);
            return IServer.STATE_UNKNOWN;
        }
        if (monitor != null && monitor.isCanceled()) {
            printlnToConsole(NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_CHECK_CANCELED, appName), appModule);
            return IServer.STATE_UNKNOWN;
        }
        state = appModule.getState();
        try {
            Thread.sleep(WAIT_TIME);
        } catch (InterruptedException e) {
        }
        currentTime = System.currentTimeMillis();
    }
    String runningStateMessage = state == IServer.STATE_STARTED ? NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_IS_RUNNING, appName) : NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_IS_NOT_RUNNING, appName);
    printlnToConsole(runningStateMessage, appModule);
    return state;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,25 +1,30 @@
-public int track(IProgressMonitor monitor) throws CoreException {

+public int track(IProgressMonitor monitor) throws CoreException, OperationCanceledException {

     long currentTime = System.currentTimeMillis();

     long totalTime = currentTime + timeout;

-    CloudFoundryApplicationModule appModule = cloudServer.getBehaviour().updateModuleWithAllCloudInfo(appName, monitor);

+    CloudFoundryServerBehaviour behaviour = cloudServer.getBehaviour();

+    String appName = appModule.getDeployedApplicationName();

     printlnToConsole(NLS.bind(Messages.ApplicationInstanceStartingTracker_STARTING_TRACKING, appName), appModule);

-    int state = appModule.getState();

+    int state = IServer.STATE_UNKNOWN;

     while (state != IServer.STATE_STARTED && state != IServer.STATE_STOPPED && currentTime < totalTime) {

-        appModule = cloudServer.getBehaviour().updateModuleWithAllCloudInfo(appName, monitor);

-        if (appModule == null || appModule.getApplication() == null) {

-            printlnToConsole(NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_NOT_EXISTS, appName), appModule);

-            return IServer.STATE_UNKNOWN;

+        if (monitor != null && monitor.isCanceled()) {

+            String error = NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_CHECK_CANCELED, appName);

+            printlnToConsole(error, appModule);

+            throw new OperationCanceledException(error);

         }

-        if (monitor != null && monitor.isCanceled()) {

-            printlnToConsole(NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_CHECK_CANCELED, appName), appModule);

-            return IServer.STATE_UNKNOWN;

+        CloudApplication cloudApp = behaviour.getCloudApplication(appName, monitor);

+        ApplicationStats applicationStats = behaviour.getApplicationStats(appName, monitor);

+        if (cloudApp == null) {

+            String error = NLS.bind(Messages.ApplicationInstanceStartingTracker_APPLICATION_NOT_EXISTS, appName);

+            printlnToConsole(error, appModule);

+            throw CloudErrorUtil.toCoreException(error);

+        } else {

+            state = CloudFoundryApplicationModule.getCloudState(cloudApp, applicationStats);

+            try {

+                Thread.sleep(WAIT_TIME);

+            } catch (InterruptedException e) {

+            }

+            currentTime = System.currentTimeMillis();

         }

```

---

### [70/102] `Return_138`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5814 |
| SARI | 0.9621 |
| GLEU | 0.6176 |
| METEOR | 0.9883 |
| xMatch | ✗ |

**原注释 (source)**
```
@return The naemspace URI mapped to the prefix.
```

**标准注释 (ground truth)**
```
@return the namespace URI mapped to the prefix
```

**生成注释 (generated)**
```
@return The namespace URI mapped to the prefix.
```

**当前代码 (new_code)**
```java
public String translateNamespacePrefixToUri(String prefix) {
    if (STR.equals(prefix)) {
        return STR;
    }
    NamespaceContext context = getNamespaceContext();
    if (context != null) {
        return context.translateNamespacePrefixToUri(prefix);
    }
    return null;
}
```

**变更前代码 (old_code)**
```java
public String translateNamespacePrefixToUri(String prefix) {
    NamespaceContext context = getNamespaceContext();
    if (context != null) {
        return context.translateNamespacePrefixToUri(prefix);
    }
    return null;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,7 @@
 public String translateNamespacePrefixToUri(String prefix) {

+    if (STR.equals(prefix)) {

+        return STR;

+    }

     NamespaceContext context = getNamespaceContext();

     if (context != null) {

         return context.translateNamespacePrefixToUri(prefix);

```

---

### [4/102] `Return_6`

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

**当前代码 (new_code)**
```java
public TwitterTokenStream getDefaultTokenStream() {
    return tokenizationStream;
}
```

**变更前代码 (old_code)**
```java
public TokenStream getDefaultTokenStream() {
    return tokenizationStream;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public TokenStream getDefaultTokenStream() {

+public TwitterTokenStream getDefaultTokenStream() {

     return tokenizationStream;

 }
```

---

### [6/102] `Return_10`

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

**当前代码 (new_code)**
```java
public static ModuleConfig getModuleConfig(HttpServletRequest request, ServletContext context) {
    ModuleConfig moduleConfig = (ModuleConfig) request.getAttribute(Globals.MODULE_KEY);
    if (moduleConfig == null) {
        moduleConfig = (ModuleConfig) context.getAttribute(Globals.MODULE_KEY);
    }
    return moduleConfig;
}
```

**变更前代码 (old_code)**
```java
public static ApplicationConfig getModuleConfig(HttpServletRequest request, ServletContext context) {
    ApplicationConfig appConfig = (ApplicationConfig) request.getAttribute(Globals.MODULE_KEY);
    if (appConfig == null) {
        appConfig = (ApplicationConfig) context.getAttribute(Globals.MODULE_KEY);
    }
    return appConfig;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,7 @@
-public static ApplicationConfig getModuleConfig(HttpServletRequest request, ServletContext context) {

-    ApplicationConfig appConfig = (ApplicationConfig) request.getAttribute(Globals.MODULE_KEY);

-    if (appConfig == null) {

-        appConfig = (ApplicationConfig) context.getAttribute(Globals.MODULE_KEY);

+public static ModuleConfig getModuleConfig(HttpServletRequest request, ServletContext context) {

+    ModuleConfig moduleConfig = (ModuleConfig) request.getAttribute(Globals.MODULE_KEY);

+    if (moduleConfig == null) {

+        moduleConfig = (ModuleConfig) context.getAttribute(Globals.MODULE_KEY);

     }

-    return appConfig;

+    return moduleConfig;

 }
```

---

### [15/102] `Return_28`

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

**当前代码 (new_code)**
```java
public final AudioInputStream getSoundChallenge() {
    return this.challenge;
}
```

**变更前代码 (old_code)**
```java
public final Sound getSoundChallenge() {
    return this.challenge;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public final Sound getSoundChallenge() {

+public final AudioInputStream getSoundChallenge() {

     return this.challenge;

 }
```

---

### [19/102] `Return_36`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
  public List<I> joinWithTimeout() {
    if (timeout < 0) {
      join();
      return null;
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

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,7 @@
 public List<I> joinWithTimeout() {

     if (timeout < 0) {

       join();

-      return null;

+      return new ArrayList<>();

     }

     // Make blocking calls to the last processes that are running

     if ( ! threadPool.isShutdown()) {

@@ -31,5 +31,5 @@
         throw new RuntimeInterruptedException(e);

       }

     }

-    return null;

+    return new ArrayList<>();

   }
```

---

### [20/102] `Return_38`

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

**当前代码 (new_code)**
```java
protected final Iterator<SyntaxTreeNode> elements() {
    return _contents.iterator();
}
```

**变更前代码 (old_code)**
```java
protected final Enumeration elements() {
    return _contents.elements();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-protected final Enumeration elements() {

-    return _contents.elements();

+protected final Iterator<SyntaxTreeNode> elements() {

+    return _contents.iterator();

 }
```

---

### [23/102] `Return_44`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public static Hashtable getXmlRpcWorkflowInstancePage(WorkflowInstancePage page) {
    Hashtable pageHash = new Hashtable();
    pageHash.put(STR, String.valueOf(page.getTotalPages()));
    pageHash.put(STR, String.valueOf(page.getPageNum()));
    pageHash.put(STR, String.valueOf(page.getPageSize()));
    pageHash.put(STR, getXmlRpcWorkflowInstances(page.getPageWorkflows()));
    return pageHash;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public static Hashtable getXmlRpcWorkflowInstancePage(WorkflowInstancePage page) {

-    Hashtable pageHash = new Hashtable();

+public static HashMap getXmlRpcWorkflowInstancePage(WorkflowInstancePage page) {

+    HashMap pageHash = new HashMap();

     pageHash.put(STR, String.valueOf(page.getTotalPages()));

     pageHash.put(STR, String.valueOf(page.getPageNum()));

     pageHash.put(STR, String.valueOf(page.getPageSize()));

```

---

### [25/102] `Return_48`

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
@return URL with query params
```

**标准注释 (ground truth)**
```
@return URL with appended query params
```

**生成注释 (generated)**
```
@return URL with appended query params
```

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
@SuppressWarnings(STR)
public static String append(String url, final Map<String, ?> params) {
    if (params == null || params.isEmpty())
        return url;
    StringBuilder result = new StringBuilder();
    if (!url.endsWith(STR))
        url += STR;
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
    return url + STR + result.toString();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,10 +1,13 @@
 @SuppressWarnings(STR)

-public static String append(String url, final Map<String, ?> params) {

+public static String append(final String url, final Map<String, ?> params) {

     if (params == null || params.isEmpty())

         return url;

-    StringBuilder result = new StringBuilder();

-    if (!url.endsWith(STR))

-        url += STR;

+    final StringBuilder result = new StringBuilder(url);

+    int firstColon = url.indexOf(STR);

+    int lastSlash = url.lastIndexOf(STR);

+    if (firstColon + NUM == lastSlash)

+        result.append(STR);

+    result.append(STR);

     Entry<String, ?> entry;

     Object value;

     Iterator<?> iterator = params.entrySet().iterator();

@@ -23,5 +26,5 @@
         if (value != null)

             result.append(value);

     }

-    return url + STR + result.toString();

+    return result.toString();

 }
```

---

### [27/102] `Return_52`

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

**当前代码 (new_code)**
```java
public ModuleJarClassLoader getLoader() {
    return loader;
}
```

**变更前代码 (old_code)**
```java
public ModuleClassLoader getLoader() {
    return loader;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public ModuleClassLoader getLoader() {

+public ModuleJarClassLoader getLoader() {

     return loader;

 }
```

---

### [36/102] `Return_70`

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

**当前代码 (new_code)**
```java
public ProcessingInstruction createProcessingInstruction(String target, String data) throws DOMException {
    if (STR.equals(target)) {
        return new SVGStyleSheetProcessingInstruction(data, this, (StyleSheetFactory) getImplementation());
    }
    return new GenericProcessingInstruction(target, data, this);
}
```

**变更前代码 (old_code)**
```java
public ProcessingInstruction createProcessingInstruction(String target, String data) throws DOMException {
    if (STR.equals(target)) {
        return new StyleSheetProcessingInstruction(data, this, (StyleSheetFactory) getImplementation());
    }
    return new GenericProcessingInstruction(target, data, this);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
 public ProcessingInstruction createProcessingInstruction(String target, String data) throws DOMException {

     if (STR.equals(target)) {

-        return new StyleSheetProcessingInstruction(data, this, (StyleSheetFactory) getImplementation());

+        return new SVGStyleSheetProcessingInstruction(data, this, (StyleSheetFactory) getImplementation());

     }

     return new GenericProcessingInstruction(target, data, this);

 }
```

---

### [37/102] `Return_72`

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

**当前代码 (new_code)**
```java
public long getId() {
    return id;
}
```

**变更前代码 (old_code)**
```java
public long getId() {
    return id_category;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public long getId() {

-    return id_category;

+    return id;

 }
```

---

### [40/102] `Return_78`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public static char[] union(char[] c1, char[] c2) {
    StringBuilder sb = new StringBuilder();
    for (int i = NUM; i < c1.length; i++) {
        if (!contains(sb, c1[i]))
            sb.append(c1[i]);
    }
    for (int i = NUM; i < c2.length; i++) {
        if (!contains(sb, c2[i]))
            sb.append(c2[i]);
    }
    char[] c3 = new char[sb.length()];
    sb.getChars(NUM, sb.length(), c3, NUM);
    Arrays.sort(c3);
    return c3;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,15 +1,13 @@
-public static char[] union(char[] c1, char[] c2) {

+public static char[] union(char[]... list) {

     StringBuilder sb = new StringBuilder();

-    for (int i = NUM; i < c1.length; i++) {

-        if (!contains(sb, c1[i]))

-            sb.append(c1[i]);

+    for (char[] characters : list) {

+        for (int i = NUM; i < list.length; i++) {

+            if (!contains(sb, characters[i]))

+                sb.append(list[i]);

+        }

     }

-    for (int i = NUM; i < c2.length; i++) {

-        if (!contains(sb, c2[i]))

-            sb.append(c2[i]);

-    }

-    char[] c3 = new char[sb.length()];

-    sb.getChars(NUM, sb.length(), c3, NUM);

-    Arrays.sort(c3);

-    return c3;

+    char[] toReturn = new char[sb.length()];

+    sb.getChars(NUM, sb.length(), toReturn, NUM);

+    Arrays.sort(toReturn);

+    return toReturn;

 }
```

---

### [41/102] `Return_80`

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

-    return createFeatureService(defaultServerUrl);

+    return createFeatureService(defaultEndpointUrl);

 }
```

---

### [42/102] `Return_82`

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

**当前代码 (new_code)**
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

**变更前代码 (old_code)**
```java
public static HornetQConnectionFactory createConnectionFactoryWithoutHA(JMSFactoryType jmsFactoryType, final TransportConfiguration... transportConfigurations) {
    HornetQConnectionFactory factory = null;
    if (jmsFactoryType.equals(JMSFactoryType.CF)) {
        factory = new HornetQJMSConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.QUEUE_CF)) {
        factory = new HornetQQueueConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.TOPIC_CF)) {
        factory = new HornetQTopicConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.XA_CF)) {
        factory = new HornetQXAConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.QUEUE_XA_CF)) {
        factory = new HornetQXAQueueConnectionFactory(false, transportConfigurations);
    } else if (jmsFactoryType.equals(JMSFactoryType.TOPIC_XA_CF)) {
        factory = new HornetQXATopicConnectionFactory(false, transportConfigurations);
    }
    return factory;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,17 +1,17 @@
-public static HornetQConnectionFactory createConnectionFactoryWithoutHA(JMSFactoryType jmsFactoryType, final TransportConfiguration... transportConfigurations) {

-    HornetQConnectionFactory factory = null;

+public static ActiveMQConnectionFactory createConnectionFactoryWithoutHA(JMSFactoryType jmsFactoryType, final TransportConfiguration... transportConfigurations) {

+    ActiveMQConnectionFactory factory = null;

     if (jmsFactoryType.equals(JMSFactoryType.CF)) {

-        factory = new HornetQJMSConnectionFactory(false, transportConfigurations);

+        factory = new ActiveMQJMSConnectionFactory(false, transportConfigurations);

     } else if (jmsFactoryType.equals(JMSFactoryType.QUEUE_CF)) {

-        factory = new HornetQQueueConnectionFactory(false, transportConfigurations);

+        factory = new ActiveMQQueueConnectionFactory(false, transportConfigurations);

     } else if (jmsFactoryType.equals(JMSFactoryType.TOPIC_CF)) {

-        factory = new HornetQTopicConnectionFactory(false, transportConfigurations);

+        factory = new ActiveMQTopicConnectionFactory(false, transportConfigurations);

     } else if (jmsFactoryType.equals(JMSFactoryType.XA_CF)) {

-        factory = new HornetQXAConnectionFactory(false, transportConfigurations);

+        factory = new ActiveMQXAConnectionFactory(false, transportConfigurations);

     } else if (jmsFactoryType.equals(JMSFactoryType.QUEUE_XA_CF)) {

-        factory = new HornetQXAQueueConnectionFactory(false, transportConfigurations);

+        factory = new ActiveMQXAQueueConnectionFactory(false, transportConfigurations);

     } else if (jmsFactoryType.equals(JMSFactoryType.TOPIC_XA_CF)) {

-        factory = new HornetQXATopicConnectionFactory(false, transportConfigurations);

+        factory = new ActiveMQXATopicConnectionFactory(false, transportConfigurations);

     }

     return factory;

 }
```

---

### [51/102] `Return_100`

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

**当前代码 (new_code)**
```java
public AtmosphereRequest getRequest() {
    return atmosphereRequest;
}
```

**变更前代码 (old_code)**
```java
public HttpServletRequest getRequest() {
    return atmosphereRequest;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public HttpServletRequest getRequest() {

+public AtmosphereRequest getRequest() {

     return atmosphereRequest;

 }
```

---

### [57/102] `Return_112`

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
@return the ScopeContext for the MODULE scope that will be associated with this deployment unit
```

**标准注释 (ground truth)**
```
@return the ScopeContainer for the MODULE scope that will be associated with this deployment unit
```

**生成注释 (generated)**
```
@return the ScopeContainer for the MODULE scope that will be associated with this deployment unit
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

### [59/102] `Return_116`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8154 |
| SARI | 1.0000 |
| GLEU | 0.8276 |
| METEOR | 0.9999 |
| xMatch | ✗ |

**原注释 (source)**
```
@return StringBuffer filled with the penn treebank forms of all trees in the matches panel
```

**标准注释 (ground truth)**
```
@return String filled with the Penn treebank forms of all trees in the matches panel
```

**生成注释 (generated)**
```
@return String filled with the penn treebank forms of all trees in the matches panel
```

**当前代码 (new_code)**
```java
public String getMatches() {
    StringBuilder sb = new StringBuilder();
    for (int i = NUM, sz = list.getModel().getSize(); i < sz; i++) {
        Tree t = ((TreeFromFile) list.getModel().getElementAt(i)).getTree();
        sb.append(t.pennString());
        sb.append(STR);
    }
    return sb.toString();
}
```

**变更前代码 (old_code)**
```java
public StringBuffer getMatches() {
    StringBuffer sb = new StringBuffer();
    for (int i = NUM; i < list.getModel().getSize(); i++) {
        Tree t = ((TreeFromFile) list.getModel().getElementAt(i)).getTree();
        sb.append(t.pennString());
        sb.append(STR);
    }
    return sb;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,9 @@
-public StringBuffer getMatches() {

-    StringBuffer sb = new StringBuffer();

-    for (int i = NUM; i < list.getModel().getSize(); i++) {

+public String getMatches() {

+    StringBuilder sb = new StringBuilder();

+    for (int i = NUM, sz = list.getModel().getSize(); i < sz; i++) {

         Tree t = ((TreeFromFile) list.getModel().getElementAt(i)).getTree();

         sb.append(t.pennString());

         sb.append(STR);

     }

-    return sb;

+    return sb.toString();

 }
```

---

### [60/102] `Return_118`

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
@return the new PartitionMetaData
```

**标准注释 (ground truth)**
```
@return the new PartitionTemplate
```

**生成注释 (generated)**
```
@return the new PartitionTemplate
```

**当前代码 (new_code)**
```java
private PartitionTemplate assembleSar(final String name, final Configuration config, final Configuration assembly) throws LoomException {
    final Configuration[] blockConfig = assembly.getChildren(STR);
    final ComponentTemplate[] blocks = buildBlocks(blockConfig, config);
    final PartitionTemplate blockPartition = new PartitionTemplate(ContainerConstants.BLOCK_PARTITION, new String[] { ContainerConstants.LISTENER_PARTITION }, PartitionTemplate.EMPTY_SET, blocks);
    final Configuration[] listenerConfig = assembly.getChildren(STR);
    final ComponentTemplate[] listeners = buildBlockListeners(listenerConfig, config);
    final PartitionTemplate listenerPartition = new PartitionTemplate(ContainerConstants.LISTENER_PARTITION, new String[NUM], PartitionTemplate.EMPTY_SET, listeners);
    final PartitionTemplate[] partitions = new PartitionTemplate[] { blockPartition, listenerPartition };
    return new PartitionTemplate(name, new String[NUM], partitions, ComponentTemplate.EMPTY_SET);
}
```

**变更前代码 (old_code)**
```java
private PartitionMetaData assembleSar(final String name, final Configuration config, final Configuration assembly) throws LoomException {
    final Configuration[] blockConfig = assembly.getChildren(STR);
    final ComponentMetaData[] blocks = buildBlocks(blockConfig, config);
    final PartitionMetaData blockPartition = new PartitionMetaData(ContainerConstants.BLOCK_PARTITION, new String[] { ContainerConstants.LISTENER_PARTITION }, PartitionMetaData.EMPTY_SET, blocks);
    final Configuration[] listenerConfig = assembly.getChildren(STR);
    final ComponentMetaData[] listeners = buildBlockListeners(listenerConfig, config);
    final PartitionMetaData listenerPartition = new PartitionMetaData(ContainerConstants.LISTENER_PARTITION, new String[NUM], PartitionMetaData.EMPTY_SET, listeners);
    final PartitionMetaData[] partitions = new PartitionMetaData[] { blockPartition, listenerPartition };
    return new PartitionMetaData(name, new String[NUM], partitions, ComponentMetaData.EMPTY_SET);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,10 +1,10 @@
-private PartitionMetaData assembleSar(final String name, final Configuration config, final Configuration assembly) throws LoomException {

+private PartitionTemplate assembleSar(final String name, final Configuration config, final Configuration assembly) throws LoomException {

     final Configuration[] blockConfig = assembly.getChildren(STR);

-    final ComponentMetaData[] blocks = buildBlocks(blockConfig, config);

-    final PartitionMetaData blockPartition = new PartitionMetaData(ContainerConstants.BLOCK_PARTITION, new String[] { ContainerConstants.LISTENER_PARTITION }, PartitionMetaData.EMPTY_SET, blocks);

+    final ComponentTemplate[] blocks = buildBlocks(blockConfig, config);

+    final PartitionTemplate blockPartition = new PartitionTemplate(ContainerConstants.BLOCK_PARTITION, new String[] { ContainerConstants.LISTENER_PARTITION }, PartitionTemplate.EMPTY_SET, blocks);

     final Configuration[] listenerConfig = assembly.getChildren(STR);

-    final ComponentMetaData[] listeners = buildBlockListeners(listenerConfig, config);

-    final PartitionMetaData listenerPartition = new PartitionMetaData(ContainerConstants.LISTENER_PARTITION, new String[NUM], PartitionMetaData.EMPTY_SET, listeners);

-    final PartitionMetaData[] partitions = new PartitionMetaData[] { blockPartition, listenerPartition };

-    return new PartitionMetaData(name, new String[NUM], partitions, ComponentMetaData.EMPTY_SET);

+    final ComponentTemplate[] listeners = buildBlockListeners(listenerConfig, config);

+    final PartitionTemplate listenerPartition = new PartitionTemplate(ContainerConstants.LISTENER_PARTITION, new String[NUM], PartitionTemplate.EMPTY_SET, listeners);

+    final PartitionTemplate[] partitions = new PartitionTemplate[] { blockPartition, listenerPartition };

+    return new PartitionTemplate(name, new String[NUM], partitions, ComponentTemplate.EMPTY_SET);

 }
```

---

### [78/102] `Return_154`

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
@return WSDL <code>Document</code>
```

**标准注释 (ground truth)**
```
@return WSDL <code>Definition</code>
```

**生成注释 (generated)**
```
@return WSDL <code>Definition</code>
```

**当前代码 (new_code)**
```java
public Definition emit(Class cls, String allowedMethods) throws Exception {
    this.cls = cls;
    this.allowedMethods = allowedMethods;
    String name = cls.getName();
    name = name.substring(name.lastIndexOf(STR) + NUM);
    setServiceName(name);
    return emit();
}
```

**变更前代码 (old_code)**
```java
public Document emit(Class cls, String allowedMethods) throws Exception {
    this.cls = cls;
    this.allowedMethods = allowedMethods;
    String name = cls.getName();
    name = name.substring(name.lastIndexOf(STR) + NUM);
    setServiceName(name);
    return emit();
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Document emit(Class cls, String allowedMethods) throws Exception {

+public Definition emit(Class cls, String allowedMethods) throws Exception {

     this.cls = cls;

     this.allowedMethods = allowedMethods;

     String name = cls.getName();

```

---

### [87/102] `Return_172`

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
@return A {@link Hashtable} representation of a {@link Workflow}.
```

**标准注释 (ground truth)**
```
@return A {@link HashMap} representation of a {@link Workflow}.
```

**生成注释 (generated)**
```
@return A {@link HashMap} representation of a {@link Workflow}.
```

**当前代码 (new_code)**
```java
public static HashMap getXmlRpcWorkflow(Workflow w) {
    HashMap workflow = new HashMap();
    workflow.put(STR, w.getId());
    workflow.put(STR, w.getName() != null ? w.getName() : STR);
    workflow.put(STR, getXmlRpcWorkflowTasks(w.getTasks()));
    workflow.put(STR, getXmlRpcWorkflowConditions(w.getConditions()));
    return workflow;
}
```

**变更前代码 (old_code)**
```java
public static Hashtable getXmlRpcWorkflow(Workflow w) {
    Hashtable workflow = new Hashtable();
    workflow.put(STR, w.getId());
    workflow.put(STR, w.getName() != null ? w.getName() : STR);
    workflow.put(STR, getXmlRpcWorkflowTasks(w.getTasks()));
    workflow.put(STR, getXmlRpcWorkflowConditions(w.getConditions()));
    return workflow;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public static Hashtable getXmlRpcWorkflow(Workflow w) {

-    Hashtable workflow = new Hashtable();

+public static HashMap getXmlRpcWorkflow(Workflow w) {

+    HashMap workflow = new HashMap();

     workflow.put(STR, w.getId());

     workflow.put(STR, w.getName() != null ? w.getName() : STR);

     workflow.put(STR, getXmlRpcWorkflowTasks(w.getTasks()));

```

---

### [89/102] `Return_176`

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
@return the list of Cassandra instances
```

**标准注释 (ground truth)**
```
@return the set of Cassandra instances
```

**生成注释 (generated)**
```
@return the set of Cassandra instances
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

-public List<CassandraInstance> findAll() {

+public Set<CassandraInstance> findAll() {

     return service.findAll();

 }
```

---

### [91/102] `Return_180`

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
@return string array of misspelt words
```

**标准注释 (ground truth)**
```
@return string array of misspelled words
```

**生成注释 (generated)**
```
@return string array of misspelled words
```

**当前代码 (new_code)**
```java
public String[] checkAllWords(String words) {
    List<String> misspelledWords = new ArrayList<String>();
    StringWordTokenizer tokenizer = new StringWordTokenizer(words);
    while (tokenizer.hasMoreWords()) {
        String word = tokenizer.nextWord();
        if (!isWordCorrect(word, tokenizer.isNewSentence())) {
            misspelledWords.add(word);
        }
    }
    return misspelledWords.toArray(new String[NUM]);
}
```

**变更前代码 (old_code)**
```java
public String[] checkAllWords(String words) {
    List<String> misspeltWords = new ArrayList<String>();
    StringWordTokenizer tokenizer = new StringWordTokenizer(words);
    while (tokenizer.hasMoreWords()) {
        String word = tokenizer.nextWord();
        if (!isWordCorrect(word, tokenizer.isNewSentence())) {
            misspeltWords.add(word);
        }
    }
    return misspeltWords.toArray(new String[NUM]);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,11 @@
 public String[] checkAllWords(String words) {

-    List<String> misspeltWords = new ArrayList<String>();

+    List<String> misspelledWords = new ArrayList<String>();

     StringWordTokenizer tokenizer = new StringWordTokenizer(words);

     while (tokenizer.hasMoreWords()) {

         String word = tokenizer.nextWord();

         if (!isWordCorrect(word, tokenizer.isNewSentence())) {

-            misspeltWords.add(word);

+            misspelledWords.add(word);

         }

     }

-    return misspeltWords.toArray(new String[NUM]);

+    return misspelledWords.toArray(new String[NUM]);

 }
```

---

### [92/102] `Return_182`

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
@return a {@link UserSpinnerAdapter} or null if there is only one profile.
```

**标准注释 (ground truth)**
```
@return a {@link UserAdapter} or null if there is only one profile.
```

**生成注释 (generated)**
```
@return a {@link UserAdapter} or null if there is only one profile.
```

**当前代码 (new_code)**
```java
public static UserAdapter createUserSpinnerAdapter(UserManager userManager, Context context) {
    List<UserHandle> userProfiles = userManager.getUserProfiles();
    if (userProfiles.size() < NUM) {
        return null;
    }
    UserHandle myUserHandle = new UserHandle(UserHandle.myUserId());
    userProfiles.remove(myUserHandle);
    userProfiles.add(NUM, myUserHandle);
    return createUserAdapter(userManager, context, userProfiles);
}
```

**变更前代码 (old_code)**
```java
public static UserSpinnerAdapter createUserSpinnerAdapter(UserManager userManager, Context context) {
    List<UserHandle> userProfiles = userManager.getUserProfiles();
    if (userProfiles.size() < NUM) {
        return null;
    }
    UserHandle myUserHandle = new UserHandle(UserHandle.myUserId());
    userProfiles.remove(myUserHandle);
    userProfiles.add(NUM, myUserHandle);
    ArrayList<UserDetails> userDetails = new ArrayList<UserDetails>(userProfiles.size());
    final int count = userProfiles.size();
    for (int i = NUM; i < count; i++) {
        userDetails.add(new UserDetails(userProfiles.get(i), userManager, context));
    }
    return new UserSpinnerAdapter(context, userDetails);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public static UserSpinnerAdapter createUserSpinnerAdapter(UserManager userManager, Context context) {

+public static UserAdapter createUserSpinnerAdapter(UserManager userManager, Context context) {

     List<UserHandle> userProfiles = userManager.getUserProfiles();

     if (userProfiles.size() < NUM) {

         return null;

@@ -6,10 +6,5 @@
     UserHandle myUserHandle = new UserHandle(UserHandle.myUserId());

     userProfiles.remove(myUserHandle);

     userProfiles.add(NUM, myUserHandle);

-    ArrayList<UserDetails> userDetails = new ArrayList<UserDetails>(userProfiles.size());

-    final int count = userProfiles.size();

-    for (int i = NUM; i < count; i++) {

-        userDetails.add(new UserDetails(userProfiles.get(i), userManager, context));

-    }

-    return new UserSpinnerAdapter(context, userDetails);

+    return createUserAdapter(userManager, context, userProfiles);

 }
```

---

### [99/102] `Return_196`

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
@return the GraphItem located at the given point, if any
```

**标准注释 (ground truth)**
```
@return the VisualItem located at the given point, if any
```

**生成注释 (generated)**
```
@return the VisualItem located at the given point, if any
```

**当前代码 (new_code)**
```java
public VisualItem findItem(Point p) {
    Point2D p2 = (m_itransform == null ? p : m_itransform.transform(p, m_tmpPoint));
    synchronized (m_registry) {
        Iterator items = m_registry.getItemsReversed();
        while (items.hasNext()) {
            VisualItem vi = (VisualItem) items.next();
            Renderer r = vi.getRenderer();
            if (r != null && r.locatePoint(p2, vi)) {
                return vi;
            }
        }
    }
    return null;
}
```

**变更前代码 (old_code)**
```java
public GraphItem findItem(Point p) {
    Point2D p2 = (m_itransform == null ? p : m_itransform.transform(p, m_tmpPoint));
    synchronized (m_registry) {
        Iterator items = m_registry.getItemsReversed();
        while (items.hasNext()) {
            GraphItem gi = (GraphItem) items.next();
            Renderer r = gi.getRenderer();
            if (r != null && r.locatePoint(p2, gi)) {
                return gi;
            }
        }
    }
    return null;
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,12 +1,12 @@
-public GraphItem findItem(Point p) {

+public VisualItem findItem(Point p) {

     Point2D p2 = (m_itransform == null ? p : m_itransform.transform(p, m_tmpPoint));

     synchronized (m_registry) {

         Iterator items = m_registry.getItemsReversed();

         while (items.hasNext()) {

-            GraphItem gi = (GraphItem) items.next();

-            Renderer r = gi.getRenderer();

-            if (r != null && r.locatePoint(p2, gi)) {

-                return gi;

+            VisualItem vi = (VisualItem) items.next();

+            Renderer r = vi.getRenderer();

+            if (r != null && r.locatePoint(p2, vi)) {

+                return vi;

             }

         }

     }

```

---

### [100/102] `Return_198`

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
@return a new variation service with the default server URL
```

**标准注释 (ground truth)**
```
@return a new variation service with the default endpoint URL
```

**生成注释 (generated)**
```
@return a new variation service with the default endpoint URL
```

**当前代码 (new_code)**
```java
public VariationService createVariationService() {
    return createVariationService(defaultEndpointUrl);
}
```

**变更前代码 (old_code)**
```java
public VariationService createVariationService() {
    return createVariationService(defaultServerUrl);
}
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public VariationService createVariationService() {

-    return createVariationService(defaultServerUrl);

+    return createVariationService(defaultEndpointUrl);

 }
```

---

### [101/102] `Return_200`

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
@return A {@link Ravioli}
```

**标准注释 (ground truth)**
```
@return A {@link Lob}
```

**生成注释 (generated)**
```
@return A {@link Lob}
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

-    return new Ravioli(this);

+public Lob build() {

+    return new Lob(this);

 }
```

---

