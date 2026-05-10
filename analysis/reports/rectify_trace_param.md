# Rectifier 逐样本追踪报告

## 汇总指标

- **xMatch (%)**: 44.12
- **BLEU-4**: 0.6805
- **GLEU**: 0.7395
- **Meteor**: 0.8306
- **SARI**: 0.808
- **Samples_Evaluated**: 102

## 汇总一览（按 SARI 升序，最差排前）

| # | ID | 检测到 | xMatch | BLEU-4 | SARI | METEOR | 原注释(前60) | 生成(前60) |
|---|---|---|---|---|---|---|---|---|
| 1 | `Param_171` | ✓ |  | 0.186 | 0.232 | 0.363 | @param regex the text to search for. The parameter will be i | @param text the parameter. The parameter is currently unused |
| 2 | `Param_97` | ✓ |  | 0.037 | 0.309 | 0.198 | @param id The identifier of the entity currently demanding l | @param collectionKey The identifier of the collection curren |
| 3 | `Param_157` | ✓ |  | 0.054 | 0.368 | 0.418 | @param element an int specifying an element in the path, whe | @param index an int specifying an element in the path, where |
| 4 | `Param_46` | ✓ |  | 0.217 | 0.386 | 0.526 | @param model Swagger Model object | @param model Swagger Schema object |
| 5 | `Param_54` | ✓ |  | 0.087 | 0.427 | 0.624 | @param context the annotation binding context with access to | @param bindingContext the annotation binding context with ac |
| 6 | `Param_119` | ✓ |  | 0.067 | 0.438 | 0.188 | @param  The type of the element we are getting. | @param selector The type of the element we are getting. |
| 7 | `Param_145` | ✓ |  | 0.311 | 0.455 | 0.476 | @param simplify Whether to simplify (in addition to normaliz | @param simplify The simplification (in addition to normalizi |
| 8 | `Param_133` | ✗(漏检) |  | 0.212 | 0.455 | 0.601 | @param node the tree corresponding to a use of an element | @param node the tree corresponding to a use of an element |
| 9 | `Param_83` | ✓ |  | 0.161 | 0.463 | 0.750 | @param call Extract expression | @param call Extract expression |
| 10 | `Param_192` | ✓ |  | 0.424 | 0.488 | 0.647 | @param driver The driver to enhance | @param element The element to enhance |
| 11 | `Param_188` | ✗(漏检) |  | 0.290 | 0.493 | 0.666 | @param persister The persister for the entities being loaded | @param persister The persister for the entities being loaded |
| 12 | `Param_18` | ✓ |  | 0.174 | 0.543 | 0.539 | @param urlPattern the URL pattern for requests that should b | @param klass the class for requests that should be handled b |
| 13 | `Param_155` | ✓ |  | 0.065 | 0.562 | 0.360 | @param methods the methods to match against | @param implClass the class containing the method |
| 14 | `Param_121` | ✓ |  | 0.346 | 0.584 | 0.640 | @param dialect The dialect in effect. | @param jdbcEnvironment The dialect in effect. |
| 15 | `Param_206` | ✓ |  | 0.669 | 0.601 | 0.794 | @param request the  HttpServletRequest | @param request the  HttpServletRequest |
| 16 | `Param_85` | ✗(漏检) |  | 0.661 | 0.602 | 0.882 | @param file file to upload (required) | @param file file to upload (required) |
| 17 | `Param_87` | ✗(漏检) |  | 0.661 | 0.602 | 0.882 | @param file file to upload (required) | @param file file to upload (required) |
| 18 | `Param_66` | ✓ |  | 0.158 | 0.602 | 0.257 | @param str the input string | @param parts the input string |
| 19 | `Param_181` | ✗(漏检) |  | 0.735 | 0.616 | 0.914 | @param allDefinitions a map of all Swagger models from the s | @param allDefinitions a map of all Swagger models from the s |
| 20 | `Param_175` | ✗(漏检) |  | 0.761 | 0.621 | 0.921 | @param t Target for finding dependents of t related by this  | @param t Target for finding dependents of t related by this  |
| 21 | `Param_89` | ✗(漏检) |  | 0.240 | 0.622 | 0.981 | @param key | @param key |
| 22 | `Param_34` | ✓ |  | 0.083 | 0.627 | 0.605 | @param name the filter's name | @param urlPattern the filter's url pattern |
| 23 | `Param_111` | ✓ |  | 0.858 | 0.633 | 0.944 | @param sub_locator used to find child element. For example t | @param sub_locator used to find child element. For example t |
| 24 | `Param_36` | ✓ |  | 0.489 | 0.641 | 0.841 | @param methodName The method name. | @param attributeName The method name. |
| 25 | `Param_163` | ✓ |  | 0.489 | 0.641 | 0.999 | @param flag the flag to check | @param flagsToCheck the flag to check |
| 26 | `Param_30` | ✗(漏检) |  | 0.916 | 0.652 | 0.969 | @param type the identifier for the required type handler. Th | @param type the identifier for the required type handler. Th |
| 27 | `Param_8` | ✓ |  | 0.088 | 0.663 | 0.243 | @param fail Whether to fail | @param litmus the litmus object |
| 28 | `Param_10` | ✓ |  | 0.839 | 0.667 | 0.944 | @param defaultGraph the default ImmutableGraph against which | @param defaultGraph the default TripleCollection against whi |
| 29 | `Param_50` | ✗(漏检) |  | 0.106 | 0.667 | 0.341 | @param value | @param value |
| 30 | `Param_52` | ✓ |  | 0.669 | 0.667 | 0.794 | @param req the  HttpServletResponse | @param req the AtmosphereRequest |
| 31 | `Param_127` | ✓ |  | 0.489 | 0.667 | 0.841 | @param appendStr The String to append | @param addStr The String to append |
| 32 | `Param_161` | ✓ |  | 0.027 | 0.667 | 0.259 | @param delimiter the delimiter between parts | @param parts the parts |
| 33 | `Param_183` | ✓ |  | 0.005 | 0.679 | 0.185 | @param props | @param properties |
| 34 | `Param_48` | ✓ |  | 0.809 | 0.690 | 0.999 | @param metaFilePath metadata cache file path | @param metaFilePaths metadata cache file paths |
| 35 | `Param_113` | ✓ |  | 0.007 | 0.701 | 0.200 | @param clazz | @param entityName |
| 36 | `Param_44` | ✓ |  | 0.419 | 0.706 | 0.440 | @param parent The PGraphics object (or any object, really) a | @param renderer The PGraphics object associated |
| 37 | `Param_40` | ✓ |  | 0.615 | 0.707 | 0.816 | @param name the filter's name | @param filter the filter's name |
| 38 | `Param_99` | ✓ |  | 0.202 | 0.720 | 0.735 | @param p Swagger property object | @param schema Swagger Schema object |
| 39 | `Param_151` | ✓ |  | 0.217 | 0.720 | 0.735 | @param p Swagger property object | @param schema Swagger schema object |
| 40 | `Param_91` | ✗(漏检) |  | 0.858 | 0.724 | 0.944 | @param spinnerIndex the index of the spinner to check.  0 if | @param spinnerIndex the index of the spinner to check.  0 if |
| 41 | `Param_105` | ✓ |  | 0.537 | 0.756 | 0.938 | @param invoker the component of the invoker | @param invokerWrapper the invoker wrapper |
| 42 | `Param_125` | ✓ |  | 0.624 | 0.778 | 0.777 | @param schemes a map of Swagger SecuritySchemeDefinition obj | @param securitySchemeMap a map of SecurityScheme object |
| 43 | `Param_167` | ✓ |  | 0.208 | 0.794 | 0.414 | @param requestRegions The input 3A regions | @param requestRegion The input 3A region |
| 44 | `Param_24` | ✓ |  | 0.289 | 0.806 | 0.532 | @param prefered | @param preferred |
| 45 | `Param_123` | ✓ |  | 0.741 | 0.812 | 0.933 | @param columnNames the comma-separated list of column names  | @param fullyQualifiedColumnNames the comma-separated list of |
| 46 | `Param_58` | ✓ |  | 0.548 | 0.819 | 0.535 | @param arg0 the object | @param reference the object |
| 47 | `Param_95` | ✓ |  | 0.619 | 0.824 | 0.784 | @param clazz the annotation class to check for | @param fqcn the fully qualified class name to check for |
| 48 | `Param_139` | ✓ |  | 0.398 | 0.844 | 0.950 | @param operator operator | @param operation operator |
| 49 | `Param_190` | ✓ |  | 0.534 | 0.848 | 0.908 | @param values the values for the new row | @param inputValues the values for the new row |
| 50 | `Param_56` | ✓ |  | 0.403 | 0.861 | 0.655 | @param operation | @param operator |
| 51 | `Param_0` | ✓ | ✓ | 1.000 | 0.917 | 0.999 | @param file file to upload (required) | @param requiredFile file to upload (required) |
| 52 | `Param_20` | ✓ | ✓ | 1.000 | 0.917 | 0.999 | @param file file to upload (required) | @param requiredFile file to upload (required) |
| 53 | `Param_64` | ✓ | ✓ | 1.000 | 0.917 | 1.000 | @param body Input composite as post body (optional) | @param outerComposite Input composite as post body (optional |
| 54 | `Param_77` | ✓ | ✓ | 1.000 | 0.917 | 0.998 | @param file file to upload | @param requiredFile file to upload |
| 55 | `Param_107` | ✓ | ✓ | 1.000 | 0.917 | 0.996 | @param client client model | @param body client model |
| 56 | `Param_115` | ✓ | ✓ | 1.000 | 0.917 | 0.996 | @param tokens the tokens | @param siteTokens the tokens |
| 57 | `Param_141` | ✓ | ✓ | 1.000 | 0.917 | 0.992 | @param signatureType SignatureType | @param signatureType OAuth1SignatureType |
| 58 | `Param_165` | ✓ | ✓ | 1.000 | 0.917 | 0.999 | @param instant instant from 1970-01-01T00:00:00 local time | @param localInstant the instant from 1970-01-01T00:00:00 loc |
| 59 | `Param_173` | ✓ | ✓ | 1.000 | 0.917 | 1.000 | @param millis the time instant in millis to query. | @param instant the time instant in millis to query. |
| 60 | `Param_186` | ✓ | ✓ | 1.000 | 0.917 | 1.000 | @param body Input boolean as post body (optional) | @param booleanPostBody Input boolean as post body (optional) |
| 61 | `Param_202` | ✓ | ✓ | 1.000 | 0.917 | 1.000 | @param millis the time instant in millis to update. | @param instant the time instant in millis to update. |
| 62 | `Param_204` | ✓ | ✓ | 1.000 | 0.917 | 0.999 | @param file file to upload (required) | @param requiredFile file to upload (required) |
| 63 | `Param_14` | ✓ | ✓ | 1.000 | 0.983 | 1.000 | @param tokenClass the class of the authenticationToken being | @param token the token being submitted for authentication. |
| 64 | `Param_131` | ✓ | ✓ | 1.000 | 0.983 | 1.000 | @param connectionManager The connection manager to wrap with | @param logicalConnection The logical connection to wrap with |
| 65 | `Param_2` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param float x The point x coordinate. | @param double x The point x coordinate. |
| 66 | `Param_4` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param tileY the y-axis coordinate of the tile | @param localY the y-axis coordinate of the tile |
| 67 | `Param_6` | ✓ | ✓ | 0.562 | 1.000 | 0.981 | @param iteratorFactory | @param indexSupport |
| 68 | `Param_12` | ✓ |  | 1.000 | 1.000 | 0.996 | @param request the  HttpServletRequest | @param request the AtmosphereRequest |
| 69 | `Param_16` | ✓ | ✓ | 1.000 | 1.000 | 0.998 | @param urlPattern the URL pattern for requests that should b | @param klass the servlet class |
| 70 | `Param_22` | ✓ |  | 1.000 | 1.000 | 0.996 | @param res the  HttpServletResponse | @param response the HttpServletResponse |
| 71 | `Param_26` | ✓ | ✓ | 0.562 | 1.000 | 0.981 | @param pluginKey | @param pluginName |
| 72 | `Param_28` | ✓ | ✓ | 0.562 | 1.000 | 0.981 | @param entryId | @param key |
| 73 | `Param_32` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @param body order placed for purchasing the pet (required) | @param order order placed for purchasing the pet (required) |
| 74 | `Param_38` | ✓ | ✓ | 1.000 | 1.000 | 0.998 | @param id the module. | @param ref the module. |
| 75 | `Param_42` | ✓ | ✓ | 0.562 | 1.000 | 0.981 | @param global | @param scenarioPattern |
| 76 | `Param_60` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param x double The x component. | @param x float The x component. |
| 77 | `Param_62` | ✓ |  | 1.000 | 1.000 | 1.000 | @param environment the current environment, which may affect | @param environment the current environment, which may affect |
| 78 | `Param_68` | ✓ | ✓ | 1.000 | 1.000 | 0.996 | @param body client model | @param client client model |
| 79 | `Param_70` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param attributes an object containing an AttributeMap | @param withAttributes an object containing an AttributeMap |
| 80 | `Param_72` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @param outerComposite Input composite as post body (optional | @param body Input composite as post body (optional) |
| 81 | `Param_74` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param contextWrappableAs the contextWrappableAs to filter p | @param type the type to filter providers by |
| 82 | `Param_79` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param y float The y component. | @param y double The y component. |
| 83 | `Param_81` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param body client model (required) | @param client client model (required) |
| 84 | `Param_93` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param tileX the x-axis coordinate of the tile | @param localX the x-axis coordinate of the tile |
| 85 | `Param_101` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param body client model (required) | @param client client model (required) |
| 86 | `Param_103` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param elems The list of items | @param elements The list of items |
| 87 | `Param_109` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param localPort local TCP port of the webdav share | @param uri URI of the webdav share |
| 88 | `Param_117` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param body client model (required) | @param client client model (required) |
| 89 | `Param_129` | ✓ |  | 1.000 | 1.000 | 0.996 | @param req the  HttpServletRequest | @param req the AtmosphereRequest |
| 90 | `Param_135` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @param body Pet object that needs to be added to the store | @param pet Pet object that needs to be added to the store |
| 91 | `Param_137` | ✓ |  | 1.000 | 1.000 | 1.000 | @param expectedMinimumNumberOfMatches the minimum number of  | @param minimumNumberOfMatches the minimum number of matches  |
| 92 | `Param_143` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param inputReq BrokerRequest that is to be optimized | @param brokerRequest BrokerRequest that is to be optimized |
| 93 | `Param_147` | ✓ |  | 1.000 | 1.000 | 0.996 | @param response the  HttpServletResponse | @param response the AtmosphereResponse |
| 94 | `Param_153` | ✓ |  | 1.000 | 1.000 | 0.996 | @param res the  HttpServletResponse | @param res the AtmosphereResponse |
| 95 | `Param_159` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @param millis milliseconds from 1970-01-01T00:00:00Z to get  | @param instant milliseconds from 1970-01-01T00:00:00Z to get |
| 96 | `Param_169` | ✓ | ✓ | 0.562 | 1.000 | 0.981 | @param astGenerator | @param editor |
| 97 | `Param_177` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @param clazz the annotation class to check for | @param fqcn the fully qualified class name of the annotation |
| 98 | `Param_179` | ✓ | ✓ | 1.000 | 1.000 | 0.998 | @param body Created user object | @param user Created user object |
| 99 | `Param_194` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @param uri the ContentValues to read from and update | @param values the ContentValues to read from and update |
| 100 | `Param_196` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param e the element to add | @param o the element to add |
| 101 | `Param_198` | ✓ | ✓ | 1.000 | 1.000 | 1.000 | @param frameAddress - frame from which the reply came | @param incomingFrameAddress - frame from which the reply cam |
| 102 | `Param_200` | ✓ | ✓ | 1.000 | 1.000 | 0.999 | @param attributes an object containing an AttributeMap | @param withAttributes an object containing an AttributeMap |

---

## 逐样本详情

### [85/102] `Param_171`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1860 |
| SARI | 0.2317 |
| GLEU | 0.2424 |
| METEOR | 0.3628 |
| xMatch | ✗ |

**原注释 (source)**
```
@param regex the text to search for. The parameter will be interpreted as a regular expression.
```

**标准注释 (ground truth)**
```
@param text the text to search for. The parameter will be interpreted as a regular expression
```

**生成注释 (generated)**
```
@param text the parameter. The parameter is currently unused.
```

**当前代码 (new_code)**
```java
	public boolean searchText(String text) {
		boolean found = searcher.searchWithTimeoutFor(TextView.class, search, 0, true);
		return found;
	}

```

**变更前代码 (old_code)**
```java
	public boolean searchText(String regex) {
		boolean found = searcher.searchWithTimeoutFor(TextView.class, regex, 0, true);
		return found;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public boolean searchText(String regex) {

-		boolean found = searcher.searchWithTimeoutFor(TextView.class, regex, 0, true);

+public boolean searchText(String text) {

+		boolean found = searcher.searchWithTimeoutFor(TextView.class, search, 0, true);

 		return found;

 	}
```

---

### [49/102] `Param_97`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0367 |
| SARI | 0.3092 |
| GLEU | 0.0870 |
| METEOR | 0.1981 |
| xMatch | ✗ |

**原注释 (source)**
```
@param id The identifier of the entity currently demanding load.
```

**标准注释 (ground truth)**
```
@param id A key that must be included in the batch fetch
```

**生成注释 (generated)**
```
@param collectionKey The identifier of the collection currently demanding load.
```

**当前代码 (new_code)**
```java
	private boolean isCached(Serializable collectionKey, CollectionPersister persister) {
		if ( persister.hasCache() ) {
			CacheKey cacheKey = context.getSession().generateCacheKey(
					collectionKey,
			        persister.getKeyType(),
			        persister.getRole()
			);
			return persister.getCacheAccessStrategy().get( cacheKey, context.getSession().getTimestamp() ) != null;
		}
		return false;
	}

```

**变更前代码 (old_code)**
```java
	private boolean isCached(EntityKey entityKey, EntityPersister persister) {
		if ( persister.hasCache() ) {
			CacheKey key = context.getSession().generateCacheKey(
					entityKey.getIdentifier(),
					persister.getIdentifierType(),
					entityKey.getEntityName()
			);
			return persister.getCacheAccessStrategy().get( key, context.getSession().getTimestamp() ) != null;
		}
		return false;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,11 @@
-private boolean isCached(EntityKey entityKey, EntityPersister persister) {

+private boolean isCached(Serializable collectionKey, CollectionPersister persister) {

 		if ( persister.hasCache() ) {

-			CacheKey key = context.getSession().generateCacheKey(

-					entityKey.getIdentifier(),

-					persister.getIdentifierType(),

-					entityKey.getEntityName()

+			CacheKey cacheKey = context.getSession().generateCacheKey(

+					collectionKey,

+			        persister.getKeyType(),

+			        persister.getRole()

 			);

-			return persister.getCacheAccessStrategy().get( key, context.getSession().getTimestamp() ) != null;

+			return persister.getCacheAccessStrategy().get( cacheKey, context.getSession().getTimestamp() ) != null;

 		}

 		return false;

 	}
```

---

### [78/102] `Param_157`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0538 |
| SARI | 0.3680 |
| GLEU | 0.1154 |
| METEOR | 0.4180 |
| xMatch | ✗ |

**原注释 (source)**
```
@param element an int specifying an element in the path, where 0 is the first element in the path
```

**标准注释 (ground truth)**
```
@param index the index of the element requested
```

**生成注释 (generated)**
```
@param index an int specifying an element in the path, where 0 is the first element in the path
```

**当前代码 (new_code)**
```java
    public Object getPathComponent(int index) {
        int          pathLength = getPathCount();

        if(index < 0 || index >= pathLength)
            throw new IllegalArgumentException("Index " + index +
                                           " is out of the specified range");

        TreePath         path = this;

        for(int i = pathLength-1; i != index; i--) {
            path = path.getParentPath();
        }
        return path.getLastPathComponent();
    }


```

**变更前代码 (old_code)**
```java
    public Object getPathComponent(int element) {
        int          pathLength = getPathCount();

        if(element < 0 || element >= pathLength)
            throw new IllegalArgumentException("Index " + element + " is out of the specified range");

        TreePath         path = this;

        for(int i = pathLength-1; i != element; i--) {
           path = path.parentPath;
        }
        return path.lastPathComponent;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,13 +1,14 @@
-public Object getPathComponent(int element) {

+public Object getPathComponent(int index) {

         int          pathLength = getPathCount();

 

-        if(element < 0 || element >= pathLength)

-            throw new IllegalArgumentException("Index " + element + " is out of the specified range");

+        if(index < 0 || index >= pathLength)

+            throw new IllegalArgumentException("Index " + index +

+                                           " is out of the specified range");

 

         TreePath         path = this;

 

-        for(int i = pathLength-1; i != element; i--) {

-           path = path.parentPath;

+        for(int i = pathLength-1; i != index; i--) {

+            path = path.getParentPath();

         }

-        return path.lastPathComponent;

+        return path.getLastPathComponent();

     }
```

---

### [24/102] `Param_46`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2171 |
| SARI | 0.3861 |
| GLEU | 0.3889 |
| METEOR | 0.5260 |
| xMatch | ✗ |

**原注释 (source)**
```
@param model Swagger Model object
```

**标准注释 (ground truth)**
```
@param model OpenAPI Model object
```

**生成注释 (generated)**
```
@param model Swagger Schema object
```

**当前代码 (new_code)**
```java
    public CodegenModel fromModel(String name, Schema model, Map<String, Schema> allDefinitions) {
        CodegenModel codegenModel = super.fromModel(name, model, allDefinitions);
        return codegenModel;
    }

```

**变更前代码 (old_code)**
```java
    public CodegenModel fromModel(String name, Model model, Map<String, Model> allDefinitions) {
        CodegenModel codegenModel = super.fromModel(name, model, allDefinitions);
        return codegenModel;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public CodegenModel fromModel(String name, Model model, Map<String, Model> allDefinitions) {

+public CodegenModel fromModel(String name, Schema model, Map<String, Schema> allDefinitions) {

         CodegenModel codegenModel = super.fromModel(name, model, allDefinitions);

         return codegenModel;

     }
```

---

### [28/102] `Param_54`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0865 |
| SARI | 0.4271 |
| GLEU | 0.2097 |
| METEOR | 0.6238 |
| xMatch | ✗ |

**原注释 (source)**
```
@param context the annotation binding context with access to the service registry and the annotation index
```

**标准注释 (ground truth)**
```
@param bindingContext The binding context, giving access to needed services and information
```

**生成注释 (generated)**
```
@param bindingContext the annotation binding context with access to the service registry and the annotation index
```

**当前代码 (new_code)**
```java
	public static Set<ConfiguredClassHierarchy<EntityClass>> createEntityHierarchies(AnnotationsBindingContext bindingContext) {
		Map<ClassInfo, List<ClassInfo>> processedClassInfos = new HashMap<ClassInfo, List<ClassInfo>>();

		for ( ClassInfo info : bindingContext.getIndex().getKnownClasses() ) {
			if ( !isEntityClass( info ) ) {
				continue;
			}

			if ( processedClassInfos.containsKey( info ) ) {
				continue;
			}

			List<ClassInfo> configuredClassList = new ArrayList<ClassInfo>();
			ClassInfo tmpClassInfo = info;
			Class<?> clazz = bindingContext.locateClassByName( tmpClassInfo.toString() );
			while ( clazz != null && !clazz.equals( Object.class ) ) {
				tmpClassInfo = bindingContext.getIndex().getClassByName( DotName.createSimple( clazz.getName() ) );
				clazz = clazz.getSuperclass();
				if ( tmpClassInfo == null ) {
					continue;
				}

				if ( existsHierarchyWithClassInfoAsLeaf( processedClassInfos, tmpClassInfo ) ) {
					List<ClassInfo> classInfoList = processedClassInfos.get( tmpClassInfo );
					for ( ClassInfo tmpInfo : configuredClassList ) {
						classInfoList.add( tmpInfo );
						processedClassInfos.put( tmpInfo, classInfoList );
					}
					break;
				}
// ... (truncated)
```

**变更前代码 (old_code)**
```java
	public static Set<ConfiguredClassHierarchy<EntityClass>> createEntityHierarchies(AnnotationsBindingContext context) {
		ClassLoaderService classLoaderService = context.getServiceRegistry().getService( ClassLoaderService.class );
		Map<ClassInfo, List<ClassInfo>> processedClassInfos = new HashMap<ClassInfo, List<ClassInfo>>();

		for ( ClassInfo info : context.getIndex().getKnownClasses() ) {
			if ( !isEntityClass( info ) ) {
				continue;
			}

			if ( processedClassInfos.containsKey( info ) ) {
				continue;
			}

			List<ClassInfo> configuredClassList = new ArrayList<ClassInfo>();
			ClassInfo tmpClassInfo = info;
			Class<?> clazz = classLoaderService.classForName( tmpClassInfo.toString() );
			while ( clazz != null && !clazz.equals( Object.class ) ) {
				tmpClassInfo = context.getIndex().getClassByName( DotName.createSimple( clazz.getName() ) );
				clazz = clazz.getSuperclass();
				if ( tmpClassInfo == null ) {
					continue;
				}

				if ( existsHierarchyWithClassInfoAsLeaf( processedClassInfos, tmpClassInfo ) ) {
					List<ClassInfo> classInfoList = processedClassInfos.get( tmpClassInfo );
					for ( ClassInfo tmpInfo : configuredClassList ) {
						classInfoList.add( tmpInfo );
						processedClassInfos.put( tmpInfo, classInfoList );
					}
					break;
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,7 @@
-public static Set<ConfiguredClassHierarchy<EntityClass>> createEntityHierarchies(AnnotationsBindingContext context) {

-		ClassLoaderService classLoaderService = context.getServiceRegistry().getService( ClassLoaderService.class );

+public static Set<ConfiguredClassHierarchy<EntityClass>> createEntityHierarchies(AnnotationsBindingContext bindingContext) {

 		Map<ClassInfo, List<ClassInfo>> processedClassInfos = new HashMap<ClassInfo, List<ClassInfo>>();

 

-		for ( ClassInfo info : context.getIndex().getKnownClasses() ) {

+		for ( ClassInfo info : bindingContext.getIndex().getKnownClasses() ) {

 			if ( !isEntityClass( info ) ) {

 				continue;

 			}

@@ -13,9 +12,9 @@
 

 			List<ClassInfo> configuredClassList = new ArrayList<ClassInfo>();

 			ClassInfo tmpClassInfo = info;

-			Class<?> clazz = classLoaderService.classForName( tmpClassInfo.toString() );

+			Class<?> clazz = bindingContext.locateClassByName( tmpClassInfo.toString() );

 			while ( clazz != null && !clazz.equals( Object.class ) ) {

-				tmpClassInfo = context.getIndex().getClassByName( DotName.createSimple( clazz.getName() ) );

+				tmpClassInfo = bindingContext.getIndex().getClassByName( DotName.createSimple( clazz.getName() ) );

 				clazz = clazz.getSuperclass();

 				if ( tmpClassInfo == null ) {

 					continue;

@@ -40,7 +39,7 @@
 		List<List<ClassInfo>> processedList = new ArrayList<List<ClassInfo>>();

 		for ( List<ClassInfo> classInfoList : processedClassInfos.values() ) {

 			if ( !processedList.contains( classInfoList ) ) {

-				hierarchies.add( ConfiguredClassHierarchy.createEntityClassHierarchy( classInfoList, context ) );

+				hierarchies.add( ConfiguredClassHierarchy.createEntityClassHierarchy( classInfoList, bindingContext ) );

 				processedList.add( classInfoList );

 			}

 		}

```

---

### [60/102] `Param_119`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0672 |
| SARI | 0.4378 |
| GLEU | 0.1176 |
| METEOR | 0.1881 |
| xMatch | ✗ |

**原注释 (source)**
```
@param  The type of the element we are getting.
```

**标准注释 (ground truth)**
```
@param selector The selector for the strings between the path, if any. If left empty, these will be omitted from the list.
```

**生成注释 (generated)**
```
@param selector The type of the element we are getting.
```

**当前代码 (new_code)**
```java
  public List<String> dependencyPathBetween(int start, int end, Optional<Function<Sentence, List<String>>> selector) {
    // Get paths from a node to the root of the sentence
    LinkedList<Integer> rootToStart = new LinkedList<>();
    LinkedList<Integer> rootToEnd = new LinkedList<>();
    int startAncestor = start;
    List<Optional<Integer>> governors = sentence.governors();
    Set<Integer> seenVertices = new HashSet<>();
    while (startAncestor >= 0 && governors.get(startAncestor).isPresent()) {
      if (seenVertices.contains(startAncestor)) {
        // Found loopiness -- revert to BFS
        return loopyDependencyPathBetween(start, end, selector);
      }
      seenVertices.add(startAncestor);
      rootToStart.addFirst(startAncestor);
      startAncestor = governors.get(startAncestor).get();
    }
    if (startAncestor == -1) {
      rootToStart.addFirst(-1);
    }
    int endAncestor = end;
    seenVertices.clear();
    while (endAncestor >= 0 && governors.get(endAncestor).isPresent()) {
      if (seenVertices.contains(endAncestor)) {
        // Found loopiness -- revert to BFS
        return loopyDependencyPathBetween(start, end, selector);
      }
      seenVertices.add(endAncestor);
      rootToEnd.addFirst(endAncestor);
      endAncestor = governors.get(endAncestor).get();
    }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public List<String> dependencyPathBetween(int start, int end, Function<Sentence, List<String>> selector) {
    // Get paths from a node to the root of the sentence
    LinkedList<Integer> rootToStart = new LinkedList<>();
    LinkedList<Integer> rootToEnd = new LinkedList<>();
    int startAncestor = start;
    List<Optional<Integer>> governors = sentence.governors();
    Set<Integer> seenVertices = new HashSet<>();
    while (startAncestor >= 0 && governors.get(startAncestor).isPresent()) {
      if (seenVertices.contains(startAncestor)) {
        return Collections.EMPTY_LIST;
      }
      seenVertices.add(startAncestor);
      rootToStart.addFirst(startAncestor);
      startAncestor = governors.get(startAncestor).get();
    }
    if (startAncestor == -1) {
      rootToStart.addFirst(-1);
    }
    int endAncestor = end;
    seenVertices.clear();
    while (endAncestor >= 0 && governors.get(endAncestor).isPresent()) {
      if (seenVertices.contains(endAncestor)) {
        return Collections.EMPTY_LIST;
      }
      seenVertices.add(endAncestor);
      rootToEnd.addFirst(endAncestor);
      endAncestor = governors.get(endAncestor).get();
    }
    if (endAncestor == -1) {
      rootToEnd.addFirst(-1);
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public List<String> dependencyPathBetween(int start, int end, Function<Sentence, List<String>> selector) {

+public List<String> dependencyPathBetween(int start, int end, Optional<Function<Sentence, List<String>>> selector) {

     // Get paths from a node to the root of the sentence

     LinkedList<Integer> rootToStart = new LinkedList<>();

     LinkedList<Integer> rootToEnd = new LinkedList<>();

@@ -7,7 +7,8 @@
     Set<Integer> seenVertices = new HashSet<>();

     while (startAncestor >= 0 && governors.get(startAncestor).isPresent()) {

       if (seenVertices.contains(startAncestor)) {

-        return Collections.EMPTY_LIST;

+        // Found loopiness -- revert to BFS

+        return loopyDependencyPathBetween(start, end, selector);

       }

       seenVertices.add(startAncestor);

       rootToStart.addFirst(startAncestor);

@@ -20,7 +21,8 @@
     seenVertices.clear();

     while (endAncestor >= 0 && governors.get(endAncestor).isPresent()) {

       if (seenVertices.contains(endAncestor)) {

-        return Collections.EMPTY_LIST;

+        // Found loopiness -- revert to BFS

+        return loopyDependencyPathBetween(start, end, selector);

       }

       seenVertices.add(endAncestor);

       rootToEnd.addFirst(endAncestor);

@@ -40,17 +42,22 @@
 

     // Construct the path

     if (leastCommonNodeIndex < 0) {

-      return Collections.EMPTY_LIST;

+      return Collections.emptyList();

     }

     List<String> path = new ArrayList<>();

+    Optional<List<String>> words = selector.map(x -> x.apply(sentence));

     for (int i = rootToStart.size() - 1; i > leastCommonNodeIndex; --i) {

-      path.add(selector.apply(sentence).get(rootToStart.get(i)));

+      final int index = i;

```

---

### [73/102] `Param_145`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3110 |
| SARI | 0.4549 |
| GLEU | 0.3636 |
| METEOR | 0.4756 |
| xMatch | ✗ |

**原注释 (source)**
```
@param simplify Whether to simplify (in addition to normalizing)
```

**标准注释 (ground truth)**
```
@param simplify Simplifier to simplify (in addition to normalizing), or null to not simplify
```

**生成注释 (generated)**
```
@param simplify The simplification (in addition to normalizing)
```

**当前代码 (new_code)**
```java
  public RexProgram normalize(RexBuilder rexBuilder, RexSimplify simplify) {
    // Normalize program by creating program builder from the program, then
    // converting to a program. getProgram does not need to normalize
    // because the builder was normalized on creation.
    assert isValid(Litmus.THROW, null);
    final RexProgramBuilder builder =
        RexProgramBuilder.create(rexBuilder, inputRowType, exprs, projects,
            condition, outputRowType, true, simplify);
    return builder.getProgram(false);
  }

```

**变更前代码 (old_code)**
```java
  public RexProgram normalize(RexBuilder rexBuilder, boolean simplify) {
    // Normalize program by creating program builder from the program, then
    // converting to a program. getProgram does not need to normalize
    // because the builder was normalized on creation.
    assert isValid(Litmus.THROW, null);
    final RexProgramBuilder builder =
        RexProgramBuilder.create(rexBuilder, inputRowType, exprs, projects,
            condition, outputRowType, true, simplify);
    return builder.getProgram(false);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public RexProgram normalize(RexBuilder rexBuilder, boolean simplify) {

+public RexProgram normalize(RexBuilder rexBuilder, RexSimplify simplify) {

     // Normalize program by creating program builder from the program, then

     // converting to a program. getProgram does not need to normalize

     // because the builder was normalized on creation.

```

---

### [67/102] `Param_133`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.2120 |
| SARI | 0.4552 |
| GLEU | 0.2381 |
| METEOR | 0.6013 |
| xMatch | ✗ |

**原注释 (source)**
```
@param node the tree corresponding to a use of an element
```

**标准注释 (ground truth)**
```
@param node the method invocation
```

**生成注释 (generated)**
```
@param node the tree corresponding to a use of an element
```

**当前代码 (new_code)**
```java
    public static final ExecutableElement elementFromUse(MethodInvocationTree node) {
        return (ExecutableElement)TreeInfo.symbol((JCTree)node.getMethodSelect());
    }


```

**变更前代码 (old_code)**
```java
    public static final Element elementFromUse(ExpressionTree node) {
        return InternalUtils.symbol(node);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static final Element elementFromUse(ExpressionTree node) {

-        return InternalUtils.symbol(node);

+public static final ExecutableElement elementFromUse(MethodInvocationTree node) {

+        return (ExecutableElement)TreeInfo.symbol((JCTree)node.getMethodSelect());

     }
```

---

### [42/102] `Param_83`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1607 |
| SARI | 0.4630 |
| GLEU | 0.4286 |
| METEOR | 0.7500 |
| xMatch | ✗ |

**原注释 (source)**
```
@param call Extract expression
```

**标准注释 (ground truth)**
```
@param rexNode Extract expression
```

**生成注释 (generated)**
```
@param call Extract expression
```

**当前代码 (new_code)**
```java
  public static boolean isValidTimeFloor(RexNode rexNode) {
    if (rexNode.getKind() != SqlKind.FLOOR) {
      return false;
    }
    final RexCall call = (RexCall) rexNode;
    if (call.operands.size() != 2) {
      return false;
    }
    final RexLiteral flag = (RexLiteral) call.operands.get(1);
    final TimeUnitRange timeUnit = (TimeUnitRange) flag.getValue();
    return timeUnit != null && VALID_TIME_EXTRACT.contains(timeUnit);
  }

```

**变更前代码 (old_code)**
```java
  public static boolean isValidTimeFloor(RexCall call) {
    if (call.getKind() != SqlKind.FLOOR) {
      return false;
    }
    final RexLiteral flag = (RexLiteral) call.operands.get(1);
    final TimeUnitRange timeUnit = (TimeUnitRange) flag.getValue();
    return timeUnit != null && VALID_TIME_EXTRACT.contains(timeUnit);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,9 @@
-public static boolean isValidTimeFloor(RexCall call) {

-    if (call.getKind() != SqlKind.FLOOR) {

+public static boolean isValidTimeFloor(RexNode rexNode) {

+    if (rexNode.getKind() != SqlKind.FLOOR) {

+      return false;

+    }

+    final RexCall call = (RexCall) rexNode;

+    if (call.operands.size() != 2) {

       return false;

     }

     final RexLiteral flag = (RexLiteral) call.operands.get(1);

```

---

### [95/102] `Param_192`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4238 |
| SARI | 0.4882 |
| GLEU | 0.5000 |
| METEOR | 0.6470 |
| xMatch | ✗ |

**原注释 (source)**
```
@param driver The driver to enhance
```

**标准注释 (ground truth)**
```
@param element The driver to enhance.
```

**生成注释 (generated)**
```
@param element The element to enhance
```

**当前代码 (new_code)**
```java
  public WebElement augment(RemoteWebElement element) {
    // TODO(simon): We should really add a "SelfDescribing" interface for this
    RemoteWebDriver parent = (RemoteWebDriver) element.getWrappedDriver();
    if (parent == null) {
      return element;
    }
    Map<String, AugmenterProvider> augmentors = elementAugmentors;

    CompoundHandler handler = determineAugmentation(parent, augmentors);
    RemoteWebElement remote = create(handler, element);

    remote.setId(element.getId());
    remote.setParent(parent);

    return remote;
  }

```

**变更前代码 (old_code)**
```java
  public WebDriver augment(WebDriver driver) {
    // TODO(simon): We should really add a "SelfDescribing" interface for this
    if (!(driver instanceof RemoteWebDriver)) {
      return driver;
    }

    Map<String, ?> capabilities = ((RemoteWebDriver) driver).getCapabilities().asMap();

    CompoundHandler handler = new CompoundHandler((RemoteWebDriver) driver);

    for (Map.Entry<String, ?> capablityName : capabilities.entrySet()) {
      AugmenterProvider augmenter = augmentors.get(capablityName.getKey());
      if (augmenter == null) {
        continue;
      }

      Object value = capablityName.getValue();
      if (value instanceof Boolean && !((Boolean) value).booleanValue()) {
        continue;
      }

      handler.addCapabilityHander(augmenter.getDescribedInterface(),
          augmenter.getImplementation(value));
    }

    if (handler.isNeedingApplication()) {
      // Gather the existing interfaces
      Set<Class<?>> interfaces = new HashSet<Class<?>>();
      interfaces.addAll(handler.getInterfaces());
      interfaces.addAll(getInterfacesFrom(driver.getClass()));
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,44 +1,16 @@
-public WebDriver augment(WebDriver driver) {

+public WebElement augment(RemoteWebElement element) {

     // TODO(simon): We should really add a "SelfDescribing" interface for this

-    if (!(driver instanceof RemoteWebDriver)) {

-      return driver;

+    RemoteWebDriver parent = (RemoteWebDriver) element.getWrappedDriver();

+    if (parent == null) {

+      return element;

     }

+    Map<String, AugmenterProvider> augmentors = elementAugmentors;

 

-    Map<String, ?> capabilities = ((RemoteWebDriver) driver).getCapabilities().asMap();

+    CompoundHandler handler = determineAugmentation(parent, augmentors);

+    RemoteWebElement remote = create(handler, element);

 

-    CompoundHandler handler = new CompoundHandler((RemoteWebDriver) driver);

+    remote.setId(element.getId());

+    remote.setParent(parent);

 

-    for (Map.Entry<String, ?> capablityName : capabilities.entrySet()) {

-      AugmenterProvider augmenter = augmentors.get(capablityName.getKey());

-      if (augmenter == null) {

-        continue;

-      }

-

-      Object value = capablityName.getValue();

-      if (value instanceof Boolean && !((Boolean) value).booleanValue()) {

-        continue;

-      }

-

-      handler.addCapabilityHander(augmenter.getDescribedInterface(),

-          augmenter.getImplementation(value));

-    }

-

-    if (handler.isNeedingApplication()) {

-      // Gather the existing interfaces

-      Set<Class<?>> interfaces = new HashSet<Class<?>>();

```

---

### [93/102] `Param_188`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.2900 |
| SARI | 0.4930 |
| GLEU | 0.3684 |
| METEOR | 0.6658 |
| xMatch | ✗ |

**原注释 (source)**
```
@param persister The persister for the entities being loaded.
```

**标准注释 (ground truth)**
```
@param collectionPersister The persister for the collection role.
```

**生成注释 (generated)**
```
@param persister The persister for the entities being loaded.
```

**当前代码 (new_code)**
```java
	private boolean isCached(Serializable collectionKey, CollectionPersister persister) {
		if ( persister.hasCache() ) {
			CacheKey cacheKey = context.getSession().generateCacheKey(
					collectionKey,
			        persister.getKeyType(),
			        persister.getRole()
			);
			return persister.getCacheAccessStrategy().get( cacheKey, context.getSession().getTimestamp() ) != null;
		}
		return false;
	}

```

**变更前代码 (old_code)**
```java
	private boolean isCached(EntityKey entityKey, EntityPersister persister) {
		if ( persister.hasCache() ) {
			CacheKey key = context.getSession().generateCacheKey(
					entityKey.getIdentifier(),
					persister.getIdentifierType(),
					entityKey.getEntityName()
			);
			return persister.getCacheAccessStrategy().get( key, context.getSession().getTimestamp() ) != null;
		}
		return false;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,11 @@
-private boolean isCached(EntityKey entityKey, EntityPersister persister) {

+private boolean isCached(Serializable collectionKey, CollectionPersister persister) {

 		if ( persister.hasCache() ) {

-			CacheKey key = context.getSession().generateCacheKey(

-					entityKey.getIdentifier(),

-					persister.getIdentifierType(),

-					entityKey.getEntityName()

+			CacheKey cacheKey = context.getSession().generateCacheKey(

+					collectionKey,

+			        persister.getKeyType(),

+			        persister.getRole()

 			);

-			return persister.getCacheAccessStrategy().get( key, context.getSession().getTimestamp() ) != null;

+			return persister.getCacheAccessStrategy().get( cacheKey, context.getSession().getTimestamp() ) != null;

 		}

 		return false;

 	}
```

---

### [10/102] `Param_18`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1740 |
| SARI | 0.5428 |
| GLEU | 0.2037 |
| METEOR | 0.5391 |
| xMatch | ✗ |

**原注释 (source)**
```
@param urlPattern the URL pattern for requests that should be handled by instances of  klass
```

**标准注释 (ground truth)**
```
@param klass the filter class
```

**生成注释 (generated)**
```
@param klass the class for requests that should be handled by instances of klass
```

**当前代码 (new_code)**
```java
    public FilterRegistration.Dynamic addFilter(String name, Class<? extends Filter> klass) {
        final FilterHolder holder = new FilterHolder(checkNotNull(klass));
        holder.setName(name);
        handler.getServletHandler().addFilter(holder);
        return holder.getRegistration();
    }


```

**变更前代码 (old_code)**
```java
    public FilterBuilder addFilter(Class<? extends Filter> klass,
                                   String urlPattern) {
        final FilterHolder holder = new FilterHolder(checkNotNull(klass));
        final FilterBuilder filterConfig = new FilterBuilder(holder, handler);
        filterConfig.addUrlPattern(checkNotNull(urlPattern));
        return filterConfig;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,6 @@
-public FilterBuilder addFilter(Class<? extends Filter> klass,

-                                   String urlPattern) {

+public FilterRegistration.Dynamic addFilter(String name, Class<? extends Filter> klass) {

         final FilterHolder holder = new FilterHolder(checkNotNull(klass));

-        final FilterBuilder filterConfig = new FilterBuilder(holder, handler);

-        filterConfig.addUrlPattern(checkNotNull(urlPattern));

-        return filterConfig;

+        holder.setName(name);

+        handler.getServletHandler().addFilter(holder);

+        return holder.getRegistration();

     }
```

---

### [77/102] `Param_155`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0650 |
| SARI | 0.5625 |
| GLEU | 0.1538 |
| METEOR | 0.3599 |
| xMatch | ✗ |

**原注释 (source)**
```
@param methods the methods to match against
```

**标准注释 (ground truth)**
```
@param operation the operation to match
```

**生成注释 (generated)**
```
@param implClass the class containing the method
```

**当前代码 (new_code)**
```java
    public static <T> Method findMethod(Class<?> implClass, Operation<T> operation) throws NoSuchMethodException {
        String name = operation.getName();
        Class<?>[] paramTypes = getPhysicalTypes(operation);
        return implClass.getMethod(name, paramTypes);
    }


```

**变更前代码 (old_code)**
```java
    public static Method findMethod(Operation<?> operation, Method[] methods) {
        for (Method method : methods) {
            if (match(operation, method)) {
                return method;
            }
        }
        return null;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,5 @@
-public static Method findMethod(Operation<?> operation, Method[] methods) {

-        for (Method method : methods) {

-            if (match(operation, method)) {

-                return method;

-            }

-        }

-        return null;

+public static <T> Method findMethod(Class<?> implClass, Operation<T> operation) throws NoSuchMethodException {

+        String name = operation.getName();

+        Class<?>[] paramTypes = getPhysicalTypes(operation);

+        return implClass.getMethod(name, paramTypes);

     }
```

---

### [61/102] `Param_121`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3457 |
| SARI | 0.5837 |
| GLEU | 0.3846 |
| METEOR | 0.6401 |
| xMatch | ✗ |

**原注释 (source)**
```
@param dialect The dialect in effect.
```

**标准注释 (ground truth)**
```
@param jdbcEnvironment The JDBC environment
```

**生成注释 (generated)**
```
@param jdbcEnvironment The dialect in effect.
```

**当前代码 (new_code)**
```java
	protected Identifier determineValueColumnName(Properties params, JdbcEnvironment jdbcEnvironment) {
		final String name = ConfigurationHelper.getString( VALUE_COLUMN_PARAM, params, DEF_VALUE_COLUMN );
		return jdbcEnvironment.getIdentifierHelper().toIdentifier( name );
	}

```

**变更前代码 (old_code)**
```java
	protected String determineValueColumnName(Properties params, Dialect dialect) {
		final ObjectNameNormalizer normalizer = (ObjectNameNormalizer) params.get( IDENTIFIER_NORMALIZER );
		final String name = ConfigurationHelper.getString( VALUE_COLUMN_PARAM, params, DEF_VALUE_COLUMN );
		return dialect.quote( normalizer.normalizeIdentifierQuoting( name ) );
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,4 @@
-protected String determineValueColumnName(Properties params, Dialect dialect) {

-		final ObjectNameNormalizer normalizer = (ObjectNameNormalizer) params.get( IDENTIFIER_NORMALIZER );

+protected Identifier determineValueColumnName(Properties params, JdbcEnvironment jdbcEnvironment) {

 		final String name = ConfigurationHelper.getString( VALUE_COLUMN_PARAM, params, DEF_VALUE_COLUMN );

-		return dialect.quote( normalizer.normalizeIdentifierQuoting( name ) );

+		return jdbcEnvironment.getIdentifierHelper().toIdentifier( name );

 	}
```

---

### [102/102] `Param_206`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6687 |
| SARI | 0.6011 |
| GLEU | 0.7143 |
| METEOR | 0.7938 |
| xMatch | ✗ |

**原注释 (source)**
```
@param request the  HttpServletRequest
```

**标准注释 (ground truth)**
```
@param request the  AtmosphereRequest
```

**生成注释 (generated)**
```
@param request the  HttpServletRequest
```

**当前代码 (new_code)**
```java
    public Action suspended(AtmosphereRequest request, AtmosphereResponse response)
            throws IOException, ServletException {
        return action(request, response);
    }

```

**变更前代码 (old_code)**
```java
    public Action suspended(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        return action(request, response);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Action suspended(HttpServletRequest request, HttpServletResponse response)

+public Action suspended(AtmosphereRequest request, AtmosphereResponse response)

             throws IOException, ServletException {

         return action(request, response);

     }
```

---

### [43/102] `Param_85`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.6606 |
| SARI | 0.6016 |
| GLEU | 0.7000 |
| METEOR | 0.8819 |
| xMatch | ✗ |

**原注释 (source)**
```
@param file file to upload (required)
```

**标准注释 (ground truth)**
```
@param requiredFile file to upload (required)
```

**生成注释 (generated)**
```
@param file file to upload (required)
```

**当前代码 (new_code)**
```java
    public ModelApiResponse uploadFileWithRequiredFile(Long petId, File requiredFile, String additionalMetadata) throws ApiException {
        ApiResponse<ModelApiResponse> resp = uploadFileWithRequiredFileWithHttpInfo(petId, requiredFile, additionalMetadata);
        return resp.getData();
    }

```

**变更前代码 (old_code)**
```java
    public ModelApiResponse uploadFileWithRequiredFile(Long petId, File file, String additionalMetadata) throws ApiException {
        ApiResponse<ModelApiResponse> resp = uploadFileWithRequiredFileWithHttpInfo(petId, file, additionalMetadata);
        return resp.getData();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public ModelApiResponse uploadFileWithRequiredFile(Long petId, File file, String additionalMetadata) throws ApiException {

-        ApiResponse<ModelApiResponse> resp = uploadFileWithRequiredFileWithHttpInfo(petId, file, additionalMetadata);

+public ModelApiResponse uploadFileWithRequiredFile(Long petId, File requiredFile, String additionalMetadata) throws ApiException {

+        ApiResponse<ModelApiResponse> resp = uploadFileWithRequiredFileWithHttpInfo(petId, requiredFile, additionalMetadata);

         return resp.getData();

     }
```

---

### [44/102] `Param_87`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.6606 |
| SARI | 0.6016 |
| GLEU | 0.7000 |
| METEOR | 0.8819 |
| xMatch | ✗ |

**原注释 (source)**
```
@param file file to upload (required)
```

**标准注释 (ground truth)**
```
@param requiredFile file to upload (required)
```

**生成注释 (generated)**
```
@param file file to upload (required)
```

**当前代码 (new_code)**
```java
  public ModelApiResponse uploadFileWithRequiredFile(Long petId, File requiredFile, String additionalMetadata) throws ApiException {
    Object localVarPostBody = new Object();
    
    // verify the required parameter 'petId' is set
    if (petId == null) {
      throw new ApiException(400, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");
    }
    
    // verify the required parameter 'requiredFile' is set
    if (requiredFile == null) {
      throw new ApiException(400, "Missing the required parameter 'requiredFile' when calling uploadFileWithRequiredFile");
    }
    
    // create path and map variables
    String localVarPath = "/fake/{petId}/uploadImageWithRequiredFile".replaceAll("\\{format\\}","json")
      .replaceAll("\\{" + "petId" + "\\}", apiClient.escapeString(petId.toString()));

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    if (additionalMetadata != null)
      localVarFormParams.put("additionalMetadata", additionalMetadata);
if (requiredFile != null)
      localVarFormParams.put("requiredFile", requiredFile);

    final String[] localVarAccepts = {
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public ModelApiResponse uploadFileWithRequiredFile(Long petId, File file, String additionalMetadata) throws ApiException {
    Object localVarPostBody = new Object();
    
    // verify the required parameter 'petId' is set
    if (petId == null) {
      throw new ApiException(400, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");
    }
    
    // verify the required parameter 'file' is set
    if (file == null) {
      throw new ApiException(400, "Missing the required parameter 'file' when calling uploadFileWithRequiredFile");
    }
    
    // create path and map variables
    String localVarPath = "/fake/{petId}/uploadImageWithRequiredFile".replaceAll("\\{format\\}","json")
      .replaceAll("\\{" + "petId" + "\\}", apiClient.escapeString(petId.toString()));

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    if (additionalMetadata != null)
      localVarFormParams.put("additionalMetadata", additionalMetadata);
if (file != null)
      localVarFormParams.put("file", file);

    final String[] localVarAccepts = {
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public ModelApiResponse uploadFileWithRequiredFile(Long petId, File file, String additionalMetadata) throws ApiException {

+public ModelApiResponse uploadFileWithRequiredFile(Long petId, File requiredFile, String additionalMetadata) throws ApiException {

     Object localVarPostBody = new Object();

     

     // verify the required parameter 'petId' is set

@@ -6,9 +6,9 @@
       throw new ApiException(400, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");

     }

     

-    // verify the required parameter 'file' is set

-    if (file == null) {

-      throw new ApiException(400, "Missing the required parameter 'file' when calling uploadFileWithRequiredFile");

+    // verify the required parameter 'requiredFile' is set

+    if (requiredFile == null) {

+      throw new ApiException(400, "Missing the required parameter 'requiredFile' when calling uploadFileWithRequiredFile");

     }

     

     // create path and map variables

@@ -24,8 +24,8 @@
     

     if (additionalMetadata != null)

       localVarFormParams.put("additionalMetadata", additionalMetadata);

-if (file != null)

-      localVarFormParams.put("file", file);

+if (requiredFile != null)

+      localVarFormParams.put("requiredFile", requiredFile);

 

     final String[] localVarAccepts = {

       "application/json"

```

---

### [34/102] `Param_66`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.1582 |
| SARI | 0.6016 |
| GLEU | 0.2174 |
| METEOR | 0.2566 |
| xMatch | ✗ |

**原注释 (source)**
```
@param str the input string
```

**标准注释 (ground truth)**
```
@param parts the parts of the identifier; may not be null
```

**生成注释 (generated)**
```
@param parts the input string
```

**当前代码 (new_code)**
```java
    protected static TableId parse(String[] parts, int numParts, boolean useCatalogBeforeSchema) {
        if (numParts == 0) return null;
        if (numParts == 1) return new TableId(null, null, parts[0]); // table only
        if (numParts == 2) {
            if (useCatalogBeforeSchema) return new TableId(parts[0], null, parts[1]); // catalog & table only
            return new TableId(null, parts[0], parts[1]); // catalog & table only
        }
        return new TableId(parts[0], parts[1], parts[2]); // catalog & table only
    }

```

**变更前代码 (old_code)**
```java
    public static TableId parse(String str, char delimiter, boolean useCatalogBeforeSchema) {
        String[] parts = str.split("[\\" + delimiter + "]");
        if (parts.length == 0) return null;
        if (parts.length == 1) return new TableId(null, null, parts[0]); // table only
        if (parts.length == 2) {
            if (useCatalogBeforeSchema) return new TableId(parts[0], null, parts[1]); // catalog & table only
            return new TableId(null, parts[0], parts[1]); // catalog & table only
        }
        return new TableId(parts[0], parts[1], parts[2]); // catalog & table only
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,7 @@
-public static TableId parse(String str, char delimiter, boolean useCatalogBeforeSchema) {

-        String[] parts = str.split("[\\" + delimiter + "]");

-        if (parts.length == 0) return null;

-        if (parts.length == 1) return new TableId(null, null, parts[0]); // table only

-        if (parts.length == 2) {

+protected static TableId parse(String[] parts, int numParts, boolean useCatalogBeforeSchema) {

+        if (numParts == 0) return null;

+        if (numParts == 1) return new TableId(null, null, parts[0]); // table only

+        if (numParts == 2) {

             if (useCatalogBeforeSchema) return new TableId(parts[0], null, parts[1]); // catalog & table only

             return new TableId(null, parts[0], parts[1]); // catalog & table only

         }

```

---

### [90/102] `Param_181`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.7349 |
| SARI | 0.6162 |
| GLEU | 0.7619 |
| METEOR | 0.9139 |
| xMatch | ✗ |

**原注释 (source)**
```
@param allDefinitions a map of all Swagger models from the spec
```

**标准注释 (ground truth)**
```
@param allDefinitions a map of all OpenAPI models from the spec
```

**生成注释 (generated)**
```
@param allDefinitions a map of all Swagger models from the spec
```

**当前代码 (new_code)**
```java
    public CodegenModel fromModel(String name, Schema model, Map<String, Schema> allDefinitions) {
        CodegenModel codegenModel = super.fromModel(name, model, allDefinitions);
        return codegenModel;
    }

```

**变更前代码 (old_code)**
```java
    public CodegenModel fromModel(String name, Model model, Map<String, Model> allDefinitions) {
        CodegenModel codegenModel = super.fromModel(name, model, allDefinitions);
        return codegenModel;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public CodegenModel fromModel(String name, Model model, Map<String, Model> allDefinitions) {

+public CodegenModel fromModel(String name, Schema model, Map<String, Schema> allDefinitions) {

         CodegenModel codegenModel = super.fromModel(name, model, allDefinitions);

         return codegenModel;

     }
```

---

### [87/102] `Param_175`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.7612 |
| SARI | 0.6215 |
| GLEU | 0.7826 |
| METEOR | 0.9209 |
| xMatch | ✗ |

**原注释 (source)**
```
@param t Target for finding dependents of t related by this GR
```

**标准注释 (ground truth)**
```
@param t Target for finding governors of t related by this GR
```

**生成注释 (generated)**
```
@param t Target for finding dependents of t related by this GR
```

**当前代码 (new_code)**
```java
  public Collection<Tree> getRelatedNodes(Tree t, Tree root) {
    if (root.value() == null) {
      root.setValue("ROOT");  // todo: cdm: it doesn't seem like this line should be here
    }
    Set<Tree> nodeList = new LinkedHashSet<Tree>();
    for (TregexPattern p : targetPatterns) {    // cdm: I deleted: && nodeList.isEmpty()
      TregexMatcher m = p.matcher(root);
      while (m.findAt(t)) {
        nodeList.add(m.getNode("target"));
        //System.out.println("found " + this + "(" + t + ", " + m.getNode("target") + ") using pattern " + p);
      }
    }
    return nodeList;
  }

```

**变更前代码 (old_code)**
```java
  public Collection<TreeGraphNode> getRelatedNodes(TreeGraphNode t, TreeGraphNode root, HeadFinder headFinder) {
    Set<TreeGraphNode> nodeList = new ArraySet<TreeGraphNode>();
    for (TregexPattern p : targetPatterns) {    // cdm: I deleted: && nodeList.isEmpty()
      // Initialize the TregexMatcher with the HeadFinder so that we
      // can use the same HeadFinder through the entire process of
      // building the dependencies
      TregexMatcher m = p.matcher(root, headFinder);
      while (m.findAt(t)) {
        TreeGraphNode target = (TreeGraphNode) m.getNode("target");
        if (target == null) {
          throw new AssertionError("Expression has no target: " + p);
        }
        nodeList.add(target);
        if (DEBUG) {
          System.err.println("found " + this + "(" + t + "-" + t.headWordNode() + ", " + m.getNode("target") + "-" + ((TreeGraphNode) m.getNode("target")).headWordNode() + ") using pattern " + p);
          for (String nodeName : m.getNodeNames()) {
            if (nodeName.equals("target"))
              continue;
            System.err.println("  node " + nodeName + ": " + m.getNode(nodeName));
          }
        }
      }
    }
    return nodeList;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,24 +1,13 @@
-public Collection<TreeGraphNode> getRelatedNodes(TreeGraphNode t, TreeGraphNode root, HeadFinder headFinder) {

-    Set<TreeGraphNode> nodeList = new ArraySet<TreeGraphNode>();

+public Collection<Tree> getRelatedNodes(Tree t, Tree root) {

+    if (root.value() == null) {

+      root.setValue("ROOT");  // todo: cdm: it doesn't seem like this line should be here

+    }

+    Set<Tree> nodeList = new LinkedHashSet<Tree>();

     for (TregexPattern p : targetPatterns) {    // cdm: I deleted: && nodeList.isEmpty()

-      // Initialize the TregexMatcher with the HeadFinder so that we

-      // can use the same HeadFinder through the entire process of

-      // building the dependencies

-      TregexMatcher m = p.matcher(root, headFinder);

+      TregexMatcher m = p.matcher(root);

       while (m.findAt(t)) {

-        TreeGraphNode target = (TreeGraphNode) m.getNode("target");

-        if (target == null) {

-          throw new AssertionError("Expression has no target: " + p);

-        }

-        nodeList.add(target);

-        if (DEBUG) {

-          System.err.println("found " + this + "(" + t + "-" + t.headWordNode() + ", " + m.getNode("target") + "-" + ((TreeGraphNode) m.getNode("target")).headWordNode() + ") using pattern " + p);

-          for (String nodeName : m.getNodeNames()) {

-            if (nodeName.equals("target"))

-              continue;

-            System.err.println("  node " + nodeName + ": " + m.getNode(nodeName));

-          }

-        }

+        nodeList.add(m.getNode("target"));

+        //System.out.println("found " + this + "(" + t + ", " + m.getNode("target") + ") using pattern " + p);

       }

     }

     return nodeList;

```

---

### [45/102] `Param_89`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.2403 |
| SARI | 0.6222 |
| GLEU | 0.5000 |
| METEOR | 0.9815 |
| xMatch | ✗ |

**原注释 (source)**
```
@param key
```

**标准注释 (ground truth)**
```
@param keys
```

**生成注释 (generated)**
```
@param key
```

**当前代码 (new_code)**
```java
  public Task<Boolean> contains(final List<CacheKey> keys) {
    if (keys.isEmpty()) {
      return Task.forResult(false);
    }
    for (CacheKey key : keys) {
      EncodedImage pinnedImage = mStagingArea.get(key);
      if (pinnedImage != null) {
        pinnedImage.close();
        FLog.v(TAG, "Found image for %s in staging area", key.toString());
        mImageCacheStatsTracker.onStagingAreaHit();
        return Task.forResult(true);
      }
    }
    Task<Boolean> masterTask = containsAsync(keys.get(0));
    if (keys.size() == 1) {
      return masterTask;
    }
    for (final CacheKey key : keys.subList(1, keys.size())) {
      masterTask = masterTask.continueWithTask(
          new Continuation<Boolean, Task<Boolean>>() {
            @Override
            public Task<Boolean> then(Task<Boolean> previousTask) throws Exception {
              if (previousTask.isCancelled() || previousTask.getResult()) {
                return previousTask;
              }
              return containsAsync(key);
            }
          },
          mReadExecutor);
    }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public Task<Boolean> contains(final CacheKey key) {
    Preconditions.checkNotNull(key);

    final EncodedImage pinnedImage = mStagingArea.get(key);
    if (pinnedImage != null) {
      pinnedImage.close();
      FLog.v(TAG, "Found image for %s in staging area", key.toString());
      mImageCacheStatsTracker.onStagingAreaHit();
      return Task.forResult(true);
    }

    try {
      return Task.call(
          new Callable<Boolean>() {
            @Override
            public Boolean call() throws Exception {
              EncodedImage result = mStagingArea.get(key);
              if (result != null) {
                result.close();
                FLog.v(TAG, "Found image for %s in staging area", key.toString());
                mImageCacheStatsTracker.onStagingAreaHit();
                return true;
              } else {
                FLog.v(TAG, "Did not find image for %s in staging area", key.toString());
                mImageCacheStatsTracker.onStagingAreaMiss();
                try {
                  return mFileCache.hasKey(key);
                } catch (Exception exception) {
                  return false;
                }
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,45 +1,32 @@
-public Task<Boolean> contains(final CacheKey key) {

-    Preconditions.checkNotNull(key);

-

-    final EncodedImage pinnedImage = mStagingArea.get(key);

-    if (pinnedImage != null) {

-      pinnedImage.close();

-      FLog.v(TAG, "Found image for %s in staging area", key.toString());

-      mImageCacheStatsTracker.onStagingAreaHit();

-      return Task.forResult(true);

+public Task<Boolean> contains(final List<CacheKey> keys) {

+    if (keys.isEmpty()) {

+      return Task.forResult(false);

     }

-

-    try {

-      return Task.call(

-          new Callable<Boolean>() {

+    for (CacheKey key : keys) {

+      EncodedImage pinnedImage = mStagingArea.get(key);

+      if (pinnedImage != null) {

+        pinnedImage.close();

+        FLog.v(TAG, "Found image for %s in staging area", key.toString());

+        mImageCacheStatsTracker.onStagingAreaHit();

+        return Task.forResult(true);

+      }

+    }

+    Task<Boolean> masterTask = containsAsync(keys.get(0));

+    if (keys.size() == 1) {

+      return masterTask;

+    }

+    for (final CacheKey key : keys.subList(1, keys.size())) {

+      masterTask = masterTask.continueWithTask(

+          new Continuation<Boolean, Task<Boolean>>() {

             @Override

-            public Boolean call() throws Exception {

-              EncodedImage result = mStagingArea.get(key);

-              if (result != null) {

```

---

### [18/102] `Param_34`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0831 |
| SARI | 0.6270 |
| GLEU | 0.2308 |
| METEOR | 0.6048 |
| xMatch | ✗ |

**原注释 (source)**
```
@param name the filter's name
```

**标准注释 (ground truth)**
```
@param klass the filter class
```

**生成注释 (generated)**
```
@param urlPattern the filter's url pattern
```

**当前代码 (new_code)**
```java
    public FilterBuilder addFilter(Class<? extends Filter> klass,
                                   String urlPattern) {
        final FilterHolder holder = new FilterHolder(checkNotNull(klass));
        final FilterBuilder filterConfig = new FilterBuilder(holder, handler);
        filterConfig.addUrlPattern(checkNotNull(urlPattern));
        return filterConfig;
    }


```

**变更前代码 (old_code)**
```java
    public FilterRegistration.Dynamic addFilter(String name, Class<? extends Filter> klass) {
        final FilterHolder holder = new FilterHolder(checkNotNull(klass));
        holder.setName(name);
        handler.getServletHandler().addFilter(holder);
        return holder.getRegistration();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,7 @@
-public FilterRegistration.Dynamic addFilter(String name, Class<? extends Filter> klass) {

+public FilterBuilder addFilter(Class<? extends Filter> klass,

+                                   String urlPattern) {

         final FilterHolder holder = new FilterHolder(checkNotNull(klass));

-        holder.setName(name);

-        handler.getServletHandler().addFilter(holder);

-        return holder.getRegistration();

+        final FilterBuilder filterConfig = new FilterBuilder(holder, handler);

+        filterConfig.addUrlPattern(checkNotNull(urlPattern));

+        return filterConfig;

     }
```

---

### [56/102] `Param_111`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8579 |
| SARI | 0.6332 |
| GLEU | 0.8636 |
| METEOR | 0.9437 |
| xMatch | ✗ |

**原注释 (source)**
```
@param sub_locator used to find child element. For example td By.xpath("./tr/td")
```

**标准注释 (ground truth)**
```
@param childLocator used to find child element. For example td By.xpath("./tr/td")
```

**生成注释 (generated)**
```
@param sub_locator used to find child element. For example td By.xpath("./tr/td")
```

**当前代码 (new_code)**
```java
      public List<WebElement> apply(WebDriver driver) {
        List<WebElement> allChildren = findElement(parent, driver).findElements(childLocator);

        return allChildren.isEmpty() ? null : allChildren;
      }

```

**变更前代码 (old_code)**
```java
      public List<WebElement> apply(WebDriver webDriver) {
        List<WebElement> elements = null;
        try {
          elements = webDriver.findElement(locator).findElements(sub_locator);
        } catch (Exception e) {/**/}
        if (elements != null && elements.size() > 0) {
          return elements;
        }
        return null;
      }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,10 +1,5 @@
-public List<WebElement> apply(WebDriver webDriver) {

-        List<WebElement> elements = null;

-        try {

-          elements = webDriver.findElement(locator).findElements(sub_locator);

-        } catch (Exception e) {/**/}

-        if (elements != null && elements.size() > 0) {

-          return elements;

-        }

-        return null;

+public List<WebElement> apply(WebDriver driver) {

+        List<WebElement> allChildren = findElement(parent, driver).findElements(childLocator);

+

+        return allChildren.isEmpty() ? null : allChildren;

       }
```

---

### [19/102] `Param_36`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4889 |
| SARI | 0.6412 |
| GLEU | 0.5909 |
| METEOR | 0.8413 |
| xMatch | ✗ |

**原注释 (source)**
```
@param methodName The method name.
```

**标准注释 (ground truth)**
```
@param attributeName The attribute name.
```

**生成注释 (generated)**
```
@param attributeName The method name.
```

**当前代码 (new_code)**
```java
	private static Method getMethod(Class<?> clazz, String attributeName) {
		try {
			char string[] = attributeName.toCharArray();
			string[0] = Character.toUpperCase( string[0] );
			String casedAttributeName = new String( string );
			try {
				return clazz.getDeclaredMethod( "get" + casedAttributeName );
			}
			catch ( NoSuchMethodException e ) {
				return clazz.getDeclaredMethod( "is" + casedAttributeName );
			}
		}
		catch ( NoSuchMethodException e ) {
			return null;
		}
	}

```

**变更前代码 (old_code)**
```java
	private static Method getMethod(Class<?> clazz, String methodName) {
		try {
			char string[] = methodName.toCharArray();
			string[0] = Character.toUpperCase( string[0] );
			methodName = new String( string );
			try {
				return clazz.getDeclaredMethod( "get" + methodName );
			}
			catch ( NoSuchMethodException e ) {
				return clazz.getDeclaredMethod( "is" + methodName );
			}
		}
		catch ( NoSuchMethodException e ) {
			return null;
		}
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,13 +1,13 @@
-private static Method getMethod(Class<?> clazz, String methodName) {

+private static Method getMethod(Class<?> clazz, String attributeName) {

 		try {

-			char string[] = methodName.toCharArray();

+			char string[] = attributeName.toCharArray();

 			string[0] = Character.toUpperCase( string[0] );

-			methodName = new String( string );

+			String casedAttributeName = new String( string );

 			try {

-				return clazz.getDeclaredMethod( "get" + methodName );

+				return clazz.getDeclaredMethod( "get" + casedAttributeName );

 			}

 			catch ( NoSuchMethodException e ) {

-				return clazz.getDeclaredMethod( "is" + methodName );

+				return clazz.getDeclaredMethod( "is" + casedAttributeName );

 			}

 		}

 		catch ( NoSuchMethodException e ) {

```

---

### [81/102] `Param_163`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4889 |
| SARI | 0.6412 |
| GLEU | 0.5909 |
| METEOR | 0.9985 |
| xMatch | ✗ |

**原注释 (source)**
```
@param flag the flag to check
```

**标准注释 (ground truth)**
```
@param flagsToCheck the flags to check
```

**生成注释 (generated)**
```
@param flagsToCheck the flag to check
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

### [16/102] `Param_30`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.9157 |
| SARI | 0.6516 |
| GLEU | 0.9180 |
| METEOR | 0.9686 |
| xMatch | ✗ |

**原注释 (source)**
```
@param type the identifier for the required type handler. This identifier may be one of those listed in  STextTypeHandlerFactory or it may be have been registered by a plug-in.
```

**标准注释 (ground truth)**
```
@param type the identifier for the required type handler. This identifier may be one of those listed in  StructuredTextTypeHandlerFactory or it may be have been registered by a plug-in.
```

**生成注释 (generated)**
```
@param type the identifier for the required type handler. This identifier may be one of those listed in  STextTypeHandlerFactory or it may be have been registered by a plug-in.
```

**当前代码 (new_code)**
```java
	static public IStructuredTextExpert getStatefulExpert(String type, StructuredTextEnvironment environment) {
		StructuredTextTypeHandler handler = StructuredTextTypeHandlerFactory.getHandler(type);
		if (handler == null)
			throw new IllegalArgumentException("Invalid type argument"); //$NON-NLS-1$
		return getStatefulExpert(handler, environment);
	}


```

**变更前代码 (old_code)**
```java
	static public ISTextExpert getStatefulExpert(String type, STextEnvironment environment) {
		STextTypeHandler handler = STextTypeHandlerFactory.getHandler(type);
		if (handler == null)
			throw new IllegalArgumentException("Invalid type argument"); //$NON-NLS-1$
		return getStatefulExpert(handler, environment);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-static public ISTextExpert getStatefulExpert(String type, STextEnvironment environment) {

-		STextTypeHandler handler = STextTypeHandlerFactory.getHandler(type);

+static public IStructuredTextExpert getStatefulExpert(String type, StructuredTextEnvironment environment) {

+		StructuredTextTypeHandler handler = StructuredTextTypeHandlerFactory.getHandler(type);

 		if (handler == null)

 			throw new IllegalArgumentException("Invalid type argument"); //$NON-NLS-1$

 		return getStatefulExpert(handler, environment);

```

---

### [5/102] `Param_8`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0878 |
| SARI | 0.6630 |
| GLEU | 0.1579 |
| METEOR | 0.2434 |
| xMatch | ✗ |

**原注释 (source)**
```
@param fail Whether to fail
```

**标准注释 (ground truth)**
```
@param litmus What to do if an error is detected
```

**生成注释 (generated)**
```
@param litmus the litmus object
```

**当前代码 (new_code)**
```java
  public boolean isValid(Litmus litmus) {
    if (inputRowType == null) {
      return litmus.fail(null);
    }
    if (exprs == null) {
      return litmus.fail(null);
    }
    if (projects == null) {
      return litmus.fail(null);
    }
    if (outputRowType == null) {
      return litmus.fail(null);
    }

    // If the input row type is a struct (contains fields) then the leading
    // expressions must be references to those fields. But we don't require
    // this if the input row type is, say, a java class.
    if (inputRowType.isStruct()) {
      if (!RexUtil.containIdentity(exprs, inputRowType, litmus)) {
        return litmus.fail(null);
      }

      // None of the other fields should be inputRefs.
      for (int i = inputRowType.getFieldCount(); i < exprs.size(); i++) {
        RexNode expr = exprs.get(i);
        if (expr instanceof RexInputRef) {
          return litmus.fail(null);
        }
      }
    }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public boolean isValid(boolean fail) {
    if (inputRowType == null) {
      assert !fail;
      return false;
    }
    if (exprs == null) {
      assert !fail;
      return false;
    }
    if (projects == null) {
      assert !fail;
      return false;
    }
    if (outputRowType == null) {
      assert !fail;
      return false;
    }

    // If the input row type is a struct (contains fields) then the leading
    // expressions must be references to those fields. But we don't require
    // this if the input row type is, say, a java class.
    if (inputRowType.isStruct()) {
      if (!RexUtil.containIdentity(exprs, inputRowType, fail)) {
        assert !fail;
        return false;
      }

      // None of the other fields should be inputRefs.
      for (int i = inputRowType.getFieldCount(); i < exprs.size(); i++) {
        RexNode expr = exprs.get(i);
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,56 +1,47 @@
-public boolean isValid(boolean fail) {

+public boolean isValid(Litmus litmus) {

     if (inputRowType == null) {

-      assert !fail;

-      return false;

+      return litmus.fail(null);

     }

     if (exprs == null) {

-      assert !fail;

-      return false;

+      return litmus.fail(null);

     }

     if (projects == null) {

-      assert !fail;

-      return false;

+      return litmus.fail(null);

     }

     if (outputRowType == null) {

-      assert !fail;

-      return false;

+      return litmus.fail(null);

     }

 

     // If the input row type is a struct (contains fields) then the leading

     // expressions must be references to those fields. But we don't require

     // this if the input row type is, say, a java class.

     if (inputRowType.isStruct()) {

-      if (!RexUtil.containIdentity(exprs, inputRowType, fail)) {

-        assert !fail;

-        return false;

+      if (!RexUtil.containIdentity(exprs, inputRowType, litmus)) {

+        return litmus.fail(null);

       }

 

       // None of the other fields should be inputRefs.

       for (int i = inputRowType.getFieldCount(); i < exprs.size(); i++) {

         RexNode expr = exprs.get(i);

```

---

### [6/102] `Param_10`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8394 |
| SARI | 0.6667 |
| GLEU | 0.8485 |
| METEOR | 0.9437 |
| xMatch | ✗ |

**原注释 (source)**
```
@param defaultGraph the default ImmutableGraph against which to execute the query if not FROM clause is present
```

**标准注释 (ground truth)**
```
@param defaultGraph the default graph against which to execute the query if not FROM clause is present
```

**生成注释 (generated)**
```
@param defaultGraph the default TripleCollection against which to execute the query if not FROM clause is present
```

**当前代码 (new_code)**
```java
    @Deprecated
    public Graph executeSparqlQuery(ConstructQuery query,
            TripleCollection defaultGraph) {
        return (Graph) executeSparqlQuery((Query) query, defaultGraph);
    }


```

**变更前代码 (old_code)**
```java
    @Deprecated
    public ImmutableGraph executeSparqlQuery(ConstructQuery query,
            Graph defaultGraph) {
        return (ImmutableGraph) executeSparqlQuery((Query) query, defaultGraph);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
 @Deprecated

-    public ImmutableGraph executeSparqlQuery(ConstructQuery query,

-            Graph defaultGraph) {

-        return (ImmutableGraph) executeSparqlQuery((Query) query, defaultGraph);

+    public Graph executeSparqlQuery(ConstructQuery query,

+            TripleCollection defaultGraph) {

+        return (Graph) executeSparqlQuery((Query) query, defaultGraph);

     }
```

---

### [26/102] `Param_50`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.1062 |
| SARI | 0.6667 |
| GLEU | 0.2308 |
| METEOR | 0.3407 |
| xMatch | ✗ |

**原注释 (source)**
```
@param value
```

**标准注释 (ground truth)**
```
@param value the value of the parameter
```

**生成注释 (generated)**
```
@param value
```

**当前代码 (new_code)**
```java
    protected String setEscapedParameter(HttpMessage message, String param, String value) {
        return variant.setEscapedParameter(message, originalPair, param, value);
    }

```

**变更前代码 (old_code)**
```java
    protected String setEscapedParameter(HttpMessage msg, String param, String value) {
        return variant.setEscapedParameter(msg, originalPair, param, value);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-protected String setEscapedParameter(HttpMessage msg, String param, String value) {

-        return variant.setEscapedParameter(msg, originalPair, param, value);

+protected String setEscapedParameter(HttpMessage message, String param, String value) {

+        return variant.setEscapedParameter(message, originalPair, param, value);

     }
```

---

### [27/102] `Param_52`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6687 |
| SARI | 0.6667 |
| GLEU | 0.7143 |
| METEOR | 0.7938 |
| xMatch | ✗ |

**原注释 (source)**
```
@param req the  HttpServletResponse
```

**标准注释 (ground truth)**
```
@param req the  AtmosphereResponse
```

**生成注释 (generated)**
```
@param req the AtmosphereRequest
```

**当前代码 (new_code)**
```java
    protected AtmosphereHandlerWrapper map(AtmosphereRequest req) throws ServletException {
        String path;
        if (req.getPathInfo() != null) {
            path = req.getServletPath() + req.getPathInfo();
        } else {
            path = req.getServletPath();
        }
        if (path == null || path.length() <= 1) {
            path = "/all";
        }

        AtmosphereHandlerWrapper atmosphereHandlerWrapper = map(path);
        if (atmosphereHandlerWrapper == null) {
            atmosphereHandlerWrapper = map("/all");
        }

        if (atmosphereHandlerWrapper == null) {
            throw new AtmosphereMappingException("No AtmosphereHandler maps request for " + path);
        }
        config.getBroadcasterFactory().add(atmosphereHandlerWrapper.broadcaster,
                atmosphereHandlerWrapper.broadcaster.getID());
        return atmosphereHandlerWrapper;
    }

```

**变更前代码 (old_code)**
```java
    protected AtmosphereHandlerWrapper map(HttpServletRequest req) throws ServletException {
        String path;
        if (req.getPathInfo() != null) {
            path = req.getServletPath() + req.getPathInfo();
        } else {
            path = req.getServletPath();
        }
        if (path == null || path.length() <= 1) {
            path = "/all";
        }

        AtmosphereHandlerWrapper atmosphereHandlerWrapper = map(path);
        if (atmosphereHandlerWrapper == null) {
            atmosphereHandlerWrapper = map("/all");
        }

        if (atmosphereHandlerWrapper == null) {
            throw new AtmosphereMappingException("No AtmosphereHandler maps request for " + path);
        }
        config.getBroadcasterFactory().add(atmosphereHandlerWrapper.broadcaster,
                atmosphereHandlerWrapper.broadcaster.getID());
        return atmosphereHandlerWrapper;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-protected AtmosphereHandlerWrapper map(HttpServletRequest req) throws ServletException {

+protected AtmosphereHandlerWrapper map(AtmosphereRequest req) throws ServletException {

         String path;

         if (req.getPathInfo() != null) {

             path = req.getServletPath() + req.getPathInfo();

```

---

### [64/102] `Param_127`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4889 |
| SARI | 0.6667 |
| GLEU | 0.5909 |
| METEOR | 0.8413 |
| xMatch | ✗ |

**原注释 (source)**
```
@param appendStr The String to append
```

**标准注释 (ground truth)**
```
@param addStrStr The String to append
```

**生成注释 (generated)**
```
@param addStr The String to append
```

**当前代码 (new_code)**
```java
    private StringBuilder appendIfNotNull(StringBuilder source, String addStr, String delimiter) {
        if (addStr != null) {
            if (addStr.length() == 0) {
                delimiter = "";
            }

            return source.append(addStr).append(delimiter);
        }
        return source;
    }


```

**变更前代码 (old_code)**
```java
    private String appendIfNotNull(String sourceStr, String appendStr, String delimiter) {
        if (appendStr != null) {
            if (appendStr.length() == 0) {
                delimiter = "";
            }
            sourceStr += delimiter + appendStr;
        }
        return sourceStr;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,10 @@
-private String appendIfNotNull(String sourceStr, String appendStr, String delimiter) {

-        if (appendStr != null) {

-            if (appendStr.length() == 0) {

+private StringBuilder appendIfNotNull(StringBuilder source, String addStr, String delimiter) {

+        if (addStr != null) {

+            if (addStr.length() == 0) {

                 delimiter = "";

             }

-            sourceStr += delimiter + appendStr;

+

+            return source.append(addStr).append(delimiter);

         }

-        return sourceStr;

+        return source;

     }
```

---

### [80/102] `Param_161`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0273 |
| SARI | 0.6667 |
| GLEU | 0.1087 |
| METEOR | 0.2587 |
| xMatch | ✗ |

**原注释 (source)**
```
@param delimiter the delimiter between parts
```

**标准注释 (ground truth)**
```
@param numParts the number of parts to use for the table identifier
```

**生成注释 (generated)**
```
@param parts the parts
```

**当前代码 (new_code)**
```java
    protected static TableId parse(String[] parts, int numParts, boolean useCatalogBeforeSchema) {
        if (numParts == 0) return null;
        if (numParts == 1) return new TableId(null, null, parts[0]); // table only
        if (numParts == 2) {
            if (useCatalogBeforeSchema) return new TableId(parts[0], null, parts[1]); // catalog & table only
            return new TableId(null, parts[0], parts[1]); // catalog & table only
        }
        return new TableId(parts[0], parts[1], parts[2]); // catalog & table only
    }

```

**变更前代码 (old_code)**
```java
    public static TableId parse(String str, char delimiter, boolean useCatalogBeforeSchema) {
        String[] parts = str.split("[\\" + delimiter + "]");
        if (parts.length == 0) return null;
        if (parts.length == 1) return new TableId(null, null, parts[0]); // table only
        if (parts.length == 2) {
            if (useCatalogBeforeSchema) return new TableId(parts[0], null, parts[1]); // catalog & table only
            return new TableId(null, parts[0], parts[1]); // catalog & table only
        }
        return new TableId(parts[0], parts[1], parts[2]); // catalog & table only
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,7 @@
-public static TableId parse(String str, char delimiter, boolean useCatalogBeforeSchema) {

-        String[] parts = str.split("[\\" + delimiter + "]");

-        if (parts.length == 0) return null;

-        if (parts.length == 1) return new TableId(null, null, parts[0]); // table only

-        if (parts.length == 2) {

+protected static TableId parse(String[] parts, int numParts, boolean useCatalogBeforeSchema) {

+        if (numParts == 0) return null;

+        if (numParts == 1) return new TableId(null, null, parts[0]); // table only

+        if (numParts == 2) {

             if (useCatalogBeforeSchema) return new TableId(parts[0], null, parts[1]); // catalog & table only

             return new TableId(null, parts[0], parts[1]); // catalog & table only

         }

```

---

### [91/102] `Param_183`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0049 |
| SARI | 0.6795 |
| GLEU | 0.0741 |
| METEOR | 0.1852 |
| xMatch | ✗ |

**原注释 (source)**
```
@param props
```

**标准注释 (ground truth)**
```
@param bean The Object whose properties will be added to the target URI.
```

**生成注释 (generated)**
```
@param properties
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

-        return addPropertiesToURI(uri.toString(), props);

+public static String addPropertiesToURI(URI uri, Map<String, String> properties) throws Exception {

+        return addPropertiesToURI(uri.toString(), properties);

     }
```

---

### [25/102] `Param_48`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.8091 |
| SARI | 0.6900 |
| GLEU | 0.8182 |
| METEOR | 0.9985 |
| xMatch | ✗ |

**原注释 (source)**
```
@param metaFilePath metadata cache file path
```

**标准注释 (ground truth)**
```
@param metaFilePaths metadata cache file path
```

**生成注释 (generated)**
```
@param metaFilePaths metadata cache file paths
```

**当前代码 (new_code)**
```java
  private FileSelection expandSelectionFromMetadataCache(FileSelection selection, List<Path> metaFilePaths) throws IOException {
    // get the metadata for the root directory by reading the metadata file
    // parquetTableMetadata contains the metadata for all files in the selection root folder, but we need to make sure
    // we only select the files that are part of selection (by setting fileSet appropriately)

    // get (and set internal field) the metadata for the directory by reading the metadata file
    FileSystem processUserFileSystem = ImpersonationUtil.createFileSystem(ImpersonationUtil.getProcessUserName(), fs.getConf());
    parquetTableMetadata = Metadata.readBlockMeta(processUserFileSystem, metaFilePaths, metaContext, readerConfig);
    if (ignoreExpandingSelection(parquetTableMetadata)) {
      return selection;
    }
    if (corruptDatesAutoCorrected) {
      ParquetReaderUtility.correctDatesInMetadataCache(this.parquetTableMetadata);
    }
    ParquetReaderUtility.transformBinaryInMetadataCache(parquetTableMetadata, readerConfig);
    List<FileStatus> fileStatuses = selection.getStatuses(fs);

    if (fileSet == null) {
      fileSet = new HashSet<>();
    }

    final Path first = fileStatuses.get(0).getPath();
    if (fileStatuses.size() == 1 && selection.getSelectionRoot().equals(first)) {
      // we are selecting all files from selection root. Expand the file list from the cache
      for (MetadataBase.ParquetFileMetadata file : parquetTableMetadata.getFiles()) {
        fileSet.add(file.getPath());
      }

    } else if (selection.isExpandedPartial() && !selection.hadWildcard() && cacheFileRoot != null) {
      if (selection.wasAllPartitionsPruned()) {
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  private FileSelection expandSelectionFromMetadataCache(FileSelection selection, Path metaFilePath) throws IOException {
    // get the metadata for the root directory by reading the metadata file
    // parquetTableMetadata contains the metadata for all files in the selection root folder, but we need to make sure
    // we only select the files that are part of selection (by setting fileSet appropriately)

    // get (and set internal field) the metadata for the directory by reading the metadata file
    FileSystem processUserFileSystem = ImpersonationUtil.createFileSystem(ImpersonationUtil.getProcessUserName(), fs.getConf());
    parquetTableMetadata = Metadata.readBlockMeta(processUserFileSystem, metaFilePath, metaContext, readerConfig);
    if (ignoreExpandingSelection(parquetTableMetadata)) {
      return selection;
    }
    if (corruptDatesAutoCorrected) {
      ParquetReaderUtility.correctDatesInMetadataCache(this.parquetTableMetadata);
    }
    ParquetReaderUtility.transformBinaryInMetadataCache(parquetTableMetadata, readerConfig);
    List<FileStatus> fileStatuses = selection.getStatuses(fs);

    if (fileSet == null) {
      fileSet = new HashSet<>();
    }

    final Path first = fileStatuses.get(0).getPath();
    if (fileStatuses.size() == 1 && selection.getSelectionRoot().equals(first)) {
      // we are selecting all files from selection root. Expand the file list from the cache
      for (MetadataBase.ParquetFileMetadata file : parquetTableMetadata.getFiles()) {
        fileSet.add(file.getPath());
      }

    } else if (selection.isExpandedPartial() && !selection.hadWildcard() && cacheFileRoot != null) {
      if (selection.wasAllPartitionsPruned()) {
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,11 @@
-private FileSelection expandSelectionFromMetadataCache(FileSelection selection, Path metaFilePath) throws IOException {

+private FileSelection expandSelectionFromMetadataCache(FileSelection selection, List<Path> metaFilePaths) throws IOException {

     // get the metadata for the root directory by reading the metadata file

     // parquetTableMetadata contains the metadata for all files in the selection root folder, but we need to make sure

     // we only select the files that are part of selection (by setting fileSet appropriately)

 

     // get (and set internal field) the metadata for the directory by reading the metadata file

     FileSystem processUserFileSystem = ImpersonationUtil.createFileSystem(ImpersonationUtil.getProcessUserName(), fs.getConf());

-    parquetTableMetadata = Metadata.readBlockMeta(processUserFileSystem, metaFilePath, metaContext, readerConfig);

+    parquetTableMetadata = Metadata.readBlockMeta(processUserFileSystem, metaFilePaths, metaContext, readerConfig);

     if (ignoreExpandingSelection(parquetTableMetadata)) {

       return selection;

     }

@@ -44,9 +44,10 @@
       for (FileStatus status : fileStatuses) {

         Path currentCacheFileRoot = status.getPath();

         if (status.isDirectory()) {

-          //TODO [DRILL-4496] read the metadata cache files in parallel

-          Path metaPath = new Path(currentCacheFileRoot, Metadata.METADATA_FILENAME);

-          MetadataBase.ParquetTableMetadataBase metadata = Metadata.readBlockMeta(processUserFileSystem, metaPath, metaContext, readerConfig);

+          // TODO [DRILL-4496] read the metadata cache files in parallel

+          // Depending on the version of metadata this may represent more than 1 metadata file paths.

+          List<Path> metaPaths = populateMetaPaths(currentCacheFileRoot, fs);

+          MetadataBase.ParquetTableMetadataBase metadata = Metadata.readBlockMeta(processUserFileSystem, metaPaths, metaContext, readerConfig);

           if (ignoreExpandingSelection(metadata)) {

             return selection;

           }

```

---

### [57/102] `Param_113`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.0074 |
| SARI | 0.7008 |
| GLEU | 0.1034 |
| METEOR | 0.2003 |
| xMatch | ✗ |

**原注释 (source)**
```
@param clazz
```

**标准注释 (ground truth)**
```
@param entityName The name of the entity to which we shoudl associate these cache settings
```

**生成注释 (generated)**
```
@param entityName
```

**当前代码 (new_code)**
```java
	public Configuration setCacheConcurrencyStrategy(String entityName, String concurrencyStrategy) {
		setCacheConcurrencyStrategy( entityName, concurrencyStrategy, entityName );
		return this;
	}

```

**变更前代码 (old_code)**
```java
	public Configuration setCacheConcurrencyStrategy(String clazz, String concurrencyStrategy)
			throws MappingException {
		setCacheConcurrencyStrategy( clazz, concurrencyStrategy, clazz );
		return this;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,4 @@
-public Configuration setCacheConcurrencyStrategy(String clazz, String concurrencyStrategy)

-			throws MappingException {

-		setCacheConcurrencyStrategy( clazz, concurrencyStrategy, clazz );

+public Configuration setCacheConcurrencyStrategy(String entityName, String concurrencyStrategy) {

+		setCacheConcurrencyStrategy( entityName, concurrencyStrategy, entityName );

 		return this;

 	}
```

---

### [23/102] `Param_44`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4192 |
| SARI | 0.7061 |
| GLEU | 0.4412 |
| METEOR | 0.4396 |
| xMatch | ✗ |

**原注释 (source)**
```
@param parent The PGraphics object (or any object, really) associated
```

**标准注释 (ground truth)**
```
@param renderer The PGraphics renderer associated to the image
```

**生成注释 (generated)**
```
@param renderer The PGraphics object associated
```

**当前代码 (new_code)**
```java
  public PMetadata getCache(PGraphics renderer) {
    if (cacheMap == null) return null;
    return cacheMap.get(renderer);
  }

```

**变更前代码 (old_code)**
```java
  public Object getCache(Object parent) {
    if (cacheMap == null) return null;
    return cacheMap.get(parent);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Object getCache(Object parent) {

+public PMetadata getCache(PGraphics renderer) {

     if (cacheMap == null) return null;

-    return cacheMap.get(parent);

+    return cacheMap.get(renderer);

   }
```

---

### [21/102] `Param_40`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6148 |
| SARI | 0.7073 |
| GLEU | 0.6364 |
| METEOR | 0.8164 |
| xMatch | ✗ |

**原注释 (source)**
```
@param name the filter's name
```

**标准注释 (ground truth)**
```
@param filter the filter instance
```

**生成注释 (generated)**
```
@param filter the filter's name
```

**当前代码 (new_code)**
```java
    public FilterBuilder addFilter(Filter filter,
                                   String urlPattern) {
        final FilterHolder holder = new FilterHolder(checkNotNull(filter));
        final FilterBuilder builder = new FilterBuilder(holder, handler);
        builder.addUrlPattern(checkNotNull(urlPattern));
        return builder;
    }


```

**变更前代码 (old_code)**
```java
    public FilterRegistration.Dynamic addFilter(String name, Filter filter) {
        final FilterHolder holder = new FilterHolder(checkNotNull(filter));
        holder.setName(name);
        handler.getServletHandler().addFilter(holder);
        return holder.getRegistration();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,7 @@
-public FilterRegistration.Dynamic addFilter(String name, Filter filter) {

+public FilterBuilder addFilter(Filter filter,

+                                   String urlPattern) {

         final FilterHolder holder = new FilterHolder(checkNotNull(filter));

-        holder.setName(name);

-        handler.getServletHandler().addFilter(holder);

-        return holder.getRegistration();

+        final FilterBuilder builder = new FilterBuilder(holder, handler);

+        builder.addUrlPattern(checkNotNull(urlPattern));

+        return builder;

     }
```

---

### [50/102] `Param_99`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2021 |
| SARI | 0.7202 |
| GLEU | 0.3333 |
| METEOR | 0.7353 |
| xMatch | ✗ |

**原注释 (source)**
```
@param p Swagger property object
```

**标准注释 (ground truth)**
```
@param schema Property schema
```

**生成注释 (generated)**
```
@param schema Swagger Schema object
```

**当前代码 (new_code)**
```java
    public String toDefaultValueWithParam(String name, Schema schema) {
        return " = data." + name + ";";
    }

```

**变更前代码 (old_code)**
```java
    public String toDefaultValueWithParam(String name, Property p) {
        return " = data." + name + ";";
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public String toDefaultValueWithParam(String name, Property p) {

+public String toDefaultValueWithParam(String name, Schema schema) {

         return " = data." + name + ";";

     }
```

---

### [75/102] `Param_151`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2171 |
| SARI | 0.7202 |
| GLEU | 0.3889 |
| METEOR | 0.7353 |
| xMatch | ✗ |

**原注释 (source)**
```
@param p Swagger property object
```

**标准注释 (ground truth)**
```
@param schema Property schema
```

**生成注释 (generated)**
```
@param schema Swagger schema object
```

**当前代码 (new_code)**
```java
    public String toDefaultValue(Schema schema) {
        if (ModelUtils.isBooleanSchema(schema)) {
            return "null";
        } else if (ModelUtils.isDateSchema(schema)) {
            return "null";
        } else if (ModelUtils.isDateTimeSchema(schema)) {
            return "null";
        } else if (ModelUtils.isNumberSchema(schema)) {
            return "null";
        } else if (ModelUtils.isIntegerSchema(schema)) {
            return "null";
        } else if (ModelUtils.isStringSchema(schema)) {
            return "null";
        } else if (ModelUtils.isObjectSchema(schema)) {
            return "null";
        } else {
            return "null";
        }
    }

```

**变更前代码 (old_code)**
```java
    public String toDefaultValue(Property p) {
        if (p instanceof StringProperty) {
            return "null";
        } else if (p instanceof BooleanProperty) {
            return "null";
        } else if (p instanceof DateProperty) {
            return "null";
        } else if (p instanceof DateTimeProperty) {
            return "null";
        } else if (p instanceof DoubleProperty) {
            DoubleProperty dp = (DoubleProperty) p;
            if (dp.getDefault() != null) {
                return dp.getDefault().toString();
            }
            return "null";
        } else if (p instanceof FloatProperty) {
            FloatProperty dp = (FloatProperty) p;
            if (dp.getDefault() != null) {
                return dp.getDefault().toString();
            }
            return "null";
        } else if (p instanceof IntegerProperty) {
            IntegerProperty dp = (IntegerProperty) p;
            if (dp.getDefault() != null) {
                return dp.getDefault().toString();
            }
            return "null";
        } else if (p instanceof LongProperty) {
            LongProperty dp = (LongProperty) p;
            if (dp.getDefault() != null) {
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,35 +1,17 @@
-public String toDefaultValue(Property p) {

-        if (p instanceof StringProperty) {

+public String toDefaultValue(Schema schema) {

+        if (ModelUtils.isBooleanSchema(schema)) {

             return "null";

-        } else if (p instanceof BooleanProperty) {

+        } else if (ModelUtils.isDateSchema(schema)) {

             return "null";

-        } else if (p instanceof DateProperty) {

+        } else if (ModelUtils.isDateTimeSchema(schema)) {

             return "null";

-        } else if (p instanceof DateTimeProperty) {

+        } else if (ModelUtils.isNumberSchema(schema)) {

             return "null";

-        } else if (p instanceof DoubleProperty) {

-            DoubleProperty dp = (DoubleProperty) p;

-            if (dp.getDefault() != null) {

-                return dp.getDefault().toString();

-            }

+        } else if (ModelUtils.isIntegerSchema(schema)) {

             return "null";

-        } else if (p instanceof FloatProperty) {

-            FloatProperty dp = (FloatProperty) p;

-            if (dp.getDefault() != null) {

-                return dp.getDefault().toString();

-            }

+        } else if (ModelUtils.isStringSchema(schema)) {

             return "null";

-        } else if (p instanceof IntegerProperty) {

-            IntegerProperty dp = (IntegerProperty) p;

-            if (dp.getDefault() != null) {

-                return dp.getDefault().toString();

-            }

-            return "null";

-        } else if (p instanceof LongProperty) {

-            LongProperty dp = (LongProperty) p;

-            if (dp.getDefault() != null) {

```

---

### [46/102] `Param_91`

| 指标 | 值 |
|---|---|
| 检测状态 | ✗ 漏检(使用原注释) |
| BLEU-4 | 0.8579 |
| SARI | 0.7242 |
| GLEU | 0.8636 |
| METEOR | 0.9437 |
| xMatch | ✗ |

**原注释 (source)**
```
@param spinnerIndex the index of the spinner to check.  0 if only one spinner is available
```

**标准注释 (ground truth)**
```
@param index the index of the spinner to check.  0 if only one spinner is available
```

**生成注释 (generated)**
```
@param spinnerIndex the index of the spinner to check.  0 if only one spinner is available
```

**当前代码 (new_code)**
```java
	public boolean isSpinnerTextSelected(int index, String text)
	{
		return checker.isSpinnerTextSelected(index, text);
	}

```

**变更前代码 (old_code)**
```java
	public boolean isSpinnerTextSelected(int spinnerIndex, String text)
	{
		return checker.isSpinnerTextSelected(spinnerIndex, text);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public boolean isSpinnerTextSelected(int spinnerIndex, String text)

+public boolean isSpinnerTextSelected(int index, String text)

 	{

-		return checker.isSpinnerTextSelected(spinnerIndex, text);

+		return checker.isSpinnerTextSelected(index, text);

 	}
```

---

### [53/102] `Param_105`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5373 |
| SARI | 0.7560 |
| GLEU | 0.6111 |
| METEOR | 0.9375 |
| xMatch | ✗ |

**原注释 (source)**
```
@param invoker the component of the invoker
```

**标准注释 (ground truth)**
```
@param invokerWrapper the wrapped invoker
```

**生成注释 (generated)**
```
@param invokerWrapper the invoker wrapper
```

**当前代码 (new_code)**
```java
	protected boolean processExtensionPopupChildren(PopupMenuUtils.PopupMenuInvokerWrapper invokerWrapper) {
		boolean childEnable = false;
		for (int index = 0; index < this.getItemCount(); index++) {
			JMenuItem item = this.getItem(index);
			if (isEnableForComponent(item, invokerWrapper)) {
				childEnable = true;
			}
		}
		return childEnable;
	}

```

**变更前代码 (old_code)**
```java
	protected boolean processExtensionPopupChildren(Component invoker) {
		boolean childEnable = false;
		for (int index = 0; index < this.getItemCount(); index++) {
			JMenuItem item = this.getItem(index);
			if (item instanceof PopupMenuHistoryReference) {
				PopupMenuHistoryReference itemRef=(PopupMenuHistoryReference) item;
				if (itemRef.isEnableForComponent(invoker)) {
					childEnable = true;
				}
			}
		}
		return childEnable;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,12 +1,9 @@
-protected boolean processExtensionPopupChildren(Component invoker) {

+protected boolean processExtensionPopupChildren(PopupMenuUtils.PopupMenuInvokerWrapper invokerWrapper) {

 		boolean childEnable = false;

 		for (int index = 0; index < this.getItemCount(); index++) {

 			JMenuItem item = this.getItem(index);

-			if (item instanceof PopupMenuHistoryReference) {

-				PopupMenuHistoryReference itemRef=(PopupMenuHistoryReference) item;

-				if (itemRef.isEnableForComponent(invoker)) {

-					childEnable = true;

-				}

+			if (isEnableForComponent(item, invokerWrapper)) {

+				childEnable = true;

 			}

 		}

 		return childEnable;

```

---

### [63/102] `Param_125`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6240 |
| SARI | 0.7781 |
| GLEU | 0.6333 |
| METEOR | 0.7773 |
| xMatch | ✗ |

**原注释 (source)**
```
@param schemes a map of Swagger SecuritySchemeDefinition object
```

**标准注释 (ground truth)**
```
@param securitySchemeMap a map of OAS SecuritySchemeDefinition object
```

**生成注释 (generated)**
```
@param securitySchemeMap a map of SecurityScheme object
```

**当前代码 (new_code)**
```java
    public List<CodegenSecurity> fromSecurity(Map<String, SecurityScheme> securitySchemeMap) {
        if (securitySchemeMap == null) {
            return Collections.emptyList();
        }

        List<CodegenSecurity> codegenSecurities = new ArrayList<CodegenSecurity>(securitySchemeMap.size());
        for (String key : securitySchemeMap.keySet()) {
            final SecurityScheme securityScheme = securitySchemeMap.get(key);

            CodegenSecurity cs = CodegenModelFactory.newInstance(CodegenModelType.SECURITY);
            cs.name = key;
            cs.type = securityScheme.getType().toString();
            cs.isCode = cs.isPassword = cs.isApplication = cs.isImplicit = false;

            if (SecurityScheme.Type.APIKEY.equals(securityScheme.getType())) {
                cs.isBasic = cs.isOAuth = false;
                cs.isApiKey = true;
                cs.keyParamName = securityScheme.getName();
                cs.isKeyInHeader = securityScheme.getIn() == SecurityScheme.In.HEADER;
                cs.isKeyInQuery = !cs.isKeyInHeader;
            } else if (SecurityScheme.Type.HTTP.equals(securityScheme.getType())) {
                cs.isKeyInHeader = cs.isKeyInQuery = cs.isApiKey = cs.isOAuth = false;
                cs.isBasic = true;
            } else if (SecurityScheme.Type.OAUTH2.equals(securityScheme.getType())) {
                cs.isKeyInHeader = cs.isKeyInQuery = cs.isApiKey = cs.isBasic = false;
                cs.isOAuth = true;
                final OAuthFlows flows = securityScheme.getFlows();
                if (securityScheme.getFlows() == null) {
                    throw new RuntimeException("missing oauth flow in " + cs.name);
                }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public List<CodegenSecurity> fromSecurity(Map<String, SecuritySchemeDefinition> schemes) {
        if (schemes == null) {
            return Collections.emptyList();
        }

        List<CodegenSecurity> secs = new ArrayList<CodegenSecurity>(schemes.size());
        for (Iterator<Map.Entry<String, SecuritySchemeDefinition>> it = schemes.entrySet().iterator(); it.hasNext(); ) {
            final Map.Entry<String, SecuritySchemeDefinition> entry = it.next();
            final SecuritySchemeDefinition schemeDefinition = entry.getValue();

            CodegenSecurity sec = CodegenModelFactory.newInstance(CodegenModelType.SECURITY);
            sec.name = entry.getKey();
            sec.type = schemeDefinition.getType();
            sec.isCode = sec.isPassword = sec.isApplication = sec.isImplicit = false;
            sec.vendorExtensions = schemeDefinition.getVendorExtensions();

            if (schemeDefinition instanceof ApiKeyAuthDefinition) {
                final ApiKeyAuthDefinition apiKeyDefinition = (ApiKeyAuthDefinition) schemeDefinition;
                sec.isBasic = sec.isOAuth = false;
                sec.isApiKey = true;
                sec.keyParamName = apiKeyDefinition.getName();
                sec.isKeyInHeader = apiKeyDefinition.getIn() == In.HEADER;
                sec.isKeyInQuery = !sec.isKeyInHeader;
            } else if(schemeDefinition instanceof BasicAuthDefinition) {
                sec.isKeyInHeader = sec.isKeyInQuery = sec.isApiKey = sec.isOAuth = false;
                sec.isBasic = true;
            } else {
                final OAuth2Definition oauth2Definition = (OAuth2Definition) schemeDefinition;
                sec.isKeyInHeader = sec.isKeyInQuery = sec.isApiKey = sec.isBasic = false;
                sec.isOAuth = true;
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,92 +1,70 @@
-public List<CodegenSecurity> fromSecurity(Map<String, SecuritySchemeDefinition> schemes) {

-        if (schemes == null) {

+public List<CodegenSecurity> fromSecurity(Map<String, SecurityScheme> securitySchemeMap) {

+        if (securitySchemeMap == null) {

             return Collections.emptyList();

         }

 

-        List<CodegenSecurity> secs = new ArrayList<CodegenSecurity>(schemes.size());

-        for (Iterator<Map.Entry<String, SecuritySchemeDefinition>> it = schemes.entrySet().iterator(); it.hasNext(); ) {

-            final Map.Entry<String, SecuritySchemeDefinition> entry = it.next();

-            final SecuritySchemeDefinition schemeDefinition = entry.getValue();

+        List<CodegenSecurity> codegenSecurities = new ArrayList<CodegenSecurity>(securitySchemeMap.size());

+        for (String key : securitySchemeMap.keySet()) {

+            final SecurityScheme securityScheme = securitySchemeMap.get(key);

 

-            CodegenSecurity sec = CodegenModelFactory.newInstance(CodegenModelType.SECURITY);

-            sec.name = entry.getKey();

-            sec.type = schemeDefinition.getType();

-            sec.isCode = sec.isPassword = sec.isApplication = sec.isImplicit = false;

-            sec.vendorExtensions = schemeDefinition.getVendorExtensions();

+            CodegenSecurity cs = CodegenModelFactory.newInstance(CodegenModelType.SECURITY);

+            cs.name = key;

+            cs.type = securityScheme.getType().toString();

+            cs.isCode = cs.isPassword = cs.isApplication = cs.isImplicit = false;

 

-            if (schemeDefinition instanceof ApiKeyAuthDefinition) {

-                final ApiKeyAuthDefinition apiKeyDefinition = (ApiKeyAuthDefinition) schemeDefinition;

-                sec.isBasic = sec.isOAuth = false;

-                sec.isApiKey = true;

-                sec.keyParamName = apiKeyDefinition.getName();

-                sec.isKeyInHeader = apiKeyDefinition.getIn() == In.HEADER;

-                sec.isKeyInQuery = !sec.isKeyInHeader;

-            } else if(schemeDefinition instanceof BasicAuthDefinition) {

-                sec.isKeyInHeader = sec.isKeyInQuery = sec.isApiKey = sec.isOAuth = false;

-                sec.isBasic = true;

-            } else {

-                final OAuth2Definition oauth2Definition = (OAuth2Definition) schemeDefinition;

```

---

### [83/102] `Param_167`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2077 |
| SARI | 0.7940 |
| GLEU | 0.3333 |
| METEOR | 0.4136 |
| xMatch | ✗ |

**原注释 (source)**
```
@param requestRegions The input 3A regions
```

**标准注释 (ground truth)**
```
@param requestRegion The input 3A region [xmin, ymin, xmax, ymax, weight]
```

**生成注释 (generated)**
```
@param requestRegion The input 3A region
```

**当前代码 (new_code)**
```java
    public static int[] getExpectedOutputRegion(int[] requestRegion, Rect cropRect){
        Rect requestRect = new Rect(requestRegion[0], requestRegion[1],
                requestRegion[2], requestRegion[3]);
        Rect resultRect = new Rect();
        assertTrue("Input 3A region must intersect cropped region",
                    resultRect.setIntersect(requestRect, cropRect));
        return new int[] {
                resultRect.left,
                resultRect.top,
                resultRect.right,
                resultRect.bottom,
                requestRegion[4]};
    }


```

**变更前代码 (old_code)**
```java
    public static MeteringRectangle[] getExpectedOutputRegion(
            MeteringRectangle[] requestRegions, Rect cropRect){
        MeteringRectangle[] resultRegions = new MeteringRectangle[requestRegions.length];
        for (int i = 0; i < requestRegions.length; i++) {
            Rect requestRect = requestRegions[i].getRect();
            Rect resultRect = new Rect();
            assertTrue("Input 3A region must intersect cropped region",
                        resultRect.setIntersect(requestRect, cropRect));
            resultRegions[i] = new MeteringRectangle(
                    resultRect,
                    requestRegions[i].getMeteringWeight());
        }
        return resultRegions;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,14 +1,13 @@
-public static MeteringRectangle[] getExpectedOutputRegion(

-            MeteringRectangle[] requestRegions, Rect cropRect){

-        MeteringRectangle[] resultRegions = new MeteringRectangle[requestRegions.length];

-        for (int i = 0; i < requestRegions.length; i++) {

-            Rect requestRect = requestRegions[i].getRect();

-            Rect resultRect = new Rect();

-            assertTrue("Input 3A region must intersect cropped region",

-                        resultRect.setIntersect(requestRect, cropRect));

-            resultRegions[i] = new MeteringRectangle(

-                    resultRect,

-                    requestRegions[i].getMeteringWeight());

-        }

-        return resultRegions;

+public static int[] getExpectedOutputRegion(int[] requestRegion, Rect cropRect){

+        Rect requestRect = new Rect(requestRegion[0], requestRegion[1],

+                requestRegion[2], requestRegion[3]);

+        Rect resultRect = new Rect();

+        assertTrue("Input 3A region must intersect cropped region",

+                    resultRect.setIntersect(requestRect, cropRect));

+        return new int[] {

+                resultRect.left,

+                resultRect.top,

+                resultRect.right,

+                resultRect.bottom,

+                requestRegion[4]};

     }
```

---

### [13/102] `Param_24`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.2887 |
| SARI | 0.8056 |
| GLEU | 0.4286 |
| METEOR | 0.5324 |
| xMatch | ✗ |

**原注释 (source)**
```
@param prefered
```

**标准注释 (ground truth)**
```
@param preferred preferred port
```

**生成注释 (generated)**
```
@param preferred
```

**当前代码 (new_code)**
```java
    public static int availablePort(int preferred) {
        int rtn = -1;
        try {
            rtn = tryPort(preferred);
        } catch (IOException ignored) {
        }
        return rtn;
    }

```

**变更前代码 (old_code)**
```java
    public static int availablePort(int prefered) {
        int rtn = -1;
        try {
            rtn = tryPort(prefered);
        } catch (IOException e) {

        }
        return rtn;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,8 @@
-public static int availablePort(int prefered) {

+public static int availablePort(int preferred) {

         int rtn = -1;

         try {

-            rtn = tryPort(prefered);

-        } catch (IOException e) {

-

+            rtn = tryPort(preferred);

+        } catch (IOException ignored) {

         }

         return rtn;

     }
```

---

### [62/102] `Param_123`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.7413 |
| SARI | 0.8123 |
| GLEU | 0.7576 |
| METEOR | 0.9326 |
| xMatch | ✗ |

**原注释 (source)**
```
@param columnNames the comma-separated list of column names names to exclude; may be null or empty
```

**标准注释 (ground truth)**
```
@param fullyQualifiedColumnNames the comma-separated list of fully-qualified column names to exclude; may be null or
```

**生成注释 (generated)**
```
@param fullyQualifiedColumnNames the comma-separated list of column names names to exclude; may be null or empty
```

**当前代码 (new_code)**
```java
    public static Predicate<ColumnId> excludeColumns(String fullyQualifiedColumnNames) {
        return Predicates.excludes(fullyQualifiedColumnNames, ColumnId::toString);
    }

```

**变更前代码 (old_code)**
```java
    public static Predicate<ColumnId> excludeColumns(String columnNames) {
        return Predicates.excludes(columnNames, ColumnId::toString);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static Predicate<ColumnId> excludeColumns(String columnNames) {

-        return Predicates.excludes(columnNames, ColumnId::toString);

+public static Predicate<ColumnId> excludeColumns(String fullyQualifiedColumnNames) {

+        return Predicates.excludes(fullyQualifiedColumnNames, ColumnId::toString);

     }
```

---

### [30/102] `Param_58`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5475 |
| SARI | 0.8190 |
| GLEU | 0.5556 |
| METEOR | 0.5350 |
| xMatch | ✗ |

**原注释 (source)**
```
@param arg0 the object
```

**标准注释 (ground truth)**
```
@param reference the service reference
```

**生成注释 (generated)**
```
@param reference the object
```

**当前代码 (new_code)**
```java
    public int compareTo(Object reference) {

        ServiceReference other = (ServiceReference) reference;

        Long id = (Long) getProperty(Constants.SERVICE_ID);
        Long otherId = (Long) other.getProperty(Constants.SERVICE_ID);

        if (id.equals(otherId)) {
            return 0; // same service
        }

        Integer rank = (Integer) getProperty(Constants.SERVICE_RANKING);
        Integer otherRank = (Integer) other
                .getProperty(Constants.SERVICE_RANKING);

        // If no rank, then spec says it defaults to zero.
        rank = (rank == null) ? new Integer(0) : rank;
        otherRank = (otherRank == null) ? new Integer(0) : otherRank;

        // Sort by rank in ascending order.
        if (rank.compareTo(otherRank) < 0) {
            return -1; // lower rank
        } else if (rank.compareTo(otherRank) > 0) {
            return 1; // higher rank
        }

        // If ranks are equal, then sort by service id in descending order.
        return (id.compareTo(otherId) < 0) ? 1 : -1;
    }

// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public int compareTo(Object arg0) {
        throw new UnsupportedOperationException("This feature has not yet been implemented.");

    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,29 @@
-public int compareTo(Object arg0) {

-        throw new UnsupportedOperationException("This feature has not yet been implemented.");

+public int compareTo(Object reference) {

 

+        ServiceReference other = (ServiceReference) reference;

+

+        Long id = (Long) getProperty(Constants.SERVICE_ID);

+        Long otherId = (Long) other.getProperty(Constants.SERVICE_ID);

+

+        if (id.equals(otherId)) {

+            return 0; // same service

+        }

+

+        Integer rank = (Integer) getProperty(Constants.SERVICE_RANKING);

+        Integer otherRank = (Integer) other

+                .getProperty(Constants.SERVICE_RANKING);

+

+        // If no rank, then spec says it defaults to zero.

+        rank = (rank == null) ? new Integer(0) : rank;

+        otherRank = (otherRank == null) ? new Integer(0) : otherRank;

+

+        // Sort by rank in ascending order.

+        if (rank.compareTo(otherRank) < 0) {

+            return -1; // lower rank

+        } else if (rank.compareTo(otherRank) > 0) {

+            return 1; // higher rank

+        }

+

+        // If ranks are equal, then sort by service id in descending order.

+        return (id.compareTo(otherId) < 0) ? 1 : -1;

     }
```

---

### [48/102] `Param_95`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.6192 |
| SARI | 0.8239 |
| GLEU | 0.6400 |
| METEOR | 0.7836 |
| xMatch | ✗ |

**原注释 (source)**
```
@param clazz the annotation class to check for
```

**标准注释 (ground truth)**
```
@param fqcn the fully qualified class name of the annotation to check for
```

**生成注释 (generated)**
```
@param fqcn the fully qualified class name to check for
```

**当前代码 (new_code)**
```java
	public static AnnotationMirror getAnnotationMirror(Element element, String fqcn) {
		assert element != null;
		assert fqcn != null;

		AnnotationMirror mirror = null;
		for ( AnnotationMirror am : element.getAnnotationMirrors() ) {
			if ( isAnnotationMirrorOfType( am, fqcn ) ) {
				mirror = am;
				break;
			}
		}
		return mirror;
	}

```

**变更前代码 (old_code)**
```java
	public static AnnotationMirror getAnnotationMirror(Element element, Class<? extends Annotation> clazz) {
		assert clazz != null;
		return getAnnotationMirror( element, clazz.getName() );
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,13 @@
-public static AnnotationMirror getAnnotationMirror(Element element, Class<? extends Annotation> clazz) {

-		assert clazz != null;

-		return getAnnotationMirror( element, clazz.getName() );

+public static AnnotationMirror getAnnotationMirror(Element element, String fqcn) {

+		assert element != null;

+		assert fqcn != null;

+

+		AnnotationMirror mirror = null;

+		for ( AnnotationMirror am : element.getAnnotationMirrors() ) {

+			if ( isAnnotationMirrorOfType( am, fqcn ) ) {

+				mirror = am;

+				break;

+			}

+		}

+		return mirror;

 	}
```

---

### [70/102] `Param_139`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.3976 |
| SARI | 0.8444 |
| GLEU | 0.6000 |
| METEOR | 0.9498 |
| xMatch | ✗ |

**原注释 (source)**
```
@param operator operator
```

**标准注释 (ground truth)**
```
@param operation
```

**生成注释 (generated)**
```
@param operation operator
```

**当前代码 (new_code)**
```java
    public static BooleanOperation predicate(Operator operation, Expression<?>... args) {
        return new BooleanOperation(operation, args);
    }

```

**变更前代码 (old_code)**
```java
    public static BooleanOperation predicate(Operator operator, Expression<?>... args) {
        return new BooleanOperation(operator, args);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static BooleanOperation predicate(Operator operator, Expression<?>... args) {

-        return new BooleanOperation(operator, args);

+public static BooleanOperation predicate(Operator operation, Expression<?>... args) {

+        return new BooleanOperation(operation, args);

     }
```

---

### [94/102] `Param_190`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.5342 |
| SARI | 0.8484 |
| GLEU | 0.5882 |
| METEOR | 0.9085 |
| xMatch | ✗ |

**原注释 (source)**
```
@param values the values for the new row
```

**标准注释 (ground truth)**
```
@param inputValues The values for the new row.
```

**生成注释 (generated)**
```
@param inputValues the values for the new row
```

**当前代码 (new_code)**
```java
    private long insertData(ContentValues inputValues, boolean callerIsSyncAdapter) {
        final Long rawContactId = inputValues.getAsLong(Data.RAW_CONTACT_ID);
        if (rawContactId == null) {
            throw new IllegalArgumentException(Data.RAW_CONTACT_ID + " is required");
        }

        final String mimeType = inputValues.getAsString(Data.MIMETYPE);
        if (TextUtils.isEmpty(mimeType)) {
            throw new IllegalArgumentException(Data.MIMETYPE + " is required");
        }

        // The input seem valid, create a shallow copy.
        final ContentValues values = new ContentValues(inputValues);

        // Populate the relevant values before inserting the new entry into the database.
        replacePackageNameByPackageId(values);

        // Replace the mimetype by the corresponding mimetype ID.
        values.put(DataColumns.MIMETYPE_ID, mDbHelper.get().getMimeTypeId(mimeType));
        values.remove(Data.MIMETYPE);

        // Insert the new entry.
        final SQLiteDatabase db = mDbHelper.get().getWritableDatabase();
        final TransactionContext context = mTransactionContext.get();
        final long dataId = getDataRowHandler(mimeType).insert(db, context, rawContactId, values);
        context.markRawContactDirtyAndChanged(rawContactId, callerIsSyncAdapter);
        context.rawContactUpdated(rawContactId);

        return dataId;
    }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    private long insertData(ContentValues values, boolean callerIsSyncAdapter) {
        long id = 0;
        mValues.clear();
        mValues.putAll(values);

        Long rawContactId = mValues.getAsLong(Data.RAW_CONTACT_ID);
        if (rawContactId == null) {
            throw new IllegalArgumentException(Data.RAW_CONTACT_ID + " is required");
        }

        // Replace package with internal mapping.
        final String packageName = mValues.getAsString(Data.RES_PACKAGE);
        if (packageName != null) {
            mValues.put(DataColumns.PACKAGE_ID, mDbHelper.get().getPackageId(packageName));
        }
        mValues.remove(Data.RES_PACKAGE);

        // Replace mimetype with internal mapping.
        final String mimeType = mValues.getAsString(Data.MIMETYPE);
        if (TextUtils.isEmpty(mimeType)) {
            throw new IllegalArgumentException(Data.MIMETYPE + " is required");
        }

        mValues.put(DataColumns.MIMETYPE_ID, mDbHelper.get().getMimeTypeId(mimeType));
        mValues.remove(Data.MIMETYPE);

        DataRowHandler rowHandler = getDataRowHandler(mimeType);
        final SQLiteDatabase db = mDbHelper.get().getWritableDatabase();
        id = rowHandler.insert(db, mTransactionContext.get(), rawContactId, mValues);
        mTransactionContext.get().markRawContactDirtyAndChanged(rawContactId, callerIsSyncAdapter);
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,33 +1,30 @@
-private long insertData(ContentValues values, boolean callerIsSyncAdapter) {

-        long id = 0;

-        mValues.clear();

-        mValues.putAll(values);

-

-        Long rawContactId = mValues.getAsLong(Data.RAW_CONTACT_ID);

+private long insertData(ContentValues inputValues, boolean callerIsSyncAdapter) {

+        final Long rawContactId = inputValues.getAsLong(Data.RAW_CONTACT_ID);

         if (rawContactId == null) {

             throw new IllegalArgumentException(Data.RAW_CONTACT_ID + " is required");

         }

 

-        // Replace package with internal mapping.

-        final String packageName = mValues.getAsString(Data.RES_PACKAGE);

-        if (packageName != null) {

-            mValues.put(DataColumns.PACKAGE_ID, mDbHelper.get().getPackageId(packageName));

-        }

-        mValues.remove(Data.RES_PACKAGE);

-

-        // Replace mimetype with internal mapping.

-        final String mimeType = mValues.getAsString(Data.MIMETYPE);

+        final String mimeType = inputValues.getAsString(Data.MIMETYPE);

         if (TextUtils.isEmpty(mimeType)) {

             throw new IllegalArgumentException(Data.MIMETYPE + " is required");

         }

 

-        mValues.put(DataColumns.MIMETYPE_ID, mDbHelper.get().getMimeTypeId(mimeType));

-        mValues.remove(Data.MIMETYPE);

+        // The input seem valid, create a shallow copy.

+        final ContentValues values = new ContentValues(inputValues);

 

-        DataRowHandler rowHandler = getDataRowHandler(mimeType);

+        // Populate the relevant values before inserting the new entry into the database.

+        replacePackageNameByPackageId(values);

+

+        // Replace the mimetype by the corresponding mimetype ID.

+        values.put(DataColumns.MIMETYPE_ID, mDbHelper.get().getMimeTypeId(mimeType));

```

---

### [29/102] `Param_56`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 0.4029 |
| SARI | 0.8611 |
| GLEU | 0.6000 |
| METEOR | 0.6553 |
| xMatch | ✗ |

**原注释 (source)**
```
@param operation
```

**标准注释 (ground truth)**
```
@param operator operator
```

**生成注释 (generated)**
```
@param operator
```

**当前代码 (new_code)**
```java
    public static BooleanOperation booleanOperation(Operator operator, Expression<?>... args) {
        return predicate(operator, args);
    }

```

**变更前代码 (old_code)**
```java
    public static BooleanOperation booleanOperation(Operator operation, Expression<?>... args) {
        return predicate(operation, args);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static BooleanOperation booleanOperation(Operator operation, Expression<?>... args) {

-        return predicate(operation, args);

+public static BooleanOperation booleanOperation(Operator operator, Expression<?>... args) {

+        return predicate(operator, args);

     }
```

---

### [1/102] `Param_0`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9993 |
| xMatch | ✓ |

**原注释 (source)**
```
@param file file to upload (required)
```

**标准注释 (ground truth)**
```
@param requiredFile file to upload (required)
```

**生成注释 (generated)**
```
@param requiredFile file to upload (required)
```

**当前代码 (new_code)**
```java
  public ApiResponse<ModelApiResponse> uploadFileWithRequiredFileWithHttpInfo(Long petId, File requiredFile, String additionalMetadata) throws ApiException {
    Object localVarPostBody = new Object();
    
    // verify the required parameter 'petId' is set
    if (petId == null) {
      throw new ApiException(400, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");
    }
    
    // verify the required parameter 'requiredFile' is set
    if (requiredFile == null) {
      throw new ApiException(400, "Missing the required parameter 'requiredFile' when calling uploadFileWithRequiredFile");
    }
    
    // create path and map variables
    String localVarPath = "/fake/{petId}/uploadImageWithRequiredFile"
      .replaceAll("\\{" + "petId" + "\\}", apiClient.escapeString(petId.toString()));

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    if (additionalMetadata != null)
      localVarFormParams.put("additionalMetadata", additionalMetadata);
if (requiredFile != null)
      localVarFormParams.put("requiredFile", requiredFile);

    final String[] localVarAccepts = {
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public ApiResponse<ModelApiResponse> uploadFileWithRequiredFileWithHttpInfo(Long petId, File file, String additionalMetadata) throws ApiException {
    Object localVarPostBody = new Object();
    
    // verify the required parameter 'petId' is set
    if (petId == null) {
      throw new ApiException(400, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");
    }
    
    // verify the required parameter 'file' is set
    if (file == null) {
      throw new ApiException(400, "Missing the required parameter 'file' when calling uploadFileWithRequiredFile");
    }
    
    // create path and map variables
    String localVarPath = "/fake/{petId}/uploadImageWithRequiredFile"
      .replaceAll("\\{" + "petId" + "\\}", apiClient.escapeString(petId.toString()));

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    if (additionalMetadata != null)
      localVarFormParams.put("additionalMetadata", additionalMetadata);
if (file != null)
      localVarFormParams.put("file", file);

    final String[] localVarAccepts = {
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public ApiResponse<ModelApiResponse> uploadFileWithRequiredFileWithHttpInfo(Long petId, File file, String additionalMetadata) throws ApiException {

+public ApiResponse<ModelApiResponse> uploadFileWithRequiredFileWithHttpInfo(Long petId, File requiredFile, String additionalMetadata) throws ApiException {

     Object localVarPostBody = new Object();

     

     // verify the required parameter 'petId' is set

@@ -6,9 +6,9 @@
       throw new ApiException(400, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");

     }

     

-    // verify the required parameter 'file' is set

-    if (file == null) {

-      throw new ApiException(400, "Missing the required parameter 'file' when calling uploadFileWithRequiredFile");

+    // verify the required parameter 'requiredFile' is set

+    if (requiredFile == null) {

+      throw new ApiException(400, "Missing the required parameter 'requiredFile' when calling uploadFileWithRequiredFile");

     }

     

     // create path and map variables

@@ -24,8 +24,8 @@
     

     if (additionalMetadata != null)

       localVarFormParams.put("additionalMetadata", additionalMetadata);

-if (file != null)

-      localVarFormParams.put("file", file);

+if (requiredFile != null)

+      localVarFormParams.put("requiredFile", requiredFile);

 

     final String[] localVarAccepts = {

       "application/json"

```

---

### [11/102] `Param_20`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9993 |
| xMatch | ✓ |

**原注释 (source)**
```
@param file file to upload (required)
```

**标准注释 (ground truth)**
```
@param requiredFile file to upload (required)
```

**生成注释 (generated)**
```
@param requiredFile file to upload (required)
```

**当前代码 (new_code)**
```java
  public ModelApiResponse uploadFileWithRequiredFile(Long petId, File requiredFile, String additionalMetadata) throws ApiException {
    return uploadFileWithRequiredFileWithHttpInfo(petId, requiredFile, additionalMetadata).getData();
      }

```

**变更前代码 (old_code)**
```java
  public ModelApiResponse uploadFileWithRequiredFile(Long petId, File file, String additionalMetadata) throws ApiException {
    return uploadFileWithRequiredFileWithHttpInfo(petId, file, additionalMetadata).getData();
      }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public ModelApiResponse uploadFileWithRequiredFile(Long petId, File file, String additionalMetadata) throws ApiException {

-    return uploadFileWithRequiredFileWithHttpInfo(petId, file, additionalMetadata).getData();

+public ModelApiResponse uploadFileWithRequiredFile(Long petId, File requiredFile, String additionalMetadata) throws ApiException {

+    return uploadFileWithRequiredFileWithHttpInfo(petId, requiredFile, additionalMetadata).getData();

       }
```

---

### [33/102] `Param_64`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9996 |
| xMatch | ✓ |

**原注释 (source)**
```
@param body Input composite as post body (optional)
```

**标准注释 (ground truth)**
```
@param outerComposite Input composite as post body (optional)
```

**生成注释 (generated)**
```
@param outerComposite Input composite as post body (optional)
```

**当前代码 (new_code)**
```java
    public OuterComposite fakeOuterCompositeSerialize(OuterComposite outerComposite) throws ApiException {
        ApiResponse<OuterComposite> resp = fakeOuterCompositeSerializeWithHttpInfo(outerComposite);
        return resp.getData();
    }

```

**变更前代码 (old_code)**
```java
    public OuterComposite fakeOuterCompositeSerialize(OuterComposite body) throws ApiException {
        ApiResponse<OuterComposite> resp = fakeOuterCompositeSerializeWithHttpInfo(body);
        return resp.getData();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public OuterComposite fakeOuterCompositeSerialize(OuterComposite body) throws ApiException {

-        ApiResponse<OuterComposite> resp = fakeOuterCompositeSerializeWithHttpInfo(body);

+public OuterComposite fakeOuterCompositeSerialize(OuterComposite outerComposite) throws ApiException {

+        ApiResponse<OuterComposite> resp = fakeOuterCompositeSerializeWithHttpInfo(outerComposite);

         return resp.getData();

     }
```

---

### [39/102] `Param_77`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9977 |
| xMatch | ✓ |

**原注释 (source)**
```
@param file file to upload
```

**标准注释 (ground truth)**
```
@param requiredFile file to upload
```

**生成注释 (generated)**
```
@param requiredFile file to upload
```

**当前代码 (new_code)**
```java
    public ModelApiResponse uploadFileWithRequiredFile(Long petId, File requiredFile, String additionalMetadata) throws RestClientException {
        Object postBody = new Object();
        
        // verify the required parameter 'petId' is set
        if (petId == null) {
            throw new HttpClientErrorException(HttpStatus.BAD_REQUEST, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");
        }
        
        // verify the required parameter 'requiredFile' is set
        if (requiredFile == null) {
            throw new HttpClientErrorException(HttpStatus.BAD_REQUEST, "Missing the required parameter 'requiredFile' when calling uploadFileWithRequiredFile");
        }
        
        // create path and map variables
        final Map<String, Object> uriVariables = new HashMap<String, Object>();
        uriVariables.put("petId", petId);
        String path = UriComponentsBuilder.fromPath("/fake/{petId}/uploadImageWithRequiredFile").buildAndExpand(uriVariables).toUriString();
        
        final MultiValueMap<String, String> queryParams = new LinkedMultiValueMap<String, String>();
        final HttpHeaders headerParams = new HttpHeaders();
        final MultiValueMap<String, Object> formParams = new LinkedMultiValueMap<String, Object>();
        
        if (additionalMetadata != null)
            formParams.add("additionalMetadata", additionalMetadata);
        if (requiredFile != null)
            formParams.add("requiredFile", new FileSystemResource(requiredFile));

        final String[] accepts = { 
            "application/json"
        };
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public ModelApiResponse uploadFileWithRequiredFile(Long petId, File file, String additionalMetadata) throws RestClientException {
        Object postBody = new Object();
        
        // verify the required parameter 'petId' is set
        if (petId == null) {
            throw new HttpClientErrorException(HttpStatus.BAD_REQUEST, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");
        }
        
        // verify the required parameter 'file' is set
        if (file == null) {
            throw new HttpClientErrorException(HttpStatus.BAD_REQUEST, "Missing the required parameter 'file' when calling uploadFileWithRequiredFile");
        }
        
        // create path and map variables
        final Map<String, Object> uriVariables = new HashMap<String, Object>();
        uriVariables.put("petId", petId);
        String path = UriComponentsBuilder.fromPath("/fake/{petId}/uploadImageWithRequiredFile").buildAndExpand(uriVariables).toUriString();
        
        final MultiValueMap<String, String> queryParams = new LinkedMultiValueMap<String, String>();
        final HttpHeaders headerParams = new HttpHeaders();
        final MultiValueMap<String, Object> formParams = new LinkedMultiValueMap<String, Object>();
        
        if (additionalMetadata != null)
            formParams.add("additionalMetadata", additionalMetadata);
        if (file != null)
            formParams.add("file", new FileSystemResource(file));

        final String[] accepts = { 
            "application/json"
        };
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public ModelApiResponse uploadFileWithRequiredFile(Long petId, File file, String additionalMetadata) throws RestClientException {

+public ModelApiResponse uploadFileWithRequiredFile(Long petId, File requiredFile, String additionalMetadata) throws RestClientException {

         Object postBody = new Object();

         

         // verify the required parameter 'petId' is set

@@ -6,9 +6,9 @@
             throw new HttpClientErrorException(HttpStatus.BAD_REQUEST, "Missing the required parameter 'petId' when calling uploadFileWithRequiredFile");

         }

         

-        // verify the required parameter 'file' is set

-        if (file == null) {

-            throw new HttpClientErrorException(HttpStatus.BAD_REQUEST, "Missing the required parameter 'file' when calling uploadFileWithRequiredFile");

+        // verify the required parameter 'requiredFile' is set

+        if (requiredFile == null) {

+            throw new HttpClientErrorException(HttpStatus.BAD_REQUEST, "Missing the required parameter 'requiredFile' when calling uploadFileWithRequiredFile");

         }

         

         // create path and map variables

@@ -22,8 +22,8 @@
         

         if (additionalMetadata != null)

             formParams.add("additionalMetadata", additionalMetadata);

-        if (file != null)

-            formParams.add("file", new FileSystemResource(file));

+        if (requiredFile != null)

+            formParams.add("requiredFile", new FileSystemResource(requiredFile));

 

         final String[] accepts = { 

             "application/json"

```

---

### [54/102] `Param_107`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9960 |
| xMatch | ✓ |

**原注释 (source)**
```
@param client client model
```

**标准注释 (ground truth)**
```
@param body client model
```

**生成注释 (generated)**
```
@param body client model
```

**当前代码 (new_code)**
```java
    public Client call123testSpecialTags(Client body, Map<String, Object> params) throws IOException {
        HttpResponse response = call123testSpecialTagsForHttpResponse(body, params);
        TypeReference typeRef = new TypeReference<Client>() {};
        return apiClient.getObjectMapper().readValue(response.getContent(), typeRef);
    }

```

**变更前代码 (old_code)**
```java
    public Client call123testSpecialTags(Client client, Map<String, Object> params) throws IOException {
        HttpResponse response = call123testSpecialTagsForHttpResponse(client, params);
        TypeReference typeRef = new TypeReference<Client>() {};
        return apiClient.getObjectMapper().readValue(response.getContent(), typeRef);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public Client call123testSpecialTags(Client client, Map<String, Object> params) throws IOException {

-        HttpResponse response = call123testSpecialTagsForHttpResponse(client, params);

+public Client call123testSpecialTags(Client body, Map<String, Object> params) throws IOException {

+        HttpResponse response = call123testSpecialTagsForHttpResponse(body, params);

         TypeReference typeRef = new TypeReference<Client>() {};

         return apiClient.getObjectMapper().readValue(response.getContent(), typeRef);

     }
```

---

### [58/102] `Param_115`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9960 |
| xMatch | ✓ |

**原注释 (source)**
```
@param tokens the tokens
```

**标准注释 (ground truth)**
```
@param siteTokens the tokens
```

**生成注释 (generated)**
```
@param siteTokens the tokens
```

**当前代码 (new_code)**
```java
	private HttpSession getMatchingHttpSession(List<HttpCookie> cookies, final HttpSessionTokensSet siteTokens) {

		// Pre-checks
		if (sessions.isEmpty()) {
			return null;
		}

		List<HttpSession> matchingSessions = new LinkedList<>(sessions);
		for (String token : siteTokens.getTokensSet()) {
			// Get the corresponding cookie from the cookies list
			HttpCookie matchingCookie = null;
			for (HttpCookie cookie : cookies) {
				if (cookie.getName().equals(token)) {
					matchingCookie = cookie;
					break;
				}
			}
			// Filter the sessions that do not match the cookie value
			Iterator<HttpSession> it = matchingSessions.iterator();
			while (it.hasNext()) {
				if (!it.next().matchesToken(token, matchingCookie)) {
					it.remove();
				}
			}
		}

		// Return the matching session
		if (matchingSessions.size() >= 1) {
			if (matchingSessions.size() > 1) {
				log.warn("Multiple sessions matching the cookies from response for site: " + getSite()
// ... (truncated)
```

**变更前代码 (old_code)**
```java
	private HttpSession getMatchingHttpSession(List<HttpCookie> cookies, final Set<String> tokens) {

		// Pre-checks
		if (sessions.isEmpty()) {
			return null;
		}

		List<HttpSession> matchingSessions = new LinkedList<>(sessions);
		for (String token : tokens) {
			// Get the corresponding cookie from the cookies list
			HttpCookie matchingCookie = null;
			for (HttpCookie cookie : cookies) {
				if (cookie.getName().equals(token)) {
					matchingCookie = cookie;
					break;
				}
			}
			// Filter the sessions that do not match the cookie value
			Iterator<HttpSession> it = matchingSessions.iterator();
			while (it.hasNext()) {
				if (!it.next().matchesToken(token, matchingCookie)) {
					it.remove();
				}
			}
		}

		// Return the matching session
		if (matchingSessions.size() >= 1) {
			if (matchingSessions.size() > 1) {
				log.warn("Multiple sessions matching the cookies from response for site: " + getSite()
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-private HttpSession getMatchingHttpSession(List<HttpCookie> cookies, final Set<String> tokens) {

+private HttpSession getMatchingHttpSession(List<HttpCookie> cookies, final HttpSessionTokensSet siteTokens) {

 

 		// Pre-checks

 		if (sessions.isEmpty()) {

@@ -6,7 +6,7 @@
 		}

 

 		List<HttpSession> matchingSessions = new LinkedList<>(sessions);

-		for (String token : tokens) {

+		for (String token : siteTokens.getTokensSet()) {

 			// Get the corresponding cookie from the cookies list

 			HttpCookie matchingCookie = null;

 			for (HttpCookie cookie : cookies) {

```

---

### [71/102] `Param_141`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9922 |
| xMatch | ✓ |

**原注释 (source)**
```
@param signatureType SignatureType
```

**标准注释 (ground truth)**
```
@param signatureType OAuth1SignatureType
```

**生成注释 (generated)**
```
@param signatureType OAuth1SignatureType
```

**当前代码 (new_code)**
```java
    public ServiceBuilder signatureType(OAuth1SignatureType signatureType) {
        this.signatureType = signatureType;
        return this;
    }

```

**变更前代码 (old_code)**
```java
    public ServiceBuilder signatureType(SignatureType signatureType) {
        Preconditions.checkNotNull(signatureType, "Signature type can't be null");
        this.signatureType = signatureType;
        return this;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,4 @@
-public ServiceBuilder signatureType(SignatureType signatureType) {

-        Preconditions.checkNotNull(signatureType, "Signature type can't be null");

+public ServiceBuilder signatureType(OAuth1SignatureType signatureType) {

         this.signatureType = signatureType;

         return this;

     }
```

---

### [82/102] `Param_165`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9993 |
| xMatch | ✓ |

**原注释 (source)**
```
@param instant instant from 1970-01-01T00:00:00 local time
```

**标准注释 (ground truth)**
```
@param localInstant the instant from 1970-01-01T00:00:00 local time
```

**生成注释 (generated)**
```
@param localInstant the instant from 1970-01-01T00:00:00 local time
```

**当前代码 (new_code)**
```java
    private long localToUTC(long localInstant) {
        DateTimeZone zone = getZone();
        int offset = zone.getOffsetFromLocal(localInstant);
        localInstant -= offset;
        if (offset != zone.getOffset(localInstant)) {
            throw new IllegalInstantException(localInstant, zone.getID());
        }
        return localInstant;
    }

```

**变更前代码 (old_code)**
```java
    private long localToUTC(long instant) {
        DateTimeZone zone = getZone();
        int offset = zone.getOffsetFromLocal(instant);
        instant -= offset;
        if (offset != zone.getOffset(instant)) {
            throw new IllegalArgumentException
                ("Illegal instant due to time zone offset transition: " +
                    DateTimeFormat.forPattern("yyyy-MM-dd'T'HH:mm:ss.SSS").print(new Instant(instant)));
        }
        return instant;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,9 @@
-private long localToUTC(long instant) {

+private long localToUTC(long localInstant) {

         DateTimeZone zone = getZone();

-        int offset = zone.getOffsetFromLocal(instant);

-        instant -= offset;

-        if (offset != zone.getOffset(instant)) {

-            throw new IllegalArgumentException

-                ("Illegal instant due to time zone offset transition: " +

-                    DateTimeFormat.forPattern("yyyy-MM-dd'T'HH:mm:ss.SSS").print(new Instant(instant)));

+        int offset = zone.getOffsetFromLocal(localInstant);

+        localInstant -= offset;

+        if (offset != zone.getOffset(localInstant)) {

+            throw new IllegalInstantException(localInstant, zone.getID());

         }

-        return instant;

+        return localInstant;

     }
```

---

### [86/102] `Param_173`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9996 |
| xMatch | ✓ |

**原注释 (source)**
```
@param millis the time instant in millis to query.
```

**标准注释 (ground truth)**
```
@param instant the time instant in millis to query.
```

**生成注释 (generated)**
```
@param instant the time instant in millis to query.
```

**当前代码 (new_code)**
```java
    public int get(long instant) {
        int year = iChronology.year().get(instant);
        //
        long firstWeekMillis1 = iChronology.getFirstWeekOfYearMillis(year);
        if (instant < firstWeekMillis1) {
            return iChronology.getWeeksInYear(year - 1);
        }
        long firstWeekMillis2 = iChronology.getFirstWeekOfYearMillis(year + 1);
        if (instant >= firstWeekMillis2) {
            return 1;
        }
        return (int) ((instant - firstWeekMillis1) / DateTimeConstants.MILLIS_PER_WEEK) + 1;
    }

```

**变更前代码 (old_code)**
```java
    public int get(long millis) {
        int year = iChronology.year().get(millis);
        //
        long firstWeekMillis1 = iChronology.getFirstWeekOfYearMillis(year);
        if (millis < firstWeekMillis1) {
            return iChronology.getWeeksInYear(year - 1);
        }
        long firstWeekMillis2 = iChronology.getFirstWeekOfYearMillis(year + 1);
        if (millis >= firstWeekMillis2) {
            return 1;
        }
        return (int) ((millis - firstWeekMillis1) / DateTimeConstants.MILLIS_PER_WEEK) + 1;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,13 +1,13 @@
-public int get(long millis) {

-        int year = iChronology.year().get(millis);

+public int get(long instant) {

+        int year = iChronology.year().get(instant);

         //

         long firstWeekMillis1 = iChronology.getFirstWeekOfYearMillis(year);

-        if (millis < firstWeekMillis1) {

+        if (instant < firstWeekMillis1) {

             return iChronology.getWeeksInYear(year - 1);

         }

         long firstWeekMillis2 = iChronology.getFirstWeekOfYearMillis(year + 1);

-        if (millis >= firstWeekMillis2) {

+        if (instant >= firstWeekMillis2) {

             return 1;

         }

-        return (int) ((millis - firstWeekMillis1) / DateTimeConstants.MILLIS_PER_WEEK) + 1;

+        return (int) ((instant - firstWeekMillis1) / DateTimeConstants.MILLIS_PER_WEEK) + 1;

     }
```

---

### [92/102] `Param_186`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9996 |
| xMatch | ✓ |

**原注释 (source)**
```
@param body Input boolean as post body (optional)
```

**标准注释 (ground truth)**
```
@param booleanPostBody Input boolean as post body (optional)
```

**生成注释 (generated)**
```
@param booleanPostBody Input boolean as post body (optional)
```

**当前代码 (new_code)**
```java
  public Boolean fakeOuterBooleanSerialize(Boolean booleanPostBody) throws ApiException {
    Object localVarPostBody = booleanPostBody;
    
    // create path and map variables
    String localVarPath = "/fake/outer/boolean".replaceAll("\\{format\\}","json");

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    
    final String[] localVarAccepts = {
      "*/*"
    };
    final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

    final String[] localVarContentTypes = {
      
    };
    final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

    String[] localVarAuthNames = new String[] {  };

    GenericType<Boolean> localVarReturnType = new GenericType<Boolean>() {};
    return apiClient.invokeAPI(localVarPath, "POST", localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAccept, localVarContentType, localVarAuthNames, localVarReturnType);
      }

```

**变更前代码 (old_code)**
```java
  public Boolean fakeOuterBooleanSerialize(Boolean body) throws ApiException {
    Object localVarPostBody = body;
    
    // create path and map variables
    String localVarPath = "/fake/outer/boolean".replaceAll("\\{format\\}","json");

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    
    final String[] localVarAccepts = {
      
    };
    final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

    final String[] localVarContentTypes = {
      
    };
    final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

    String[] localVarAuthNames = new String[] {  };

    GenericType<Boolean> localVarReturnType = new GenericType<Boolean>() {};
    return apiClient.invokeAPI(localVarPath, "POST", localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAccept, localVarContentType, localVarAuthNames, localVarReturnType);
      }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public Boolean fakeOuterBooleanSerialize(Boolean body) throws ApiException {

-    Object localVarPostBody = body;

+public Boolean fakeOuterBooleanSerialize(Boolean booleanPostBody) throws ApiException {

+    Object localVarPostBody = booleanPostBody;

     

     // create path and map variables

     String localVarPath = "/fake/outer/boolean".replaceAll("\\{format\\}","json");

@@ -13,7 +13,7 @@
     

     

     final String[] localVarAccepts = {

-      

+      "*/*"

     };

     final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

 

```

---

### [100/102] `Param_202`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9996 |
| xMatch | ✓ |

**原注释 (source)**
```
@param millis the time instant in millis to update.
```

**标准注释 (ground truth)**
```
@param instant the time instant in millis to update.
```

**生成注释 (generated)**
```
@param instant the time instant in millis to update.
```

**当前代码 (new_code)**
```java
    public long add(long instant, int months) {
        if (months == 0) {
            return instant; // the easy case
        }
        //
        // Save time part first.
        //
        long timePart = iChronology.millisOfDay().get(instant);
        //
        //
        // Get this year and month.
        //
        int thisYear = iChronology.year().get(instant);
        int thisMonth = iChronology.getMonthOfYear(instant, thisYear);
        // ----------------------------------------------------------
        //
        // Do not refactor without careful consideration.
        // Order of calculation is important.
        //
        int yearToUse;
        // Initially, monthToUse is zero-based
        int monthToUse = thisMonth - 1 + months;
        if (monthToUse >= 0) {
            yearToUse = thisYear + (monthToUse / MAX);
            monthToUse = (monthToUse % MAX) + 1;
        } else {
            yearToUse = thisYear + (monthToUse / MAX) - 1;
            monthToUse = Math.abs(monthToUse);
            int remMonthToUse = monthToUse % MAX;
            // Take care of the boundary condition
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public long add(long millis, int months) {
        if (months == 0) {
            return millis; // the easy case
        }
        //
        // Save time part first.
        //
        long timePart = iChronology.millisOfDay().get(millis);
        //
        //
        // Get this year and month.
        //
        int thisYear = iChronology.year().get(millis);
        int thisMonth = iChronology.getMonthOfYear(millis, thisYear);
        // ----------------------------------------------------------
        //
        // Do not refactor without careful consideration.
        // Order of calculation is important.
        //
        int yearToUse;
        // Initially, monthToUse is zero-based
        int monthToUse = thisMonth - 1 + months;
        if (monthToUse >= 0) {
            yearToUse = thisYear + (monthToUse / MAX);
            monthToUse = (monthToUse % MAX) + 1;
        } else {
            yearToUse = thisYear + (monthToUse / MAX) - 1;
            monthToUse = Math.abs(monthToUse);
            int remMonthToUse = monthToUse % MAX;
            // Take care of the boundary condition
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,17 +1,17 @@
-public long add(long millis, int months) {

+public long add(long instant, int months) {

         if (months == 0) {

-            return millis; // the easy case

+            return instant; // the easy case

         }

         //

         // Save time part first.

         //

-        long timePart = iChronology.millisOfDay().get(millis);

+        long timePart = iChronology.millisOfDay().get(instant);

         //

         //

         // Get this year and month.

         //

-        int thisYear = iChronology.year().get(millis);

-        int thisMonth = iChronology.getMonthOfYear(millis, thisYear);

+        int thisYear = iChronology.year().get(instant);

+        int thisMonth = iChronology.getMonthOfYear(instant, thisYear);

         // ----------------------------------------------------------

         //

         // Do not refactor without careful consideration.

@@ -43,7 +43,7 @@
         //

         // Quietly force DOM to nearest sane value.

         //

-        int dayToUse = iChronology.getDayOfMonth(millis, thisYear, thisMonth);

+        int dayToUse = iChronology.getDayOfMonth(instant, thisYear, thisMonth);

         int maxDay = iChronology.getDaysInYearMonth(yearToUse, monthToUse);

         if (dayToUse > maxDay) {

             dayToUse = maxDay;

```

---

### [101/102] `Param_204`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9167 |
| GLEU | 1.0000 |
| METEOR | 0.9993 |
| xMatch | ✓ |

**原注释 (source)**
```
@param file file to upload (required)
```

**标准注释 (ground truth)**
```
@param requiredFile file to upload (required)
```

**生成注释 (generated)**
```
@param requiredFile file to upload (required)
```

**当前代码 (new_code)**
```java
    public ApiResponse<ModelApiResponse> uploadFileWithRequiredFileWithHttpInfo(Long petId, File requiredFile, String additionalMetadata) throws ApiException {
        com.squareup.okhttp.Call call = uploadFileWithRequiredFileValidateBeforeCall(petId, requiredFile, additionalMetadata, null, null);
        Type localVarReturnType = new TypeToken<ModelApiResponse>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

```

**变更前代码 (old_code)**
```java
    public ApiResponse<ModelApiResponse> uploadFileWithRequiredFileWithHttpInfo(Long petId, File file, String additionalMetadata) throws ApiException {
        com.squareup.okhttp.Call call = uploadFileWithRequiredFileValidateBeforeCall(petId, file, additionalMetadata, null, null);
        Type localVarReturnType = new TypeToken<ModelApiResponse>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public ApiResponse<ModelApiResponse> uploadFileWithRequiredFileWithHttpInfo(Long petId, File file, String additionalMetadata) throws ApiException {

-        com.squareup.okhttp.Call call = uploadFileWithRequiredFileValidateBeforeCall(petId, file, additionalMetadata, null, null);

+public ApiResponse<ModelApiResponse> uploadFileWithRequiredFileWithHttpInfo(Long petId, File requiredFile, String additionalMetadata) throws ApiException {

+        com.squareup.okhttp.Call call = uploadFileWithRequiredFileValidateBeforeCall(petId, requiredFile, additionalMetadata, null, null);

         Type localVarReturnType = new TypeToken<ModelApiResponse>(){}.getType();

         return apiClient.execute(call, localVarReturnType);

     }
```

---

### [8/102] `Param_14`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9833 |
| GLEU | 1.0000 |
| METEOR | 0.9995 |
| xMatch | ✓ |

**原注释 (source)**
```
@param tokenClass the class of the authenticationToken being submitted for authentication.
```

**标准注释 (ground truth)**
```
@param token the token being submitted for authentication.
```

**生成注释 (generated)**
```
@param token the token being submitted for authentication.
```

**当前代码 (new_code)**
```java
    public boolean supports(AuthenticationToken token) {
        if ( log.isInfoEnabled() ) {
            log.info( "Received null AuthenticationToken.  Returning false for supports(token) implementation (can't " +
                "process null tokens)." );
        }
        return token != null && getAuthenticationTokenClass().isAssignableFrom(token.getClass());
    }


```

**变更前代码 (old_code)**
```java
    public boolean supports(Class tokenClass) {
        return getAuthenticationTokenClass().isAssignableFrom( tokenClass );
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,7 @@
-public boolean supports(Class tokenClass) {

-        return getAuthenticationTokenClass().isAssignableFrom( tokenClass );

+public boolean supports(AuthenticationToken token) {

+        if ( log.isInfoEnabled() ) {

+            log.info( "Received null AuthenticationToken.  Returning false for supports(token) implementation (can't " +

+                "process null tokens)." );

+        }

+        return token != null && getAuthenticationTokenClass().isAssignableFrom(token.getClass());

     }
```

---

### [66/102] `Param_131`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 0.9833 |
| GLEU | 1.0000 |
| METEOR | 0.9998 |
| xMatch | ✓ |

**原注释 (source)**
```
@param connectionManager The connection manager to wrap with the connection proxy.
```

**标准注释 (ground truth)**
```
@param logicalConnection The logical connection to wrap with the connection proxy.
```

**生成注释 (generated)**
```
@param logicalConnection The logical connection to wrap with the connection proxy.
```

**当前代码 (new_code)**
```java
	public static Connection generateProxy(LogicalConnectionImpl logicalConnection) {
		BorrowedConnectionProxy handler = new BorrowedConnectionProxy( logicalConnection );
		return ( Connection ) Proxy.newProxyInstance(
				getProxyClassLoader(),
		        PROXY_INTERFACES,
		        handler
		);
	}

```

**变更前代码 (old_code)**
```java
	public static Connection generateProxy(ConnectionManager connectionManager) {
		BorrowedConnectionProxy handler = new BorrowedConnectionProxy( connectionManager );
		return ( Connection ) Proxy.newProxyInstance(
				getProxyClassLoader(),
		        PROXY_INTERFACES,
		        handler
		);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public static Connection generateProxy(ConnectionManager connectionManager) {

-		BorrowedConnectionProxy handler = new BorrowedConnectionProxy( connectionManager );

+public static Connection generateProxy(LogicalConnectionImpl logicalConnection) {

+		BorrowedConnectionProxy handler = new BorrowedConnectionProxy( logicalConnection );

 		return ( Connection ) Proxy.newProxyInstance(

 				getProxyClassLoader(),

 		        PROXY_INTERFACES,

```

---

### [2/102] `Param_2`

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
@param float x The point x coordinate.
```

**标准注释 (ground truth)**
```
@param double x The point x coordinate.
```

**生成注释 (generated)**
```
@param double x The point x coordinate.
```

**当前代码 (new_code)**
```java
	public double distanceTo(double x, double y, double z) {
		final double a = this.x - x;
		final double b = this.y - y;
		final double c = this.z - z;
		return Math.sqrt(a * a + b * b + c * c);
	}


```

**变更前代码 (old_code)**
```java
	public float distanceTo(float x, float y, float z) {
		final float a = this.x - x;
		final float b = this.y - y;
		final float c = this.z - z;
		return (float) Math.sqrt(a * a + b * b + c * c);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
-public float distanceTo(float x, float y, float z) {

-		final float a = this.x - x;

-		final float b = this.y - y;

-		final float c = this.z - z;

-		return (float) Math.sqrt(a * a + b * b + c * c);

+public double distanceTo(double x, double y, double z) {

+		final double a = this.x - x;

+		final double b = this.y - y;

+		final double c = this.z - z;

+		return Math.sqrt(a * a + b * b + c * c);

 	}
```

---

### [3/102] `Param_4`

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
@param tileY the y-axis coordinate of the tile
```

**标准注释 (ground truth)**
```
@param localY the y-axis coordinate of the tile
```

**生成注释 (generated)**
```
@param localY the y-axis coordinate of the tile
```

**当前代码 (new_code)**
```java
	public static Area getClickbox(@Nonnull Client client, Model model, int orientation, int localX, int localY)
	{
		if (model == null)
		{
			return null;
		}

		List<Triangle> triangles = model.getTriangles().stream()
			.map(triangle -> triangle.rotate(orientation))
			.collect(Collectors.toList());

		List<Vertex> vertices = model.getVertices().stream()
				.map(v -> v.rotate(orientation))
				.collect(Collectors.toList());

		Area clickBox = get2DGeometry(client, triangles, orientation, localX, localY);
		Area visibleAABB = getAABB(client, vertices, orientation, localX, localY);

		if (visibleAABB == null || clickBox == null)
		{
			return null;
		}

		clickBox.intersect(visibleAABB);
		return clickBox;
	}

```

**变更前代码 (old_code)**
```java
	public static Area getClickbox(@Nonnull Client client, Model model, int orientation, int tileX, int tileY)
	{
		if (model == null)
		{
			return null;
		}

		List<Triangle> triangles = model.getTriangles().stream()
			.map(triangle -> triangle.rotate(orientation))
			.collect(Collectors.toList());

		List<Vertex> vertices = model.getVertices().stream()
				.map(v -> v.rotate(orientation))
				.collect(Collectors.toList());

		Area clickBox = get2DGeometry(client, triangles, orientation, tileX, tileY);
		Area visibleAABB = getAABB(client, vertices, orientation, tileX, tileY);

		if (visibleAABB == null || clickBox == null)
		{
			return null;
		}

		clickBox.intersect(visibleAABB);
		return clickBox;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public static Area getClickbox(@Nonnull Client client, Model model, int orientation, int tileX, int tileY)

+public static Area getClickbox(@Nonnull Client client, Model model, int orientation, int localX, int localY)

 	{

 		if (model == null)

 		{

@@ -13,8 +13,8 @@
 				.map(v -> v.rotate(orientation))

 				.collect(Collectors.toList());

 

-		Area clickBox = get2DGeometry(client, triangles, orientation, tileX, tileY);

-		Area visibleAABB = getAABB(client, vertices, orientation, tileX, tileY);

+		Area clickBox = get2DGeometry(client, triangles, orientation, localX, localY);

+		Area visibleAABB = getAABB(client, vertices, orientation, localX, localY);

 

 		if (visibleAABB == null || clickBox == null)

 		{

```

---

### [4/102] `Param_6`

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
@param iteratorFactory
```

**标准注释 (ground truth)**
```
@param indexSupport
```

**生成注释 (generated)**
```
@param indexSupport
```

**当前代码 (new_code)**
```java
    public MultiIterator init(IndexSupport indexSupport){
        this.indexSupport = indexSupport;
        this.iterators = new Iterator<?>[sources.size()];
        this.lastEntry = new boolean[iterators.length];
        this.values = new Object[iterators.length];
        return this;
    }

```

**变更前代码 (old_code)**
```java
    public MultiIterator init(IteratorFactory iteratorFactory){
        this.iteratorFactory = iteratorFactory;
        this.iterators = new Iterator<?>[sources.size()];
        this.lastEntry = new boolean[iterators.length];
        this.values = new Object[iterators.length];
        return this;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public MultiIterator init(IteratorFactory iteratorFactory){

-        this.iteratorFactory = iteratorFactory;

+public MultiIterator init(IndexSupport indexSupport){

+        this.indexSupport = indexSupport;

         this.iterators = new Iterator<?>[sources.size()];

         this.lastEntry = new boolean[iterators.length];

         this.values = new Object[iterators.length];

```

---

### [7/102] `Param_12`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9960 |
| xMatch | ✗ |

**原注释 (source)**
```
@param request the  HttpServletRequest
```

**标准注释 (ground truth)**
```
@param request the  AtmosphereRequest
```

**生成注释 (generated)**
```
@param request the AtmosphereRequest
```

**当前代码 (new_code)**
```java
    public Action timedout(AtmosphereRequest request, AtmosphereResponse response)
            throws IOException, ServletException {

        AtmosphereResourceImpl r = null;
        try {
            if (trackActiveRequest) {
                long l = (Long) request.getAttribute(MAX_INACTIVE);
                if (l == -1) {
                    // The closedDetector closed the connection.
                    return timedoutAction;
                }
                request.setAttribute(MAX_INACTIVE, (long) -1);
            }

            logger.debug("Timing out the connection for request {}", request);

            // Something went wrong.
            if (request == null || response == null) {
                logger.warn("Invalid Request/Response: {}/{}", request, response);
                return timedoutAction;
            }

            r = (AtmosphereResourceImpl) request.getAttribute(FrameworkConfig.ATMOSPHERE_RESOURCE);

            if (r != null && r.getAtmosphereResourceEvent().isSuspended()) {
                r.getAtmosphereResourceEvent().setIsResumedOnTimeout(true);

                Broadcaster b = r.getBroadcaster();
                if (b instanceof DefaultBroadcaster) {
                    ((DefaultBroadcaster) b).broadcastOnResume(r);
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public Action timedout(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {

        AtmosphereResourceImpl r = null;
        try {
            if (trackActiveRequest) {
                long l = (Long) request.getAttribute(MAX_INACTIVE);
                if (l == -1) {
                    // The closedDetector closed the connection.
                    return timedoutAction;
                }
                request.setAttribute(MAX_INACTIVE, (long) -1);
            }

            logger.debug("Timing out the connection for request {}", request);

            // Something went wrong.
            if (request == null || response == null) {
                logger.warn("Invalid Request/Response: {}/{}", request, response);
                return timedoutAction;
            }

            r = (AtmosphereResourceImpl) request.getAttribute(FrameworkConfig.ATMOSPHERE_RESOURCE);

            if (r != null && r.getAtmosphereResourceEvent().isSuspended()) {
                r.getAtmosphereResourceEvent().setIsResumedOnTimeout(true);

                Broadcaster b = r.getBroadcaster();
                if (b instanceof DefaultBroadcaster) {
                    ((DefaultBroadcaster) b).broadcastOnResume(r);
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Action timedout(HttpServletRequest request, HttpServletResponse response)

+public Action timedout(AtmosphereRequest request, AtmosphereResponse response)

             throws IOException, ServletException {

 

         AtmosphereResourceImpl r = null;

```

---

### [9/102] `Param_16`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9977 |
| xMatch | ✓ |

**原注释 (source)**
```
@param urlPattern the URL pattern for requests that should be handled by instances of  klass
```

**标准注释 (ground truth)**
```
@param klass the servlet class
```

**生成注释 (generated)**
```
@param klass the servlet class
```

**当前代码 (new_code)**
```java
    public ServletRegistration.Dynamic addServlet(String name, Class<? extends Servlet> klass) {
        final ServletHolder holder = new ServletHolder(checkNotNull(klass));
        holder.setName(name);
        handler.getServletHandler().addServlet(holder);
        return holder.getRegistration();
    }


```

**变更前代码 (old_code)**
```java
    public ServletBuilder addServlet(Class<? extends Servlet> klass,
                                     String urlPattern) {
        final ServletHolder holder = new ServletHolder(checkNotNull(klass));
        final ServletBuilder builder = new ServletBuilder(holder, handler);
        builder.addUrlPattern(checkNotNull(urlPattern));
        return builder;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,6 @@
-public ServletBuilder addServlet(Class<? extends Servlet> klass,

-                                     String urlPattern) {

+public ServletRegistration.Dynamic addServlet(String name, Class<? extends Servlet> klass) {

         final ServletHolder holder = new ServletHolder(checkNotNull(klass));

-        final ServletBuilder builder = new ServletBuilder(holder, handler);

-        builder.addUrlPattern(checkNotNull(urlPattern));

-        return builder;

+        holder.setName(name);

+        handler.getServletHandler().addServlet(holder);

+        return holder.getRegistration();

     }
```

---

### [12/102] `Param_22`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9960 |
| xMatch | ✗ |

**原注释 (source)**
```
@param res the  HttpServletResponse
```

**标准注释 (ground truth)**
```
@param response the  HttpServletResponse
```

**生成注释 (generated)**
```
@param response the HttpServletResponse
```

**当前代码 (new_code)**
```java
    public Action timedout(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {

        AtmosphereResourceImpl re;
        long l = (Long) request.getAttribute(MAX_INACTIVE);
        if (l == -1) {
            // The closedDetector closed the connection.
            return timedoutAction;            
        }
        request.setAttribute(MAX_INACTIVE, (long) -1);

        // Something went wrong.
        if (request == null || response == null) {
            logger.warn("Invalid Request/Response: {}/{}", request, response);
            return timedoutAction;
        }

        re = (AtmosphereResourceImpl) request.getAttribute(AtmosphereServlet.ATMOSPHERE_RESOURCE);

        if (re != null) {
            re.getAtmosphereResourceEvent().setIsResumedOnTimeout(true);

            Broadcaster b = re.getBroadcaster();
            if (b instanceof DefaultBroadcaster) {
                ((DefaultBroadcaster)b).broadcastOnResume(re);
            }

            if (re.getRequest().getAttribute(AtmosphereServlet.RESUMED_ON_TIMEOUT) != null) {
                re.getAtmosphereResourceEvent().setIsResumedOnTimeout(
                        (Boolean) re.getRequest().getAttribute(AtmosphereServlet.RESUMED_ON_TIMEOUT));
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public Action timedout(HttpServletRequest req, HttpServletResponse res)
            throws IOException, ServletException {

        AtmosphereResourceImpl re;
        long l = (Long) req.getAttribute(MAX_INACTIVE);
        if (l == -1) {
            // The closedDetector closed the connection.
            return timedoutAction;            
        }
        req.setAttribute(MAX_INACTIVE, (long)-1);

        // Something went wrong.
        if (req == null || res == null) {
            logger.warning("Invalid Request/Response: " + req + "/" + res);
            return timedoutAction;
        }

        re = (AtmosphereResourceImpl) req.getAttribute(AtmosphereServlet.ATMOSPHERE_RESOURCE);

        if (re != null) {
            re.getAtmosphereResourceEvent().setIsResumedOnTimeout(true);

            Broadcaster b = re.getBroadcaster();
            if (b instanceof DefaultBroadcaster) {
                ((DefaultBroadcaster)b).broadcastOnResume(re);
            }

            if (re.getRequest().getAttribute(AtmosphereServlet.RESUMED_ON_TIMEOUT) != null) {
                re.getAtmosphereResourceEvent().setIsResumedOnTimeout(
                        (Boolean) re.getRequest().getAttribute(AtmosphereServlet.RESUMED_ON_TIMEOUT));
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,21 +1,21 @@
-public Action timedout(HttpServletRequest req, HttpServletResponse res)

+public Action timedout(HttpServletRequest request, HttpServletResponse response)

             throws IOException, ServletException {

 

         AtmosphereResourceImpl re;

-        long l = (Long) req.getAttribute(MAX_INACTIVE);

+        long l = (Long) request.getAttribute(MAX_INACTIVE);

         if (l == -1) {

             // The closedDetector closed the connection.

             return timedoutAction;            

         }

-        req.setAttribute(MAX_INACTIVE, (long)-1);

+        request.setAttribute(MAX_INACTIVE, (long) -1);

 

         // Something went wrong.

-        if (req == null || res == null) {

-            logger.warning("Invalid Request/Response: " + req + "/" + res);

+        if (request == null || response == null) {

+            logger.warn("Invalid Request/Response: {}/{}", request, response);

             return timedoutAction;

         }

 

-        re = (AtmosphereResourceImpl) req.getAttribute(AtmosphereServlet.ATMOSPHERE_RESOURCE);

+        re = (AtmosphereResourceImpl) request.getAttribute(AtmosphereServlet.ATMOSPHERE_RESOURCE);

 

         if (re != null) {

             re.getAtmosphereResourceEvent().setIsResumedOnTimeout(true);

```

---

### [14/102] `Param_26`

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
@param pluginKey
```

**标准注释 (ground truth)**
```
@param pluginName
```

**生成注释 (generated)**
```
@param pluginName
```

**当前代码 (new_code)**
```java
    public synchronized <T extends AbstractTypeServerPluginContainer> T getPluginContainerByPlugin(String pluginName) {
        for (AbstractTypeServerPluginContainer pc : this.pluginContainers.values()) {
            if (null != pc.getPluginManager().getPluginEnvironment(pluginName)) {
                return (T) pc;
            }
        }
        return null;
    }


```

**变更前代码 (old_code)**
```java
    public synchronized <T extends AbstractTypeServerPluginContainer> T getPluginContainerByPlugin(PluginKey pluginKey) {
        for (AbstractTypeServerPluginContainer pc : this.pluginContainers.values()) {
            try {
                if (pc.getSupportedServerPluginType().equals(new ServerPluginType(pluginKey.getPluginType()))) {
                    if (null != pc.getPluginManager().getPluginEnvironment(pluginKey.getPluginName())) {
                        return (T) pc;
                    }
                }
            } catch (Exception skip) {
                // should never really happen
                log.error("Bad plugin key: " + pluginKey);
            }
        }
        return null;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,14 +1,7 @@
-public synchronized <T extends AbstractTypeServerPluginContainer> T getPluginContainerByPlugin(PluginKey pluginKey) {

+public synchronized <T extends AbstractTypeServerPluginContainer> T getPluginContainerByPlugin(String pluginName) {

         for (AbstractTypeServerPluginContainer pc : this.pluginContainers.values()) {

-            try {

-                if (pc.getSupportedServerPluginType().equals(new ServerPluginType(pluginKey.getPluginType()))) {

-                    if (null != pc.getPluginManager().getPluginEnvironment(pluginKey.getPluginName())) {

-                        return (T) pc;

-                    }

-                }

-            } catch (Exception skip) {

-                // should never really happen

-                log.error("Bad plugin key: " + pluginKey);

+            if (null != pc.getPluginManager().getPluginEnvironment(pluginName)) {

+                return (T) pc;

             }

         }

         return null;

```

---

### [15/102] `Param_28`

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
@param entryId
```

**标准注释 (ground truth)**
```
@param key
```

**生成注释 (generated)**
```
@param key
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

### [17/102] `Param_32`

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
@param body order placed for purchasing the pet (required)
```

**标准注释 (ground truth)**
```
@param order order placed for purchasing the pet (required)
```

**生成注释 (generated)**
```
@param order order placed for purchasing the pet (required)
```

**当前代码 (new_code)**
```java
    public Order placeOrder(Order order) throws ApiException {
        ApiResponse<Order> resp = placeOrderWithHttpInfo(order);
        return resp.getData();
    }

```

**变更前代码 (old_code)**
```java
    public Order placeOrder(Order body) throws ApiException {
        ApiResponse<Order> resp = placeOrderWithHttpInfo(body);
        return resp.getData();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Order placeOrder(Order body) throws ApiException {

-        ApiResponse<Order> resp = placeOrderWithHttpInfo(body);

+public Order placeOrder(Order order) throws ApiException {

+        ApiResponse<Order> resp = placeOrderWithHttpInfo(order);

         return resp.getData();

     }
```

---

### [20/102] `Param_38`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9977 |
| xMatch | ✓ |

**原注释 (source)**
```
@param id the module.
```

**标准注释 (ground truth)**
```
@param ref the module.
```

**生成注释 (generated)**
```
@param ref the module.
```

**当前代码 (new_code)**
```java
    public final List<ModuleReference> getDependentModulesRecursively(final ModuleReference ref) throws Exception {
        return getDependentModulesRecursively(ref, new ArrayList<ModuleReference>());
    }


```

**变更前代码 (old_code)**
```java
    public synchronized final List<String> getDependentModulesRecursively(final String id) throws Exception {
        final List<String> res = new ArrayList<String>();
        for (final String depModule : getDependentModules(id)) {
            res.add(depModule);
            // the graph has no cycle, so we don't need to protected against infinite loop

            res.addAll(this.getDependentModulesRecursively(depModule));
        }
        Collections.reverse(res);
        return res;
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,11 +1,3 @@
-public synchronized final List<String> getDependentModulesRecursively(final String id) throws Exception {

-        final List<String> res = new ArrayList<String>();

-        for (final String depModule : getDependentModules(id)) {

-            res.add(depModule);

-            // the graph has no cycle, so we don't need to protected against infinite loop

-

-            res.addAll(this.getDependentModulesRecursively(depModule));

-        }

-        Collections.reverse(res);

-        return res;

+public final List<ModuleReference> getDependentModulesRecursively(final ModuleReference ref) throws Exception {

+        return getDependentModulesRecursively(ref, new ArrayList<ModuleReference>());

     }
```

---

### [22/102] `Param_42`

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
@param global
```

**标准注释 (ground truth)**
```
@param scenarioPattern
```

**生成注释 (generated)**
```
@param scenarioPattern
```

**当前代码 (new_code)**
```java
    public static SummaryEntry[] querySummaries(Variations variationPatterns, String scenarioPattern) {
        return getDefault().internalQuerySummaries(variationPatterns, scenarioPattern);
    }


```

**变更前代码 (old_code)**
```java
    public static SummaryEntry[] querySummaries(Variations variationPatterns, boolean global) {
        return getDefault().internalQuerySummaries(variationPatterns, null);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static SummaryEntry[] querySummaries(Variations variationPatterns, boolean global) {

-        return getDefault().internalQuerySummaries(variationPatterns, null);

+public static SummaryEntry[] querySummaries(Variations variationPatterns, String scenarioPattern) {

+        return getDefault().internalQuerySummaries(variationPatterns, scenarioPattern);

     }
```

---

### [31/102] `Param_60`

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
@param x double The x component.
```

**标准注释 (ground truth)**
```
@param x float The x component.
```

**生成注释 (generated)**
```
@param x float The x component.
```

**当前代码 (new_code)**
```java
	public static float length(float x, float y, float z) {
		return (float) Math.sqrt(length2(x, y, z));
	}


```

**变更前代码 (old_code)**
```java
	public static double length(double x, double y, double z) {
		return Math.sqrt(length2(x, y, z));
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static double length(double x, double y, double z) {

-		return Math.sqrt(length2(x, y, z));

+public static float length(float x, float y, float z) {

+		return (float) Math.sqrt(length2(x, y, z));

 	}
```

---

### [32/102] `Param_62`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 1.0000 |
| xMatch | ✗ |

**原注释 (source)**
```
@param environment the current environment, which may affect the behavior of the expert. This parameter may be specified as null, in which case the  STextEnvironment#DEFAULT environment should be assumed.
```

**标准注释 (ground truth)**
```
@param environment the current environment, which may affect the behavior of the expert. This parameter may be specified as null, in which case the  StructuredTextEnvironment#DEFAULT environment should be assumed.
```

**生成注释 (generated)**
```
@param environment the current environment, which may affect the behavior of the expert. This parameter may be specified as null, in which case the StructuredTextEnvironment#DEFAULT environment should be assumed.
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

### [35/102] `Param_68`

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
@param body client model
```

**标准注释 (ground truth)**
```
@param client client model
```

**生成注释 (generated)**
```
@param client client model
```

**当前代码 (new_code)**
```java
    public Client testSpecialTags(Client client, Map<String, Object> params) throws IOException {
        HttpResponse response = testSpecialTagsForHttpResponse(client, params);
        TypeReference typeRef = new TypeReference<Client>() {};
        return apiClient.getObjectMapper().readValue(response.getContent(), typeRef);
    }

```

**变更前代码 (old_code)**
```java
    public Client testSpecialTags(Client body, Map<String, Object> params) throws IOException {
        HttpResponse response = testSpecialTagsForHttpResponse(body, params);
        TypeReference typeRef = new TypeReference<Client>() {};
        return apiClient.getObjectMapper().readValue(response.getContent(), typeRef);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public Client testSpecialTags(Client body, Map<String, Object> params) throws IOException {

-        HttpResponse response = testSpecialTagsForHttpResponse(body, params);

+public Client testSpecialTags(Client client, Map<String, Object> params) throws IOException {

+        HttpResponse response = testSpecialTagsForHttpResponse(client, params);

         TypeReference typeRef = new TypeReference<Client>() {};

         return apiClient.getObjectMapper().readValue(response.getContent(), typeRef);

     }
```

---

### [36/102] `Param_70`

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
@param attributes an object containing an AttributeMap
```

**标准注释 (ground truth)**
```
@param withAttributes an object containing an AttributeMap
```

**生成注释 (generated)**
```
@param withAttributes an object containing an AttributeMap
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

-        return attributes.getAttributes().get(this);

+public double get(WithAttributes withAttributes) {

+        return withAttributes.getAttributes().get(this);

     }
```

---

### [37/102] `Param_72`

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
@param outerComposite Input composite as post body (optional)
```

**标准注释 (ground truth)**
```
@param body Input composite as post body (optional)
```

**生成注释 (generated)**
```
@param body Input composite as post body (optional)
```

**当前代码 (new_code)**
```java
  public OuterComposite fakeOuterCompositeSerialize(OuterComposite body) throws ApiException {
    Object localVarPostBody = body;
    
    // create path and map variables
    String localVarPath = "/fake/outer/composite".replaceAll("\\{format\\}","json");

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    
    final String[] localVarAccepts = {
      "*/*"
    };
    final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

    final String[] localVarContentTypes = {
      
    };
    final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

    String[] localVarAuthNames = new String[] {  };

    GenericType<OuterComposite> localVarReturnType = new GenericType<OuterComposite>() {};
    return apiClient.invokeAPI(localVarPath, "POST", localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAccept, localVarContentType, localVarAuthNames, localVarReturnType);
      }

```

**变更前代码 (old_code)**
```java
  public OuterComposite fakeOuterCompositeSerialize(OuterComposite outerComposite) throws ApiException {
    Object localVarPostBody = outerComposite;
    
    // create path and map variables
    String localVarPath = "/fake/outer/composite".replaceAll("\\{format\\}","json");

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    
    final String[] localVarAccepts = {
      "*/*"
    };
    final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

    final String[] localVarContentTypes = {
      
    };
    final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

    String[] localVarAuthNames = new String[] {  };

    GenericType<OuterComposite> localVarReturnType = new GenericType<OuterComposite>() {};
    return apiClient.invokeAPI(localVarPath, "POST", localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAccept, localVarContentType, localVarAuthNames, localVarReturnType);
      }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,5 @@
-public OuterComposite fakeOuterCompositeSerialize(OuterComposite outerComposite) throws ApiException {

-    Object localVarPostBody = outerComposite;

+public OuterComposite fakeOuterCompositeSerialize(OuterComposite body) throws ApiException {

+    Object localVarPostBody = body;

     

     // create path and map variables

     String localVarPath = "/fake/outer/composite".replaceAll("\\{format\\}","json");

```

---

### [38/102] `Param_74`

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
@param contextWrappableAs the contextWrappableAs to filter providers by
```

**标准注释 (ground truth)**
```
@param type the type to filter providers by
```

**生成注释 (generated)**
```
@param type the type to filter providers by
```

**当前代码 (new_code)**
```java
   public static Iterable<ProviderMetadata<?, ?, ?, ?>> boundedByIso3166Code(String iso3166Code, ApiType type) {
      return filter(all(),
            Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates.type(type)));
   }


```

**变更前代码 (old_code)**
```java
   public static Iterable<ProviderMetadata> boundedByIso3166Code(String iso3166Code,
            TypeToken<? extends Wrapper> contextWrappableAs) {
      return filter(all(), Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates
               .contextWrappableAs(contextWrappableAs)));
   }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,5 +1,4 @@
-public static Iterable<ProviderMetadata> boundedByIso3166Code(String iso3166Code,

-            TypeToken<? extends Wrapper> contextWrappableAs) {

-      return filter(all(), Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates

-               .contextWrappableAs(contextWrappableAs)));

+public static Iterable<ProviderMetadata<?, ?, ?, ?>> boundedByIso3166Code(String iso3166Code, ApiType type) {

+      return filter(all(),

+            Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates.type(type)));

    }
```

---

### [40/102] `Param_79`

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
@param y float The y component.
```

**标准注释 (ground truth)**
```
@param y double The y component.
```

**生成注释 (generated)**
```
@param y double The y component.
```

**当前代码 (new_code)**
```java
	public static double length(double x, double y, double z) {
		return Math.sqrt(length2(x, y, z));
	}


```

**变更前代码 (old_code)**
```java
	public static float length(float x, float y, float z) {
		return (float) Math.sqrt(length2(x, y, z));
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static float length(float x, float y, float z) {

-		return (float) Math.sqrt(length2(x, y, z));

+public static double length(double x, double y, double z) {

+		return Math.sqrt(length2(x, y, z));

 	}
```

---

### [41/102] `Param_81`

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
@param body client model (required)
```

**标准注释 (ground truth)**
```
@param client client model (required)
```

**生成注释 (generated)**
```
@param client client model (required)
```

**当前代码 (new_code)**
```java
  public Client testClientModel(Client client) throws ApiException {
    Object localVarPostBody = client;
    
    // verify the required parameter 'client' is set
    if (client == null) {
      throw new ApiException(400, "Missing the required parameter 'client' when calling testClientModel");
    }
    
    // create path and map variables
    String localVarPath = "/fake";

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    
    final String[] localVarAccepts = {
      "application/json"
    };
    final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

    final String[] localVarContentTypes = {
      "application/json"
    };
    final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public Client testClientModel(Client body) throws ApiException {
    Object localVarPostBody = body;
    
    // verify the required parameter 'body' is set
    if (body == null) {
      throw new ApiException(400, "Missing the required parameter 'body' when calling testClientModel");
    }
    
    // create path and map variables
    String localVarPath = "/fake";

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    
    final String[] localVarAccepts = {
      "application/json"
    };
    final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

    final String[] localVarContentTypes = {
      "application/json"
    };
    final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,9 @@
-public Client testClientModel(Client body) throws ApiException {

-    Object localVarPostBody = body;

+public Client testClientModel(Client client) throws ApiException {

+    Object localVarPostBody = client;

     

-    // verify the required parameter 'body' is set

-    if (body == null) {

-      throw new ApiException(400, "Missing the required parameter 'body' when calling testClientModel");

+    // verify the required parameter 'client' is set

+    if (client == null) {

+      throw new ApiException(400, "Missing the required parameter 'client' when calling testClientModel");

     }

     

     // create path and map variables

```

---

### [47/102] `Param_93`

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
@param tileX the x-axis coordinate of the tile
```

**标准注释 (ground truth)**
```
@param localX the x-axis coordinate of the tile
```

**生成注释 (generated)**
```
@param localX the x-axis coordinate of the tile
```

**当前代码 (new_code)**
```java
	public static Area getClickbox(@Nonnull Client client, Model model, int orientation, int localX, int localY)
	{
		if (model == null)
		{
			return null;
		}

		List<Triangle> triangles = model.getTriangles().stream()
			.map(triangle -> triangle.rotate(orientation))
			.collect(Collectors.toList());

		List<Vertex> vertices = model.getVertices().stream()
				.map(v -> v.rotate(orientation))
				.collect(Collectors.toList());

		Area clickBox = get2DGeometry(client, triangles, orientation, localX, localY);
		Area visibleAABB = getAABB(client, vertices, orientation, localX, localY);

		if (visibleAABB == null || clickBox == null)
		{
			return null;
		}

		clickBox.intersect(visibleAABB);
		return clickBox;
	}

```

**变更前代码 (old_code)**
```java
	public static Area getClickbox(@Nonnull Client client, Model model, int orientation, int tileX, int tileY)
	{
		if (model == null)
		{
			return null;
		}

		List<Triangle> triangles = model.getTriangles().stream()
			.map(triangle -> triangle.rotate(orientation))
			.collect(Collectors.toList());

		List<Vertex> vertices = model.getVertices().stream()
				.map(v -> v.rotate(orientation))
				.collect(Collectors.toList());

		Area clickBox = get2DGeometry(client, triangles, orientation, tileX, tileY);
		Area visibleAABB = getAABB(client, vertices, orientation, tileX, tileY);

		if (visibleAABB == null || clickBox == null)
		{
			return null;
		}

		clickBox.intersect(visibleAABB);
		return clickBox;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public static Area getClickbox(@Nonnull Client client, Model model, int orientation, int tileX, int tileY)

+public static Area getClickbox(@Nonnull Client client, Model model, int orientation, int localX, int localY)

 	{

 		if (model == null)

 		{

@@ -13,8 +13,8 @@
 				.map(v -> v.rotate(orientation))

 				.collect(Collectors.toList());

 

-		Area clickBox = get2DGeometry(client, triangles, orientation, tileX, tileY);

-		Area visibleAABB = getAABB(client, vertices, orientation, tileX, tileY);

+		Area clickBox = get2DGeometry(client, triangles, orientation, localX, localY);

+		Area visibleAABB = getAABB(client, vertices, orientation, localX, localY);

 

 		if (visibleAABB == null || clickBox == null)

 		{

```

---

### [51/102] `Param_101`

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
@param body client model (required)
```

**标准注释 (ground truth)**
```
@param client client model (required)
```

**生成注释 (generated)**
```
@param client client model (required)
```

**当前代码 (new_code)**
```java
    public Client testSpecialTags(Client client) throws ApiException {
        ApiResponse<Client> resp = testSpecialTagsWithHttpInfo(client);
        return resp.getData();
    }

```

**变更前代码 (old_code)**
```java
    public Client testSpecialTags(Client body) throws ApiException {
        ApiResponse<Client> resp = testSpecialTagsWithHttpInfo(body);
        return resp.getData();
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Client testSpecialTags(Client body) throws ApiException {

-        ApiResponse<Client> resp = testSpecialTagsWithHttpInfo(body);

+public Client testSpecialTags(Client client) throws ApiException {

+        ApiResponse<Client> resp = testSpecialTagsWithHttpInfo(client);

         return resp.getData();

     }
```

---

### [52/102] `Param_103`

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
@param elems The list of items
```

**标准注释 (ground truth)**
```
@param elements The list of items
```

**生成注释 (generated)**
```
@param elements The list of items
```

**当前代码 (new_code)**
```java
  public int[] indices(Collection<E> elements) {
    int[] indices = new int[elements.size()];
    int i = 0;
    for (E elem : elements) {
      indices[i++] = indexOf(elem);
    }
    return indices;
  }

```

**变更前代码 (old_code)**
```java
  public int[] indices(Collection<E> elems) {
    int[] indices = new int[elems.size()];
    int i = 0;
    for (E elem : elems) {
      indices[i++] = indexOf(elem);
    }
    return indices;
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,7 +1,7 @@
-public int[] indices(Collection<E> elems) {

-    int[] indices = new int[elems.size()];

+public int[] indices(Collection<E> elements) {

+    int[] indices = new int[elements.size()];

     int i = 0;

-    for (E elem : elems) {

+    for (E elem : elements) {

       indices[i++] = indexOf(elem);

     }

     return indices;

```

---

### [55/102] `Param_109`

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
@param localPort local TCP port of the webdav share
```

**标准注释 (ground truth)**
```
@param uri URI of the webdav share
```

**生成注释 (generated)**
```
@param uri URI of the webdav share
```

**当前代码 (new_code)**
```java
	public static WebDavMount mount(URI uri) throws CommandFailedException {
		return chooseStrategy().mount(uri);
	}

```

**变更前代码 (old_code)**
```java
	public static WebDavMount mount(int localPort) throws CommandFailedException {
		return chooseStrategy().mount(localPort);
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public static WebDavMount mount(int localPort) throws CommandFailedException {

-		return chooseStrategy().mount(localPort);

+public static WebDavMount mount(URI uri) throws CommandFailedException {

+		return chooseStrategy().mount(uri);

 	}
```

---

### [59/102] `Param_117`

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
@param body client model (required)
```

**标准注释 (ground truth)**
```
@param client client model (required)
```

**生成注释 (generated)**
```
@param client client model (required)
```

**当前代码 (new_code)**
```java
  public Client testClassname(Client client) throws ApiException {
    Object localVarPostBody = client;
    
    // verify the required parameter 'client' is set
    if (client == null) {
      throw new ApiException(400, "Missing the required parameter 'client' when calling testClassname");
    }
    
    // create path and map variables
    String localVarPath = "/fake_classname_test";

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    
    final String[] localVarAccepts = {
      "application/json"
    };
    final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

    final String[] localVarContentTypes = {
      "application/json"
    };
    final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public Client testClassname(Client body) throws ApiException {
    Object localVarPostBody = body;
    
    // verify the required parameter 'body' is set
    if (body == null) {
      throw new ApiException(400, "Missing the required parameter 'body' when calling testClassname");
    }
    
    // create path and map variables
    String localVarPath = "/fake_classname_test";

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    Map<String, Object> localVarFormParams = new HashMap<String, Object>();


    
    
    final String[] localVarAccepts = {
      "application/json"
    };
    final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);

    final String[] localVarContentTypes = {
      "application/json"
    };
    final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);

// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,9 @@
-public Client testClassname(Client body) throws ApiException {

-    Object localVarPostBody = body;

+public Client testClassname(Client client) throws ApiException {

+    Object localVarPostBody = client;

     

-    // verify the required parameter 'body' is set

-    if (body == null) {

-      throw new ApiException(400, "Missing the required parameter 'body' when calling testClassname");

+    // verify the required parameter 'client' is set

+    if (client == null) {

+      throw new ApiException(400, "Missing the required parameter 'client' when calling testClassname");

     }

     

     // create path and map variables

```

---

### [65/102] `Param_129`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9960 |
| xMatch | ✗ |

**原注释 (source)**
```
@param req the  HttpServletRequest
```

**标准注释 (ground truth)**
```
@param req the  AtmosphereRequest
```

**生成注释 (generated)**
```
@param req the AtmosphereRequest
```

**当前代码 (new_code)**
```java
    public Action cancelled(AtmosphereRequest req, AtmosphereResponse res)
            throws IOException, ServletException {

        synchronized (req) {
            AtmosphereResourceImpl r = null;
            try {
                if (trackActiveRequest) {
                    long l = (Long) req.getAttribute(MAX_INACTIVE);
                    if (l == -1) {
                        // The closedDetector closed the connection.
                        return timedoutAction;
                    }
                    req.setAttribute(MAX_INACTIVE, (long) -1);
                }

                logger.debug("Cancelling the connection for request {}", req);

                r = (AtmosphereResourceImpl) req.getAttribute(FrameworkConfig.ATMOSPHERE_RESOURCE);
                if (r != null) {
                    r.getAtmosphereResourceEvent().setCancelled(true);
                    invokeAtmosphereHandler(r);

                    try {
                        r.getResponse().sendError(503);
                        r.getResponse().getOutputStream().close();
                    } catch (Throwable t) {
                        try {
                            r.getResponse().getWriter().close();
                        } catch (Throwable t2) {
                        }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public Action cancelled(HttpServletRequest req, HttpServletResponse res)
            throws IOException, ServletException {

        synchronized (req) {
            AtmosphereResourceImpl r = null;
            try {
                if (trackActiveRequest) {
                    long l = (Long) req.getAttribute(MAX_INACTIVE);
                    if (l == -1) {
                        // The closedDetector closed the connection.
                        return timedoutAction;
                    }
                    req.setAttribute(MAX_INACTIVE, (long) -1);
                }

                logger.debug("Cancelling the connection for request {}", req);

                r = (AtmosphereResourceImpl) req.getAttribute(FrameworkConfig.ATMOSPHERE_RESOURCE);
                if (r != null) {
                    r.getAtmosphereResourceEvent().setCancelled(true);
                    invokeAtmosphereHandler(r);

                    try {
                        r.getResponse().sendError(503);
                        r.getResponse().getOutputStream().close();
                    } catch (Throwable t) {
                        try {
                            r.getResponse().getWriter().close();
                        } catch (Throwable t2) {
                        }
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Action cancelled(HttpServletRequest req, HttpServletResponse res)

+public Action cancelled(AtmosphereRequest req, AtmosphereResponse res)

             throws IOException, ServletException {

 

         synchronized (req) {

```

---

### [68/102] `Param_135`

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
@param body Pet object that needs to be added to the store
```

**标准注释 (ground truth)**
```
@param pet Pet object that needs to be added to the store
```

**生成注释 (generated)**
```
@param pet Pet object that needs to be added to the store
```

**当前代码 (new_code)**
```java
  public void addPet (Pet pet) throws TimeoutException, ExecutionException, InterruptedException, ApiException {
    Object postBody = pet;
    // verify the required parameter 'pet' is set
    if (pet == null) {
      VolleyError error = new VolleyError("Missing the required parameter 'pet' when calling addPet",
        new ApiException(400, "Missing the required parameter 'pet' when calling addPet"));
    }

    // create path and map variables
    String path = "/pet";

    // query params
    List<Pair> queryParams = new ArrayList<Pair>();
    // header params
    Map<String, String> headerParams = new HashMap<String, String>();
    // form params
    Map<String, String> formParams = new HashMap<String, String>();
    String[] contentTypes = {
    };
    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

    if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();
      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
    } else {
      // normal form params
    }

// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public void addPet (Pet body) throws TimeoutException, ExecutionException, InterruptedException, ApiException {
    Object postBody = body;
    // verify the required parameter 'body' is set
    if (body == null) {
      VolleyError error = new VolleyError("Missing the required parameter 'body' when calling addPet",
        new ApiException(400, "Missing the required parameter 'body' when calling addPet"));
    }

    // create path and map variables
    String path = "/pet";

    // query params
    List<Pair> queryParams = new ArrayList<Pair>();
    // header params
    Map<String, String> headerParams = new HashMap<String, String>();
    // form params
    Map<String, String> formParams = new HashMap<String, String>();
    String[] contentTypes = {
      "application/json",
      "application/xml"
    };
    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

    if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();
      HttpEntity httpEntity = localVarBuilder.build();
      postBody = httpEntity;
    } else {
      // normal form params
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,9 +1,9 @@
-public void addPet (Pet body) throws TimeoutException, ExecutionException, InterruptedException, ApiException {

-    Object postBody = body;

-    // verify the required parameter 'body' is set

-    if (body == null) {

-      VolleyError error = new VolleyError("Missing the required parameter 'body' when calling addPet",

-        new ApiException(400, "Missing the required parameter 'body' when calling addPet"));

+public void addPet (Pet pet) throws TimeoutException, ExecutionException, InterruptedException, ApiException {

+    Object postBody = pet;

+    // verify the required parameter 'pet' is set

+    if (pet == null) {

+      VolleyError error = new VolleyError("Missing the required parameter 'pet' when calling addPet",

+        new ApiException(400, "Missing the required parameter 'pet' when calling addPet"));

     }

 

     // create path and map variables

@@ -16,8 +16,6 @@
     // form params

     Map<String, String> formParams = new HashMap<String, String>();

     String[] contentTypes = {

-      "application/json",

-      "application/xml"

     };

     String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

 

```

---

### [69/102] `Param_137`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 1.0000 |
| xMatch | ✗ |

**原注释 (source)**
```
@param expectedMinimumNumberOfMatches the minimum number of matches expected to be found.  0 matches means that one or more matches are expected to be found
```

**标准注释 (ground truth)**
```
@param minimumNumberOfMatches the minimum number of matches expected to be found.  0 matches means that one or more matches are expected to be found
```

**生成注释 (generated)**
```
@param minimumNumberOfMatches the minimum number of matches expected to be found. 0 matches means that one or more matches are expected to be found
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

### [72/102] `Param_143`

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
@param inputReq BrokerRequest that is to be optimized
```

**标准注释 (ground truth)**
```
@param brokerRequest BrokerRequest that is to be optimized
```

**生成注释 (generated)**
```
@param brokerRequest BrokerRequest that is to be optimized
```

**当前代码 (new_code)**
```java
  public BrokerRequest optimize(BrokerRequest brokerRequest) {
    optimizeFilterQueryTree(brokerRequest);

    return brokerRequest;
  }


```

**变更前代码 (old_code)**
```java
  public BrokerRequest optimize(BrokerRequest inputReq) {
    // Flatten the query tree if possible
    return flatten(inputReq);
  }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,5 @@
-public BrokerRequest optimize(BrokerRequest inputReq) {

-    // Flatten the query tree if possible

-    return flatten(inputReq);

+public BrokerRequest optimize(BrokerRequest brokerRequest) {

+    optimizeFilterQueryTree(brokerRequest);

+

+    return brokerRequest;

   }
```

---

### [74/102] `Param_147`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9960 |
| xMatch | ✗ |

**原注释 (source)**
```
@param response the  HttpServletResponse
```

**标准注释 (ground truth)**
```
@param response the  AtmosphereResponse
```

**生成注释 (generated)**
```
@param response the AtmosphereResponse
```

**当前代码 (new_code)**
```java
    public Action resumed(AtmosphereRequest request, AtmosphereResponse response)
            throws IOException, ServletException {
        return action(request, response);
    }

```

**变更前代码 (old_code)**
```java
    public Action resumed(HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        return action(request, response);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Action resumed(HttpServletRequest request, HttpServletResponse response)

+public Action resumed(AtmosphereRequest request, AtmosphereResponse response)

             throws IOException, ServletException {

         return action(request, response);

     }
```

---

### [76/102] `Param_153`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9960 |
| xMatch | ✗ |

**原注释 (source)**
```
@param res the  HttpServletResponse
```

**标准注释 (ground truth)**
```
@param res the  AtmosphereResponse
```

**生成注释 (generated)**
```
@param res the AtmosphereResponse
```

**当前代码 (new_code)**
```java
    public Action cancelled(AtmosphereRequest req, AtmosphereResponse res)
            throws IOException, ServletException {

        synchronized (req) {
            AtmosphereResourceImpl r = null;
            try {
                if (trackActiveRequest) {
                    long l = (Long) req.getAttribute(MAX_INACTIVE);
                    if (l == -1) {
                        // The closedDetector closed the connection.
                        return timedoutAction;
                    }
                    req.setAttribute(MAX_INACTIVE, (long) -1);
                }

                logger.debug("Cancelling the connection for request {}", req);

                r = (AtmosphereResourceImpl) req.getAttribute(FrameworkConfig.ATMOSPHERE_RESOURCE);
                if (r != null) {
                    r.getAtmosphereResourceEvent().setCancelled(true);
                    invokeAtmosphereHandler(r);

                    try {
                        r.getResponse().sendError(503);
                        r.getResponse().getOutputStream().close();
                    } catch (Throwable t) {
                        try {
                            r.getResponse().getWriter().close();
                        } catch (Throwable t2) {
                        }
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public Action cancelled(HttpServletRequest req, HttpServletResponse res)
            throws IOException, ServletException {

        synchronized (req) {
            AtmosphereResourceImpl r = null;
            try {
                if (trackActiveRequest) {
                    long l = (Long) req.getAttribute(MAX_INACTIVE);
                    if (l == -1) {
                        // The closedDetector closed the connection.
                        return timedoutAction;
                    }
                    req.setAttribute(MAX_INACTIVE, (long) -1);
                }

                logger.debug("Cancelling the connection for request {}", req);

                r = (AtmosphereResourceImpl) req.getAttribute(FrameworkConfig.ATMOSPHERE_RESOURCE);
                if (r != null) {
                    r.getAtmosphereResourceEvent().setCancelled(true);
                    invokeAtmosphereHandler(r);

                    try {
                        r.getResponse().sendError(503);
                        r.getResponse().getOutputStream().close();
                    } catch (Throwable t) {
                        try {
                            r.getResponse().getWriter().close();
                        } catch (Throwable t2) {
                        }
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
-public Action cancelled(HttpServletRequest req, HttpServletResponse res)

+public Action cancelled(AtmosphereRequest req, AtmosphereResponse res)

             throws IOException, ServletException {

 

         synchronized (req) {

```

---

### [79/102] `Param_159`

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
@param millis milliseconds from 1970-01-01T00:00:00Z to get the name for
```

**标准注释 (ground truth)**
```
@param instant milliseconds from 1970-01-01T00:00:00Z to get the name for
```

**生成注释 (generated)**
```
@param instant milliseconds from 1970-01-01T00:00:00Z to get the name for
```

**当前代码 (new_code)**
```java
    public String getShortName(long instant, Locale locale) {
        if (locale == null) {
            locale = Locale.getDefault();
        }
        String nameKey = getNameKey(instant);
        if (nameKey == null) {
            return iID;
        }
        String name = cNameProvider.getShortName(locale, iID, nameKey);
        if (name != null) {
            return name;
        }
        return offsetFormatter().print(instant, this);
    }

```

**变更前代码 (old_code)**
```java
    public String getShortName(long millis, Locale locale) {
        if (locale == null) {
            locale = Locale.getDefault();
        }
        String nameKey = getNameKey(millis);
        if (nameKey == null) {
            return iID;
        }
        String name = cNameProvider.getShortName(locale, iID, nameKey);
        if (name != null) {
            return name;
        }
        return offsetFormatter().print(millis, this);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,8 @@
-public String getShortName(long millis, Locale locale) {

+public String getShortName(long instant, Locale locale) {

         if (locale == null) {

             locale = Locale.getDefault();

         }

-        String nameKey = getNameKey(millis);

+        String nameKey = getNameKey(instant);

         if (nameKey == null) {

             return iID;

         }

@@ -10,5 +10,5 @@
         if (name != null) {

             return name;

         }

-        return offsetFormatter().print(millis, this);

+        return offsetFormatter().print(instant, this);

     }
```

---

### [84/102] `Param_169`

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
@param astGenerator
```

**标准注释 (ground truth)**
```
@param editor
```

**生成注释 (generated)**
```
@param editor
```

**当前代码 (new_code)**
```java
  public boolean highlightNode(JavaEditor editor){
    if (!(node instanceof SimpleName)) {
      return false;
    }
    SimpleName nodeName = (SimpleName) node;
    try {
      //TODO: Redundant code. See ASTGenerator.getJavaSourceCodeline()
      int javaLineNumber = getLineNumber(nodeName);
      int pdeOffs[] = editor.getErrorChecker().calculateTabIndexAndLineNumber(javaLineNumber);
      PlainDocument javaSource = new PlainDocument();
      javaSource.insertString(0, editor.getErrorChecker().sourceCode, null);
      Element lineElement = javaSource.getDefaultRootElement()
          .getElement(javaLineNumber-1);
      if(lineElement == null) {
        Messages.log(lineNumber + " line element null while highlighting " + nodeName);
        return false;
      }

      String javaLine = javaSource.getText(lineElement.getStartOffset(),
                                           lineElement.getEndOffset()
                                               - lineElement.getStartOffset());
      editor.getSketch().setCurrentCode(pdeOffs[0]);
      String pdeLine = editor.getLineText(pdeOffs[1]);
      String lookingFor = nodeName.toString();
      Messages.log(lookingFor + ", " + nodeName.getStartPosition());
      Messages.log(javaLineNumber +" JL " + javaLine + " LSO " + lineElement.getStartOffset() + ","
          + lineElement.getEndOffset());
      Messages.log(pdeOffs[1] + " PL " + pdeLine);
      if (!javaLine.contains(lookingFor) || !pdeLine.contains(lookingFor)) {
        Messages.loge("Logical error in highLightNode(). Please file a bug report.");
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public boolean highlightNode(ASTGenerator astGenerator){
    if (!(Node instanceof SimpleName)) {
      return false;
    }
    SimpleName nodeName = (SimpleName) node;
    try {
      //TODO: Redundant code. See ASTGenerator.getJavaSourceCodeline()
      int javaLineNumber = getLineNumber(nodeName);
      int pdeOffs[] = astGenerator.errorCheckerService
          .calculateTabIndexAndLineNumber(javaLineNumber);
      PlainDocument javaSource = new PlainDocument();
      javaSource.insertString(0, astGenerator.errorCheckerService.sourceCode, null);
      Element lineElement = javaSource.getDefaultRootElement()
          .getElement(javaLineNumber-1);
      if(lineElement == null) {
        Messages.log(lineNumber + " line element null while highlighting " + nodeName);
        return false;
      }

      String javaLine = javaSource.getText(lineElement.getStartOffset(),
                                           lineElement.getEndOffset()
                                               - lineElement.getStartOffset());
      astGenerator.editor.getSketch().setCurrentCode(pdeOffs[0]);
      String pdeLine = astGenerator.editor.getLineText(pdeOffs[1]);
      String lookingFor = nodeName.toString();
      Messages.log(lookingFor + ", " + nodeName.getStartPosition());
      Messages.log(javaLineNumber +" JL " + javaLine + " LSO " + lineElement.getStartOffset() + ","
          + lineElement.getEndOffset());
      Messages.log(pdeOffs[1] + " PL " + pdeLine);
      if (!javaLine.contains(lookingFor) || !pdeLine.contains(lookingFor)) {
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,15 +1,14 @@
-public boolean highlightNode(ASTGenerator astGenerator){

-    if (!(Node instanceof SimpleName)) {

+public boolean highlightNode(JavaEditor editor){

+    if (!(node instanceof SimpleName)) {

       return false;

     }

     SimpleName nodeName = (SimpleName) node;

     try {

       //TODO: Redundant code. See ASTGenerator.getJavaSourceCodeline()

       int javaLineNumber = getLineNumber(nodeName);

-      int pdeOffs[] = astGenerator.errorCheckerService

-          .calculateTabIndexAndLineNumber(javaLineNumber);

+      int pdeOffs[] = editor.getErrorChecker().calculateTabIndexAndLineNumber(javaLineNumber);

       PlainDocument javaSource = new PlainDocument();

-      javaSource.insertString(0, astGenerator.errorCheckerService.sourceCode, null);

+      javaSource.insertString(0, editor.getErrorChecker().sourceCode, null);

       Element lineElement = javaSource.getDefaultRootElement()

           .getElement(javaLineNumber-1);

       if(lineElement == null) {

@@ -20,8 +19,8 @@
       String javaLine = javaSource.getText(lineElement.getStartOffset(),

                                            lineElement.getEndOffset()

                                                - lineElement.getStartOffset());

-      astGenerator.editor.getSketch().setCurrentCode(pdeOffs[0]);

-      String pdeLine = astGenerator.editor.getLineText(pdeOffs[1]);

+      editor.getSketch().setCurrentCode(pdeOffs[0]);

+      String pdeLine = editor.getLineText(pdeOffs[1]);

       String lookingFor = nodeName.toString();

       Messages.log(lookingFor + ", " + nodeName.getStartPosition());

       Messages.log(javaLineNumber +" JL " + javaLine + " LSO " + lineElement.getStartOffset() + ","

@@ -41,9 +40,9 @@
         		"Please file a bug report.");

         return false;

       }

-      int lso = astGenerator.editor.getTextArea().getLineStartOffset(pdeOffs[1]);

+      int lso = editor.getTextArea().getLineStartOffset(pdeOffs[1]);

       highlightStart += lso;

```

---

### [88/102] `Param_177`

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
@param clazz the annotation class to check for
```

**标准注释 (ground truth)**
```
@param fqcn the fully qualified class name of the annotation to check for
```

**生成注释 (generated)**
```
@param fqcn the fully qualified class name of the annotation to check for
```

**当前代码 (new_code)**
```java
	public static AnnotationMirror getAnnotationMirror(Element element, String fqcn) {
		assert element != null;
		assert fqcn != null;

		AnnotationMirror mirror = null;
		for ( AnnotationMirror am : element.getAnnotationMirrors() ) {
			if ( isAnnotationMirrorOfType( am, fqcn ) ) {
				mirror = am;
				break;
			}
		}
		return mirror;
	}

```

**变更前代码 (old_code)**
```java
	public static AnnotationMirror getAnnotationMirror(Element element, Class<? extends Annotation> clazz) {
		assert element != null;
		assert clazz != null;

		AnnotationMirror mirror = null;
		for ( AnnotationMirror am : element.getAnnotationMirrors() ) {
			if ( isAnnotationMirrorOfType( am, clazz ) ) {
				mirror = am;
				break;
			}
		}
		return mirror;
	}

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,10 +1,10 @@
-public static AnnotationMirror getAnnotationMirror(Element element, Class<? extends Annotation> clazz) {

+public static AnnotationMirror getAnnotationMirror(Element element, String fqcn) {

 		assert element != null;

-		assert clazz != null;

+		assert fqcn != null;

 

 		AnnotationMirror mirror = null;

 		for ( AnnotationMirror am : element.getAnnotationMirrors() ) {

-			if ( isAnnotationMirrorOfType( am, clazz ) ) {

+			if ( isAnnotationMirrorOfType( am, fqcn ) ) {

 				mirror = am;

 				break;

 			}

```

---

### [89/102] `Param_179`

| 指标 | 值 |
|---|---|
| 检测状态 | ✓ 已检测 |
| BLEU-4 | 1.0000 |
| SARI | 1.0000 |
| GLEU | 1.0000 |
| METEOR | 0.9977 |
| xMatch | ✓ |

**原注释 (source)**
```
@param body Created user object
```

**标准注释 (ground truth)**
```
@param user Created user object
```

**生成注释 (generated)**
```
@param user Created user object
```

**当前代码 (new_code)**
```java
  public void  createUser (User user) throws ApiException {
    Object localVarPostBody = user;
    // verify the required parameter 'user' is set
    if (user == null) {
       throw new ApiException(400, "Missing the required parameter 'user' when calling createUser");
    }

    // create path and map variables
    String localVarPath = "/user".replaceAll("\\{format\\}","json");

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    // header params
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    // form params
    Map<String, String> localVarFormParams = new HashMap<String, String>();



    String[] localVarContentTypes = {
      "application/json"
    };
    String localVarContentType = localVarContentTypes.length > 0 ? localVarContentTypes[0] : "application/json";

    if (localVarContentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();
      

      localVarPostBody = localVarBuilder.build();
// ... (truncated)
```

**变更前代码 (old_code)**
```java
  public void  createUser (User body) throws ApiException {
    Object localVarPostBody = body;
    // verify the required parameter 'body' is set
    if (body == null) {
       throw new ApiException(400, "Missing the required parameter 'body' when calling createUser");
    }

    // create path and map variables
    String localVarPath = "/user".replaceAll("\\{format\\}","json");

    // query params
    List<Pair> localVarQueryParams = new ArrayList<Pair>();
    // header params
    Map<String, String> localVarHeaderParams = new HashMap<String, String>();
    // form params
    Map<String, String> localVarFormParams = new HashMap<String, String>();



    String[] localVarContentTypes = {
      
    };
    String localVarContentType = localVarContentTypes.length > 0 ? localVarContentTypes[0] : "application/json";

    if (localVarContentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder localVarBuilder = MultipartEntityBuilder.create();
      

      localVarPostBody = localVarBuilder.build();
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,8 +1,8 @@
-public void  createUser (User body) throws ApiException {

-    Object localVarPostBody = body;

-    // verify the required parameter 'body' is set

-    if (body == null) {

-       throw new ApiException(400, "Missing the required parameter 'body' when calling createUser");

+public void  createUser (User user) throws ApiException {

+    Object localVarPostBody = user;

+    // verify the required parameter 'user' is set

+    if (user == null) {

+       throw new ApiException(400, "Missing the required parameter 'user' when calling createUser");

     }

 

     // create path and map variables

@@ -18,7 +18,7 @@
 

 

     String[] localVarContentTypes = {

-      

+      "application/json"

     };

     String localVarContentType = localVarContentTypes.length > 0 ? localVarContentTypes[0] : "application/json";

 

```

---

### [96/102] `Param_194`

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
@param uri the ContentValues to read from and update
```

**标准注释 (ground truth)**
```
@param values the ContentValues to read from and update
```

**生成注释 (generated)**
```
@param values the ContentValues to read from and update
```

**当前代码 (new_code)**
```java
    private boolean resolveAccount(ContentValues values, Account account) {
        // If either is specified then both must be specified.
        final String accountName = values.getAsString(RawContacts.ACCOUNT_NAME);
        final String accountType = values.getAsString(RawContacts.ACCOUNT_TYPE);
        if (!TextUtils.isEmpty(accountName) || !TextUtils.isEmpty(accountType)) {
            final Account valuesAccount = new Account(accountName, accountType);
            if (account != null && !valuesAccount.equals(account)) {
                return false;
            }
            account = valuesAccount;
        }
        if (account != null) {
            values.put(RawContacts.ACCOUNT_NAME, account.name);
            values.put(RawContacts.ACCOUNT_TYPE, account.type);
        }
        return true;
    }


```

**变更前代码 (old_code)**
```java
    private boolean resolveAccount(Uri uri, ContentValues values) {
        String accountName = getQueryParameter(uri, RawContacts.ACCOUNT_NAME);
        String accountType = getQueryParameter(uri, RawContacts.ACCOUNT_TYPE);

        if (TextUtils.isEmpty(accountName) || TextUtils.isEmpty(accountType)) {
            accountName = null;
            accountType = null;
        }

        String valueAccountName = values.getAsString(RawContacts.ACCOUNT_NAME);
        String valueAccountType = values.getAsString(RawContacts.ACCOUNT_TYPE);

        if (TextUtils.isEmpty(valueAccountName) && TextUtils.isEmpty(valueAccountType)) {
            values.put(RawContacts.ACCOUNT_NAME, accountName);
            values.put(RawContacts.ACCOUNT_TYPE, accountType);
        } else {
            if (accountName != null && !accountName.equals(valueAccountName)) {
                return false;
            }

            if (accountType != null && !accountType.equals(valueAccountType)) {
                return false;
            }

            accountName = valueAccountName;
            accountType = valueAccountType;
        }

        if (TextUtils.isEmpty(accountName) || TextUtils.isEmpty(accountType)) {
            mAccount = null;
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,41 +1,17 @@
-private boolean resolveAccount(Uri uri, ContentValues values) {

-        String accountName = getQueryParameter(uri, RawContacts.ACCOUNT_NAME);

-        String accountType = getQueryParameter(uri, RawContacts.ACCOUNT_TYPE);

-

-        if (TextUtils.isEmpty(accountName) || TextUtils.isEmpty(accountType)) {

-            accountName = null;

-            accountType = null;

-        }

-

-        String valueAccountName = values.getAsString(RawContacts.ACCOUNT_NAME);

-        String valueAccountType = values.getAsString(RawContacts.ACCOUNT_TYPE);

-

-        if (TextUtils.isEmpty(valueAccountName) && TextUtils.isEmpty(valueAccountType)) {

-            values.put(RawContacts.ACCOUNT_NAME, accountName);

-            values.put(RawContacts.ACCOUNT_TYPE, accountType);

-        } else {

-            if (accountName != null && !accountName.equals(valueAccountName)) {

+private boolean resolveAccount(ContentValues values, Account account) {

+        // If either is specified then both must be specified.

+        final String accountName = values.getAsString(RawContacts.ACCOUNT_NAME);

+        final String accountType = values.getAsString(RawContacts.ACCOUNT_TYPE);

+        if (!TextUtils.isEmpty(accountName) || !TextUtils.isEmpty(accountType)) {

+            final Account valuesAccount = new Account(accountName, accountType);

+            if (account != null && !valuesAccount.equals(account)) {

                 return false;

             }

-

-            if (accountType != null && !accountType.equals(valueAccountType)) {

-                return false;

-            }

-

-            accountName = valueAccountName;

-            accountType = valueAccountType;

+            account = valuesAccount;

         }

-

-        if (TextUtils.isEmpty(accountName) || TextUtils.isEmpty(accountType)) {

```

---

### [97/102] `Param_196`

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
@param e the element to add
```

**标准注释 (ground truth)**
```
@param o the element to add
```

**生成注释 (generated)**
```
@param o the element to add
```

**当前代码 (new_code)**
```java
    public boolean add(E o) {
        return super.add(o);
    }


```

**变更前代码 (old_code)**
```java
    public boolean add(E e) {
        return offer(e);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean add(E e) {

-        return offer(e);

+public boolean add(E o) {

+        return super.add(o);

     }
```

---

### [98/102] `Param_198`

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
@param frameAddress - frame from which the reply came
```

**标准注释 (ground truth)**
```
@param incomingFrameAddress - frame from which the reply came
```

**生成注释 (generated)**
```
@param incomingFrameAddress - frame from which the reply came
```

**当前代码 (new_code)**
```java
    public SeleneseCommand handleCommandResult(String commandResult, FrameAddress incomingFrameAddress, String uniqueId) {
        SeleneseQueue queue;
        if (!SeleniumServer.isProxyInjectionMode()) {
            queue = getSeleneseQueue();
        }
        else {
            if (incomingFrameAddress.getWindowName().equals(SELENIUM_WINDOW_NAME_UNKNOWN_POPUP)) {
                boolean foundFrameAddressOfUnknownPopup = false;
                for (FrameAddress knownFrameAddress : frameAddressToSeleneseQueue.keySet()) {
                    // the situation being handled here: a pop-up window has either just loaded or reloaded, and therefore
                    // doesn't know its name.  It uses SELENIUM_WINDOW_NAME_UNKNOWN_POPUP as a placeholder.
                    // Meanwhile, on the selenium server-side, a thread is waiting for this result.
                    //
                    // To determine if this has happened, we cycle through all of the SeleneseQueue objects,
                    // looking for ones with a matching local frame address (e.g., top.frames[1]), is also a
                    // pop-up, and which has a thread waiting on a result.  If all of these conditions hold,
                    // then we figure this queue is the one that we want:
                    if (knownFrameAddress.getLocalFrameAddress().equals(incomingFrameAddress.getLocalFrameAddress())
                            && !knownFrameAddress.getWindowName().equals(DEFAULT_SELENIUM_WINDOW_NAME)
                            && frameAddressToSeleneseQueue.get(knownFrameAddress).getCommandResultHolder().hasBlockedGetter()) {
                        incomingFrameAddress = knownFrameAddress;
                        foundFrameAddressOfUnknownPopup = true;
                        break;
                    }
                }
                if (!foundFrameAddressOfUnknownPopup) {
                    SeleniumServer.log("WARNING: unknown popup " + incomingFrameAddress + " was not resolved");
                }
            }
            queue = getSeleneseQueue(incomingFrameAddress);
// ... (truncated)
```

**变更前代码 (old_code)**
```java
    public SeleneseCommand handleCommandResult(String commandResult, FrameAddress frameAddress, String uniqueId) {
        SeleneseQueue queue;
        if (!SeleniumServer.isProxyInjectionMode()) {
            queue = getSeleneseQueue();
        }
        else {
            if (frameAddress.getWindowName().equals(SELENIUM_WINDOW_NAME_UNKNOWN_POPUP)) {
                boolean foundFrameAddressOfUnknownPopup = false;
                for (FrameAddress f : frameAddressToSeleneseQueue.keySet()) {
                    // the situation being handled here: a pop-up window has either just loaded or reloaded, and therefore
                    // doesn't know its name.  It uses SELENIUM_WINDOW_NAME_UNKNOWN_POPUP as a placeholder.
                    // Meanwhile, on the selenium server-side, a thread is waiting for this result.
                    //
                    // To determine if this has happened, we cycle through all of the SeleneseQueue objects,
                    // looking for ones with a matching local frame address (e.g., top.frames[1]), is also a
                    // pop-up, and which has a thread waiting on a result.  If all of these conditions hold,
                    // then we figure this queue is the one that we want:
                    if (f.getLocalFrameAddress().equals(frameAddress.getLocalFrameAddress())
                            && !f.getWindowName().equals(DEFAULT_SELENIUM_WINDOW_NAME)
                            && frameAddressToSeleneseQueue.get(f).getCommandResultHolder().hasBlockedGetter()) {
                        frameAddress = f;
                        foundFrameAddressOfUnknownPopup = true;
                        break;
                    }
                }
                if (!foundFrameAddressOfUnknownPopup) {
                    SeleniumServer.log("WARNING: unknown popup " + frameAddress + " was not resolved");
                }
            }
            queue = getSeleneseQueue(frameAddress);
// ... (truncated)
```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,12 +1,12 @@
-public SeleneseCommand handleCommandResult(String commandResult, FrameAddress frameAddress, String uniqueId) {

+public SeleneseCommand handleCommandResult(String commandResult, FrameAddress incomingFrameAddress, String uniqueId) {

         SeleneseQueue queue;

         if (!SeleniumServer.isProxyInjectionMode()) {

             queue = getSeleneseQueue();

         }

         else {

-            if (frameAddress.getWindowName().equals(SELENIUM_WINDOW_NAME_UNKNOWN_POPUP)) {

+            if (incomingFrameAddress.getWindowName().equals(SELENIUM_WINDOW_NAME_UNKNOWN_POPUP)) {

                 boolean foundFrameAddressOfUnknownPopup = false;

-                for (FrameAddress f : frameAddressToSeleneseQueue.keySet()) {

+                for (FrameAddress knownFrameAddress : frameAddressToSeleneseQueue.keySet()) {

                     // the situation being handled here: a pop-up window has either just loaded or reloaded, and therefore

                     // doesn't know its name.  It uses SELENIUM_WINDOW_NAME_UNKNOWN_POPUP as a placeholder.

                     // Meanwhile, on the selenium server-side, a thread is waiting for this result.

@@ -15,19 +15,19 @@
                     // looking for ones with a matching local frame address (e.g., top.frames[1]), is also a

                     // pop-up, and which has a thread waiting on a result.  If all of these conditions hold,

                     // then we figure this queue is the one that we want:

-                    if (f.getLocalFrameAddress().equals(frameAddress.getLocalFrameAddress())

-                            && !f.getWindowName().equals(DEFAULT_SELENIUM_WINDOW_NAME)

-                            && frameAddressToSeleneseQueue.get(f).getCommandResultHolder().hasBlockedGetter()) {

-                        frameAddress = f;

+                    if (knownFrameAddress.getLocalFrameAddress().equals(incomingFrameAddress.getLocalFrameAddress())

+                            && !knownFrameAddress.getWindowName().equals(DEFAULT_SELENIUM_WINDOW_NAME)

+                            && frameAddressToSeleneseQueue.get(knownFrameAddress).getCommandResultHolder().hasBlockedGetter()) {

+                        incomingFrameAddress = knownFrameAddress;

                         foundFrameAddressOfUnknownPopup = true;

                         break;

                     }

                 }

                 if (!foundFrameAddressOfUnknownPopup) {

-                    SeleniumServer.log("WARNING: unknown popup " + frameAddress + " was not resolved");

+                    SeleniumServer.log("WARNING: unknown popup " + incomingFrameAddress + " was not resolved");

                 }

             }

-            queue = getSeleneseQueue(frameAddress);

```

---

### [99/102] `Param_200`

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
@param attributes an object containing an AttributeMap
```

**标准注释 (ground truth)**
```
@param withAttributes an object containing an AttributeMap
```

**生成注释 (generated)**
```
@param withAttributes an object containing an AttributeMap
```

**当前代码 (new_code)**
```java
    public boolean get(WithAttributes withAttributes) {
        return withAttributes.getAttributes().get(this);
    }


```

**变更前代码 (old_code)**
```java
    public boolean get(WithAttributes attributes) {
        return attributes.getAttributes().get(this);
    }

```

**代码变更 (diff)**
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public boolean get(WithAttributes attributes) {

-        return attributes.getAttributes().get(this);

+public boolean get(WithAttributes withAttributes) {

+        return withAttributes.getAttributes().get(this);

     }
```

---

