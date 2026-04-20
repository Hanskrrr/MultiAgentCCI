# Summary 类别错误批次3 — 全量误判案例（compact 紧凑模式） — 全链路 Agent 判定报告

| 项目 | 值 |
|---|---|
| 模型 | `glm-4-plus` |
| use-diff | `True` |
| parser | `treesitter` |
| compact 模式 | `True` |
| 总样本 | 77 |
| 运行报错 | 0 |
| 本次判对 | 39 / 77 |

## 共用 Prompt 分类规则（所有样本通用，以下每个样本不再重复）

```text
Classification Guidelines (IMPORTANT):

=== Core Principle ===
A method summary is a concise sentence describing WHAT the method does — its action, its subject (the thing being acted upon), and its effect.
It is INCONSISTENT when the summary no longer accurately describes the method after the code change.
It is CONSISTENT only when every key phrase in the summary still maps to something the current code actually does.

=== What MUST be flagged as INCONSISTENT ===

1. ACTION CHANGE: The summary's verb phrase ("creates", "returns", "checks", "initializes") no longer matches. E.g., summary says "initializes panelCommand" but code is now `getExportButton()` returning a button. INCONSISTENT.

2. SUBJECT/OBJECT CHANGE: The thing described in the summary (what is returned / operated on / created) has changed. E.g., summary says "Add a tag to the set of filters" (object = tag) but code now takes `tagId` and `category` strings. Even if the "purpose feels similar", the OBJECT changed → INCONSISTENT.

3. QUALIFIER/DETAIL NO LONGER TRUE: The summary mentions a specific qualifier ("as single member of a cluster", "with the default server URL") that the current code no longer satisfies. INCONSISTENT.

4. PLACEHOLDER / VAGUE SUMMARY: A summary that is just "Returns", "DOCUMENT ME!", "TODO", a single word, or similarly non-descriptive IS INCONSISTENT whenever the method body is non-trivial. A real method deserves a real summary — placeholders do not honestly describe the code.

5. INCOMPLETENESS: If the summary describes a SUBSET of the method's behavior (e.g., mentions one return path but the code has extra branches returning different things or adds a new condition), and the omission is significant (not a trivial internal helper), it is INCONSISTENT.

6. SIGNATURE/STRUCTURAL DRIFT: When structural observations show RETURN TYPE CHANGED, PARAMETERS CHANGED, or METHOD NAME CHANGED, and the summary's description no longer maps cleanly onto the new signature, it is INCONSISTENT. Do not dismiss a parameter-count change as "implementation detail" when the summary presupposes the old signature.

=== What counts as CONSISTENT (be strict — do NOT over-tolerate) ===

A. PURE RENAMING / REFORMAT: The method was reformatted, a local variable was renamed, or a helper method is called, but the visible action/subject/qualifiers in the summary all still hold. CONSISTENT.

B. INTERNAL ALGORITHMIC CHANGE WITH SAME CONTRACT: The method body switched algorithms (e.g., `for` loop replaced with `stream`, or `StringBuffer` replaced with `StringBuilder`) but the summary's action + subject + effect are all unchanged. CONSISTENT.

C. WARNING — DO NOT USE THIS REASONING: Phrases like "the core functionality remains the same", "fundamental purpose is unchanged", "core behavior is preserved", "high-level purpose remains" are OFTEN WRONG defenses that mask real drift. If you find yourself reaching for one of these phrases, stop and re-check: did the subject change? did a qualifier stop being true? did a parameter disappear? If yes to ANY, it is INCONSISTENT.

=== Using Observations ===
- A PARAMETERS CHANGED signal means the method's inputs changed. Check if the summary implicitly assumed the old inputs.
- A RETURN TYPE CHANGED signal means the method now produces a different thing. If the summary describes what is returned, it is almost certainly INCONSISTENT.
- A PLACEHOLDER SUMMARY signal almost always means INCONSISTENT — the non-descriptive comment cannot possibly faithfully describe a real method body.
- A METHOD NAME CHANGED signal is strong evidence of a rewrite → summary is likely outdated.

Benchmark Examples:
- Ex A (INCONSISTENT): Summary "Creates elastic node as single member of a cluster"; code was rewritten to "Creates an instance with existing settings" — the qualifier "single member of a cluster" is no longer true. INCONSISTENT.
- Ex B (INCONSISTENT): Summary "This method initializes panelCommand"; code now `getExportButton()` returning button — subject changed entirely. INCONSISTENT.
- Ex C (INCONSISTENT): Summary "Returns" alone; method body is non-trivial (e.g., delegates through a queue). Placeholder → INCONSISTENT.
- Ex D (INCONSISTENT): Summary "Add a tag to the set of filters"; code now takes (tagId, category) strings and returns boolean — object of action changed. INCONSISTENT.
- Ex E (CONSISTENT): Summary "Sends an email to the given address"; code still does `smtp.send(to_addr, content)`. Variables renamed but action/subject/effect unchanged → CONSISTENT.

Output Requirement:
Reasoning: Decompose the summary into (action, subject, qualifiers) and verify each against the current code:
- ACTION: "<the verb phrase>" → still done by the code? YES/NO
- SUBJECT: "<the object being acted upon>" → still this same thing? YES/NO
- QUALIFIERS: "<specific modifiers/conditions>" → still all true? YES/NO
- Brief conclusion: <1 sentence on whether summary still describes the method>
CONCLUSION: [CONSISTENT or INCONSISTENT]
```

---

## 汇总一览

| # | ID | 真实 | 预测 | 判定方式 | 原始注释 |
|---|---|---|---|---|---|
| FAIL 1 | `Summary_5` | `True` | `False` | `llm` | Construct the value of the data attribute of CloudEvent |
| FAIL 2 | `Summary_7` | `True` | `False` | `llm` | This method initializes txtPattern |
| OK 3 | `Summary_10` | `False` | `False` | `llm` | Returns the providers that are bound to the same locati |
| FAIL 4 | `Summary_11` | `True` | `False` | `llm` | Generate a "standard" (i.e., non-identifier and non-ver |
| OK 5 | `Summary_13` | `True` | `True` | `llm` | HBase region cut size, in GB |
| OK 6 | `Summary_15` | `True` | `True` | `llm` | Create a new  Builder configuration builder that starts |
| FAIL 7 | `Summary_17` | `True` | `False` | `llm` | Loads item sprite from game, makes transparent, and gen |
| FAIL 8 | `Summary_18` | `False` | `True` | `llm` | Return XML schema for the specified type, suitable for  |
| OK 9 | `Summary_19` | `True` | `True` | `llm` | Given a Class of something that extends AsyncSupport, i |
| OK 10 | `Summary_21` | `True` | `True` | `llm` | Allow to print directives. |
| FAIL 11 | `Summary_24` | `False` | `True` | `llm` | Check if the Elasticsearch  Node is connected and that  |
| OK 12 | `Summary_26` | `False` | `False` | `llm` | Returns true if, the lockClient is keeping the lock for |
| FAIL 13 | `Summary_30` | `False` | `True` | `llm` | Checks if a flag is set. |
| OK 14 | `Summary_31` | `True` | `True` | `llm` | Builds the  Client instance. |
| FAIL 15 | `Summary_36` | `False` | `True` | `llm` | Method that get's left and right incoming batch and pro |
| OK 16 | `Summary_39` | `True` | `True` | `llm` | Converts a value object for an expected JDBC type of  T |
| FAIL 17 | `Summary_40` | `False` | `True` | `llm` | Determines if a specified set of columns from a specifi |
| FAIL 18 | `Summary_43` | `True` | `False` | `llm` | Create RelNode tree that produces a list of correlated  |
| OK 19 | `Summary_46` | `False` | `False` | `llm` | Returns if this query should buffer before emitting res |
| OK 20 | `Summary_47` | `True` | `True` | `llm` | Retrieve the fetch descriptor associated with the given |
| OK 21 | `Summary_49` | `True` | `True` | `llm` | Provided we  #supportsInsertSelectIdentity, then attach |
| OK 22 | `Summary_54` | `False` | `False` | `llm` | Checks if a flag is set. |
| OK 23 | `Summary_58` | `False` | `False` | `llm` | Creates and returns a new comparison object for the SQL |
| FAIL 24 | `Summary_60` | `True` | `False` | `llm` | Method for getting counts using named filters |
| OK 25 | `Summary_61` | `False` | `False` | `llm` | Returns all currently displayed sentences in string buf |
| OK 26 | `Summary_62` | `True` | `True` | `llm` | Returns newest checkmark that has already been computed |
| FAIL 27 | `Summary_65` | `False` | `True` | `llm` | Returns all currently displayed sentences in plain text |
| FAIL 28 | `Summary_66` | `True` | `False` | `llm` | This method initializes panelCommand |
| FAIL 29 | `Summary_67` | `False` | `True` | `llm` | If a Schema contains a reference to an other Schema wit |
| OK 30 | `Summary_76` | `True` | `True` | `llm` | All proprietary Comet based  Servlet must invoke the ti |
| OK 31 | `Summary_77` | `False` | `False` | `llm` | Returns the common base directory between a current bas |
| FAIL 32 | `Summary_79` | `False` | `True` | `llm` | Does this time interval contain the specified time inte |
| OK 33 | `Summary_81` | `False` | `False` | `llm` | Installs a list of  RemotePackage and their dependent p |
| OK 34 | `Summary_83` | `False` | `False` | `llm` | Get the global configuration table name including the c |
| OK 35 | `Summary_87` | `False` | `False` | `llm` | Obtains a ISTextExpert instance for processing structur |
| OK 36 | `Summary_89` | `False` | `False` | `llm` | Create and return a new feature service with the defaul |
| FAIL 37 | `Summary_90` | `True` | `False` | `llm` | expect absolute request and allow both absolute and per |
| FAIL 38 | `Summary_91` | `True` | `False` | `llm` | GET /user/username |
| OK 39 | `Summary_93` | `True` | `True` | `llm` | Returns an Iterable of the lines in the file, wrapping  |
| OK 40 | `Summary_95` | `True` | `True` | `llm` | Returns a Button which shows a given text. |
| FAIL 41 | `Summary_99` | `True` | `False` | `llm` | Override with any special handling of response codes |
| OK 42 | `Summary_101` | `True` | `True` | `llm` | Seeks the field with the given name in the stream and p |
| FAIL 43 | `Summary_103` | `True` | `False` | `llm` | Checks if this potato is baked. |
| FAIL 44 | `Summary_104` | `False` | `True` | `llm` | Creates a renderscript allocation from a bitmap |
| FAIL 45 | `Summary_105` | `True` | `False` | `llm` | Computes the row type of an  Aggregate before it exists |
| FAIL 46 | `Summary_106` | `False` | `True` | `llm` | Returns the sibling on the right of the end of given  T |
| OK 47 | `Summary_107` | `True` | `True` | `llm` | Output the date time in ISO8601 format (yyyy-MM-ddTHH:m |
| FAIL 48 | `Summary_108` | `False` | `True` | `llm` | Evaluate a PLAIN login challenge, returning the a resul |
| OK 49 | `Summary_109` | `True` | `True` | `llm` | Gets the given  start and  end view positions offset to |
| FAIL 50 | `Summary_115` | `True` | `False` | `llm` | This method initializes tableAuth |
| OK 51 | `Summary_118` | `False` | `False` | `llm` | Removes the content source from this channel, if it exi |
| FAIL 52 | `Summary_119` | `True` | `False` | `llm` | Returns whether an instance of Chrome is currently conn |
| FAIL 53 | `Summary_121` | `True` | `False` | `llm` | Creates a new UserFolder, inflated from R.layout.user_f |
| OK 54 | `Summary_124` | `False` | `False` | `llm` | First authenticates the AuthenticationToken argument, a |
| FAIL 55 | `Summary_126` | `False` | `True` | `llm` | Make fully qualified URI based on the default file syst |
| OK 56 | `Summary_130` | `False` | `False` | `llm` | Build a DruidDimensionsLoader. |
| OK 57 | `Summary_144` | `False` | `False` | `llm` | Gets the element for the method corresponding to this i |
| FAIL 58 | `Summary_147` | `True` | `False` | `llm` | Get a  Struct representation of the source  #partition( |
| OK 59 | `Summary_149` | `True` | `True` | `llm` | When initializing the profile, Opera rapidly starts, st |
| OK 60 | `Summary_152` | `False` | `False` | `llm` | Creates a  UserAdapter if there is more than one profil |
| FAIL 61 | `Summary_153` | `True` | `False` | `llm` | An expectation for checking child WebElement as a part  |
| OK 62 | `Summary_164` | `False` | `False` | `llm` | Invoke the proprietary  CometSupport |
| FAIL 63 | `Summary_169` | `True` | `False` | `llm` | Returns a DurationField representing seconds. |
| FAIL 64 | `Summary_170` | `False` | `True` | `llm` | Given a URL, attempt to infer and return the hostname f |
| FAIL 65 | `Summary_172` | `False` | `True` | `llm` | Helper method to return the constant string for a  CstI |
| OK 66 | `Summary_174` | `False` | `False` | `llm` | Does this time interval contain or equal the specified  |
| OK 67 | `Summary_177` | `True` | `True` | `llm` | Converts an old style id to a new style id. |
| FAIL 68 | `Summary_179` | `True` | `False` | `llm` | Checks if this function replacement is needed. |
| FAIL 69 | `Summary_181` | `True` | `False` | `llm` | Converts a value object for an expected JDBC type of  T |
| OK 70 | `Summary_182` | `False` | `False` | `llm` | Tests if the editor is in word-wrap mode. |
| FAIL 71 | `Summary_184` | `False` | `True` | `llm` | If a ApiResponse contains a reference to an other ApiRe |
| OK 72 | `Summary_186` | `False` | `False` | `llm` | Try to get the primary  java.net.InetAddress of the pri |
| FAIL 73 | `Summary_189` | `True` | `False` | `llm` | Maps offset from java code to pde code. |
| FAIL 74 | `Summary_194` | `False` | `True` | `llm` | Checks if toolitem is selected |
| OK 75 | `Summary_195` | `True` | `True` | `llm` | Set the Year of a week based year component of the spec |
| OK 76 | `Summary_204` | `False` | `False` | `llm` | Returns the encoding used to send and receive lines fro |
| FAIL 77 | `Summary_205` | `True` | `False` | `llm` | Returns the label associated with the current node, or  |

---

## FAIL [1/77] `Summary_5`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Construct the value of the data attribute of CloudEvents.` |
| ground_truth_comment | `Construct the value of the data attribute of CloudEvents.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public Struct ceDataAttribute() {
        Struct data = new Struct(ceDataAttributeSchema());
        if (recordParser.before() != null) {
            data.put(Envelope.FieldName.BEFORE, recordParser.before());
        }
        if (recordParser.after() != null) {
            data.put(Envelope.FieldName.AFTER, recordParser.after());
        }
        return data;
    }
```

**code_snippet**

```java
public Struct ceDataAttribute() {
        return recordParser.data();
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: ceDataAttribute() -> Struct
Parameters Details: []
intention:      Method 'ceDataAttribute' (ce Data Attribute)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Construct the value of the data attribute of CloudEvents.

[Current Code]
    public Struct ceDataAttribute() {
        return recordParser.data();
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,10 +1,3 @@
 public Struct ceDataAttribute() {

-        Struct data = new Struct(ceDataAttributeSchema());

-        if (recordParser.before() != null) {

-            data.put(Envelope.FieldName.BEFORE, recordParser.before());

-        }

-        if (recordParser.after() != null) {

-            data.put(Envelope.FieldName.AFTER, recordParser.after());

-        }

-        return data;

+        return recordParser.data();

     }
```

[Code Context]
- Signature: Full Signature: ceDataAttribute() -> Struct
Parameters Details: []
- Intent: Method 'ceDataAttribute' (ce Data Attribute)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Construct the value of" → The code now simply returns recordParser.data() rather than constructing a new Struct. The action has changed from constructing to returning an existing value. NO
- SUBJECT: "the data attribute of CloudEvents" → The method still returns a Struct that represents the data attribute of CloudEvents. YES
- QUALIFIERS: None specified in the summary. N/A
- Brief conclusion: The summary indicates the method constructs the data attribute, but the current code simply returns an existing data structure without construction.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: ceDataAttribute() -> Struct
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Construct the value of" → The code now simply returns recordParser.data() rath...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [2/77] `Summary_7`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `This method initializes txtPattern` |
| ground_truth_comment | `This method initializes txtPattern` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public JTextField getTxtPattern() {
		if (txtPattern == null) {
			txtPattern = new JTextField();
		}
		return txtPattern;
	}
```

**code_snippet**

```java
public ZapTextField getTxtPattern() {
		if (txtPattern == null) {
			txtPattern = new ZapTextField();
		}
		return txtPattern;
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getTxtPattern() -> ZapTextField
Parameters Details: []
intention:      Method 'getTxtPattern' (get Txt Pattern)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'JTextField' -> 'ZapTextField'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
This method initializes txtPattern

[Current Code]
	public ZapTextField getTxtPattern() {
		if (txtPattern == null) {
			txtPattern = new ZapTextField();
		}
		return txtPattern;
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
-public JTextField getTxtPattern() {

+public ZapTextField getTxtPattern() {

 		if (txtPattern == null) {

-			txtPattern = new JTextField();

+			txtPattern = new ZapTextField();

 		}

 		return txtPattern;

 	}
```

[Code Context]
- Signature: Full Signature: getTxtPattern() -> ZapTextField
Parameters Details: []
- Intent: Method 'getTxtPattern' (get Txt Pattern)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'JTextField' -> 'ZapTextField'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "initializes" → NO, the method doesn't initialize txtPattern, it returns it (lazy initialization pattern)
- SUBJECT: "txtPattern" → YES, the method is still about txtPattern
- QUALIFIERS: None mentioned in the summary
- Brief conclusion: The summary incorrectly states that the method initializes txtPattern when it actually returns a lazily initialized instance of txtPattern.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getTxtPattern() -> ZapTextField
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "initializes" → NO, the method doesn't initialize txtPattern, it returns it (la...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [3/77] `Summary_10`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns the providers that are bound to the same location as the given ISO 3166 code and of the given type.` |
| ground_truth_comment | `Returns the providers that are bound to the same location as the given ISO 3166 code and of the given contextWrappableAs.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static Iterable<ProviderMetadata<?, ?, ?, ?>> boundedByIso3166Code(String iso3166Code, ApiType type) {
      return filter(all(),
            Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates.type(type)));
   }
```

**code_snippet**

```java
public static Iterable<ProviderMetadata> boundedByIso3166Code(String iso3166Code,
            TypeToken<? extends Wrapper> contextWrappableAs) {
      return filter(all(), Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates
               .contextWrappableAs(contextWrappableAs)));
   }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: boundedByIso3166Code(String iso3166Code, TypeToken<? extends Wrapper> contextWrappableAs) -> Iterable<ProviderMetadata>
Parameters Details: [{"name": "iso3166Code", "type": "String"}, {"name": "contextWrappableAs", "type": "TypeToken<? extends Wrapper>"}]
intention:      Method 'boundedByIso3166Code' (bounded By Iso3166Code)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'Iterable<ProviderMetadata<?, ?, ?, ?>>' -> 'Iterable<ProviderMetadata>'. If the comment references the old return type, it is INCONSISTENT.", "PARAMETERS CHANGED: removed params: {'type'}; added params: {'contextWrappableAs'}.", "IDENTIFIER DRIFT: comment mentions 'type' which no longer exists in new code. Possible renames: ['TypeToken']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns the providers that are bound to the same location as the given ISO 3166 code and of the given type.

[Current Code]
   public static Iterable<ProviderMetadata> boundedByIso3166Code(String iso3166Code,
            TypeToken<? extends Wrapper> contextWrappableAs) {
      return filter(all(), Predicates.and(ProviderPredicates.boundedByIso3166Code(iso3166Code), ProviderPredicates
               .contextWrappableAs(contextWrappableAs)));
   }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: boundedByIso3166Code(String iso3166Code, TypeToken<? extends Wrapper> contextWrappableAs) -> Iterable<ProviderMetadata>
Parameters Details: [{"name": "iso3166Code", "type": "String"}, {"name": "contextWrappableAs", "type": "TypeToken<? extends Wrapper>"}]
- Intent: Method 'boundedByIso3166Code' (bounded By Iso3166Code)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'Iterable<ProviderMetadata<?, ?, ?, ?>>' -> 'Iterable<ProviderMetadata>'. If the comment references the old return type, it is INCONSISTENT.
- PARAMETERS CHANGED: removed params: {'type'}; added params: {'contextWrappableAs'}.
- IDENTIFIER DRIFT: comment mentions 'type' which no longer exists in new code. Possible renames: ['TypeToken'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES. The method still returns an Iterable of ProviderMetadata.
- SUBJECT: "the providers that are bound to the same location as the given ISO 3166 code" → still this same thing? YES. The method still filters providers based on the ISO 3166 code.
- QUALIFIERS: "and of the given type" → still all true? NO. The method no longer takes a "type" parameter but instead takes a "contextWrappableAs" parameter. The qualifier mentions "type" which no longer exists in the current code.

Brief conclusion: The summary mentions a "type" parameter that no longer exists in the current code, and the method now uses a different parameter ("contextWrappableAs") instead.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: boundedByIso3166Code(String iso3166Code, TypeToken<? extends Wrapper> contextWra
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → still done by the code? YES. The method still returns an Iterable o...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [4/77] `Summary_11`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Generate a "standard" (i.e., non-identifier and non-version) based on the given mapped property.` |
| ground_truth_comment | `Generate a "standard" (i.e., non-identifier and non-version) based on the given mapped property.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static StandardProperty buildStandardProperty(Property property, boolean lazyAvailable) {
		
		final Type type = property.getValue().getType();
		
		// we need to dirty check collections, since they can cause an owner
		// version number increment
		
		// we need to dirty check many-to-ones with not-found="ignore" in order 
		// to update the cache (not the database), since in this case a null
		// entity reference can lose information
		
		boolean alwaysDirtyCheck = type.isAssociationType() && 
				( (AssociationType) type ).isAlwaysDirtyChecked(); 

		return new StandardProperty(
				property.getName(),
				property.getNodeName(),
				type,
				lazyAvailable && property.isLazy(),
				property.isInsertable(),
				property.isUpdateable(),
		        property.getGeneration() == PropertyGeneration.INSERT || property.getGeneration() == PropertyGeneration.ALWAYS,
				property.getGeneration() == PropertyGeneration.ALWAYS,
				property.isOptional(),
				alwaysDirtyCheck || property.isUpdateable(),
				property.isOptimisticLocked(),
				property.getCascadeStyle(),
		        property.getValue().getFetchMode()
			);
	}
```

**code_snippet**

```java
public static StandardProperty buildStandardProperty(AttributeBinding property, boolean lazyAvailable) {

		final Type type = property.getHibernateTypeDescriptor().getExplicitType();

		// we need to dirty check collections, since they can cause an owner
		// version number increment

		// we need to dirty check many-to-ones with not-found="ignore" in order
		// to update the cache (not the database), since in this case a null
		// entity reference can lose information

		boolean alwaysDirtyCheck = type.isAssociationType() &&
				( (AssociationType) type ).isAlwaysDirtyChecked();

		if ( property.isSimpleValue() ) {
			SimpleAttributeBinding simpleProperty = ( SimpleAttributeBinding ) property;
			return new StandardProperty(
					simpleProperty.getAttribute().getName(),
					simpleProperty.getNodeName(),
					type,
					lazyAvailable && simpleProperty.isLazy(),
					simpleProperty.isInsertable(),
					simpleProperty.isUpdatable(),
					simpleProperty.getGeneration() == PropertyGeneration.INSERT || simpleProperty.getGeneration() == PropertyGeneration.ALWAYS,
					simpleProperty.getGeneration() == PropertyGeneration.ALWAYS,
					simpleProperty.isNullable(),
					alwaysDirtyCheck || simpleProperty.isUpdatable(),
					simpleProperty.isOptimisticLockable(),
					// TODO: get cascadeStyle from simpleProperty when HHH-6355 is fixed; for now, assume NONE
					//simpleProperty.getCascadeStyle(),
					CascadeStyle.NONE,
					// TODO: get fetchMode() from simpleProperty when HHH-6357 is fixed; for now, assume FetchMode.DEFAULT
					//simpleProperty.getFetchMode()
					FetchMode.DEFAULT
				);
		}
		else {
			PluralAttributeBinding pluralProperty = ( PluralAttributeBinding ) property;

			return new StandardProperty(
					pluralProperty.getAttribute().getName(),
					pluralProperty.getNodeName(),
					type,
					lazyAvailable && pluralProperty.isLazy(),
					// TODO: fix this when HHH-6356 is fixed; for now assume PluralAttributeBinding is updatable and insertable
					// pluralProperty.isInsertable(),
					//pluralProperty.isUpdatable(),
					true,
					true,
					false,
					false,
					pluralProperty.isNullable(),
					// TODO: fix this when HHH-6356 is fixed; for now assume PluralAttributeBinding is updatable and insertable
					//alwaysDirtyCheck || pluralProperty.isUpdatable(),
					true,
					pluralProperty.isOptimisticLocked(),
					// TODO: get cascadeStyle from property when HHH-6355 is fixed; for now, assume NONE
					//pluralProperty.getCascadeStyle(),
					CascadeStyle.NONE,
					// TODO: get fetchMode() from simpleProperty when HHH-6357 is fixed; for now, assume FetchMode.DEFAULT
					//pluralProperty.getFetchMode()
					FetchMode.DEFAULT
				);
		}
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: buildStandardProperty(AttributeBinding property, boolean lazyAvailable) -> StandardProperty
Parameters Details: [{"name": "property", "type": "AttributeBinding"}, {"name": "lazyAvailable", "type": "boolean"}]
intention:      Method 'buildStandardProperty' (build Standard Property)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'Property' which no longer exists in new code. Possible renames: ['pluralProperty', 'PluralAttributeBinding']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Generate a "standard" (i.e., non-identifier and non-version) based on the given mapped property.

[Current Code]
	public static StandardProperty buildStandardProperty(AttributeBinding property, boolean lazyAvailable) {

		final Type type = property.getHibernateTypeDescriptor().getExplicitType();

		// we need to dirty check collections, since they can cause an owner
		// version number increment

		// we need to dirty check many-to-ones with not-found="ignore" in order
		// to update the cache (not the database), since in this case a null
		// entity reference can lose information

		boolean alwaysDirtyCheck = type.isAssociationType() &&
				( (AssociationType) type ).isAlwaysDirtyChecked();

		if ( property.isSimpleValue() ) {
			SimpleAttributeBinding simpleProperty = ( SimpleAttributeBinding ) property;
			return new StandardProperty(
					simpleProperty.getAttribute().getName(),
					simpleProperty.getNodeName(),
					type,
					lazyAvailable && simpleProperty.isLazy(),
					simpleProperty.isInsertable(),
					simpleProperty.isUpdatable(),
					simpleProperty.getGeneration() == PropertyGeneration.INSERT || simpleProperty.getGeneration() == PropertyGeneration.ALWAYS,
					simpleProperty.getGeneration() == PropertyGeneration.ALWAYS,
					simpleProperty.isNullable(),
					alwaysDirtyCheck || simpleProperty.isUpdatable(),
					simpleProperty.isOptimisticLockable(),
					// TODO: get cascadeStyle from simpleProperty when HHH-6355 is fixed; for now, assume NONE
					//simpleProperty.getCascadeStyle(),
					CascadeStyle.NONE,
					// TODO: get fetchMode() from simpleProperty when HHH-6357 is fixed; for now, assume FetchMode.DEFAULT
					//simpleProperty.getFetchMode()
					FetchMode.DEFAULT
				);
		}
		else {
			PluralAttributeBinding pluralProperty = ( PluralAttributeBinding ) property;

			return new StandardProperty(
					pluralProperty.getAttribute().getName(),
					pluralProperty.getNodeName(),
					type,
					lazyAvailable && pluralProperty.isLazy(),
					// TODO: fix this when HHH-6356 is fixed; for now assume PluralAttributeBinding is updatable and insertable
					// pluralProperty.isInsertable(),
					//pluralProperty.isUpdatable(),
					true,
					true,
					false,
					false,
					pluralProperty.isNullable(),
					// TODO: fix this when HHH-6356 is fixed; for now assume PluralAttributeBinding is updatable and insertable
					//alwaysDirtyCheck || pluralProperty.isUpdatable(),
					true,
					pluralProperty.isOptimisticLocked(),
					// TODO: get cascadeStyle from property when HHH-6355 is fixed; for now, assume NONE
					//pluralProperty.getCascadeStyle(),
					CascadeStyle.NONE,
					// TODO: get fetchMode() from simpleProperty when HHH-6357 is fixed; for now, assume FetchMode.DEFAULT
					//pluralProperty.getFetchMode()
					FetchMode.DEFAULT
				);
		}
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,30 +1,65 @@
-public static StandardProperty buildStandardProperty(Property property, boolean lazyAvailable) {

-		

-		final Type type = property.getValue().getType();

-		

+public static StandardProperty buildStandardProperty(AttributeBinding property, boolean lazyAvailable) {

+

+		final Type type = property.getHibernateTypeDescriptor().getExplicitType();

+

 		// we need to dirty check collections, since they can cause an owner

 		// version number increment

-		

-		// we need to dirty check many-to-ones with not-found="ignore" in order 

+

+		// we need to dirty check many-to-ones with not-found="ignore" in order

 		// to update the cache (not the database), since in this case a null

 		// entity reference can lose information

-		

-		boolean alwaysDirtyCheck = type.isAssociationType() && 

-				( (AssociationType) type ).isAlwaysDirtyChecked(); 

 

-		return new StandardProperty(

-				property.getName(),

-				property.getNodeName(),

-				type,

-				lazyAvailable && property.isLazy(),

-				property.isInsertable(),

-				property.isUpdateable(),

-		        property.getGeneration() == PropertyGeneration.INSERT || property.getGeneration() == PropertyGeneration.ALWAYS,

-				property.getGeneration() == PropertyGeneration.ALWAYS,

-				property.isOptional(),

-				alwaysDirtyCheck || property.isUpdateable(),

-				property.isOptimisticLocked(),

-				property.getCascadeStyle(),

-		        property.getValue().getFetchMode()

-			);

+		boolean alwaysDirtyCheck = type.isAssociationType() &&

+				( (AssociationType) type ).isAlwaysDirtyChecked();

+

+		if ( property.isSimpleValue() ) {

+			SimpleAttributeBinding simpleProperty = ( SimpleAttributeBinding ) property;

+			return new StandardProperty(

+					simpleProperty.getAttribute().getName(),

+					simpleProperty.getNodeName(),

+					type,

+					lazyAvailable && simpleProperty.isLazy(),

+					simpleProperty.isInsertable(),

+					simpleProperty.isUpdatable(),

+					simpleProperty.getGeneration() == PropertyGeneration.INSERT || simpleProperty.getGeneration() == PropertyGeneration.ALWAYS,

+					simpleProperty.getGeneration() == PropertyGeneration.ALWAYS,

+					simpleProperty.isNullable(),

+					alwaysDirtyCheck || simpleProperty.isUpdatable(),

+					simpleProperty.isOptimisticLockable(),

+					// TODO: get cascadeStyle from simpleProperty when HHH-6355 is fixed; for now, assume NONE

+					//simpleProperty.getCascadeStyle(),

+					CascadeStyle.NONE,

+					// TODO: get fetchMode() from simpleProperty when HHH-6357 is fixed; for now, assume FetchMode.DEFAULT

+					//simpleProperty.getFetchMode()

```

[Code Context]
- Signature: Full Signature: buildStandardProperty(AttributeBinding property, boolean lazyAvailable) -> StandardProperty
Parameters Details: [{"name": "property", "type": "AttributeBinding"}, {"name": "lazyAvailable", "type": "boolean"}]
- Intent: Method 'buildStandardProperty' (build Standard Property)

[Rule-based Signals — HIGH PRIORITY]
- IDENTIFIER DRIFT: comment mentions 'Property' which no longer exists in new code. Possible renames: ['pluralProperty', 'PluralAttributeBinding'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Generate a 'standard' (i.e., non-identifier and non-version) based on the given mapped property" → The method still generates a StandardProperty based on a property, but the property type has changed from Property to AttributeBinding. The core action remains similar.
- SUBJECT: "mapped property" → The method now works with AttributeBinding instead of Property, which is a significant change in the subject type.
- QUALIFIERS: "standard (i.e., non-identifier and non-version)" → The method still creates a StandardProperty, but the implementation has changed significantly with branching logic for simple vs plural properties.

The comment mentions "Property" which no longer exists in the new code (IDENTIFIER DRIFT signal). The method now has different logic with conditional branches for simple vs plural properties that weren't present in the original code. The core purpose is similar, but the specific implementation and subject type have changed significantly.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: buildStandardProperty(AttributeBinding property, boolean lazyAvailable) -> Stand
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Generate a 'standard' (i.e., non-identifier and non-version) based on the give...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [5/77] `Summary_13`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `HBase region cut size, in GB` |
| ground_truth_comment | `HBase region cut size, in GB` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public float getKylinHBaseRegionCut() {
        return Float.valueOf(getOptional("kylin.hbase.region.cut", "1.0"));
    }
```

**code_snippet**

```java
public float getKylinHBaseRegionCut() {
        return Float.valueOf(getOptional("kylin.hbase.region.cut", "5.0"));
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getKylinHBaseRegionCut() -> float
Parameters Details: []
intention:      Method 'getKylinHBaseRegionCut' (get Kylin H Base Region Cut)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
HBase region cut size, in GB

[Current Code]
    public float getKylinHBaseRegionCut() {
        return Float.valueOf(getOptional("kylin.hbase.region.cut", "5.0"));
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public float getKylinHBaseRegionCut() {

-        return Float.valueOf(getOptional("kylin.hbase.region.cut", "1.0"));

+        return Float.valueOf(getOptional("kylin.hbase.region.cut", "5.0"));

     }
```

[Code Context]
- Signature: Full Signature: getKylinHBaseRegionCut() -> float
Parameters Details: []
- Intent: Method 'getKylinHBaseRegionCut' (get Kylin H Base Region Cut)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "HBase region cut size, in GB" → This is not a verb phrase describing an action, but rather a description of what the method returns. The method returns a float value representing HBase region cut size in GB.
- SUBJECT: The subject is "HBase region cut size, in GB" → The method still returns a float value representing the HBase region cut size.
- QUALIFIERS: "in GB" → The method returns a float value that represents the size in GB, though the actual unit conversion isn't shown in the code.

The comment describes what the method returns rather than what it does. The method still returns the HBase region cut size, though the default value has changed from "1.0" to "5.0". The comment doesn't mention the default value, so this change doesn't affect the consistency of the comment.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getKylinHBaseRegionCut() -> float
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [6/77] `Summary_15`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Create a new  Builder configuration builder that starts with a copy of the supplied configuration.` |
| ground_truth_comment | `Create a new  Builder configuration builder that starts with a copy of the supplied configuration.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static Builder copy(Configuration config) {
        return new Builder() {
            private Properties props = config.asProperties();

            @Override
            public Builder with(String key, String value) {
                props.setProperty(key, value);
                return this;
            }

            @Override
            public Builder withDefault(String key, String value) {
                if (!props.containsKey(key)) {
                    props.setProperty(key, value);
                }
                return this;
            }

            @Override
            public Builder apply(Consumer<Builder> function) {
                function.accept(this);
                return this;
            }

            @Override
            public JdbcConfiguration build() {
                return JdbcConfiguration.adapt(Configuration.from(props));
            }

            @Override
            public String toString() {
                return props.toString();
            }
        };
    }
```

**code_snippet**

```java
public static Builder copy(Configuration config) {
        return new Builder() {
            private Configuration.Builder builder = Configuration.copy(config);

            @Override
            public Builder with(String key, String value) {
                builder.with(key, value);
                return this;
            }

            @Override
            public Builder withDefault(String key, String value) {
                builder.withDefault(key, value);
                return this;
            }

            @Override
            public Builder apply(Consumer<Builder> function) {
                function.accept(this);
                return this;
            }
            
            @Override
            public Builder changeString(Field field, Function<String, String> function) {
                changeString(field,function);
                return this;
            }
            
            @Override
            public Builder changeString(String key, Function<String, String> function) {
                changeString(key,function);
                return this;
            }

            @Override
            public JdbcConfiguration build() {
                return JdbcConfiguration.adapt(builder.build());
            }

            @Override
            public String toString() {
                return builder.toString();
            }
        };
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: copy(Configuration config) -> Builder
Parameters Details: [{"name": "config", "type": "Configuration"}]
intention:      Method 'copy' (copy)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Create a new  Builder configuration builder that starts with a copy of the supplied configuration.

[Current Code]
    public static Builder copy(Configuration config) {
        return new Builder() {
            private Configuration.Builder builder = Configuration.copy(config);

            @Override
            public Builder with(String key, String value) {
                builder.with(key, value);
                return this;
            }

            @Override
            public Builder withDefault(String key, String value) {
                builder.withDefault(key, value);
                return this;
            }

            @Override
            public Builder apply(Consumer<Builder> function) {
                function.accept(this);
                return this;
            }
            
            @Override
            public Builder changeString(Field field, Function<String, String> function) {
                changeString(field,function);
                return this;
            }
            
            @Override
            public Builder changeString(String key, Function<String, String> function) {
                changeString(key,function);
                return this;
            }

            @Override
            public JdbcConfiguration build() {
                return JdbcConfiguration.adapt(builder.build());
            }

            @Override
            public String toString() {
                return builder.toString();
            }
        };
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,18 +1,16 @@
 public static Builder copy(Configuration config) {

         return new Builder() {

-            private Properties props = config.asProperties();

+            private Configuration.Builder builder = Configuration.copy(config);

 

             @Override

             public Builder with(String key, String value) {

-                props.setProperty(key, value);

+                builder.with(key, value);

                 return this;

             }

 

             @Override

             public Builder withDefault(String key, String value) {

-                if (!props.containsKey(key)) {

-                    props.setProperty(key, value);

-                }

+                builder.withDefault(key, value);

                 return this;

             }

 

@@ -21,15 +19,27 @@
                 function.accept(this);

                 return this;

             }

+            

+            @Override

+            public Builder changeString(Field field, Function<String, String> function) {

+                changeString(field,function);

+                return this;

+            }

+            

+            @Override

+            public Builder changeString(String key, Function<String, String> function) {

+                changeString(key,function);

+                return this;

+            }

 

             @Override

             public JdbcConfiguration build() {

-                return JdbcConfiguration.adapt(Configuration.from(props));

+                return JdbcConfiguration.adapt(builder.build());

             }

 

             @Override

             public String toString() {

-                return props.toString();

+                return builder.toString();

             }

         };

     }
```

[Code Context]
- Signature: Full Signature: copy(Configuration config) -> Builder
Parameters Details: [{"name": "config", "type": "Configuration"}]
- Intent: Method 'copy' (copy)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Create a new Builder configuration builder" → The code still creates a new Builder instance, so YES
- SUBJECT: "that starts with a copy of the supplied configuration" → The code now uses Configuration.copy(config) to create a copy of the supplied configuration, so YES
- QUALIFIERS: None specified in the summary, so YES
- Brief conclusion: The summary still accurately describes what the method does - it creates a new Builder that starts with a copy of the supplied configuration.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: copy(Configuration config) -> Builder
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [7/77] `Summary_17`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Loads item sprite from game, makes transparent, and generates image` |
| ground_truth_comment | `Loads item sprite from game, makes transparent, and generates image` |

### Step 0 · 原始数据

**old_code_snippet**

```java
private AsyncBufferedImage loadImage(int itemId, int quantity, boolean stackable)
	{
		AsyncBufferedImage img = new AsyncBufferedImage(36, 32, BufferedImage.TYPE_INT_ARGB);
		clientThread.invokeLater(() ->
		{
			if (client.getGameState().ordinal() < GameState.LOGIN_SCREEN.ordinal())
			{
				return false;
			}
			SpritePixels sprite = client.createItemSprite(itemId, quantity, 1, SpritePixels.DEFAULT_SHADOW_COLOR,
				stackable ? 1 : 0, false, CLIENT_DEFAULT_ZOOM);
			if (sprite == null)
			{
				return false;
			}
			sprite.toBufferedImage(img);
			img.changed();
			return true;
		});
		return img;
	}
```

**code_snippet**

```java
private BufferedImage loadImage(int itemId, int quantity, boolean stackable)
	{
		SpritePixels sprite = client.get().createItemSprite(itemId, quantity, 1, SpritePixels.DEFAULT_SHADOW_COLOR,
			stackable ? 1 : 0, false, CLIENT_DEFAULT_ZOOM);
		return sprite.toBufferedImage();
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: loadImage(int itemId, int quantity, boolean stackable) -> BufferedImage
Parameters Details: [{"name": "itemId", "type": "int"}, {"name": "quantity", "type": "int"}, {"name": "stackable", "type": "boolean"}]
intention:      Method 'loadImage' (load Image)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'AsyncBufferedImage' -> 'BufferedImage'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Loads item sprite from game, makes transparent, and generates image

[Current Code]
	private BufferedImage loadImage(int itemId, int quantity, boolean stackable)
	{
		SpritePixels sprite = client.get().createItemSprite(itemId, quantity, 1, SpritePixels.DEFAULT_SHADOW_COLOR,
			stackable ? 1 : 0, false, CLIENT_DEFAULT_ZOOM);
		return sprite.toBufferedImage();
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,21 +1,6 @@
-private AsyncBufferedImage loadImage(int itemId, int quantity, boolean stackable)

+private BufferedImage loadImage(int itemId, int quantity, boolean stackable)

 	{

-		AsyncBufferedImage img = new AsyncBufferedImage(36, 32, BufferedImage.TYPE_INT_ARGB);

-		clientThread.invokeLater(() ->

-		{

-			if (client.getGameState().ordinal() < GameState.LOGIN_SCREEN.ordinal())

-			{

-				return false;

-			}

-			SpritePixels sprite = client.createItemSprite(itemId, quantity, 1, SpritePixels.DEFAULT_SHADOW_COLOR,

-				stackable ? 1 : 0, false, CLIENT_DEFAULT_ZOOM);

-			if (sprite == null)

-			{

-				return false;

-			}

-			sprite.toBufferedImage(img);

-			img.changed();

-			return true;

-		});

-		return img;

+		SpritePixels sprite = client.get().createItemSprite(itemId, quantity, 1, SpritePixels.DEFAULT_SHADOW_COLOR,

+			stackable ? 1 : 0, false, CLIENT_DEFAULT_ZOOM);

+		return sprite.toBufferedImage();

 	}
```

[Code Context]
- Signature: Full Signature: loadImage(int itemId, int quantity, boolean stackable) -> BufferedImage
Parameters Details: [{"name": "itemId", "type": "int"}, {"name": "quantity", "type": "int"}, {"name": "stackable", "type": "boolean"}]
- Intent: Method 'loadImage' (load Image)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'AsyncBufferedImage' -> 'BufferedImage'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Loads item sprite from game, makes transparent, and generates image" → The code still loads an item sprite and generates an image, but it no longer makes it transparent. The transparency handling was removed with the AsyncBufferedImage implementation.
- SUBJECT: "item sprite" → The code still operates on item sprites, so this part is consistent.
- QUALIFIERS: "from game, makes transparent, and generates image" → The "from game" part is still true, but "makes transparent" is no longer true as the transparency handling was removed. The "generates image" part is still true.
- Brief conclusion: The summary is inconsistent because it mentions making the image transparent, which is no longer done in the current code.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: loadImage(int itemId, int quantity, boolean stackable) -> BufferedImage
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Loads item sprite from game, makes transparent, and generates image" → The cod...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [8/77] `Summary_18`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Return XML schema for the specified type, suitable for insertion into the  element of a WSDL document.` |
| ground_truth_comment | `Return XML schema for the specified type, suitable for insertion into the &lt;types&gt; element of a WSDL document, or underneath an &lt;element&gt; or &lt;attribute&gt; declaration.` |

### Step 0 · 原始数据

**old_code_snippet**

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
                            propName = propName;
                            qname = new QName("", propName);
                        }

                        //  write attribute element
                        Class fieldType = propertyDescriptor[i].getType();

                        // Attribute must be a simple type, enum or SimpleType
                        if (!types.isAcceptableAsAttribute(fieldType)) {
                            throw new AxisFault(Messages.getMessage("AttrNotSimpleType00",
                                    propName,
                                    fieldType.getName()));
                        }

                        // write attribute element
                        // TODO the attribute name needs to be preserved from the XML
                        String elementType = types.writeType(fieldType);
                        Element elem = types.createAttributeElement(propName,
                                elementType,
                                false,
                                extension.getOwnerDocument());
                        extension.appendChild(elem);
                    }
                }
                continue;
            }

            BeanPropertyDescriptor bpd = propertyDescriptor[i];
            Class type = bpd.getType();
            // Attribute must extend a simple type, enum or SimpleType
            if (!types.isAcceptableAsAttribute(type)) {
                throw new AxisFault(Messages.getMessage("AttrNotSimpleType01",
                        type.getName()));
            }
            base = types.writeType(type);
            extension.setAttribute("base", base);
        }

        // done
        return true;

    }
```

**code_snippet**

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
                            qname = new QName("", propName);
                        }

                        //  write attribute element
                        Class fieldType = propertyDescriptor[i].getType();

                        // Attribute must be a simple type, enum or SimpleType
                        if (!types.isAcceptableAsAttribute(fieldType)) {
                            throw new AxisFault(Messages.getMessage("AttrNotSimpleType00",
                                    propName,
                                    fieldType.getName()));
                        }

                        // write attribute element
                        // TODO the attribute name needs to be preserved from the XML
                        Element elem = types.createAttributeElement(propName,
                                fieldType,
                                field.getXmlType(),
                                false,
                                extension.getOwnerDocument());
                        extension.appendChild(elem);
                    }
                }
                continue;
            }

            BeanPropertyDescriptor bpd = propertyDescriptor[i];
            Class type = bpd.getType();
            // Attribute must extend a simple type, enum or SimpleType
            if (!types.isAcceptableAsAttribute(type)) {
                throw new AxisFault(Messages.getMessage("AttrNotSimpleType01",
                        type.getName()));
            }
            base = types.writeType(type);
            extension.setAttribute("base", base);
        }

        // done
        return complexType;

    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: writeSchema(Class javaType, Types types) -> Element throws Exception
Parameters Details: [{"name": "javaType", "type": "Class"}, {"name": "types", "type": "Types"}]
intention:      Method 'writeSchema' (write Schema)
implementation: Return paths: 2, throws: Exception
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'boolean' -> 'Element'. If the comment references the old return type, it is INCONSISTENT.", "PARAMETERS CHANGED: added params: {'javaType'}."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Return XML schema for the specified type, suitable for insertion into the  element of a WSDL document.

[Current Code]
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
                            qname = new QName("", propName);
                        }

                        //  write attribute element
                        Class fieldType = propertyDescriptor[i].getType();

                        // Attribute must be a simple type, enum or SimpleType
                        if (!types.isAcceptableAsAttribute(fieldType)) {
                            throw new AxisFault(Messages.getMessage("AttrNotSimpleType00",
                                    propName,
                                    fieldType.getName()));
                        }

                        // write attribute element
                        // TODO the attribute name needs to be preserved from the XML
                        Element elem = types.createAttributeElement(propName,
                                fieldType,
                                field.getXmlType(),
                                false,
                                extension.getOwnerDocument());
                        extension.appendChild(elem);
                    }
                }
                continue;
            }

            BeanPropertyDescriptor bpd = propertyDescriptor[i];
            Class type = bpd.getType();
            // Attribute must extend a simple type, enum or SimpleType
            if (!types.isAcceptableAsAttribute(type)) {
                throw new AxisFault(Messages.getMessage("AttrNotSimpleType01",
                        type.getName()));
            }
            base = types.writeType(type);
            extension.setAttribute("base", base);
        }

        // done
        return complexType;

    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: writeSchema(Class javaType, Types types) -> Element throws Exception
Parameters Details: [{"name": "javaType", "type": "Class"}, {"name": "types", "type": "Types"}]
- Intent: Method 'writeSchema' (write Schema)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'boolean' -> 'Element'. If the comment references the old return type, it is INCONSISTENT.
- PARAMETERS CHANGED: added params: {'javaType'}.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Return XML schema" → The method now returns an Element representing XML schema, so this matches.
- SUBJECT: "for the specified type" → The method now takes a javaType parameter, so this matches.
- QUALIFIERS: "suitable for insertion into the <types> element of a WSDL document" → The code still generates XML schema elements that would be suitable for WSDL, so this matches.

Brief conclusion: The summary still accurately describes what the method does after the changes.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: writeSchema(Class javaType, Types types) -> Element throws Exception
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [9/77] `Summary_19`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Given a Class of something that extends AsyncSupport, it tries to return an instance of that class.` |
| ground_truth_comment | `Given a Class of something that extends AsyncSupport, it tries to return an instance of that class.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public AsyncSupport newCometSupport(final Class<? extends AsyncSupport> targetClass) {
        try {
            return targetClass.getDeclaredConstructor(new Class[]{AtmosphereConfig.class})
                    .newInstance(config);
        } catch (final Exception e) {
            logger.error("Failed to create comet support class: {}, error: {}", targetClass, e);
            logger.error("Switching to BlockingIO");

            return new BlockingIOCometSupport(config);
        }
    }
```

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: newCometSupport(Class<? extends AsyncSupport> targetClass) -> AsyncSupport
Parameters Details: [{"name": "targetClass", "type": "Class<? extends AsyncSupport>"}]
intention:      Method 'newCometSupport' (new Comet Support)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Given a Class of something that extends AsyncSupport, it tries to return an instance of that class.

[Current Code]
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


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
 public AsyncSupport newCometSupport(final Class<? extends AsyncSupport> targetClass) {

         try {

-            return targetClass.getDeclaredConstructor(new Class[]{AtmosphereConfig.class})

+            return (AsyncSupport) targetClass.getDeclaredConstructor(new Class[]{AtmosphereConfig.class})

                     .newInstance(config);

         } catch (final Exception e) {

             logger.error("Failed to create comet support class: {}, error: {}", targetClass, e);

```

[Code Context]
- Signature: Full Signature: newCometSupport(Class<? extends AsyncSupport> targetClass) -> AsyncSupport
Parameters Details: [{"name": "targetClass", "type": "Class<? extends AsyncSupport>"}]
- Intent: Method 'newCometSupport' (new Comet Support)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "tries to return an instance of that class" → The code still attempts to return an instance of the target class through reflection. YES
- SUBJECT: "a Class of something that extends AsyncSupport" → The method still takes a Class<? extends AsyncSupport> as parameter. YES
- QUALIFIERS: None specified in the original comment. N/A
- Brief conclusion: The summary still accurately describes what the method does - it takes a class that extends AsyncSupport and tries to return an instance of it.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: newCometSupport(Class<? extends AsyncSupport> targetClass) -> AsyncSupport
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [10/77] `Summary_21`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Allow to print directives.` |
| ground_truth_comment | `Allow to print directives.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public Options includeDirectives(boolean flag) {
            return new Options(this.includeIntrospectionTypes, this.includeScalars, this.includeExtendedScalars, this.includeSchemaDefinition, flag, this.useAstDefinitions, this.descriptionsAsHashComments, this.comparatorRegistry);
        }
```

**code_snippet**

```java
public Options includeDirectives(boolean flag) {
            return new Options(this.includeIntrospectionTypes, this.includeScalars, this.includeExtendedScalars, this.includeSchemaDefinition, this.useAstDefinitions, this.descriptionsAsHashComments, directive -> flag, this.comparatorRegistry);
        }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: includeDirectives(boolean flag) -> Options
Parameters Details: [{"name": "flag", "type": "boolean"}]
intention:      Method 'includeDirectives' (include Directives)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Allow to print directives.

[Current Code]
        public Options includeDirectives(boolean flag) {
            return new Options(this.includeIntrospectionTypes, this.includeScalars, this.includeExtendedScalars, this.includeSchemaDefinition, this.useAstDefinitions, this.descriptionsAsHashComments, directive -> flag, this.comparatorRegistry);
        }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public Options includeDirectives(boolean flag) {

-            return new Options(this.includeIntrospectionTypes, this.includeScalars, this.includeExtendedScalars, this.includeSchemaDefinition, flag, this.useAstDefinitions, this.descriptionsAsHashComments, this.comparatorRegistry);

+            return new Options(this.includeIntrospectionTypes, this.includeScalars, this.includeExtendedScalars, this.includeSchemaDefinition, this.useAstDefinitions, this.descriptionsAsHashComments, directive -> flag, this.comparatorRegistry);

         }
```

[Code Context]
- Signature: Full Signature: includeDirectives(boolean flag) -> Options
Parameters Details: [{"name": "flag", "type": "boolean"}]
- Intent: Method 'includeDirectives' (include Directives)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Allow to print" → The method still allows setting a flag related to directives, but the implementation has changed from directly using the flag to using a lambda function (directive -> flag). The core action of allowing to print directives is still there.
- SUBJECT: "directives" → The method is still about directives, as evidenced by the parameter name "flag" and the lambda function "directive -> flag" which is clearly related to directives.
- QUALIFIERS: None mentioned in the summary.

The method signature and purpose remain the same - it's still about including directives with a boolean flag. The implementation detail changed from passing the flag directly to passing a lambda that returns the flag, but this doesn't change the fundamental behavior described in the summary.

Brief conclusion: The summary still accurately describes what the method does, despite the implementation change.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: includeDirectives(boolean flag) -> Options
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [11/77] `Summary_24`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Check if the Elasticsearch  Node is connected and that the cluster health status is not  ClusterHealthStatus#RED.` |
| ground_truth_comment | `Check if the Elasticsearch  Node is connected and that the cluster health status is not  ClusterHealthStatus#RED and that the  org.graylog2.indexer.Deflector#isUp() deflector is up.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: isConnectedAndHealthy() -> boolean
Parameters Details: []
intention:      Method 'isConnectedAndHealthy' (is Connected And Healthy)
implementation: Return paths: 4
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Check if the Elasticsearch  Node is connected and that the cluster health status is not  ClusterHealthStatus#RED.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: isConnectedAndHealthy() -> boolean
Parameters Details: []
- Intent: Method 'isConnectedAndHealthy' (is Connected And Healthy)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Check if" → still done by the code? YES. The method still performs checks.
- SUBJECT: "the Elasticsearch Node is connected and that the cluster health status" → still this same thing? YES. The method still checks both node connection and cluster health.
- QUALIFIERS: "is not ClusterHealthStatus#RED" → still true? YES. The method still specifically checks that the health status is not RED.

The original comment accurately describes what the method does: it checks if the Elasticsearch node is connected (by verifying nodeMap is not empty and deflector is up) and that the cluster health status is not RED. The added code actually makes the comment more accurate by explicitly checking the node connection conditions.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isConnectedAndHealthy() -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [12/77] `Summary_26`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns true if, the lockClient is keeping the lock for the lockPath` |
| ground_truth_comment | `Returns true if, the job server is keeping the lock for the lockPath` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: isKeepLock(String serverName, String lockPath) -> boolean
Parameters Details: [{"name": "serverName", "type": "String"}, {"name": "lockPath", "type": "String"}]
intention:      Method 'isKeepLock' (is Keep Lock)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'lockClient'}; added params: {'serverName'}.", "IDENTIFIER DRIFT: comment mentions 'lockClient' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns true if, the lockClient is keeping the lock for the lockPath

[Current Code]

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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: isKeepLock(String serverName, String lockPath) -> boolean
Parameters Details: [{"name": "serverName", "type": "String"}, {"name": "lockPath", "type": "String"}]
- Intent: Method 'isKeepLock' (is Keep Lock)

[Rule-based Signals — HIGH PRIORITY]
- PARAMETERS CHANGED: removed params: {'lockClient'}; added params: {'serverName'}.
- IDENTIFIER DRIFT: comment mentions 'lockClient' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns true if" → still done by the code? YES (the method still returns a boolean value)
- SUBJECT: "the lockClient is keeping the lock for the lockPath" → NO (the method now checks if serverName matches the lockServerName, not lockClient)
- QUALIFIERS: "for the lockPath" → YES (the method still operates on the lockPath parameter)

The original comment mentions "lockClient" which is no longer a parameter in the method. The method now checks if the serverName matches the lockServerName stored in ZooKeeper. The subject of the check has changed from lockClient to serverName.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isKeepLock(String serverName, String lockPath) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns true if" → still done by the code? YES (the method still returns a boo...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [13/77] `Summary_30`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Checks if a flag is set.` |
| ground_truth_comment | `Returns  true if any of the flags supplied in the argument are set.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public boolean isFlagSet(int flag) {
        return (flags & flag) != 0;
    }
```

**code_snippet**

```java
public boolean isFlagSet(int flagsToCheck) {
        return (flags & flagsToCheck) != 0;
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: isFlagSet(int flagsToCheck) -> boolean
Parameters Details: [{"name": "flagsToCheck", "type": "int"}]
intention:      Method 'isFlagSet' (is Flag Set)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'flag'}; added params: {'flagsToCheck'}.", "IDENTIFIER DRIFT: comment mentions 'flag' which no longer exists in new code. Possible renames: ['flagsToCheck']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Checks if a flag is set.

[Current Code]
    public boolean isFlagSet(int flagsToCheck) {
        return (flags & flagsToCheck) != 0;
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: isFlagSet(int flagsToCheck) -> boolean
Parameters Details: [{"name": "flagsToCheck", "type": "int"}]
- Intent: Method 'isFlagSet' (is Flag Set)

[Rule-based Signals — HIGH PRIORITY]
- PARAMETERS CHANGED: removed params: {'flag'}; added params: {'flagsToCheck'}.
- IDENTIFIER DRIFT: comment mentions 'flag' which no longer exists in new code. Possible renames: ['flagsToCheck'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Checks if" → still done by the code? YES. The method still performs a check operation.
- SUBJECT: "a flag" → still this same thing? NO. The parameter was renamed from "flag" to "flagsToCheck", which is a more descriptive name but still refers to a flag being checked.
- QUALIFIERS: "is set" → still all true? YES. The method still checks if the flag is set by performing a bitwise AND operation.

The comment is slightly imprecise because it refers to "a flag" while the parameter is now named "flagsToCheck", but the core functionality remains the same. The method still checks if a flag (or flags) is set in the flags field.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isFlagSet(int flagsToCheck) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [14/77] `Summary_31`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Builds the  Client instance.` |
| ground_truth_comment | `Builds the  Client instance.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public Client build() {
        if ((environment == null) && (executorService == null) && (objectMapper == null)) {
            throw new IllegalStateException("Must have either an environment or both " +
                                                    "an executor service and an object mapper");
        }

        if (environment == null) {
            return build(executorService, objectMapper);
        }

        return build(environment.getLifecycleEnvironment()
                                .managedExecutorService("jersey-client-%d",
                                                        configuration.getMinThreads(),
                                                        configuration.getMaxThreads(),
                                                        60,
                                                        TimeUnit.SECONDS),
                     environment.getJsonEnvironment().buildObjectMapper());
    }
```

**code_snippet**

```java
public Client build() {
        if ((environment == null) && (executorService == null) && (objectMapper == null)) {
            throw new IllegalStateException("Must have either an environment or both " +
                                                    "an executor service and an object mapper");
        }

        if (environment == null) {
            return build(executorService, objectMapper);
        }

        return build(environment.getLifecycleEnvironment()
                                .managedExecutorService("jersey-client-%d",
                                                        configuration.getMinThreads(),
                                                        configuration.getMaxThreads(),
                                                        60,
                                                        TimeUnit.SECONDS),
                     environment.getJsonEnvironment().build());
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: build() -> Client
Parameters Details: []
intention:      Method 'build' (build)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Builds the  Client instance.

[Current Code]
    public Client build() {
        if ((environment == null) && (executorService == null) && (objectMapper == null)) {
            throw new IllegalStateException("Must have either an environment or both " +
                                                    "an executor service and an object mapper");
        }

        if (environment == null) {
            return build(executorService, objectMapper);
        }

        return build(environment.getLifecycleEnvironment()
                                .managedExecutorService("jersey-client-%d",
                                                        configuration.getMinThreads(),
                                                        configuration.getMaxThreads(),
                                                        60,
                                                        TimeUnit.SECONDS),
                     environment.getJsonEnvironment().build());
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -14,5 +14,5 @@
                                                         configuration.getMaxThreads(),

                                                         60,

                                                         TimeUnit.SECONDS),

-                     environment.getJsonEnvironment().buildObjectMapper());

+                     environment.getJsonEnvironment().build());

     }
```

[Code Context]
- Signature: Full Signature: build() -> Client
Parameters Details: []
- Intent: Method 'build' (build)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Builds" → still done by the code? YES - The method is still building a Client instance
- SUBJECT: "the Client instance" → still this same thing? YES - The method still returns a Client instance
- QUALIFIERS: None in the original comment → N/A
- Brief conclusion: The comment accurately describes what the method does - it builds a Client instance.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: build() -> Client
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [15/77] `Summary_36`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Method that get's left and right incoming batch and produce the output batch.` |
| ground_truth_comment | `Gets the left and right incoming batch and produce the output batch.` |

### Step 0 · 原始数据

**old_code_snippet**

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

    // reset this state after calling processLeftBatch above.
    processLeftBatchInFuture = false;
    hasRemainderForLeftJoin = false;

    // If the left batch doesn't have any record in the incoming batch (with OK_NEW_SCHEMA/EMIT) or the state returned
    // from left side is terminal state then just return the IterOutcome and don't call next() on right branch
    if (isTerminalOutcome(childOutcome) || left.getRecordCount() == 0) {
      container.setRecordCount(0);
      return childOutcome;
    }

    // Left side has some records in the batch so let's process right batch
    childOutcome = processRightBatch();
    logger.debug("Received right batch with outcome {}", childOutcome);

    // reset the left & right outcomes to OK here and send the empty batch downstream. Non-Empty right batch with
    // OK_NEW_SCHEMA will be handled in subsequent next call
    if (childOutcome == OK_NEW_SCHEMA) {
      leftUpstream = (leftUpstream != EMIT) ? OK : leftUpstream;
      rightUpstream = OK;
      return childOutcome;
    }

    if (isTerminalOutcome(childOutcome)) {
      return childOutcome;
    }

    // If OK_NEW_SCHEMA is seen only on non empty left batch but not on right batch, then we should setup schema in
    // output container based on new left schema and old right schema. If schema change failed then return STOP
    // downstream
    if (leftUpstream == OK_NEW_SCHEMA && !handleSchemaChange()) {
      return STOP;
    }

    // Setup the references of left, right and outgoing container in generated operator
    state = BatchState.NOT_FIRST;

    // Update the memory manager only if its a brand new incoming i.e. leftJoinIndex and rightJoinIndex is 0
    // Otherwise there will be a case where while filling last output batch, some records from previous left or
    // right batch are still left to be sent in output for which we will count this batch twice. The actual checks
    // are done in updateMemoryManager
    updateMemoryManager(LEFT_INDEX);

    // We have to call update on memory manager for empty batches (rightJoinIndex = -1) as well since other wise while
    // allocating memory for vectors below it can fail. Since in that case colSize will not have any info on right side
    // vectors and throws NPE. The actual checks are done in updateMemoryManager
    updateMemoryManager(RIGHT_INDEX);

    if (outputIndex > 0) {
      // this means batch is already allocated but because of new incoming the width and output row count might have
      // changed. So update the maxOutputRowCount with new value
      if (useMemoryManager) {
        setMaxOutputRowCount(batchMemoryManager.getCurrentOutgoingMaxRowCount());
      }
    }
    // if output is not allocated then maxRowCount will be set correctly below
    // allocate space for the outgoing batch
    allocateVectors();

    return produceOutputBatch();
  }
```

**code_snippet**

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

    // reset this state after calling processLeftBatch above.
    processLeftBatchInFuture = false;
    hasRemainderForLeftJoin = false;

    // If the left batch doesn't have any record in the incoming batch (with OK_NEW_SCHEMA/EMIT) or the state returned
    // from left side is terminal state then just return the IterOutcome and don't call next() on right branch
    if (isTerminalOutcome(childOutcome) || left.getRecordCount() == 0) {
      container.setRecordCount(0);
      return childOutcome;
    }

    // Left side has some records in the batch so let's process right batch
    childOutcome = processRightBatch();
    logger.debug("Received right batch with outcome {}", childOutcome);

    // reset the left & right outcomes to OK here and send the empty batch downstream. Non-Empty right batch with
    // OK_NEW_SCHEMA will be handled in subsequent next call
    if (childOutcome == OK_NEW_SCHEMA) {
      leftUpstream = (leftUpstream != EMIT) ? OK : leftUpstream;
      rightUpstream = OK;
      return childOutcome;
    }

    if (isTerminalOutcome(childOutcome)) {
      return childOutcome;
    }

    // If OK_NEW_SCHEMA is seen only on non empty left batch but not on right batch, then we should setup schema in
    // output container based on new left schema and old right schema. If schema change failed then return STOP
    // downstream
    if (leftUpstream == OK_NEW_SCHEMA) {
      handleSchemaChange();
    }

    // Setup the references of left, right and outgoing container in generated operator
    state = BatchState.NOT_FIRST;

    // Update the memory manager only if its a brand new incoming i.e. leftJoinIndex and rightJoinIndex is 0
    // Otherwise there will be a case where while filling last output batch, some records from previous left or
    // right batch are still left to be sent in output for which we will count this batch twice. The actual checks
    // are done in updateMemoryManager
    updateMemoryManager(LEFT_INDEX);

    // We have to call update on memory manager for empty batches (rightJoinIndex = -1) as well since other wise while
    // allocating memory for vectors below it can fail. Since in that case colSize will not have any info on right side
    // vectors and throws NPE. The actual checks are done in updateMemoryManager
    updateMemoryManager(RIGHT_INDEX);

    if (outputIndex > 0) {
      // this means batch is already allocated but because of new incoming the width and output row count might have
      // changed. So update the maxOutputRowCount with new value
      if (useMemoryManager) {
        setMaxOutputRowCount(batchMemoryManager.getCurrentOutgoingMaxRowCount());
      }
    }
    // if output is not allocated then maxRowCount will be set correctly below
    // allocate space for the outgoing batch
    allocateVectors();

    return produceOutputBatch();
  }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: innerNext() -> IterOutcome
Parameters Details: []
intention:      Method 'innerNext' (inner Next)
implementation: Return paths: 6
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Method that get's left and right incoming batch and produce the output batch.

[Current Code]
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

    // reset this state after calling processLeftBatch above.
    processLeftBatchInFuture = false;
    hasRemainderForLeftJoin = false;

    // If the left batch doesn't have any record in the incoming batch (with OK_NEW_SCHEMA/EMIT) or the state returned
    // from left side is terminal state then just return the IterOutcome and don't call next() on right branch
    if (isTerminalOutcome(childOutcome) || left.getRecordCount() == 0) {
      container.setRecordCount(0);
      return childOutcome;
    }

    // Left side has some records in the batch so let's process right batch
    childOutcome = processRightBatch();
    logger.debug("Received right batch with outcome {}", childOutcome);

    // reset the left & right outcomes to OK here and send the empty batch downstream. Non-Empty right batch with
    // OK_NEW_SCHEMA will be handled in subsequent next call
    if (childOutcome == OK_NEW_SCHEMA) {
      leftUpstream = (leftUpstream != EMIT) ? OK : leftUpstream;
      rightUpstream = OK;
      return childOutcome;
    }

    if (isTerminalOutcome(childOutcome)) {
      return childOutcome;
    }

    // If OK_NEW_SCHEMA is seen only on non empty left batch but not on right batch, then we should setup schema in
    // output container based on new left schema and old right schema. If schema change failed then return STOP
    // downstream
    if (leftUpstream == OK_NEW_SCHEMA) {
      handleSchemaChange();
    }

    // Setup the references of left, right and outgoing container in generated operator
    state = BatchState.NOT_FIRST;

    // Update the memory manager only if its a brand new incoming i.e. leftJoinIndex and rightJoinIndex is 0
    // Otherwise there will be a case where while filling last output batch, some records from previous left or
    // right batch are still left to be sent in output for which we will count this batch twice. The actual checks
    // are done in updateMemoryManager
    updateMemoryManager(LEFT_INDEX);

    // We have to call update on memory manager for empty batches (rightJoinIndex = -1) as well since other wise while
    // allocating memory for vectors below it can fail. Since in that case colSize will not have any info on right side
    // vectors and throws NPE. The actual checks are done in updateMemoryManager
    updateMemoryManager(RIGHT_INDEX);

    if (outputIndex > 0) {
      // this means batch is already allocated but because of new incoming the width and output row count might have
      // changed. So update the maxOutputRowCount with new value
      if (useMemoryManager) {
        setMaxOutputRowCount(batchMemoryManager.getCurrentOutgoingMaxRowCount());
      }
    }
    // if output is not allocated then maxRowCount will be set correctly below
    // allocate space for the outgoing batch
    allocateVectors();

    return produceOutputBatch();
  }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: innerNext() -> IterOutcome
Parameters Details: []
- Intent: Method 'innerNext' (inner Next)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Method that get's left and right incoming batch and produce the output batch" → The method still processes left and right incoming batches and produces an output batch. YES
- SUBJECT: "left and right incoming batch" → The method still operates on left and right incoming batches. YES
- QUALIFIERS: None significant in the original summary. The code change only modified how schema changes are handled, not the fundamental operation of processing batches. YES
- Brief conclusion: The summary still accurately describes the method's core functionality despite the internal change in schema handling.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: innerNext() -> IterOutcome
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [16/77] `Summary_39`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Converts a value object for an expected JDBC type of  Types#TIMESTAMP.` |
| ground_truth_comment | `Converts a value object for an expected JDBC type of  Types#TIMESTAMP.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
protected Object convertTimestamp(Field fieldDefn, Object data) {
        java.util.Date date = null;
        if (data instanceof java.sql.Timestamp) {
            // JDBC specification indicates that this will be the canonical object for this JDBC type.
            date = (java.util.Date) data;
        } else if (data instanceof java.sql.Date) {
            // This should still work, even though it should have just date info
            date = (java.util.Date) data;
        } else if (data instanceof java.util.Date) {
            // Possible that some implementations might use this.
            date = (java.util.Date) data;
        } else if (data instanceof java.time.LocalDate) {
            // If we get a local date (no TZ info), we need to just convert to a util.Date (no TZ info) ...
            java.time.LocalDate local = (java.time.LocalDate) data;
            date = java.util.Date.from(local.atStartOfDay().toInstant(ZoneOffset.UTC));
        } else if (data instanceof java.time.LocalDateTime) {
            // Get the instant in time by changing any date info to the epoch day so we only have time ...
            java.time.LocalDateTime local = (java.time.LocalDateTime) data;
            date = java.util.Date.from(local.toInstant(ZoneOffset.UTC));
        } else {
            // An unexpected
            date = unexpectedTimestamp(data, fieldDefn);
        }
        return date == null ? null : Timestamp.fromLogical(fieldDefn.schema(), date);
    }
```

**code_snippet**

```java
protected Object convertTimestamp(Field fieldDefn, Object data) {
        java.util.Date date = null;
        if (data instanceof java.sql.Timestamp) {
            // JDBC specification indicates that this will be the canonical object for this JDBC type.
            date = (java.util.Date) data;
        } else if (data instanceof java.sql.Date) {
            // This should still work, even though it should have just date info
            date = (java.util.Date) data;
        } else if (data instanceof java.util.Date) {
            // Possible that some implementations might use this.
            date = (java.util.Date) data;
        } else if (data instanceof java.time.LocalDate) {
            // If we get a local date (no TZ info), we need to just convert to a util.Date (no TZ info) ...
            java.time.LocalDate local = (java.time.LocalDate) data;
            date = java.util.Date.from(local.atStartOfDay().toInstant(ZoneOffset.UTC));
        } else if (data instanceof java.time.LocalDateTime) {
            // Get the instant in time by changing any date info to the epoch day so we only have time ...
            java.time.LocalDateTime local = (java.time.LocalDateTime) data;
            date = java.util.Date.from(local.toInstant(ZoneOffset.UTC));
        } else {
            // An unexpected
            date = unexpectedTimestamp(data, fieldDefn);
        }
        return date;
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: convertTimestamp(Field fieldDefn, Object data) -> Object
Parameters Details: [{"name": "fieldDefn", "type": "Field"}, {"name": "data", "type": "Object"}]
intention:      Method 'convertTimestamp' (convert Timestamp)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Converts a value object for an expected JDBC type of  Types#TIMESTAMP.

[Current Code]
    protected Object convertTimestamp(Field fieldDefn, Object data) {
        java.util.Date date = null;
        if (data instanceof java.sql.Timestamp) {
            // JDBC specification indicates that this will be the canonical object for this JDBC type.
            date = (java.util.Date) data;
        } else if (data instanceof java.sql.Date) {
            // This should still work, even though it should have just date info
            date = (java.util.Date) data;
        } else if (data instanceof java.util.Date) {
            // Possible that some implementations might use this.
            date = (java.util.Date) data;
        } else if (data instanceof java.time.LocalDate) {
            // If we get a local date (no TZ info), we need to just convert to a util.Date (no TZ info) ...
            java.time.LocalDate local = (java.time.LocalDate) data;
            date = java.util.Date.from(local.atStartOfDay().toInstant(ZoneOffset.UTC));
        } else if (data instanceof java.time.LocalDateTime) {
            // Get the instant in time by changing any date info to the epoch day so we only have time ...
            java.time.LocalDateTime local = (java.time.LocalDateTime) data;
            date = java.util.Date.from(local.toInstant(ZoneOffset.UTC));
        } else {
            // An unexpected
            date = unexpectedTimestamp(data, fieldDefn);
        }
        return date;
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -21,5 +21,5 @@
             // An unexpected

             date = unexpectedTimestamp(data, fieldDefn);

         }

-        return date == null ? null : Timestamp.fromLogical(fieldDefn.schema(), date);

+        return date;

     }
```

[Code Context]
- Signature: Full Signature: convertTimestamp(Field fieldDefn, Object data) -> Object
Parameters Details: [{"name": "fieldDefn", "type": "Field"}, {"name": "data", "type": "Object"}]
- Intent: Method 'convertTimestamp' (convert Timestamp)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Converts a value object" → The method still performs conversion of different timestamp types to a java.util.Date. YES
- SUBJECT: "for an expected JDBC type of Types#TIMESTAMP" → The method still handles various timestamp-related types from JDBC and Java time packages. YES
- QUALIFIERS: None specified in the summary. YES
- Brief conclusion: The summary still accurately describes what the method does - it converts various timestamp-related objects to a java.util.Date.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: convertTimestamp(Field fieldDefn, Object data) -> Object
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [17/77] `Summary_40`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Determines if a specified set of columns from a specified relational expression are unique.` |
| ground_truth_comment | `Returns the  BuiltInMetadata.ColumnUniqueness#areColumnsUnique(BitSet, boolean) statistic.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static Boolean areColumnsUnique(RelNode rel, BitSet columns) {
    return (Boolean) rel.getCluster().getMetadataProvider().getRelMetadata(
        rel,
        "areColumnsUnique",
        new Object[]{columns, false});
  }
```

**code_snippet**

```java
public static Boolean areColumnsUnique(RelNode rel, BitSet columns) {
    final BuiltInMetadata.ColumnUniqueness metadata =
        rel.metadata(BuiltInMetadata.ColumnUniqueness.class);
    return metadata.areColumnsUnique(columns, false);
  }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: areColumnsUnique(RelNode rel, BitSet columns) -> Boolean
Parameters Details: [{"name": "rel", "type": "RelNode"}, {"name": "columns", "type": "BitSet"}]
intention:      Method 'areColumnsUnique' (are Columns Unique)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Determines if a specified set of columns from a specified relational expression are unique.

[Current Code]
  public static Boolean areColumnsUnique(RelNode rel, BitSet columns) {
    final BuiltInMetadata.ColumnUniqueness metadata =
        rel.metadata(BuiltInMetadata.ColumnUniqueness.class);
    return metadata.areColumnsUnique(columns, false);
  }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: areColumnsUnique(RelNode rel, BitSet columns) -> Boolean
Parameters Details: [{"name": "rel", "type": "RelNode"}, {"name": "columns", "type": "BitSet"}]
- Intent: Method 'areColumnsUnique' (are Columns Unique)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Determines if" → still done by the code? YES. The method still determines/evaluates uniqueness.
- SUBJECT: "a specified set of columns from a specified relational expression" → still this same thing? YES. The method still takes a RelNode (relational expression) and a BitSet (columns) as parameters.
- QUALIFIERS: "are unique" → still all true? YES. The method still checks if the specified columns are unique.

The implementation has changed from using a direct metadata provider call to using a BuiltInMetadata.ColumnUniqueness object, but the core functionality and purpose remain the same. The method still determines if the specified columns in the relational expression are unique.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: areColumnsUnique(RelNode rel, BitSet columns) -> Boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [18/77] `Summary_43`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Create RelNode tree that produces a list of correlated variables.` |
| ground_truth_comment | `Create RelNode tree that produces a list of correlated variables.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
private Frame getFrame(RelNode r, boolean safe) {
    final Frame frame = map.get(r);
    if (frame == null && safe) {
      return new Frame(r, r, ImmutableSortedMap.<CorDef, Integer>of(),
          identityMap(r.getRowType().getFieldCount()));
    }
    return frame;
  }
```

**code_snippet**

```java
private Frame getFrame(RelNode r, boolean safe) {
    final Frame frame = map.get(r);
    if (frame == null && safe) {
      return new Frame(r, r, ImmutableSortedMap.of(),
          identityMap(r.getRowType().getFieldCount()));
    }
    return frame;
  }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getFrame(RelNode r, boolean safe) -> Frame
Parameters Details: [{"name": "r", "type": "RelNode"}, {"name": "safe", "type": "boolean"}]
intention:      Method 'getFrame' (get Frame)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Create RelNode tree that produces a list of correlated variables.

[Current Code]
  private Frame getFrame(RelNode r, boolean safe) {
    final Frame frame = map.get(r);
    if (frame == null && safe) {
      return new Frame(r, r, ImmutableSortedMap.of(),
          identityMap(r.getRowType().getFieldCount()));
    }
    return frame;
  }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,7 +1,7 @@
 private Frame getFrame(RelNode r, boolean safe) {

     final Frame frame = map.get(r);

     if (frame == null && safe) {

-      return new Frame(r, r, ImmutableSortedMap.<CorDef, Integer>of(),

+      return new Frame(r, r, ImmutableSortedMap.of(),

           identityMap(r.getRowType().getFieldCount()));

     }

     return frame;

```

[Code Context]
- Signature: Full Signature: getFrame(RelNode r, boolean safe) -> Frame
Parameters Details: [{"name": "r", "type": "RelNode"}, {"name": "safe", "type": "boolean"}]
- Intent: Method 'getFrame' (get Frame)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Create RelNode tree" → The code doesn't create a RelNode tree, it retrieves a Frame from a map based on a RelNode parameter. NO
- SUBJECT: "RelNode tree" → The code operates on a RelNode but doesn't create a tree. The subject is partially correct but not fully accurate. NO
- QUALIFIERS: "that produces a list of correlated variables" → The code doesn't produce a list of correlated variables. NO

Brief conclusion: The summary describes creating a RelNode tree that produces correlated variables, but the actual code retrieves a Frame from a map based on a RelNode parameter, which is a completely different operation.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getFrame(RelNode r, boolean safe) -> Frame
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Create RelNode tree" → The code doesn't create a RelNode tree, it retrieves a ...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [19/77] `Summary_46`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns if this query should buffer before emitting results.` |
| ground_truth_comment | `Returns if this query should buffer before emitting the final results.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

```java
public boolean shouldBuffer() {
        Window window = runningQuery.getQuery().getWindow();
        boolean noWindow =  window == null;
        // Only buffer if there is no window (including Raw) or if it's a record based window.
        return noWindow || !window.isTimeBased();
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: shouldBuffer() -> boolean
Parameters Details: []
intention:      Method 'shouldBuffer' (should Buffer)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'should' which no longer exists in new code.", "IDENTIFIER DRIFT: comment mentions 'this' which no longer exists in new code. Possible renames: ['there'].", "IDENTIFIER DRIFT: comment mentions 'query' which no longer exists in new code.", "IDENTIFIER DRIFT: comment mentions 'This' which no longer exists in new code. Possible renames: ['there'].", "IDENTIFIER DRIFT: comment mentions 'results' which no longer exists in new code. Possible renames: ['record']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns if this query should buffer before emitting results.

[Current Code]
    public boolean shouldBuffer() {
        Window window = runningQuery.getQuery().getWindow();
        boolean noWindow =  window == null;
        // Only buffer if there is no window (including Raw) or if it's a record based window.
        return noWindow || !window.isTimeBased();
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: shouldBuffer() -> boolean
Parameters Details: []
- Intent: Method 'shouldBuffer' (should Buffer)

[Rule-based Signals — HIGH PRIORITY]
- IDENTIFIER DRIFT: comment mentions 'should' which no longer exists in new code.
- IDENTIFIER DRIFT: comment mentions 'this' which no longer exists in new code. Possible renames: ['there'].
- IDENTIFIER DRIFT: comment mentions 'query' which no longer exists in new code.
- IDENTIFIER DRIFT: comment mentions 'This' which no longer exists in new code. Possible renames: ['there'].
- IDENTIFIER DRIFT: comment mentions 'results' which no longer exists in new code. Possible renames: ['record'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a boolean value)
- SUBJECT: "if this query should buffer before emitting results" → still this same thing? NO (the logic has changed significantly)
- QUALIFIERS: "before emitting results" → still all true? NO (the condition for buffering has changed)

The original comment states that the method returns if the query should buffer before emitting results. However, the code logic has changed. The old code had special handling for RAW queries without windows, but the new code has simplified logic: it returns true if there's no window (including Raw) OR if the window is not time-based. The comment mentions "this query" and "results" which are no longer directly referenced in the code. The condition for buffering has been inverted for time-based windows.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: shouldBuffer() -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a boolean val...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [20/77] `Summary_47`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Retrieve the fetch descriptor associated with the given entity key.` |
| ground_truth_comment | `Retrieve the fetch descriptor associated with the given entity key.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public SubselectFetch getSubselect(EntityKey key) {
		return (SubselectFetch) subselectsByEntityKey.get(key);
	}
```

**code_snippet**

```java
public SubselectFetch getSubselect(EntityKey key) {
		return subselectsByEntityKey.get( key );
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getSubselect(EntityKey key) -> SubselectFetch
Parameters Details: [{"name": "key", "type": "EntityKey"}]
intention:      Method 'getSubselect' (get Subselect)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Retrieve the fetch descriptor associated with the given entity key.

[Current Code]
	public SubselectFetch getSubselect(EntityKey key) {
		return subselectsByEntityKey.get( key );
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public SubselectFetch getSubselect(EntityKey key) {

-		return (SubselectFetch) subselectsByEntityKey.get(key);

+		return subselectsByEntityKey.get( key );

 	}
```

[Code Context]
- Signature: Full Signature: getSubselect(EntityKey key) -> SubselectFetch
Parameters Details: [{"name": "key", "type": "EntityKey"}]
- Intent: Method 'getSubselect' (get Subselect)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Retrieve" → still done by the code? YES. The method still retrieves a value from a map.
- SUBJECT: "the fetch descriptor associated with the given entity key" → still this same thing? YES. The method still returns a SubselectFetch associated with the EntityKey parameter.
- QUALIFIERS: None in the original comment.
- Brief conclusion: The summary accurately describes what the method does - it retrieves a fetch descriptor (SubselectFetch) based on an entity key.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getSubselect(EntityKey key) -> SubselectFetch
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [21/77] `Summary_49`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Provided we  #supportsInsertSelectIdentity, then attach the "select identity" clause to the insert statement.` |
| ground_truth_comment | `Provided we  #supportsInsertSelectIdentity, then attach the "select identity" clause to the insert statement.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public String appendIdentitySelectToInsert(String insertString) {
		return insertString;
	}
```

**code_snippet**

```java
public String appendIdentitySelectToInsert(String insertString) {
		return getIdentityColumnSupport().appendIdentitySelectToInsert( insertString );
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: appendIdentitySelectToInsert(String insertString) -> String
Parameters Details: [{"name": "insertString", "type": "String"}]
intention:      Method 'appendIdentitySelectToInsert' (append Identity Select To Insert)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Provided we  #supportsInsertSelectIdentity, then attach the "select identity" clause to the insert statement.

[Current Code]
	public String appendIdentitySelectToInsert(String insertString) {
		return getIdentityColumnSupport().appendIdentitySelectToInsert( insertString );
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public String appendIdentitySelectToInsert(String insertString) {

-		return insertString;

+		return getIdentityColumnSupport().appendIdentitySelectToInsert( insertString );

 	}
```

[Code Context]
- Signature: Full Signature: appendIdentitySelectToInsert(String insertString) -> String
Parameters Details: [{"name": "insertString", "type": "String"}]
- Intent: Method 'appendIdentitySelectToInsert' (append Identity Select To Insert)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "attach the 'select identity' clause to the insert statement" → still done by the code? YES
- SUBJECT: "insert statement" → still this same thing? YES
- QUALIFIERS: "Provided we #supportsInsertSelectIdentity" → still all true? YES (the method now delegates to getIdentityColumnSupport().appendIdentitySelectToInsert, which would presumably check this condition)
- Brief conclusion: The summary still accurately describes what the method does, though the implementation has changed to delegate to another method.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: appendIdentitySelectToInsert(String insertString) -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [22/77] `Summary_54`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Checks if a flag is set.` |
| ground_truth_comment | `Returns  true if any of the flags supplied in the argument are set.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public boolean isFlagSet(int flag) {
        return (flags & flag) != 0;
    }
```

**code_snippet**

```java
public boolean isFlagSet(int flagsToCheck) {
        return isFlagSet(flags, flagsToCheck);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: isFlagSet(int flagsToCheck) -> boolean
Parameters Details: [{"name": "flagsToCheck", "type": "int"}]
intention:      Method 'isFlagSet' (is Flag Set)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'flag'}; added params: {'flagsToCheck'}.", "IDENTIFIER DRIFT: comment mentions 'flag' which no longer exists in new code. Possible renames: ['flagsToCheck']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Checks if a flag is set.

[Current Code]
    public boolean isFlagSet(int flagsToCheck) {
        return isFlagSet(flags, flagsToCheck);
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: isFlagSet(int flagsToCheck) -> boolean
Parameters Details: [{"name": "flagsToCheck", "type": "int"}]
- Intent: Method 'isFlagSet' (is Flag Set)

[Rule-based Signals — HIGH PRIORITY]
- PARAMETERS CHANGED: removed params: {'flag'}; added params: {'flagsToCheck'}.
- IDENTIFIER DRIFT: comment mentions 'flag' which no longer exists in new code. Possible renames: ['flagsToCheck'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Checks if" → still done by the code? YES. The method still performs a check operation.
- SUBJECT: "a flag" → still this same thing? NO. The method now takes "flagsToCheck" as a parameter, not "flag". The parameter name has changed.
- QUALIFIERS: "is set" → still all true? YES. The method still checks if a flag is set.

The comment mentions "flag" but the current code uses "flagsToCheck" as the parameter name. This is a parameter name change that affects the subject of the comment. While the core functionality remains similar, the specific identifier mentioned in the comment no longer exists in the code.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isFlagSet(int flagsToCheck) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Checks if" → still done by the code? YES. The method still performs a check op...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [23/77] `Summary_58`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Creates and returns a new comparison object for the SQL "in" operator.` |
| ground_truth_comment | `Creates and returns an expression for the SQL "in" operator.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public DBCompareColExpr in(Object value)
    {
        return cmp(DBCmpType.IN, listToArray(value));
    }
```

**code_snippet**

```java
public final DBCompareColExpr in(Collection<?> values)
    {
        if (values==null || values.isEmpty())
            return cmp(DBCmpType.EQUAL, null);
        // create expression
        return cmp(DBCmpType.IN, values);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: in(Collection<?> values) -> DBCompareColExpr
Parameters Details: [{"name": "values", "type": "Collection<?>"}]
intention:      Method 'in' (in)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'value'}; added params: {'values'}.", "IDENTIFIER DRIFT: comment mentions 'Object' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Creates and returns a new comparison object for the SQL "in" operator.

[Current Code]
    public final DBCompareColExpr in(Collection<?> values)
    {
        if (values==null || values.isEmpty())
            return cmp(DBCmpType.EQUAL, null);
        // create expression
        return cmp(DBCmpType.IN, values);
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: in(Collection<?> values) -> DBCompareColExpr
Parameters Details: [{"name": "values", "type": "Collection<?>"}]
- Intent: Method 'in' (in)

[Rule-based Signals — HIGH PRIORITY]
- PARAMETERS CHANGED: removed params: {'value'}; added params: {'values'}.
- IDENTIFIER DRIFT: comment mentions 'Object' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Creates and returns" → The code still creates and returns a DBCompareColExpr object. YES
- SUBJECT: "a new comparison object for the SQL 'in' operator" → The code still creates a comparison object for the SQL "in" operator. YES
- QUALIFIERS: None specified in the comment. YES

However, there are significant structural changes that the comment doesn't account for:
1. The parameter changed from a single Object to a Collection<?> - this is a major change in what the method accepts
2. The method now has special handling for null or empty collections, returning an EQUAL comparison instead of IN
3. The method is now final (though this doesn't affect functionality)

The comment doesn't mention these behavioral changes, particularly the special case handling for null/empty collections. While the high-level purpose remains similar, the specific behavior has changed in ways that affect how the method works.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: in(Collection<?> values) -> DBCompareColExpr
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Creates and returns" → The code still creates and returns a DBCompareColExpr o...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [24/77] `Summary_60`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Method for getting counts using named filters` |
| ground_truth_comment | `Method for getting counts using named filters` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (obj == this) {
            return true;
        }
        if (obj.getClass() != getClass()) {
            return false;
        }

        FiltersAggregation rhs = (FiltersAggregation) obj;
        return new EqualsBuilder()
                .appendSuper(super.equals(obj))
                .append(bucketMap, rhs.bucketMap)
                .isEquals();
    }
```

**code_snippet**

```java
public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (obj == this) {
            return true;
        }
        if (obj.getClass() != getClass()) {
            return false;
        }

        FiltersAggregation rhs = (FiltersAggregation) obj;
        return super.equals(obj) && Objects.equals(bucketMap, rhs.bucketMap);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: equals(Object obj) -> boolean
Parameters Details: [{"name": "obj", "type": "Object"}]
intention:      Method 'equals' (equals)
implementation: Return paths: 4
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Method for getting counts using named filters

[Current Code]
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (obj == this) {
            return true;
        }
        if (obj.getClass() != getClass()) {
            return false;
        }

        FiltersAggregation rhs = (FiltersAggregation) obj;
        return super.equals(obj) && Objects.equals(bucketMap, rhs.bucketMap);
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -10,8 +10,5 @@
         }

 

         FiltersAggregation rhs = (FiltersAggregation) obj;

-        return new EqualsBuilder()

-                .appendSuper(super.equals(obj))

-                .append(bucketMap, rhs.bucketMap)

-                .isEquals();

+        return super.equals(obj) && Objects.equals(bucketMap, rhs.bucketMap);

     }
```

[Code Context]
- Signature: Full Signature: equals(Object obj) -> boolean
Parameters Details: [{"name": "obj", "type": "Object"}]
- Intent: Method 'equals' (equals)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Method for getting counts using named filters" → The code is actually an equals method, not a method for getting counts. NO
- SUBJECT: The summary suggests the method operates on filters to get counts, but the code is comparing two FiltersAggregation objects for equality. NO
- QUALIFIERS: "using named filters" → The code doesn't mention or use named filters at all. NO
- Brief conclusion: The summary completely misdescribes what the method does - it's an equals method, not a method for getting counts.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: equals(Object obj) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Method for getting counts using named filters" → The code is actually an equal...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [25/77] `Summary_61`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns all currently displayed sentences in string buffer, plain text form` |
| ground_truth_comment | `Returns all currently displayed sentences in plain text form.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getMatchedSentences() -> String
Parameters Details: []
intention:      Method 'getMatchedSentences' (get Matched Sentences)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'StringBuffer' -> 'String'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns all currently displayed sentences in string buffer, plain text form

[Current Code]
  public String getMatchedSentences() {
    StringBuilder sb = new StringBuilder();
    for (int i = 0, sz = list.getModel().getSize(); i < sz; i++) {
      String t = list.getModel().getElementAt(i).getLabel().getText();
      sb.append(t);
      sb.append("\n");
    }
    return sb.toString();
  }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getMatchedSentences() -> String
Parameters Details: []
- Intent: Method 'getMatchedSentences' (get Matched Sentences)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'StringBuffer' -> 'String'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES. The method still returns a value.
- SUBJECT: "all currently displayed sentences" → still this same thing? YES. The method still retrieves text from list elements.
- QUALIFIERS: "in string buffer, plain text form" → still all true? NO. The method now returns a String directly rather than a StringBuffer/StringBuilder, and the comment about "string buffer" is no longer accurate.

Brief conclusion: The summary is inconsistent because it mentions returning a "string buffer" when the method now returns a plain String directly.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getMatchedSentences() -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → still done by the code? YES. The method still returns a value.
- SU...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [26/77] `Summary_62`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns newest checkmark that has already been computed.` |
| ground_truth_comment | `Returns newest checkmark that has already been computed.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
protected Checkmark findNewest()
    {
        return new Select().from(Checkmark.class)
                .where("habit = ?", habit.getId())
                .and("timestamp <= ?", DateHelper.getStartOfToday())
                .orderBy("timestamp desc")
                .limit(1)
                .executeSingle();
    }
```

**code_snippet**

```java
protected Checkmark findNewest()
    {
        return new Select().from(Checkmark.class)
                .where("habit = ?", habit.getId())
                .and("timestamp <= ?", DateUtils.getStartOfToday())
                .orderBy("timestamp desc")
                .limit(1)
                .executeSingle();
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: findNewest() -> Checkmark
Parameters Details: []
intention:      Method 'findNewest' (find Newest)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns newest checkmark that has already been computed.

[Current Code]
    protected Checkmark findNewest()
    {
        return new Select().from(Checkmark.class)
                .where("habit = ?", habit.getId())
                .and("timestamp <= ?", DateUtils.getStartOfToday())
                .orderBy("timestamp desc")
                .limit(1)
                .executeSingle();
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -2,7 +2,7 @@
     {

         return new Select().from(Checkmark.class)

                 .where("habit = ?", habit.getId())

-                .and("timestamp <= ?", DateHelper.getStartOfToday())

+                .and("timestamp <= ?", DateUtils.getStartOfToday())

                 .orderBy("timestamp desc")

                 .limit(1)

                 .executeSingle();

```

[Code Context]
- Signature: Full Signature: findNewest() -> Checkmark
Parameters Details: []
- Intent: Method 'findNewest' (find Newest)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a Checkmark object)
- SUBJECT: "newest checkmark" → still this same thing? YES (the code still queries for the newest checkmark)
- QUALIFIERS: "that has already been computed" → still all true? YES (the code still retrieves a checkmark that was previously computed/stored)

The only change in the code was replacing DateHelper with DateUtils, which is an internal implementation detail that doesn't affect the method's behavior or what it returns. The summary still accurately describes what the method does.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: findNewest() -> Checkmark
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [27/77] `Summary_65`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns all currently displayed sentences in plain text form.` |
| ground_truth_comment | `Returns all currently displayed sentences in string buffer, plain text form` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getMatchedSentences() -> StringBuffer
Parameters Details: []
intention:      Method 'getMatchedSentences' (get Matched Sentences)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'String' -> 'StringBuffer'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns all currently displayed sentences in plain text form.

[Current Code]
  public StringBuffer getMatchedSentences() {
    StringBuffer sb = new StringBuffer();
    for(int i = 0; i < list.getModel().getSize(); i++) {
      String t = ((TreeFromFile) list.getModel().getElementAt(i)).getLabel().getText();
      sb.append(t);
      sb.append("\n");
    }
    return sb;
  }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getMatchedSentences() -> StringBuffer
Parameters Details: []
- Intent: Method 'getMatchedSentences' (get Matched Sentences)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'String' -> 'StringBuffer'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → The method still returns something, so YES.
- SUBJECT: "all currently displayed sentences" → The method still iterates through all elements in the list and extracts text from them, so YES.
- QUALIFIERS: "in plain text form" → The method now returns a StringBuffer directly instead of converting it to a String, but it's still in plain text form, so YES.
- Brief conclusion: The summary still accurately describes what the method does, despite the return type change from String to StringBuffer.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getMatchedSentences() -> StringBuffer
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [28/77] `Summary_66`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `This method initializes panelCommand` |
| ground_truth_comment | `This method initializes panelCommand` |

### Step 0 · 原始数据

**old_code_snippet**

```java
private JButton getExportButton() {
		JButton csvExportButton = new JButton(Constant.messages.getString("params.toolbar.button.export"));
		csvExportButton.setIcon(new ImageIcon(ParamsPanel.class.getResource("/resource/icon/16/115.png")));
		csvExportButton.addActionListener((new AbstractAction() {
			private static final long serialVersionUID = 1L;

			@Override
			public void actionPerformed(ActionEvent e) {
				WritableFileChooser chooser = new WritableFileChooser();
				chooser.setSelectedFile(new File(Constant.messages.getString("params.button.export.default.name")));
				if (chooser
						.showSaveDialog(View.getSingleton().getMainFrame()) == WritableFileChooser.APPROVE_OPTION) {
					String file = chooser.getSelectedFile().toString();
					if (!file.endsWith(".csv")) {
						file += ".csv";
					}
					try (CSVPrinter pw = new CSVPrinter(
							Files.newBufferedWriter(chooser.getSelectedFile().toPath(), StandardCharsets.UTF_8),
							CSVFormat.DEFAULT)) {
						pw.printRecord(((ParamsTableModel) paramsTable.getModel()).getColumnNames());
						int rowCount = paramsTable.getRowCount();
						int colCount = paramsTable.getColumnCount();
						for (int row = 0; row < rowCount; row++) {
							List<Object> valueOfRow = new ArrayList<Object>();
							for (int col = 0; col < colCount; col++) {
								valueOfRow.add(paramsTable.getValueAt(row, col));
							}
							pw.printRecord(valueOfRow);
						}
						JOptionPane.showMessageDialog(View.getSingleton().getMainFrame(),
								Constant.messages.getString("params.button.export.success"));
					} catch (Exception ex) {
						JOptionPane.showMessageDialog(View.getSingleton().getMainFrame(),
								Constant.messages.getString("params.button.export.error") + "\n"
										+ ex.getLocalizedMessage());
						LOGGER.error("Export Failed: " + ex);
					}
				}
			}
		}));
		return csvExportButton;
	}
```

**code_snippet**

```java
private TableExportButton getExportButton() {
		if (exportButton == null) {
			exportButton = new TableExportButton(getParamsTable());
		}
		return exportButton;
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getExportButton() -> TableExportButton
Parameters Details: []
intention:      Method 'getExportButton' (get Export Button)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'JButton' -> 'TableExportButton'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
This method initializes panelCommand

[Current Code]
	private TableExportButton getExportButton() {
		if (exportButton == null) {
			exportButton = new TableExportButton(getParamsTable());
		}
		return exportButton;
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,42 +1,6 @@
-private JButton getExportButton() {

-		JButton csvExportButton = new JButton(Constant.messages.getString("params.toolbar.button.export"));

-		csvExportButton.setIcon(new ImageIcon(ParamsPanel.class.getResource("/resource/icon/16/115.png")));

-		csvExportButton.addActionListener((new AbstractAction() {

-			private static final long serialVersionUID = 1L;

-

-			@Override

-			public void actionPerformed(ActionEvent e) {

-				WritableFileChooser chooser = new WritableFileChooser();

-				chooser.setSelectedFile(new File(Constant.messages.getString("params.button.export.default.name")));

-				if (chooser

-						.showSaveDialog(View.getSingleton().getMainFrame()) == WritableFileChooser.APPROVE_OPTION) {

-					String file = chooser.getSelectedFile().toString();

-					if (!file.endsWith(".csv")) {

-						file += ".csv";

-					}

-					try (CSVPrinter pw = new CSVPrinter(

-							Files.newBufferedWriter(chooser.getSelectedFile().toPath(), StandardCharsets.UTF_8),

-							CSVFormat.DEFAULT)) {

-						pw.printRecord(((ParamsTableModel) paramsTable.getModel()).getColumnNames());

-						int rowCount = paramsTable.getRowCount();

-						int colCount = paramsTable.getColumnCount();

-						for (int row = 0; row < rowCount; row++) {

-							List<Object> valueOfRow = new ArrayList<Object>();

-							for (int col = 0; col < colCount; col++) {

-								valueOfRow.add(paramsTable.getValueAt(row, col));

-							}

-							pw.printRecord(valueOfRow);

-						}

-						JOptionPane.showMessageDialog(View.getSingleton().getMainFrame(),

-								Constant.messages.getString("params.button.export.success"));

-					} catch (Exception ex) {

-						JOptionPane.showMessageDialog(View.getSingleton().getMainFrame(),

-								Constant.messages.getString("params.button.export.error") + "\n"

-										+ ex.getLocalizedMessage());

-						LOGGER.error("Export Failed: " + ex);

-					}

-				}

-			}

-		}));

-		return csvExportButton;

+private TableExportButton getExportButton() {

+		if (exportButton == null) {

+			exportButton = new TableExportButton(getParamsTable());

+		}

+		return exportButton;

 	}
```

[Code Context]
- Signature: Full Signature: getExportButton() -> TableExportButton
Parameters Details: []
- Intent: Method 'getExportButton' (get Export Button)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'JButton' -> 'TableExportButton'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "initializes" → NO, the method now returns a pre-existing instance if it exists or creates a new one if null. It doesn't initialize anything.
- SUBJECT: "panelCommand" → NO, the method now deals with "exportButton" of type "TableExportButton", not "panelCommand".
- QUALIFIERS: None specified in the summary.
- Brief conclusion: The summary completely misdescribes the method's purpose, action, and subject.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getExportButton() -> TableExportButton
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "initializes" → NO, the method now returns a pre-existing instance if it exists...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [29/77] `Summary_67`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `If a Schema contains a reference to an other Schema with '$ref', returns the referenced Schema or the actual Schema in the other cases.` |
| ground_truth_comment | `If a Schema contains a reference to an other Schema with '$ref', returns the referenced Schema if it is found or the actual Schema in the other cases.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static Schema getReferencedSchema(OpenAPI openAPI, Schema schema) {
        if (schema != null && StringUtils.isNotEmpty(schema.get$ref())) {
            String name = getSimpleRef(schema.get$ref());
            return getSchema(openAPI, name);
        }
        return schema;
    }
```

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getReferencedSchema(OpenAPI openAPI, Schema schema) -> Schema
Parameters Details: [{"name": "openAPI", "type": "OpenAPI"}, {"name": "schema", "type": "Schema"}]
intention:      Method 'getReferencedSchema' (get Referenced Schema)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
If a Schema contains a reference to an other Schema with '$ref', returns the referenced Schema or the actual Schema in the other cases.

[Current Code]
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


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getReferencedSchema(OpenAPI openAPI, Schema schema) -> Schema
Parameters Details: [{"name": "openAPI", "type": "OpenAPI"}, {"name": "schema", "type": "Schema"}]
- Intent: Method 'getReferencedSchema' (get Referenced Schema)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "returns the referenced Schema or the actual Schema in the other cases" → still done by the code? YES
- SUBJECT: "a Schema" → still this same thing? YES
- QUALIFIERS: "If a Schema contains a reference to an other Schema with '$ref'" → still all true? YES

The original comment accurately describes the current code. The change adds a null check for the referenced schema before returning it, but the overall behavior remains the same: if a schema has a $ref, it returns the referenced schema (if found), otherwise it returns the original schema.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getReferencedSchema(OpenAPI openAPI, Schema schema) -> Schema
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [30/77] `Summary_76`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `All proprietary Comet based  Servlet must invoke the timedout method when the underlying WebServer time out the  AtmosphereResponse.` |
| ground_truth_comment | `All proprietary Comet based  Servlet must invoke the timedout method when the underlying WebServer time out the  AtmosphereResponse.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public Action timedout(AtmosphereRequest request, AtmosphereResponse response)
            throws IOException, ServletException {

        AtmosphereResourceImpl r = null;

        try {
            SessionTimeoutSupport.restoreTimeout(request);

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

            if (r != null && r.isCancelled()) {
                return cancelledAction;
            }

            if (r == null) {
                logger.debug("AtmosphereResource was null, failed to timeout AtmosphereRequest {}", request);
            }

            if (r != null && r.getAtmosphereResourceEvent().isSuspended()) {
                r.getAtmosphereResourceEvent().setIsResumedOnTimeout(true);

                Broadcaster b = r.getBroadcaster();
                if (b instanceof DefaultBroadcaster) {
                    ((DefaultBroadcaster) b).broadcastOnResume(r);
                }

                if (request.getAttribute(ApplicationConfig.RESUMED_ON_TIMEOUT) != null) {
                    r.getAtmosphereResourceEvent().setIsResumedOnTimeout(
                            (Boolean) request.getAttribute(ApplicationConfig.RESUMED_ON_TIMEOUT));
                }

                invokeAtmosphereHandler(r);
            }
        } catch (Throwable t) {
            logger.error("failed to timeout resource {}", r, t);
        } finally {
            config.framework().notify(Action.TYPE.TIMEOUT, request, response);
            try {
                if (r != null) {
                    r.notifyListeners();
                    r.setIsInScope(false);
                    r.cancel();
                }
            } catch (Throwable t) {
                logger.trace("timedout", t);
            } finally {
                try {
                    response.getOutputStream().close();
                } catch (Throwable t) {
                    try {
                        response.getWriter().close();
                    } catch (Throwable t2) {
                    }
                }

                if (r != null) {
                    r._destroy();
                }
            }
        }

        return timedoutAction;
    }
```

**code_snippet**

```java
public Action timedout(AtmosphereRequest request, AtmosphereResponse response)
            throws IOException, ServletException {

        AtmosphereResourceImpl r = null;

        try {
            SessionTimeoutSupport.restoreTimeout(request);

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
                }

                if (request.getAttribute(ApplicationConfig.RESUMED_ON_TIMEOUT) != null) {
                    r.getAtmosphereResourceEvent().setIsResumedOnTimeout(
                            (Boolean) request.getAttribute(ApplicationConfig.RESUMED_ON_TIMEOUT));
                }

                invokeAtmosphereHandler(r);
            }
        } catch (Throwable t) {
            logger.error("failed to timeout resource {}", r, t);
        } finally {
            config.framework().notify(Action.TYPE.TIMEOUT, request, response);
            try {
                if (r != null) {
                    r.notifyListeners();
                    r.setIsInScope(false);
                    r.cancel();
                }
            } catch (Throwable t) {
                logger.trace("timedout", t);
            } finally {

                try {
                    response.getOutputStream().close();
                } catch (Throwable t) {
                    try {
                        response.getWriter().close();
                    } catch (Throwable t2) {
                    }
                }

                if (r != null) {
                    destroyResource(r);
                }
            }
        }

        return timedoutAction;
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: timedout(AtmosphereRequest request, AtmosphereResponse response) -> Action throws IOException, ServletException
Parameters Details: [{"name": "request", "type": "AtmosphereRequest"}, {"name": "response", "type": "AtmosphereResponse"}]
intention:      Method 'timedout' (timedout)
implementation: Return paths: 3, throws: IOException, ServletException
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
All proprietary Comet based  Servlet must invoke the timedout method when the underlying WebServer time out the  AtmosphereResponse.

[Current Code]
    public Action timedout(AtmosphereRequest request, AtmosphereResponse response)
            throws IOException, ServletException {

        AtmosphereResourceImpl r = null;

        try {
            SessionTimeoutSupport.restoreTimeout(request);

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
                }

                if (request.getAttribute(ApplicationConfig.RESUMED_ON_TIMEOUT) != null) {
                    r.getAtmosphereResourceEvent().setIsResumedOnTimeout(
                            (Boolean) request.getAttribute(ApplicationConfig.RESUMED_ON_TIMEOUT));
                }

                invokeAtmosphereHandler(r);
            }
        } catch (Throwable t) {
            logger.error("failed to timeout resource {}", r, t);
        } finally {
            config.framework().notify(Action.TYPE.TIMEOUT, request, response);
            try {
                if (r != null) {
                    r.notifyListeners();
                    r.setIsInScope(false);
                    r.cancel();
                }
            } catch (Throwable t) {
                logger.trace("timedout", t);
            } finally {

                try {
                    response.getOutputStream().close();
                } catch (Throwable t) {
                    try {
                        response.getWriter().close();
                    } catch (Throwable t2) {
                    }
                }

                if (r != null) {
                    destroyResource(r);
                }
            }
        }

        return timedoutAction;
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -24,14 +24,6 @@
             }

 

             r = (AtmosphereResourceImpl) request.getAttribute(FrameworkConfig.ATMOSPHERE_RESOURCE);

-

-            if (r != null && r.isCancelled()) {

-                return cancelledAction;

-            }

-

-            if (r == null) {

-                logger.debug("AtmosphereResource was null, failed to timeout AtmosphereRequest {}", request);

-            }

 

             if (r != null && r.getAtmosphereResourceEvent().isSuspended()) {

                 r.getAtmosphereResourceEvent().setIsResumedOnTimeout(true);

@@ -61,6 +53,7 @@
             } catch (Throwable t) {

                 logger.trace("timedout", t);

             } finally {

+

                 try {

                     response.getOutputStream().close();

                 } catch (Throwable t) {

@@ -71,7 +64,7 @@
                 }

 

                 if (r != null) {

-                    r._destroy();

+                    destroyResource(r);

                 }

             }

         }

```

[Code Context]
- Signature: Full Signature: timedout(AtmosphereRequest request, AtmosphereResponse response) -> Action throws IOException, ServletException
Parameters Details: [{"name": "request", "type": "AtmosphereRequest"}, {"name": "response", "type": "AtmosphereResponse"}]
- Intent: Method 'timedout' (timedout)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "invoke the timedout method" → The method is still named "timedout" and is being called in the same context. YES
- SUBJECT: "All proprietary Comet based Servlet" → The method is still part of the Comet-based Servlet framework handling timeout scenarios. YES
- QUALIFIERS: "when the underlying WebServer time out the AtmosphereResponse" → The method still handles the timeout scenario for AtmosphereResponse, though some internal logic has changed. YES

The method still handles the timeout scenario for Comet-based Servlets when the WebServer times out the AtmosphereResponse. While some internal implementation details have changed (like the removal of the cancelled check and changing from r._destroy() to destroyResource(r)), the core purpose and functionality described in the comment remain intact.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: timedout(AtmosphereRequest request, AtmosphereResponse response) -> Action throw
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [31/77] `Summary_77`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns the common base directory between a current base directory and a given file.` |
| ground_truth_comment | `Returns the common base directory between the passed file1 and file2.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getBaseDir(File file1, File file2) -> File
Parameters Details: [{"name": "file1", "type": "File"}, {"name": "file2", "type": "File"}]
intention:      Method 'getBaseDir' (get Base Dir)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'base', 'file'}; added params: {'file1', 'file2'}.", "IDENTIFIER DRIFT: comment mentions 'base' which no longer exists in new code.", "IDENTIFIER DRIFT: comment mentions 'file' which no longer exists in new code. Possible renames: ['final', 'file1', 'file2']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns the common base directory between a current base directory and a given file.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getBaseDir(File file1, File file2) -> File
Parameters Details: [{"name": "file1", "type": "File"}, {"name": "file2", "type": "File"}]
- Intent: Method 'getBaseDir' (get Base Dir)

[Rule-based Signals — HIGH PRIORITY]
- PARAMETERS CHANGED: removed params: {'base', 'file'}; added params: {'file1', 'file2'}.
- IDENTIFIER DRIFT: comment mentions 'base' which no longer exists in new code.
- IDENTIFIER DRIFT: comment mentions 'file' which no longer exists in new code. Possible renames: ['final', 'file1', 'file2'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → The code still returns a value, so YES.
- SUBJECT: "the common base directory between a current base directory and a given file" → The code now takes two File objects (file1 and file2) and finds their common base directory. The subject has changed from "between a current base directory and a given file" to "between two files". The original comment implied one was a base directory and the other was a file, but now both are treated symmetrically as files. NO.
- QUALIFIERS: None specified in the original comment.

The original comment described a method that took a base directory and a file, but the current code takes two files and treats them symmetrically. The subject of the operation has changed.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getBaseDir(File file1, File file2) -> File
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → The code still returns a value, so YES.
- SUBJECT: "the common base...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [32/77] `Summary_79`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Does this time interval contain the specified time interval completely.` |
| ground_truth_comment | `Does this time interval contain or equal the specified time interval.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: contains(ReadableInterval interval) -> boolean
Parameters Details: [{"name": "interval", "type": "ReadableInterval"}]
intention:      Method 'contains' (contains)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Does this time interval contain the specified time interval completely.

[Current Code]
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


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: contains(ReadableInterval interval) -> boolean
Parameters Details: [{"name": "interval", "type": "ReadableInterval"}]
- Intent: Method 'contains' (contains)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Does this time interval contain" → The method still checks if one time interval contains another. YES
- SUBJECT: "the specified time interval completely" → The method still checks if the current interval completely contains the passed interval. YES
- QUALIFIERS: None specified in the summary. YES

The original comment states that the method checks if one time interval completely contains another. The current code still performs this check, though it has been modified to also explicitly handle the case where the intervals are exactly equal (which was already implicitly handled by the original condition). The core functionality remains the same.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: contains(ReadableInterval interval) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [33/77] `Summary_81`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Installs a list of  RemotePackage and their dependent packages.` |
| ground_truth_comment | `Installs a  RemotePackage and its dependent packages.` |

### Step 0 · 原始数据

**old_code_snippet**

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
                        installResults.put(p, InstallResultType.INSTALL_FAIL);
                    }
                }
            }
        }
        return installResults;
    }
```

**code_snippet**

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

            if (!result) {
                return false;
            }
        }

        return true;
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: installRemotePackages(List<RemotePackage> requestPackages, RepoManager repoManager, Downloader downloader, ProgressIndicator progress) -> boolean
Parameters Details: [{"name": "requestPackages", "type": "List<RemotePackage>"}, {"name": "repoManager", "type": "RepoManager"}, {"name": "downloader", "type": "Downloader"}, {"name": "progress", "type": "ProgressIndicator"}]
intention:      Method 'installRemotePackages' (install Remote Packages)
implementation: Return paths: 4
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'Map<RemotePackage, InstallResultType>' -> 'boolean'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Installs a list of  RemotePackage and their dependent packages.

[Current Code]
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

            if (!result) {
                return false;
            }
        }

        return true;
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

+                    repoManager.getLocalPath(), mSdkHandler.getFileOp())) {

+                progress.setText(

+                        "The license for package " + p.getDisplayName() + " was not accepted. "

+                                + "Please install this package through Android Studio SDK "

+                                + "Manager.");

+                return false;

+            }

+

+            Installer installer = SdkInstallerUtil

+                    .findBestInstallerFactory(p, mSdkHandler)

+                    .createInstaller(p, repoManager, downloader, mSdkHandler.getFileOp());

+            boolean result = installer.prepare(progress)

+                    && installer.complete(progress);

+

+            if (!result) {

+                return false;

             }

         }

-        return installResults;

+

```

[Code Context]
- Signature: Full Signature: installRemotePackages(List<RemotePackage> requestPackages, RepoManager repoManager, Downloader downloader, ProgressIndicator progress) -> boolean
Parameters Details: [{"name": "requestPackages", "type": "List<RemotePackage>"}, {"name": "repoManager", "type": "RepoManager"}, {"name": "downloader", "type": "Downloader"}, {"name": "progress", "type": "ProgressIndicator"}]
- Intent: Method 'installRemotePackages' (install Remote Packages)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'Map<RemotePackage, InstallResultType>' -> 'boolean'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Installs" → The code still performs installation of packages, so YES.
- SUBJECT: "a list of RemotePackage and their dependent packages" → The code still takes a list of RemotePackage and computes required packages, so YES.
- QUALIFIERS: None significant in the original comment.
- Brief conclusion: The comment describes the general purpose of the method, but there's a significant change in the return type and behavior.

CONCLUSION: INCONSISTENT

The original comment is inconsistent with the current code because the method's return type has changed from `Map<RemotePackage, InstallResultType>` to `boolean`. The original method returned detailed installation results for each package, while the current method simply returns a boolean indicating success or failure of the entire installation process. This is a fundamental change in the method's contract that the comment doesn't reflect.
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: installRemotePackages(List<RemotePackage> requestPackages, RepoManager repoManag
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Installs" → The code still performs installation of packages, so YES.
- SUBJEC...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [34/77] `Summary_83`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Get the global configuration table name including the correct escaped schema` |
| ground_truth_comment | `Get the global configuration table name including the correct schema` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getConfigurationTable(Connection con) -> String
Parameters Details: [{"name": "con", "type": "Connection"}]
intention:      Method 'getConfigurationTable' (get Configuration Table)
implementation: Return paths: 3
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Get the global configuration table name including the correct escaped schema

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getConfigurationTable(Connection con) -> String
Parameters Details: [{"name": "con", "type": "Connection"}]
- Intent: Method 'getConfigurationTable' (get Configuration Table)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Get the global configuration table name" → The method still returns a table name, so this is still accurate. YES
- SUBJECT: "global configuration table" → The method still returns a table name related to global configuration. YES
- QUALIFIERS: "including the correct escaped schema" → The original comment mentions "escaped schema", but the new code no longer uses escaping (the quotes around the schema were removed). The qualifier is no longer true. NO

Brief conclusion: The method still returns a global configuration table name, but it no longer includes schema escaping as mentioned in the original comment.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getConfigurationTable(Connection con) -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Get the global configuration table name" → The method still returns a table na...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [35/77] `Summary_87`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Obtains a ISTextExpert instance for processing structured text with the specified type handler and the specified environment.` |
| ground_truth_comment | `Obtains a IStructuredTextExpert instance for processing structured text with the specified type handler and the specified environment.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
static public ISTextExpert getStatefulExpert(STextTypeHandler handler, STextEnvironment environment) {
		if (environment == null)
			environment = STextEnvironment.DEFAULT;
		return new STextImpl(handler, environment, true);
	}
```

**code_snippet**

```java
static public IStructuredTextExpert getStatefulExpert(StructuredTextTypeHandler handler, StructuredTextEnvironment environment) {
		if (environment == null)
			environment = StructuredTextEnvironment.DEFAULT;
		return new StructuredTextImpl(handler, environment, true);
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getStatefulExpert(StructuredTextTypeHandler handler, StructuredTextEnvironment environment) -> IStructuredTextExpert
Parameters Details: [{"name": "handler", "type": "StructuredTextTypeHandler"}, {"name": "environment", "type": "StructuredTextEnvironment"}]
intention:      Method 'getStatefulExpert' (get Stateful Expert)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'ISTextExpert' -> 'IStructuredTextExpert'. If the comment references the old return type, it is INCONSISTENT.", "IDENTIFIER DRIFT: comment mentions 'ISTextExpert' which no longer exists in new code. Possible renames: ['IStructuredTextExpert']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Obtains a ISTextExpert instance for processing structured text with the specified type handler and the specified environment.

[Current Code]
	static public IStructuredTextExpert getStatefulExpert(StructuredTextTypeHandler handler, StructuredTextEnvironment environment) {
		if (environment == null)
			environment = StructuredTextEnvironment.DEFAULT;
		return new StructuredTextImpl(handler, environment, true);
	}



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getStatefulExpert(StructuredTextTypeHandler handler, StructuredTextEnvironment environment) -> IStructuredTextExpert
Parameters Details: [{"name": "handler", "type": "StructuredTextTypeHandler"}, {"name": "environment", "type": "StructuredTextEnvironment"}]
- Intent: Method 'getStatefulExpert' (get Stateful Expert)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'ISTextExpert' -> 'IStructuredTextExpert'. If the comment references the old return type, it is INCONSISTENT.
- IDENTIFIER DRIFT: comment mentions 'ISTextExpert' which no longer exists in new code. Possible renames: ['IStructuredTextExpert'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Obtains a" → The code still obtains/creates an expert object by instantiating StructuredTextImpl. YES
- SUBJECT: "ISTextExpert instance" → The return type has changed from ISTextExpert to IStructuredTextExpert. NO
- QUALIFIERS: "for processing structured text with the specified type handler and the specified environment" → The method still takes a handler and environment parameter and uses them to create the expert. YES

The comment mentions "ISTextExpert" which is no longer the return type of the method. The return type has changed to "IStructuredTextExpert", which is a significant structural change that makes the comment inconsistent with the current code.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getStatefulExpert(StructuredTextTypeHandler handler, StructuredTextEnvironment e
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Obtains a" → The code still obtains/creates an expert object by instantiating ...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [36/77] `Summary_89`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Create and return a new feature service with the default server URL.` |
| ground_truth_comment | `Create and return a new feature service with the default endpoint URL.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public FeatureService createFeatureService() {
        return createFeatureService(defaultServerUrl);
    }
```

**code_snippet**

```java
public FeatureService createFeatureService() {
        return createFeatureService(defaultEndpointUrl);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: createFeatureService() -> FeatureService
Parameters Details: []
intention:      Method 'createFeatureService' (create Feature Service)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Create and return a new feature service with the default server URL.

[Current Code]
    public FeatureService createFeatureService() {
        return createFeatureService(defaultEndpointUrl);
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public FeatureService createFeatureService() {

-        return createFeatureService(defaultServerUrl);

+        return createFeatureService(defaultEndpointUrl);

     }
```

[Code Context]
- Signature: Full Signature: createFeatureService() -> FeatureService
Parameters Details: []
- Intent: Method 'createFeatureService' (create Feature Service)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Create and return" → The code still creates and returns a FeatureService. YES
- SUBJECT: "a new feature service" → The code still creates a FeatureService object. YES
- QUALIFIERS: "with the default server URL" → The code now uses "defaultEndpointUrl" instead of "defaultServerUrl". This qualifier is no longer accurate. NO

Brief conclusion: The summary is inconsistent because it mentions "default server URL" while the code now uses "defaultEndpointUrl".

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: createFeatureService() -> FeatureService
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Create and return" → The code still creates and returns a FeatureService. YES
...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [37/77] `Summary_90`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `expect absolute request and allow both absolute and percent response based on pump capabilities` |
| ground_truth_comment | `expect absolute request and allow both absolute and percent response based on pump capabilities` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public boolean applyAPSRequest(APSResult request, Callback callback) {
        PumpInterface pump = getActivePump();
        request.rate = applyBasalConstraints(request.rate);
        PumpEnactResult result;

        if (!pump.isInitialized()) {
            log.debug("applyAPSRequest: " + MainApp.sResources.getString(R.string.pumpNotInitialized));
            if (callback != null) {
                callback.result(new PumpEnactResult().comment(MainApp.sResources.getString(R.string.pumpNotInitialized)).enacted(false).success(false)).run();
            }
            return false;
        }

        if (pump.isSuspended()) {
            log.debug("applyAPSRequest: " + MainApp.sResources.getString(R.string.pumpsuspended));
            if (callback != null) {
                callback.result(new PumpEnactResult().comment(MainApp.sResources.getString(R.string.pumpsuspended)).enacted(false).success(false)).run();
            }
            return false;
        }

        if (Config.logCongigBuilderActions)
            log.debug("applyAPSRequest: " + request.toString());
        if ((request.rate == 0 && request.duration == 0) || Math.abs(request.rate - pump.getBaseBasalRate()) < pump.getPumpDescription().basalStep) {
            if (isTempBasalInProgress()) {
                if (Config.logCongigBuilderActions)
                    log.debug("applyAPSRequest: cancelTempBasal()");
                getCommandQueue().cancelTempBasal(false, callback);
                return true;
            } else {
                if (Config.logCongigBuilderActions)
                    log.debug("applyAPSRequest: Basal set correctly");
                if (callback != null) {
                    callback.result(new PumpEnactResult().absolute(request.rate).duration(0).enacted(false).success(true).comment("Basal set correctly")).run();
                }
                return false;
            }
        } else if (isTempBasalInProgress() && Math.abs(request.rate - getTempBasalAbsoluteRateHistory()) < pump.getPumpDescription().basalStep) {
            if (Config.logCongigBuilderActions)
                log.debug("applyAPSRequest: Temp basal set correctly");
            if (callback != null) {
                callback.result(new PumpEnactResult().absolute(getTempBasalAbsoluteRateHistory()).duration(getTempBasalFromHistory(System.currentTimeMillis()).getPlannedRemainingMinutes()).enacted(false).success(true).comment("Temp basal set correctly")).run();
            }
            return false;
        } else {
            if (Config.logCongigBuilderActions)
                log.debug("applyAPSRequest: setTempBasalAbsolute()");
            getCommandQueue().tempBasalAbsolute(request.rate, request.duration, false, callback);
            return true;
        }
    }
```

**code_snippet**

```java
public PumpEnactResult applyAPSRequest(APSResult request) {
        request.rate = applyBasalConstraints(request.rate);
        PumpEnactResult result;

        if (!isInitialized()) {
            result = new PumpEnactResult();
            result.comment = MainApp.sResources.getString(R.string.pumpNotInitialized);
            result.enacted = false;
            result.success = false;
            log.debug("applyAPSRequest: " + MainApp.sResources.getString(R.string.pumpNotInitialized));
            return result;
        }

        if (isSuspended()) {
            result = new PumpEnactResult();
            result.comment = MainApp.sResources.getString(R.string.pumpsuspended);
            result.enacted = false;
            result.success = false;
            log.debug("applyAPSRequest: " + MainApp.sResources.getString(R.string.pumpsuspended));
            return result;
        }

        if (Config.logCongigBuilderActions)
            log.debug("applyAPSRequest: " + request.toString());
        if ((request.rate == 0 && request.duration == 0) || Math.abs(request.rate - getBaseBasalRate()) < getPumpDescription().basalStep) {
            if (isTempBasalInProgress()) {
                if (Config.logCongigBuilderActions)
                    log.debug("applyAPSRequest: cancelTempBasal()");
                result = cancelTempBasal(false);
            } else {
                result = new PumpEnactResult();
                result.absolute = request.rate;
                result.duration = 0;
                result.enacted = false;
                result.comment = "Basal set correctly";
                result.success = true;
                if (Config.logCongigBuilderActions)
                    log.debug("applyAPSRequest: Basal set correctly");
            }
        } else if (isTempBasalInProgress() && Math.abs(request.rate - getTempBasalAbsoluteRateHistory()) < getPumpDescription().basalStep) {
            result = new PumpEnactResult();
            result.absolute = getTempBasalAbsoluteRateHistory();
            result.duration = getTempBasalFromHistory(System.currentTimeMillis()).getPlannedRemainingMinutes();
            result.enacted = false;
            result.comment = "Temp basal set correctly";
            result.success = true;
            if (Config.logCongigBuilderActions)
                log.debug("applyAPSRequest: Temp basal set correctly");
        } else {
            if (Config.logCongigBuilderActions)
                log.debug("applyAPSRequest: setTempBasalAbsolute()");
            result = setTempBasalAbsolute(request.rate, request.duration);
        }
        return result;
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: applyAPSRequest(APSResult request) -> PumpEnactResult
Parameters Details: [{"name": "request", "type": "APSResult"}]
intention:      Method 'applyAPSRequest' (apply APS Request)
implementation: Return paths: 3
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'boolean' -> 'PumpEnactResult'. If the comment references the old return type, it is INCONSISTENT.", "PARAMETERS CHANGED: removed params: {'callback'}.", "IDENTIFIER DRIFT: comment mentions 'pump' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
expect absolute request and allow both absolute and percent response based on pump capabilities

[Current Code]
    public PumpEnactResult applyAPSRequest(APSResult request) {
        request.rate = applyBasalConstraints(request.rate);
        PumpEnactResult result;

        if (!isInitialized()) {
            result = new PumpEnactResult();
            result.comment = MainApp.sResources.getString(R.string.pumpNotInitialized);
            result.enacted = false;
            result.success = false;
            log.debug("applyAPSRequest: " + MainApp.sResources.getString(R.string.pumpNotInitialized));
            return result;
        }

        if (isSuspended()) {
            result = new PumpEnactResult();
            result.comment = MainApp.sResources.getString(R.string.pumpsuspended);
            result.enacted = false;
            result.success = false;
            log.debug("applyAPSRequest: " + MainApp.sResources.getString(R.string.pumpsuspended));
            return result;
        }

        if (Config.logCongigBuilderActions)
            log.debug("applyAPSRequest: " + request.toString());
        if ((request.rate == 0 && request.duration == 0) || Math.abs(request.rate - getBaseBasalRate()) < getPumpDescription().basalStep) {
            if (isTempBasalInProgress()) {
                if (Config.logCongigBuilderActions)
                    log.debug("applyAPSRequest: cancelTempBasal()");
                result = cancelTempBasal(false);
            } else {
                result = new PumpEnactResult();
                result.absolute = request.rate;
                result.duration = 0;
                result.enacted = false;
                result.comment = "Basal set correctly";
                result.success = true;
                if (Config.logCongigBuilderActions)
                    log.debug("applyAPSRequest: Basal set correctly");
            }
        } else if (isTempBasalInProgress() && Math.abs(request.rate - getTempBasalAbsoluteRateHistory()) < getPumpDescription().basalStep) {
            result = new PumpEnactResult();
            result.absolute = getTempBasalAbsoluteRateHistory();
            result.duration = getTempBasalFromHistory(System.currentTimeMillis()).getPlannedRemainingMinutes();
            result.enacted = false;
            result.comment = "Temp basal set correctly";
            result.success = true;
            if (Config.logCongigBuilderActions)
                log.debug("applyAPSRequest: Temp basal set correctly");
        } else {
            if (Config.logCongigBuilderActions)
                log.debug("applyAPSRequest: setTempBasalAbsolute()");
            result = setTempBasalAbsolute(request.rate, request.duration);
        }
        return result;
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,51 +1,55 @@
-public boolean applyAPSRequest(APSResult request, Callback callback) {

-        PumpInterface pump = getActivePump();

+public PumpEnactResult applyAPSRequest(APSResult request) {

         request.rate = applyBasalConstraints(request.rate);

         PumpEnactResult result;

 

-        if (!pump.isInitialized()) {

+        if (!isInitialized()) {

+            result = new PumpEnactResult();

+            result.comment = MainApp.sResources.getString(R.string.pumpNotInitialized);

+            result.enacted = false;

+            result.success = false;

             log.debug("applyAPSRequest: " + MainApp.sResources.getString(R.string.pumpNotInitialized));

-            if (callback != null) {

-                callback.result(new PumpEnactResult().comment(MainApp.sResources.getString(R.string.pumpNotInitialized)).enacted(false).success(false)).run();

-            }

-            return false;

+            return result;

         }

 

-        if (pump.isSuspended()) {

+        if (isSuspended()) {

+            result = new PumpEnactResult();

+            result.comment = MainApp.sResources.getString(R.string.pumpsuspended);

+            result.enacted = false;

+            result.success = false;

             log.debug("applyAPSRequest: " + MainApp.sResources.getString(R.string.pumpsuspended));

-            if (callback != null) {

-                callback.result(new PumpEnactResult().comment(MainApp.sResources.getString(R.string.pumpsuspended)).enacted(false).success(false)).run();

-            }

-            return false;

+            return result;

         }

 

         if (Config.logCongigBuilderActions)

             log.debug("applyAPSRequest: " + request.toString());

-        if ((request.rate == 0 && request.duration == 0) || Math.abs(request.rate - pump.getBaseBasalRate()) < pump.getPumpDescription().basalStep) {

+        if ((request.rate == 0 && request.duration == 0) || Math.abs(request.rate - getBaseBasalRate()) < getPumpDescription().basalStep) {

             if (isTempBasalInProgress()) {

                 if (Config.logCongigBuilderActions)

                     log.debug("applyAPSRequest: cancelTempBasal()");

-                getCommandQueue().cancelTempBasal(false, callback);

-                return true;

+                result = cancelTempBasal(false);

             } else {

+                result = new PumpEnactResult();

+                result.absolute = request.rate;

+                result.duration = 0;

+                result.enacted = false;

+                result.comment = "Basal set correctly";

+                result.success = true;

                 if (Config.logCongigBuilderActions)

                     log.debug("applyAPSRequest: Basal set correctly");

-                if (callback != null) {

-                    callback.result(new PumpEnactResult().absolute(request.rate).duration(0).enacted(false).success(true).comment("Basal set correctly")).run();

-                }

-                return false;

```

[Code Context]
- Signature: Full Signature: applyAPSRequest(APSResult request) -> PumpEnactResult
Parameters Details: [{"name": "request", "type": "APSResult"}]
- Intent: Method 'applyAPSRequest' (apply APS Request)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'boolean' -> 'PumpEnactResult'. If the comment references the old return type, it is INCONSISTENT.
- PARAMETERS CHANGED: removed params: {'callback'}.
- IDENTIFIER DRIFT: comment mentions 'pump' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "expect absolute request and allow both absolute and percent response based on pump capabilities" → The method still handles requests and determines how to respond based on pump capabilities, but the implementation has changed significantly.
- SUBJECT: The method now deals with APSResult requests and returns PumpEnactResult instead of boolean.
- QUALIFIERS: The comment mentions "absolute request and allow both absolute and percent response" but the code now only handles absolute rates (no percent responses visible in the new code).

The comment mentions expecting absolute requests and allowing both absolute and percent responses, but the new code only shows handling of absolute rates. Additionally, the method signature has changed significantly (return type and parameters), and the implementation has been refactored to return PumpEnactResult objects instead of boolean values.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: applyAPSRequest(APSResult request) -> PumpEnactResult
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "expect absolute request and allow both absolute and percent response based on ...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [38/77] `Summary_91`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `GET /user/username` |
| ground_truth_comment | `GET /user/username` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public User executeAs(Function<Response, Response> handler) {
            Type type = new TypeToken<User>(){}.getType();
            return getJSON().deserialize(execute(handler).asString(), type);
        }
```

**code_snippet**

```java
public User executeAs(Function<Response, Response> handler) {
            Type type = new TypeToken<User>(){}.getType();
            return execute(handler).as(type);
        }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: executeAs(Function<Response, Response> handler) -> User
Parameters Details: [{"name": "handler", "type": "Function<Response, Response>"}]
intention:      Method 'executeAs' (execute As)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
GET /user/username

[Current Code]
        public User executeAs(Function<Response, Response> handler) {
            Type type = new TypeToken<User>(){}.getType();
            return execute(handler).as(type);
        }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
 public User executeAs(Function<Response, Response> handler) {

             Type type = new TypeToken<User>(){}.getType();

-            return getJSON().deserialize(execute(handler).asString(), type);

+            return execute(handler).as(type);

         }
```

[Code Context]
- Signature: Full Signature: executeAs(Function<Response, Response> handler) -> User
Parameters Details: [{"name": "handler", "type": "Function<Response, Response>"}]
- Intent: Method 'executeAs' (execute As)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "GET /user/username" → The method is still performing a GET operation to retrieve user data, but the summary doesn't accurately describe the method's action which is actually executing a handler and returning a User object.
- SUBJECT: "/user/username" → The subject in the comment suggests it's specifically getting a user by username, but the current code is more generic - it executes a handler and returns a User object without specifying the endpoint.
- QUALIFIERS: None specified in the comment that can be verified against the current code.

The comment appears to be describing an API endpoint rather than the method's actual functionality. The method is executing a handler and returning a User object, not specifically performing a GET to /user/username.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: executeAs(Function<Response, Response> handler) -> User
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "GET /user/username" → The method is still performing a GET operation to retrie...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [39/77] `Summary_93`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns an Iterable of the lines in the file, wrapping the generated` |
| ground_truth_comment | `Returns an Iterable of the lines in the file, wrapping the generated` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public Iterator<String> iterator() {
        return new Iterator<String>() {

          protected BufferedReader reader = this.getReader();
          protected String line = this.getLine();

          public boolean hasNext() {
            return this.line != null;
          }

          public String next() {
            String nextLine = this.line;
            if (nextLine == null) {
              throw new NoSuchElementException();
            }
            line = getLine();
            return nextLine;
          }

          protected String getLine() {
            try {
              String result = this.reader.readLine();
              if (result == null) {
                this.reader.close();
              }
              return result;
            } catch (IOException e) {
              throw new RuntimeIOException(e);
            }
          }

          protected BufferedReader getReader() {
            try {
              InputStream stream = new FileInputStream(file);
              if (fileInputStreamWrapper != null) {
                stream = fileInputStreamWrapper.getConstructor(
                        InputStream.class).newInstance(stream);
              }
              return new BufferedReader(new InputStreamReader(stream));
            } catch (Exception e) {
              throw new RuntimeIOException(e);
            }
          }

          public void remove() {
            throw new UnsupportedOperationException();
          }
        };
      }
```

**code_snippet**

```java
public Iterator<String> iterator() {
        return new Iterator<String>() {

          protected BufferedReader reader = this.getReader();
          protected String line = this.getLine();

          public boolean hasNext() {
            return this.line != null;
          }

          public String next() {
            String nextLine = this.line;
            if (nextLine == null) {
              throw new NoSuchElementException();
            }
            line = getLine();
            return nextLine;
          }

          protected String getLine() {
            try {
              String result = this.reader.readLine();
              if (result == null) {
                this.reader.close();
              }
              return result;
            } catch (IOException e) {
              throw new RuntimeIOException(e);
            }
          }

          protected BufferedReader getReader() {
            try {
              InputStream stream = new FileInputStream(file);
              if (fileInputStreamWrapper != null) {
                stream = fileInputStreamWrapper.getConstructor(
                        InputStream.class).newInstance(stream);
              }
              if (encoding == null) {
                return new BufferedReader(new InputStreamReader(stream));
              } else {
                return new BufferedReader(new InputStreamReader(stream, encoding));
              }
            } catch (Exception e) {
              throw new RuntimeIOException(e);
            }
          }

          public void remove() {
            throw new UnsupportedOperationException();
          }
        };
      }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: iterator() -> Iterator<String>
Parameters Details: []
intention:      Method 'iterator' (iterator)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns an Iterable of the lines in the file, wrapping the generated

[Current Code]
      public Iterator<String> iterator() {
        return new Iterator<String>() {

          protected BufferedReader reader = this.getReader();
          protected String line = this.getLine();

          public boolean hasNext() {
            return this.line != null;
          }

          public String next() {
            String nextLine = this.line;
            if (nextLine == null) {
              throw new NoSuchElementException();
            }
            line = getLine();
            return nextLine;
          }

          protected String getLine() {
            try {
              String result = this.reader.readLine();
              if (result == null) {
                this.reader.close();
              }
              return result;
            } catch (IOException e) {
              throw new RuntimeIOException(e);
            }
          }

          protected BufferedReader getReader() {
            try {
              InputStream stream = new FileInputStream(file);
              if (fileInputStreamWrapper != null) {
                stream = fileInputStreamWrapper.getConstructor(
                        InputStream.class).newInstance(stream);
              }
              if (encoding == null) {
                return new BufferedReader(new InputStreamReader(stream));
              } else {
                return new BufferedReader(new InputStreamReader(stream, encoding));
              }
            } catch (Exception e) {
              throw new RuntimeIOException(e);
            }
          }

          public void remove() {
            throw new UnsupportedOperationException();
          }
        };
      }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -36,7 +36,11 @@
                 stream = fileInputStreamWrapper.getConstructor(

                         InputStream.class).newInstance(stream);

               }

-              return new BufferedReader(new InputStreamReader(stream));

+              if (encoding == null) {

+                return new BufferedReader(new InputStreamReader(stream));

+              } else {

+                return new BufferedReader(new InputStreamReader(stream, encoding));

+              }

             } catch (Exception e) {

               throw new RuntimeIOException(e);

             }

```

[Code Context]
- Signature: Full Signature: iterator() -> Iterator<String>
Parameters Details: []
- Intent: Method 'iterator' (iterator)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns an Iterable" → The code still returns an Iterator (which is an Iterable), so YES
- SUBJECT: "the lines in the file" → The code still processes lines from a file, so YES
- QUALIFIERS: "wrapping the generated" → This qualifier is vague and doesn't clearly describe anything specific about the implementation. The code does wrap the generated lines in an Iterator, but this qualifier is too vague to be meaningful.

Brief conclusion: The summary still describes the high-level action and subject of the method, though the qualifier is vague.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: iterator() -> Iterator<String>
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [40/77] `Summary_95`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns a Button which shows a given text.` |
| ground_truth_comment | `Returns a Button which shows a given text.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public Button getButton(String text, boolean onlyVisible)
	{
		return viewFetcher.getView(Button.class, text, onlyVisible);
	}
```

**code_snippet**

```java
public Button getButton(String text, boolean onlyVisible)
	{
		return getter.getView(Button.class, text, onlyVisible);
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getButton(String text, boolean onlyVisible) -> Button
Parameters Details: [{"name": "text", "type": "String"}, {"name": "onlyVisible", "type": "boolean"}]
intention:      Method 'getButton' (get Button)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns a Button which shows a given text.

[Current Code]
	public Button getButton(String text, boolean onlyVisible)
	{
		return getter.getView(Button.class, text, onlyVisible);
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,4 +1,4 @@
 public Button getButton(String text, boolean onlyVisible)

 	{

-		return viewFetcher.getView(Button.class, text, onlyVisible);

+		return getter.getView(Button.class, text, onlyVisible);

 	}
```

[Code Context]
- Signature: Full Signature: getButton(String text, boolean onlyVisible) -> Button
Parameters Details: [{"name": "text", "type": "String"}, {"name": "onlyVisible", "type": "boolean"}]
- Intent: Method 'getButton' (get Button)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a Button)
- SUBJECT: "a Button" → still this same thing? YES (the method still returns a Button)
- QUALIFIERS: "which shows a given text" → still all true? YES (the method still takes a text parameter and uses it to get a Button)

The summary accurately describes what the method does - it returns a Button that shows a given text. The only change was from `viewFetcher.getView()` to `getter.getView()`, which is an internal implementation detail that doesn't change the method's purpose or behavior.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getButton(String text, boolean onlyVisible) -> Button
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [41/77] `Summary_99`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Override with any special handling of response codes` |
| ground_truth_comment | `Override with any special handling of response codes` |

### Step 0 · 原始数据

**old_code_snippet**

```java
protected Response findMethodResponse(Map<String, Response> responses) {

        String code = null;
        for (String responseCode : responses.keySet()) {
            if (responseCode.startsWith("2") || responseCode.equals("default")) {
                if (code == null || code.compareTo(responseCode) > 0) {
                    code = responseCode;
                }
            }
        }
        if (code == null) {
            return null;
        }
        return responses.get(code);
    }
```

**code_snippet**

```java
protected ApiResponse findMethodResponse(ApiResponses responses) {
        String code = null;
        for (String responseCode : responses.keySet()) {
            if (responseCode.startsWith("2") || responseCode.equals("default")) {
                if (code == null || code.compareTo(responseCode) > 0) {
                    code = responseCode;
                }
            }
        }
        if (code == null) {
            return null;
        }
        return responses.get(code);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: findMethodResponse(ApiResponses responses) -> ApiResponse
Parameters Details: [{"name": "responses", "type": "ApiResponses"}]
intention:      Method 'findMethodResponse' (find Method Response)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'Response' -> 'ApiResponse'. If the comment references the old return type, it is INCONSISTENT.", "IDENTIFIER DRIFT: comment mentions 'Response' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Override with any special handling of response codes

[Current Code]
    protected ApiResponse findMethodResponse(ApiResponses responses) {
        String code = null;
        for (String responseCode : responses.keySet()) {
            if (responseCode.startsWith("2") || responseCode.equals("default")) {
                if (code == null || code.compareTo(responseCode) > 0) {
                    code = responseCode;
                }
            }
        }
        if (code == null) {
            return null;
        }
        return responses.get(code);
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,5 +1,4 @@
-protected Response findMethodResponse(Map<String, Response> responses) {

-

+protected ApiResponse findMethodResponse(ApiResponses responses) {

         String code = null;

         for (String responseCode : responses.keySet()) {

             if (responseCode.startsWith("2") || responseCode.equals("default")) {

```

[Code Context]
- Signature: Full Signature: findMethodResponse(ApiResponses responses) -> ApiResponse
Parameters Details: [{"name": "responses", "type": "ApiResponses"}]
- Intent: Method 'findMethodResponse' (find Method Response)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'Response' -> 'ApiResponse'. If the comment references the old return type, it is INCONSISTENT.
- IDENTIFIER DRIFT: comment mentions 'Response' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Override with any special handling of response codes" → The method doesn't appear to be handling response codes in a special way, but rather finding a specific response code (starting with "2" or "default") from a collection of responses. NO
- SUBJECT: "response codes" → The method does operate on response codes, but it's not about special handling of them. PARTIAL
- QUALIFIERS: "special handling" → The method doesn't provide special handling but rather selects the lowest 2xx code or "default" response. NO
- Brief conclusion: The comment suggests the method is for special handling of response codes, but the actual implementation is about finding a specific response code based on priority rules.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: findMethodResponse(ApiResponses responses) -> ApiResponse
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Override with any special handling of response codes" → The method doesn't app...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [42/77] `Summary_101`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Seeks the field with the given name in the stream and positions (and returns) the parser to the next available token (value or not).` |
| ground_truth_comment | `Seeks the field with the given name in the stream and positions (and returns) the parser to the next available token (value or not).` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static Token seek(String path, Parser parser) {
        // return current token if no path is given
        if (!StringUtils.hasText(path)) {
            return null;
        }

        List<String> tokens = StringUtils.tokenize(path, "/");
        ListIterator<String> li = tokens.listIterator();
        return doSeekToken(li.next(), li, parser);
    }
```

**code_snippet**

```java
public static Token seek(String path, Parser parser) {
        // return current token if no path is given
        if (!StringUtils.hasText(path)) {
            return null;
        }

        List<String> tokens = StringUtils.tokenize(path, "/");
        return seek(parser, tokens.toArray(new String[tokens.size()]));
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: seek(String path, Parser parser) -> Token
Parameters Details: [{"name": "path", "type": "String"}, {"name": "parser", "type": "Parser"}]
intention:      Method 'seek' (seek)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'next' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Seeks the field with the given name in the stream and positions (and returns) the parser to the next available token (value or not).

[Current Code]
    public static Token seek(String path, Parser parser) {
        // return current token if no path is given
        if (!StringUtils.hasText(path)) {
            return null;
        }

        List<String> tokens = StringUtils.tokenize(path, "/");
        return seek(parser, tokens.toArray(new String[tokens.size()]));
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -5,6 +5,5 @@
         }

 

         List<String> tokens = StringUtils.tokenize(path, "/");

-        ListIterator<String> li = tokens.listIterator();

-        return doSeekToken(li.next(), li, parser);

+        return seek(parser, tokens.toArray(new String[tokens.size()]));

     }
```

[Code Context]
- Signature: Full Signature: seek(String path, Parser parser) -> Token
Parameters Details: [{"name": "path", "type": "String"}, {"name": "parser", "type": "Parser"}]
- Intent: Method 'seek' (seek)

[Rule-based Signals — HIGH PRIORITY]
- IDENTIFIER DRIFT: comment mentions 'next' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Seeks the field with the given name in the stream and positions (and returns) the parser to the next available token (value or not)" → The code still seeks a field in the stream and returns a token, but the implementation has changed. The action is still fundamentally the same.
- SUBJECT: "the field with the given name in the stream" → The code still takes a path parameter and processes it to find a field in the stream.
- QUALIFIERS: "positions (and returns) the parser to the next available token (value or not)" → The code still returns a token and positions the parser, but the implementation details have changed.

The core functionality remains the same - the method seeks a field in the stream and returns a token while positioning the parser. The implementation has been refactored to use a different approach (calling another seek method with an array instead of using a list iterator), but the high-level behavior described in the comment is still accurate.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: seek(String path, Parser parser) -> Token
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [43/77] `Summary_103`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Checks if this potato is baked.` |
| ground_truth_comment | `Checks if this potato is baked.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public boolean isBaked() {
        try {
            return this.isPutIntoOven();
        } catch (OvenException e) {
            return false;
        }
    }
```

**code_snippet**

```java
public boolean isBaked() throws NotDeliciousException {
        try {
            long begin = System.currentTimeMillis();
            boolean isInOven = this.isPutIntoOven();
            long bakeTime = (System.currentTimeMillis() - begin);
            if (bakeTime > 1100) throw new NotDeliciousException(NotDeliciousReason.OVERCOOKED);
            return isInOven;
        } catch (OvenException e) {
            return false;
        }
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: isBaked() -> boolean throws NotDeliciousException
Parameters Details: []
intention:      Method 'isBaked' (is Baked)
implementation: Return paths: 2, throws: NotDeliciousException
```

### Step 2 · 规则信号

```text
rule_signals    = ["THROWS CHANGED: none -> {'NotDeliciousException'}."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Checks if this potato is baked.

[Current Code]
    public boolean isBaked() throws NotDeliciousException {
        try {
            long begin = System.currentTimeMillis();
            boolean isInOven = this.isPutIntoOven();
            long bakeTime = (System.currentTimeMillis() - begin);
            if (bakeTime > 1100) throw new NotDeliciousException(NotDeliciousReason.OVERCOOKED);
            return isInOven;
        } catch (OvenException e) {
            return false;
        }
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,6 +1,10 @@
-public boolean isBaked() {

+public boolean isBaked() throws NotDeliciousException {

         try {

-            return this.isPutIntoOven();

+            long begin = System.currentTimeMillis();

+            boolean isInOven = this.isPutIntoOven();

+            long bakeTime = (System.currentTimeMillis() - begin);

+            if (bakeTime > 1100) throw new NotDeliciousException(NotDeliciousReason.OVERCOOKED);

+            return isInOven;

         } catch (OvenException e) {

             return false;

         }

```

[Code Context]
- Signature: Full Signature: isBaked() -> boolean throws NotDeliciousException
Parameters Details: []
- Intent: Method 'isBaked' (is Baked)

[Rule-based Signals — HIGH PRIORITY]
- THROWS CHANGED: none -> {'NotDeliciousException'}.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Checks if" → The method still performs a check by returning a boolean value. YES
- SUBJECT: "this potato" → The method is still checking the state of the same object (potato). YES
- QUALIFIERS: "is baked" → The method still checks if the potato is in the oven, but now also includes a time check and can throw an exception if overcooked. The core concept of checking if it's baked remains, but with additional constraints. PARTIALLY
- Brief conclusion: The summary still describes the basic action and subject, but doesn't mention the new time-based check or exception handling.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isBaked() -> boolean throws NotDeliciousException
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Checks if" → The method still performs a check by returning a boolean value. Y...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [44/77] `Summary_104`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Creates a renderscript allocation from a bitmap` |
| ground_truth_comment | `Creates an Allocation from a  android.graphics.Bitmap.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

            // keep a reference to the Bitmap around to prevent GC
            Allocation alloc = new Allocation(id, rs, t, usage);
            alloc.setBitmap(b);
            return alloc;
        }


        int id = rs.nAllocationCreateFromBitmap(t.getID(rs), mips.mID, b, usage);
        if (id == 0) {
            throw new RSRuntimeException("Load failed.");
        }
        return new Allocation(id, rs, t, usage);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: createFromBitmap(RenderScript rs, Bitmap b, MipmapControl mips, int usage) -> Allocation
Parameters Details: [{"name": "rs", "type": "RenderScript"}, {"name": "b", "type": "Bitmap"}, {"name": "mips", "type": "MipmapControl"}, {"name": "usage", "type": "int"}]
intention:      Method 'createFromBitmap' (create From Bitmap)
implementation: Return paths: 4
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Creates a renderscript allocation from a bitmap

[Current Code]
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

            // keep a reference to the Bitmap around to prevent GC
            Allocation alloc = new Allocation(id, rs, t, usage);
            alloc.setBitmap(b);
            return alloc;
        }


        int id = rs.nAllocationCreateFromBitmap(t.getID(rs), mips.mID, b, usage);
        if (id == 0) {
            throw new RSRuntimeException("Load failed.");
        }
        return new Allocation(id, rs, t, usage);
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

 

         int id = rs.nAllocationCreateFromBitmap(t.getID(rs), mips.mID, b, usage);

         if (id == 0) {

```

[Code Context]
- Signature: Full Signature: createFromBitmap(RenderScript rs, Bitmap b, MipmapControl mips, int usage) -> Allocation
Parameters Details: [{"name": "rs", "type": "RenderScript"}, {"name": "b", "type": "Bitmap"}, {"name": "mips", "type": "MipmapControl"}, {"name": "usage", "type": "int"}]
- Intent: Method 'createFromBitmap' (create From Bitmap)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Creates a renderscript allocation" → The method still creates an Allocation object, so YES
- SUBJECT: "from a bitmap" → The method still takes a Bitmap as input and creates an Allocation from it, so YES
- QUALIFIERS: None mentioned in the summary, so N/A

The method has been enhanced with additional logic for handling native RenderScript instances, null bitmap configs, and optimized paths for certain conditions, but the core functionality of creating a renderscript allocation from a bitmap remains unchanged.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: createFromBitmap(RenderScript rs, Bitmap b, MipmapControl mips, int usage) -> Al
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [45/77] `Summary_105`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Computes the row type of an  Aggregate before it exists.` |
| ground_truth_comment | `Computes the row type of an  Aggregate before it exists.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public boolean isValid(Litmus litmus) {
    return super.isValid(litmus)
        && litmus.check(Util.isDistinct(getRowType().getFieldNames()), getRowType());
  }
```

**code_snippet**

```java
public boolean isValid(Litmus litmus) {
    return super.isValid(litmus)
        && litmus.check(Util.isDistinct(getRowType().getFieldNames()),
            "distinct field names: {}", getRowType());
  }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: isValid(Litmus litmus) -> boolean
Parameters Details: [{"name": "litmus", "type": "Litmus"}]
intention:      Method 'isValid' (is Valid)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Computes the row type of an  Aggregate before it exists.

[Current Code]
  public boolean isValid(Litmus litmus) {
    return super.isValid(litmus)
        && litmus.check(Util.isDistinct(getRowType().getFieldNames()),
            "distinct field names: {}", getRowType());
  }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,4 +1,5 @@
 public boolean isValid(Litmus litmus) {

     return super.isValid(litmus)

-        && litmus.check(Util.isDistinct(getRowType().getFieldNames()), getRowType());

+        && litmus.check(Util.isDistinct(getRowType().getFieldNames()),

+            "distinct field names: {}", getRowType());

   }
```

[Code Context]
- Signature: Full Signature: isValid(Litmus litmus) -> boolean
Parameters Details: [{"name": "litmus", "type": "Litmus"}]
- Intent: Method 'isValid' (is Valid)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Computes" → The current code doesn't compute anything, it validates using litmus checks. NO
- SUBJECT: "the row type of an Aggregate" → The current code uses getRowType() but doesn't compute it. NO
- QUALIFIERS: "before it exists" → This doesn't apply to the current code which simply validates existing field names. NO

The original comment describes a computation that doesn't match the current validation logic. The method now performs validation checks on field names rather than computing row types.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isValid(Litmus litmus) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Computes" → The current code doesn't compute anything, it validates using litm...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [46/77] `Summary_106`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns the sibling on the right of the end of given  Treepath.` |
| ground_truth_comment | `Returns the sibling on the left of the bottom of given  Treepath.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static Treepath getNextSibling( Treepath treepath ) {
    throw new UnsupportedOperationException( "getNextSibling" ) ;
  }
```

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getNextSibling(Treepath treepath) -> Treepath
Parameters Details: [{"name": "treepath", "type": "Treepath"}]
intention:      Method 'getNextSibling' (get Next Sibling)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns the sibling on the right of the end of given  Treepath.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getNextSibling(Treepath treepath) -> Treepath
Parameters Details: [{"name": "treepath", "type": "Treepath"}]
- Intent: Method 'getNextSibling' (get Next Sibling)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → The code does return a Treepath object, so this matches.
- SUBJECT: "the sibling on the right of the end of given Treepath" → The code finds the next sibling of the bottom node in the Treepath, which matches this description.
- QUALIFIERS: None specific in the comment beyond the basic action.

The comment accurately describes what the method does - it returns the next sibling (right sibling) of the bottom node in the given Treepath. The implementation has changed from throwing an UnsupportedOperationException to actually implementing this functionality, but the comment's description of what the method should do remains accurate.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getNextSibling(Treepath treepath) -> Treepath
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [47/77] `Summary_107`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Output the date time in ISO8601 format (yyyy-MM-ddTHH:mm:ss.SSSZ).` |
| ground_truth_comment | `Output the date time in ISO8601 format (yyyy-MM-ddTHH:mm:ss.SSSZ).` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public String toString() {
        return ISODateTimeFormat.getInstance(getChronology()).dateTime().print(this);
    }
```

**code_snippet**

```java
public String toString() {
        return ISODateTimeFormat.getInstance().dateTime().print(this);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: toString() -> String
Parameters Details: []
intention:      Method 'toString' (to String)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Output the date time in ISO8601 format (yyyy-MM-ddTHH:mm:ss.SSSZ).

[Current Code]
    public String toString() {
        return ISODateTimeFormat.getInstance().dateTime().print(this);
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public String toString() {

-        return ISODateTimeFormat.getInstance(getChronology()).dateTime().print(this);

+        return ISODateTimeFormat.getInstance().dateTime().print(this);

     }
```

[Code Context]
- Signature: Full Signature: toString() -> String
Parameters Details: []
- Intent: Method 'toString' (to String)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Output the date time" → The code still outputs a date time string using ISODateTimeFormat. YES
- SUBJECT: "date time" → The method still operates on a date time object (this). YES
- QUALIFIERS: "in ISO8601 format (yyyy-MM-ddTHH:mm:ss.SSSZ)" → The code still uses ISODateTimeFormat to format the date time, which produces ISO8601 format. YES

Brief conclusion: The summary still accurately describes what the method does after the code change.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: toString() -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [48/77] `Summary_108`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Evaluate a PLAIN login challenge, returning the a result string that should satisfy the clallenge.` |
| ground_truth_comment | `Evaluate a PLAIN login challenge, returning the a result string that should satisfy the challenge.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: evaluateChallenge(byte[] challenge) -> byte[] throws MessagingException
Parameters Details: [{"name": "challenge", "type": "byte[]"}]
intention:      Method 'evaluateChallenge' (evaluate Challenge)
implementation: Return paths: 1, throws: MessagingException
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Evaluate a PLAIN login challenge, returning the a result string that should satisfy the clallenge.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: evaluateChallenge(byte[] challenge) -> byte[] throws MessagingException
Parameters Details: [{"name": "challenge", "type": "byte[]"}]
- Intent: Method 'evaluateChallenge' (evaluate Challenge)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Evaluate a PLAIN login challenge" → The method still evaluates a login challenge, though the implementation has changed. YES
- SUBJECT: "returning a result string that should satisfy the challenge" → The method still returns a result string (converted to bytes) that satisfies the challenge. YES
- QUALIFIERS: "PLAIN" → The method still handles a PLAIN authentication challenge (username/password with optional authzid). YES

Brief conclusion: The summary still accurately describes what the method does, despite the implementation change.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: evaluateChallenge(byte[] challenge) -> byte[] throws MessagingException
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [49/77] `Summary_109`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Gets the given  start and  end view positions offset to a header.` |
| ground_truth_comment | `Gets the given  start and  end view positions offset to a header.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static int[] getViewToHeaderPosition(JTextArea view, int start, int end) {
        validateView(view);
        validateStartEnd(start, end, view.getDocument().getLength());
        return getViewToHeaderPositionImpl(view, start, end);
    }
```

**code_snippet**

```java
public static int[] getViewToHeaderPosition(JTextArea view, int start, int end) {
        validateView(view);
        validateStartEnd(start, end);

        if (!isValidStartEndForLength(start, end, view.getDocument().getLength())) {
            return INVALID_POSITION;
        }

        return getViewToHeaderPositionImpl(view, start, end);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getViewToHeaderPosition(JTextArea view, int start, int end) -> int[]
Parameters Details: [{"name": "view", "type": "JTextArea"}, {"name": "start", "type": "int"}, {"name": "end", "type": "int"}]
intention:      Method 'getViewToHeaderPosition' (get View To Header Position)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Gets the given  start and  end view positions offset to a header.

[Current Code]
    public static int[] getViewToHeaderPosition(JTextArea view, int start, int end) {
        validateView(view);
        validateStartEnd(start, end);

        if (!isValidStartEndForLength(start, end, view.getDocument().getLength())) {
            return INVALID_POSITION;
        }

        return getViewToHeaderPositionImpl(view, start, end);
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,5 +1,10 @@
 public static int[] getViewToHeaderPosition(JTextArea view, int start, int end) {

         validateView(view);

-        validateStartEnd(start, end, view.getDocument().getLength());

+        validateStartEnd(start, end);

+

+        if (!isValidStartEndForLength(start, end, view.getDocument().getLength())) {

+            return INVALID_POSITION;

+        }

+

         return getViewToHeaderPositionImpl(view, start, end);

     }
```

[Code Context]
- Signature: Full Signature: getViewToHeaderPosition(JTextArea view, int start, int end) -> int[]
Parameters Details: [{"name": "view", "type": "JTextArea"}, {"name": "start", "type": "int"}, {"name": "end", "type": "int"}]
- Intent: Method 'getViewToHeaderPosition' (get View To Header Position)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Gets the given start and end view positions offset to a header" → The method still gets view positions and returns them, but now with additional validation. The core action remains.
- SUBJECT: "start and end view positions" → The method still operates on start and end positions as parameters.
- QUALIFIERS: "offset to a header" → This qualifier is still accurate as the method name and purpose remain the same.

The summary still accurately describes the method's purpose, even though the implementation has been enhanced with additional validation logic. The core functionality of getting view positions offset to a header remains unchanged.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getViewToHeaderPosition(JTextArea view, int start, int end) -> int[]
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [50/77] `Summary_115`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `This method initializes tableAuth` |
| ground_truth_comment | `This method initializes tableAuth` |

### Step 0 · 原始数据

**old_code_snippet**

```java
private JTable getTableExtension() {
		if (tableExt == null) {
			tableExt = new JTable();
			tableExt.setModel(getExtensionModel());
			tableExt.setRowHeight(DisplayUtils.getScaledSize(18));
			tableExt.getColumnModel().getColumn(0).setPreferredWidth(DisplayUtils.getScaledSize(70));
			tableExt.getColumnModel().getColumn(1).setPreferredWidth(DisplayUtils.getScaledSize(70));
			tableExt.getColumnModel().getColumn(2).setPreferredWidth(DisplayUtils.getScaledSize(120));
			tableExt.getColumnModel().getColumn(3).setPreferredWidth(DisplayUtils.getScaledSize(220));
			
			ListSelectionListener sl = new ListSelectionListener() {

				@Override
				public void valueChanged(ListSelectionEvent arg0) {
	        		if (tableExt.getSelectedRow() > -1) {
	        			Extension ext = ((OptionsExtensionTableModel)tableExt.getModel()).getExtension(
	        					tableExt.getSelectedRow());
	        			if (ext != null) {
	        				try {
								extName.setText(ext.getUIName());
								boolean addOnExtension = ext.getAddOn() != null;
								addOnNameLabel.setVisible(addOnExtension);
								addOnName.setVisible(addOnExtension);
								addOnName.setText(addOnExtension ? ext.getAddOn().getName() : "");
								extDescription.setText(ext.getDescription());
								if (ext.getAuthor() != null) {
									extAuthor.setText(ext.getAuthor());
								} else {
									extAuthor.setText("");
								}
								if (ext.getURL() != null) {
									extURL.setText(ext.getURL().toString());
									getUrlLaunchButton().setEnabled(true);
								} else {
									extURL.setText("");
									getUrlLaunchButton().setEnabled(false);
								}
							} catch (Exception e) {
								// Just to be safe
								log.error(e.getMessage(), e);
							}
	        			}
	        		}
				}};
			
			tableExt.getSelectionModel().addListSelectionListener(sl);
			tableExt.getColumnModel().getSelectionModel().addListSelectionListener(sl);
			
		}
		return tableExt;
	}
```

**code_snippet**

```java
private JXTable getTableExtension() {
		if (tableExt == null) {
			tableExt = new JXTable();
			tableExt.setModel(getExtensionModel());
			tableExt.setRowHeight(DisplayUtils.getScaledSize(18));
			tableExt.getColumnModel().getColumn(0).setPreferredWidth(DisplayUtils.getScaledSize(70));
			tableExt.getColumnModel().getColumn(1).setPreferredWidth(DisplayUtils.getScaledSize(70));
			tableExt.getColumnModel().getColumn(2).setPreferredWidth(DisplayUtils.getScaledSize(120));
			tableExt.getColumnModel().getColumn(3).setPreferredWidth(DisplayUtils.getScaledSize(220));
			tableExt.setSortOrder(3, SortOrder.ASCENDING);
			
			ListSelectionListener sl = new ListSelectionListener() {

				@Override
				public void valueChanged(ListSelectionEvent arg0) {
	        		int selectedRow = tableExt.getSelectedRow();
	        		if (selectedRow > -1) {
	        			Extension ext = getExtensionModel().getExtension(tableExt.convertRowIndexToModel(selectedRow));
	        			if (ext != null) {
	        				try {
								extName.setText(ext.getUIName());
								extDescription.setText(ext.getDescription());
								if (ext.getAuthor() != null) {
									extAuthor.setText(ext.getAuthor());
								} else {
									extAuthor.setText("");
								}
								if (ext.getURL() != null) {
									extURL.setText(ext.getURL().toString());
									getUrlLaunchButton().setEnabled(true);
								} else {
									extURL.setText("");
									getUrlLaunchButton().setEnabled(false);
								}
							} catch (Exception e) {
								// Just to be safe
								log.error(e.getMessage(), e);
							}
	        			}
	        		}
				}};
			
			tableExt.getSelectionModel().addListSelectionListener(sl);
			tableExt.setColumnControlVisible(true);
		}
		return tableExt;
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getTableExtension() -> JXTable
Parameters Details: []
intention:      Method 'getTableExtension' (get Table Extension)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'JTable' -> 'JXTable'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
This method initializes tableAuth

[Current Code]
	private JXTable getTableExtension() {
		if (tableExt == null) {
			tableExt = new JXTable();
			tableExt.setModel(getExtensionModel());
			tableExt.setRowHeight(DisplayUtils.getScaledSize(18));
			tableExt.getColumnModel().getColumn(0).setPreferredWidth(DisplayUtils.getScaledSize(70));
			tableExt.getColumnModel().getColumn(1).setPreferredWidth(DisplayUtils.getScaledSize(70));
			tableExt.getColumnModel().getColumn(2).setPreferredWidth(DisplayUtils.getScaledSize(120));
			tableExt.getColumnModel().getColumn(3).setPreferredWidth(DisplayUtils.getScaledSize(220));
			tableExt.setSortOrder(3, SortOrder.ASCENDING);
			
			ListSelectionListener sl = new ListSelectionListener() {

				@Override
				public void valueChanged(ListSelectionEvent arg0) {
	        		int selectedRow = tableExt.getSelectedRow();
	        		if (selectedRow > -1) {
	        			Extension ext = getExtensionModel().getExtension(tableExt.convertRowIndexToModel(selectedRow));
	        			if (ext != null) {
	        				try {
								extName.setText(ext.getUIName());
								extDescription.setText(ext.getDescription());
								if (ext.getAuthor() != null) {
									extAuthor.setText(ext.getAuthor());
								} else {
									extAuthor.setText("");
								}
								if (ext.getURL() != null) {
									extURL.setText(ext.getURL().toString());
									getUrlLaunchButton().setEnabled(true);
								} else {
									extURL.setText("");
									getUrlLaunchButton().setEnabled(false);
								}
							} catch (Exception e) {
								// Just to be safe
								log.error(e.getMessage(), e);
							}
	        			}
	        		}
				}};
			
			tableExt.getSelectionModel().addListSelectionListener(sl);
			tableExt.setColumnControlVisible(true);
		}
		return tableExt;
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,27 +1,24 @@
-private JTable getTableExtension() {

+private JXTable getTableExtension() {

 		if (tableExt == null) {

-			tableExt = new JTable();

+			tableExt = new JXTable();

 			tableExt.setModel(getExtensionModel());

 			tableExt.setRowHeight(DisplayUtils.getScaledSize(18));

 			tableExt.getColumnModel().getColumn(0).setPreferredWidth(DisplayUtils.getScaledSize(70));

 			tableExt.getColumnModel().getColumn(1).setPreferredWidth(DisplayUtils.getScaledSize(70));

 			tableExt.getColumnModel().getColumn(2).setPreferredWidth(DisplayUtils.getScaledSize(120));

 			tableExt.getColumnModel().getColumn(3).setPreferredWidth(DisplayUtils.getScaledSize(220));

+			tableExt.setSortOrder(3, SortOrder.ASCENDING);

 			

 			ListSelectionListener sl = new ListSelectionListener() {

 

 				@Override

 				public void valueChanged(ListSelectionEvent arg0) {

-	        		if (tableExt.getSelectedRow() > -1) {

-	        			Extension ext = ((OptionsExtensionTableModel)tableExt.getModel()).getExtension(

-	        					tableExt.getSelectedRow());

+	        		int selectedRow = tableExt.getSelectedRow();

+	        		if (selectedRow > -1) {

+	        			Extension ext = getExtensionModel().getExtension(tableExt.convertRowIndexToModel(selectedRow));

 	        			if (ext != null) {

 	        				try {

 								extName.setText(ext.getUIName());

-								boolean addOnExtension = ext.getAddOn() != null;

-								addOnNameLabel.setVisible(addOnExtension);

-								addOnName.setVisible(addOnExtension);

-								addOnName.setText(addOnExtension ? ext.getAddOn().getName() : "");

 								extDescription.setText(ext.getDescription());

 								if (ext.getAuthor() != null) {

 									extAuthor.setText(ext.getAuthor());

@@ -44,8 +41,7 @@
 				}};

 			

 			tableExt.getSelectionModel().addListSelectionListener(sl);

-			tableExt.getColumnModel().getSelectionModel().addListSelectionListener(sl);

-			

+			tableExt.setColumnControlVisible(true);

 		}

 		return tableExt;

 	}
```

[Code Context]
- Signature: Full Signature: getTableExtension() -> JXTable
Parameters Details: []
- Intent: Method 'getTableExtension' (get Table Extension)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'JTable' -> 'JXTable'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "initializes" → The method still initializes a table object (now JXTable instead of JTable). YES
- SUBJECT: "tableAuth" → The method now initializes "tableExt" (not "tableAuth"). The subject has changed. NO
- QUALIFIERS: None specified in the comment. N/A

The comment mentions "tableAuth" but the code now initializes "tableExt". This is a clear subject/object change that makes the comment inconsistent with the current code.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getTableExtension() -> JXTable
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "initializes" → The method still initializes a table object (now JXTable instea...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [51/77] `Summary_118`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Removes the content source from this channel, if it exists.` |
| ground_truth_comment | `Removes the content source from this repo, if it exists.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: removeContentSource(ContentSource contentSource) -> RepoContentSource
Parameters Details: [{"name": "contentSource", "type": "ContentSource"}]
intention:      Method 'removeContentSource' (remove Content Source)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'ChannelContentSource' -> 'RepoContentSource'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Removes the content source from this channel, if it exists.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: removeContentSource(ContentSource contentSource) -> RepoContentSource
Parameters Details: [{"name": "contentSource", "type": "ContentSource"}]
- Intent: Method 'removeContentSource' (remove Content Source)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'ChannelContentSource' -> 'RepoContentSource'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Removes" → still done by the code? YES. The method still removes an element from a collection.
- SUBJECT: "the content source" → still this same thing? YES. The method still operates on a ContentSource object passed as parameter.
- QUALIFIERS: "from this channel, if it exists" → still all true? PARTIALLY. The method still checks if the content source exists before removal, but it's now removing from "repoContentSources" instead of "channelContentSources". The subject of the removal has changed from "channel" to "repo".
- Brief conclusion: The summary is no longer accurate because the method now removes from "repoContentSources" rather than "channelContentSources", and the return type has changed from ChannelContentSource to RepoContentSource.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: removeContentSource(ContentSource contentSource) -> RepoContentSource
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Removes" → still done by the code? YES. The method still removes an element fr...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [52/77] `Summary_119`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns whether an instance of Chrome is currently connected` |
| ground_truth_comment | `Returns whether an instance of Chrome is currently connected` |

### Step 0 · 原始数据

**old_code_snippet**

```java
boolean hasClient() {
    return listeningThread != null && listeningThread.hasClient;
  }
```

**code_snippet**

```java
boolean hasClient() {
    return listeningThread != null && listeningThread.hasClient && !listeningThread.sockets.isEmpty();
  }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: hasClient() -> boolean
Parameters Details: []
intention:      Method 'hasClient' (has Client)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns whether an instance of Chrome is currently connected

[Current Code]
  boolean hasClient() {
    return listeningThread != null && listeningThread.hasClient && !listeningThread.sockets.isEmpty();
  }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 boolean hasClient() {

-    return listeningThread != null && listeningThread.hasClient;

+    return listeningThread != null && listeningThread.hasClient && !listeningThread.sockets.isEmpty();

   }
```

[Code Context]
- Signature: Full Signature: hasClient() -> boolean
Parameters Details: []
- Intent: Method 'hasClient' (has Client)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a boolean value)
- SUBJECT: "whether an instance of Chrome is currently connected" → still this same thing? NO (the method now also checks if sockets is empty, which is a new condition not mentioned in the original comment)
- QUALIFIERS: "currently connected" → still all true? PARTIALLY (the method still checks if a client is connected, but now with an additional condition about sockets being empty)

Brief conclusion: The original comment is incomplete as it doesn't mention the new condition about checking if sockets is empty, making it inconsistent with the current implementation.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: hasClient() -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a boolean val...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [53/77] `Summary_121`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Creates a new UserFolder, inflated from R.layout.user_folder.` |
| ground_truth_comment | `Creates a new UserFolder, inflated from R.layout.user_folder.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
static Folder fromXml(Launcher launcher) {
        return (Folder) launcher.getLayoutInflater().inflate(
                FeatureFlags.LAUNCHER3_DISABLE_ICON_NORMALIZATION
                        ? R.layout.user_folder : R.layout.user_folder_icon_normalized, null);
    }
```

**code_snippet**

```java
static Folder fromXml(Launcher launcher) {
        return (Folder) launcher.getLayoutInflater()
                .inflate(R.layout.user_folder_icon_normalized, null);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: fromXml(Launcher launcher) -> Folder
Parameters Details: [{"name": "launcher", "type": "Launcher"}]
intention:      Method 'fromXml' (from Xml)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'user_folder' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Creates a new UserFolder, inflated from R.layout.user_folder.

[Current Code]
    static Folder fromXml(Launcher launcher) {
        return (Folder) launcher.getLayoutInflater()
                .inflate(R.layout.user_folder_icon_normalized, null);
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,5 +1,4 @@
 static Folder fromXml(Launcher launcher) {

-        return (Folder) launcher.getLayoutInflater().inflate(

-                FeatureFlags.LAUNCHER3_DISABLE_ICON_NORMALIZATION

-                        ? R.layout.user_folder : R.layout.user_folder_icon_normalized, null);

+        return (Folder) launcher.getLayoutInflater()

+                .inflate(R.layout.user_folder_icon_normalized, null);

     }
```

[Code Context]
- Signature: Full Signature: fromXml(Launcher launcher) -> Folder
Parameters Details: [{"name": "launcher", "type": "Launcher"}]
- Intent: Method 'fromXml' (from Xml)

[Rule-based Signals — HIGH PRIORITY]
- IDENTIFIER DRIFT: comment mentions 'user_folder' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Creates a new UserFolder" → NO, the code inflates a layout and casts it to Folder, but doesn't explicitly create a new UserFolder
- SUBJECT: "UserFolder" → NO, the code now works with a generic Folder object, not specifically a UserFolder
- QUALIFIERS: "inflated from R.layout.user_folder" → NO, the code now inflates from R.layout.user_folder_icon_normalized, not R.layout.user_folder

Brief conclusion: The original comment is inconsistent because it mentions creating a UserFolder (while code now creates a generic Folder) and inflating from a different layout than what's actually used.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: fromXml(Launcher launcher) -> Folder
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Creates a new UserFolder" → NO, the code inflates a layout and casts it to Fol...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [54/77] `Summary_124`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `First authenticates the AuthenticationToken argument, and if successful, constructs a SecurityContext instance representing the authenticated account's identity.` |
| ground_truth_comment | `First authenticates the AuthenticationToken argument, and if successful, constructs a Subject instance representing the authenticated account's identity.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: login(AuthenticationToken token) -> Subject throws AuthenticationException
Parameters Details: [{"name": "token", "type": "AuthenticationToken"}]
intention:      Method 'login' (login)
implementation: Return paths: 1, throws: AuthenticationException
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'SecurityContext' -> 'Subject'. If the comment references the old return type, it is INCONSISTENT.", "IDENTIFIER DRIFT: comment mentions 'SecurityContext' which no longer exists in new code. Possible renames: ['Subject']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
First authenticates the AuthenticationToken argument, and if successful, constructs a SecurityContext instance representing the authenticated account's identity.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: login(AuthenticationToken token) -> Subject throws AuthenticationException
Parameters Details: [{"name": "token", "type": "AuthenticationToken"}]
- Intent: Method 'login' (login)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'SecurityContext' -> 'Subject'. If the comment references the old return type, it is INCONSISTENT.
- IDENTIFIER DRIFT: comment mentions 'SecurityContext' which no longer exists in new code. Possible renames: ['Subject'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "First authenticates the AuthenticationToken argument, and if successful, constructs a SecurityContext instance representing the authenticated account's identity" → The authentication part is still done, but the construction part now creates a Subject instead of a SecurityContext.
- SUBJECT: The method now returns a Subject instead of a SecurityContext.
- QUALIFIERS: The qualifier "representing the authenticated account's identity" still holds, but the type has changed from SecurityContext to Subject.

The comment mentions "SecurityContext" which is no longer the return type of the method. The method now returns a "Subject" instead. This is a significant structural change that affects the core description of what the method returns.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: login(AuthenticationToken token) -> Subject throws AuthenticationException
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "First authenticates the AuthenticationToken argument, and if successful, const...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [55/77] `Summary_126`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Make fully qualified URI based on the default file system Scheme and Authority` |
| ground_truth_comment | `Make fully qualified URI if Scheme and/or Authority is missing, based on the default file system Scheme and Authority.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: makeFullQualifiedURI(String uriName) -> URI throws IOException
Parameters Details: [{"name": "uriName", "type": "String"}]
intention:      Method 'makeFullQualifiedURI' (make Full Qualified URI)
implementation: Return paths: 2, throws: IOException
```

### Step 2 · 规则信号

```text
rule_signals    = ["THROWS CHANGED: {'IOException', 'URISyntaxException'} -> {'IOException'}."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Make fully qualified URI based on the default file system Scheme and Authority

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: makeFullQualifiedURI(String uriName) -> URI throws IOException
Parameters Details: [{"name": "uriName", "type": "String"}]
- Intent: Method 'makeFullQualifiedURI' (make Full Qualified URI)

[Rule-based Signals — HIGH PRIORITY]
- THROWS CHANGED: {'IOException', 'URISyntaxException'} -> {'IOException'}.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Make fully qualified URI" → The method still creates a fully qualified URI from a string input. YES
- SUBJECT: "URI based on the default file system Scheme and Authority" → The method still creates a URI using the default file system's scheme and authority when they're missing. YES
- QUALIFIERS: "fully qualified" → The method now has additional validation to ensure the URI is normalized and has an absolute path before making it fully qualified. The qualifier "fully qualified" still applies to the output URI. YES
- The method now has additional logic to handle relative URI paths by returning null, but this doesn't contradict the original summary about making a fully qualified URI.

Brief conclusion: The summary still accurately describes the method's primary functionality of creating a fully qualified URI using the default file system's scheme and authority.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: makeFullQualifiedURI(String uriName) -> URI throws IOException
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [56/77] `Summary_130`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Build a DruidDimensionsLoader.` |
| ground_truth_comment | `Build a DimensionValueLoadTask.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: buildDruidDimensionsLoader(DruidWebService webService, PhysicalTableDictionary physicalTableDictionary, DimensionDictionary dimensionDictionary) -> DimensionValueLoadTask
Parameters Details: [{"name": "webService", "type": "DruidWebService"}, {"name": "physicalTableDictionary", "type": "PhysicalTableDictionary"}, {"name": "dimensionDictionary", "type": "DimensionDictionary"}]
intention:      Method 'buildDruidDimensionsLoader' (build Druid Dimensions Loader)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'DruidDimensionsLoader' -> 'DimensionValueLoadTask'. If the comment references the old return type, it is INCONSISTENT.", "IDENTIFIER DRIFT: comment mentions 'DruidDimensionsLoader' which no longer exists in new code. Possible renames: ['DimensionValueLoadTask', 'DruidDimensionValueLoader', 'druidDimensionRowProvider']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Build a DruidDimensionsLoader.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: buildDruidDimensionsLoader(DruidWebService webService, PhysicalTableDictionary physicalTableDictionary, DimensionDictionary dimensionDictionary) -> DimensionValueLoadTask
Parameters Details: [{"name": "webService", "type": "DruidWebService"}, {"name": "physicalTableDictionary", "type": "PhysicalTableDictionary"}, {"name": "dimensionDictionary", "type": "DimensionDictionary"}]
- Intent: Method 'buildDruidDimensionsLoader' (build Druid Dimensions Loader)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'DruidDimensionsLoader' -> 'DimensionValueLoadTask'. If the comment references the old return type, it is INCONSISTENT.
- IDENTIFIER DRIFT: comment mentions 'DruidDimensionsLoader' which no longer exists in new code. Possible renames: ['DimensionValueLoadTask', 'DruidDimensionValueLoader', 'druidDimensionRowProvider'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Build" → The method still builds something, but it's now building a DimensionValueLoadTask rather than a DruidDimensionsLoader. The action of building is still there, but the specific thing being built has changed.
- SUBJECT: "a DruidDimensionsLoader" → The method now returns a DimensionValueLoadTask, not a DruidDimensionsLoader. The subject has changed completely.
- QUALIFIERS: None specified in the summary.

The summary specifically mentions building a "DruidDimensionsLoader", but the method now returns a "DimensionValueLoadTask" and creates a "DruidDimensionValueLoader" as an intermediate step. The return type has changed, and the class name mentioned in the summary no longer exists in the code.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: buildDruidDimensionsLoader(DruidWebService webService, PhysicalTableDictionary p
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Build" → The method still builds something, but it's now building a DimensionV...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [57/77] `Summary_144`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Gets the element for the method corresponding to this invocation.` |
| ground_truth_comment | `Gets the element for the declaration corresponding to this use of an element.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static final ExecutableElement elementFromUse(MethodInvocationTree node) {
        return (ExecutableElement)TreeInfo.symbol((JCTree)node.getMethodSelect());
    }
```

**code_snippet**

```java
public static final Element elementFromUse(ExpressionTree node) {
        return InternalUtils.symbol(node);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: elementFromUse(ExpressionTree node) -> Element
Parameters Details: [{"name": "node", "type": "ExpressionTree"}]
intention:      Method 'elementFromUse' (element From Use)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'ExecutableElement' -> 'Element'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Gets the element for the method corresponding to this invocation.

[Current Code]
    public static final Element elementFromUse(ExpressionTree node) {
        return InternalUtils.symbol(node);
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: elementFromUse(ExpressionTree node) -> Element
Parameters Details: [{"name": "node", "type": "ExpressionTree"}]
- Intent: Method 'elementFromUse' (element From Use)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'ExecutableElement' -> 'Element'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Gets" → The method still retrieves something, so this matches.
- SUBJECT: "the element for the method" → The method now returns a generic Element rather than specifically an ExecutableElement, which is a change in the type of element being returned.
- QUALIFIERS: "corresponding to this invocation" → The method now takes an ExpressionTree instead of a MethodInvocationTree, so the specific type of invocation has changed.

The comment suggests the method gets an ExecutableElement from a method invocation, but the current code gets a generic Element from any ExpressionTree. The return type has changed from ExecutableElement to Element, and the parameter type has changed from MethodInvocationTree to ExpressionTree. These changes make the comment inconsistent with the current implementation.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: elementFromUse(ExpressionTree node) -> Element
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Gets" → The method still retrieves something, so this matches.
- SUBJECT: "the...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [58/77] `Summary_147`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Get a  Struct representation of the source  #partition(String) partition and  #lastOffset(String) offset information.` |
| ground_truth_comment | `Get a  Struct representation of the source  #partition(String) partition and  #lastOffset(String) offset information.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public Struct offsetStructForEvent(String replicaSetName, Document oplogEvent) {
        Position position = INITIAL_POSITION;
        String namespace = "";
        if (oplogEvent != null) {
            BsonTimestamp ts = extractEventTimestamp(oplogEvent);
            Long opId = oplogEvent.getLong("h");
            position = new Position(ts, opId);
            namespace = oplogEvent.getString("ns");
        }
        positionsByReplicaSetName.put(replicaSetName, position);
        return offsetStructFor(replicaSetName, namespace, position, isInitialSyncOngoing(replicaSetName));
    }
```

**code_snippet**

```java
public Struct offsetStructForEvent(String replicaSetName, Document oplogEvent) {
        Position position = INITIAL_POSITION;
        String namespace = "";
        if (oplogEvent != null) {
            BsonTimestamp ts = extractEventTimestamp(oplogEvent);
            Long opId = oplogEvent.getLong("h");
            position = new Position(ts, opId);
            namespace = oplogEvent.getString("ns");
        }
        positionsByReplicaSetName.put(replicaSetName, position);
        return offsetStructFor(replicaSetName, CollectionId.parse(replicaSetName + "." + namespace), position, isInitialSyncOngoing(replicaSetName));
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: offsetStructForEvent(String replicaSetName, Document oplogEvent) -> Struct
Parameters Details: [{"name": "replicaSetName", "type": "String"}, {"name": "oplogEvent", "type": "Document"}]
intention:      Method 'offsetStructForEvent' (offset Struct For Event)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Get a  Struct representation of the source  #partition(String) partition and  #lastOffset(String) offset information.

[Current Code]
    public Struct offsetStructForEvent(String replicaSetName, Document oplogEvent) {
        Position position = INITIAL_POSITION;
        String namespace = "";
        if (oplogEvent != null) {
            BsonTimestamp ts = extractEventTimestamp(oplogEvent);
            Long opId = oplogEvent.getLong("h");
            position = new Position(ts, opId);
            namespace = oplogEvent.getString("ns");
        }
        positionsByReplicaSetName.put(replicaSetName, position);
        return offsetStructFor(replicaSetName, CollectionId.parse(replicaSetName + "." + namespace), position, isInitialSyncOngoing(replicaSetName));
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -8,5 +8,5 @@
             namespace = oplogEvent.getString("ns");

         }

         positionsByReplicaSetName.put(replicaSetName, position);

-        return offsetStructFor(replicaSetName, namespace, position, isInitialSyncOngoing(replicaSetName));

+        return offsetStructFor(replicaSetName, CollectionId.parse(replicaSetName + "." + namespace), position, isInitialSyncOngoing(replicaSetName));

     }
```

[Code Context]
- Signature: Full Signature: offsetStructForEvent(String replicaSetName, Document oplogEvent) -> Struct
Parameters Details: [{"name": "replicaSetName", "type": "String"}, {"name": "oplogEvent", "type": "Document"}]
- Intent: Method 'offsetStructForEvent' (offset Struct For Event)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Get a Struct representation" → The method still returns a Struct, so this is YES.
- SUBJECT: "of the source #partition(String) partition and #lastOffset(String) offset information" → The method still deals with partition and offset information, but the way it handles the partition has changed. It now uses CollectionId.parse(replicaSetName + "." + namespace) instead of just the namespace.
- QUALIFIERS: None explicitly mentioned in the summary.

The key change is that the method now uses CollectionId.parse() to create a more complex partition identifier rather than using the namespace directly. This is a significant change in how the partition information is handled, even though the high-level purpose remains similar.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: offsetStructForEvent(String replicaSetName, Document oplogEvent) -> Struct
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Get a Struct representation" → The method still returns a Struct, so this is Y...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [59/77] `Summary_149`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `When initializing the profile, Opera rapidly starts, stops, restarts and stops again; we need to wait a bit to make sure the file lock is really gone.` |
| ground_truth_comment | `When initializing the profile, Opera rapidly starts, stops, restarts and stops again; we need to wait a bit to make sure the file lock is really gone.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
private boolean makeSureFileLockRemainsGone(File lock, long timeToWait) {
        for (long start = System.currentTimeMillis(); System.currentTimeMillis() < start + timeToWait;) {
            AsyncExecute.sleepTight(500);
            if (lock.exists()) return false;
        }
        if (!lock.exists()) return true;
        return false;
    }
```

**code_snippet**

```java
private boolean makeSureFileLockRemainsGone(File lock, long timeToWait) {
        for (long start = System.currentTimeMillis(); System.currentTimeMillis() < start + timeToWait;) {
            AsyncExecute.sleepTight(500);
            if (lock.exists()) return false;
        }
        return !lock.exists();
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: makeSureFileLockRemainsGone(File lock, long timeToWait) -> boolean
Parameters Details: [{"name": "lock", "type": "File"}, {"name": "timeToWait", "type": "long"}]
intention:      Method 'makeSureFileLockRemainsGone' (make Sure File Lock Remains Gone)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
When initializing the profile, Opera rapidly starts, stops, restarts and stops again; we need to wait a bit to make sure the file lock is really gone.

[Current Code]
    private boolean makeSureFileLockRemainsGone(File lock, long timeToWait) {
        for (long start = System.currentTimeMillis(); System.currentTimeMillis() < start + timeToWait;) {
            AsyncExecute.sleepTight(500);
            if (lock.exists()) return false;
        }
        return !lock.exists();
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -3,6 +3,5 @@
             AsyncExecute.sleepTight(500);

             if (lock.exists()) return false;

         }

-        if (!lock.exists()) return true;

-        return false;

+        return !lock.exists();

     }
```

[Code Context]
- Signature: Full Signature: makeSureFileLockRemainsGone(File lock, long timeToWait) -> boolean
Parameters Details: [{"name": "lock", "type": "File"}, {"name": "timeToWait", "type": "long"}]
- Intent: Method 'makeSureFileLockRemainsGone' (make Sure File Lock Remains Gone)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "we need to wait a bit to make sure the file lock is really gone" → The code still waits in a loop with sleepTight(500) and checks if the lock file exists. YES
- SUBJECT: "file lock" → The method still operates on a File lock object. YES
- QUALIFIERS: "When initializing the profile, Opera rapidly starts, stops, restarts and stops again" → This is context about why the method is needed, but isn't directly reflected in the code. However, the core functionality of waiting and checking remains. YES
- The code change simplified the return logic but didn't change the fundamental behavior of waiting and checking.

Brief conclusion: The summary still accurately describes what the method does despite the implementation simplification.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: makeSureFileLockRemainsGone(File lock, long timeToWait) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [60/77] `Summary_152`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Creates a  UserAdapter if there is more than one profile on the device.` |
| ground_truth_comment | `Creates a  UserSpinnerAdapter if there is more than one profile on the device.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: createUserSpinnerAdapter(UserManager userManager, Context context) -> UserSpinnerAdapter
Parameters Details: [{"name": "userManager", "type": "UserManager"}, {"name": "context", "type": "Context"}]
intention:      Method 'createUserSpinnerAdapter' (create User Spinner Adapter)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'UserAdapter' -> 'UserSpinnerAdapter'. If the comment references the old return type, it is INCONSISTENT.", "IDENTIFIER DRIFT: comment mentions 'UserAdapter' which no longer exists in new code. Possible renames: ['userDetails', 'UserDetails', 'UserSpinnerAdapter']."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Creates a  UserAdapter if there is more than one profile on the device.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: createUserSpinnerAdapter(UserManager userManager, Context context) -> UserSpinnerAdapter
Parameters Details: [{"name": "userManager", "type": "UserManager"}, {"name": "context", "type": "Context"}]
- Intent: Method 'createUserSpinnerAdapter' (create User Spinner Adapter)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'UserAdapter' -> 'UserSpinnerAdapter'. If the comment references the old return type, it is INCONSISTENT.
- IDENTIFIER DRIFT: comment mentions 'UserAdapter' which no longer exists in new code. Possible renames: ['userDetails', 'UserDetails', 'UserSpinnerAdapter'].
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Creates a UserAdapter" → NO, the code now creates a UserSpinnerAdapter
- SUBJECT: "UserAdapter" → NO, the method now returns a UserSpinnerAdapter, not a UserAdapter
- QUALIFIERS: "if there is more than one profile on the device" → YES, this condition is still checked with `if (userProfiles.size() < 2)`

The comment mentions creating a "UserAdapter" but the code now creates a "UserSpinnerAdapter". This is a clear change in the return type and the object being created. The core condition about multiple profiles remains, but the subject of the creation has changed.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: createUserSpinnerAdapter(UserManager userManager, Context context) -> UserSpinne
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Creates a UserAdapter" → NO, the code now creates a UserSpinnerAdapter
- SUBJE...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [61/77] `Summary_153`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `An expectation for checking child WebElement as a part of parent element to be visible` |
| ground_truth_comment | `An expectation for checking child WebElement as a part of parent element to be visible` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public List<WebElement> apply(WebDriver webDriver) {
        Boolean displayed = false;
        Boolean exists = false;
        try {
          exists =
            element.findElements(sub_locator).size()
            > 0; //duplicating search is to avoid dom rebuilding problems
          displayed = element.findElement(sub_locator).isDisplayed();
        } catch (Exception e) {/**/}
        return (exists && displayed) ? element.findElements(sub_locator) : null;
      }
```

**code_snippet**

```java
public List<WebElement> apply(WebDriver webDriver) {
        Boolean displayed = false;
        Boolean exists = false;
        try {
          exists =
            findElements(sub_locator, webDriver).size() > 0;
          //duplicating search is to avoid dom rebuilding problems
          displayed = findElement(sub_locator, webDriver).isDisplayed();
        } catch (Exception e) {/**/}
        return (exists && displayed) ? findElements(sub_locator, webDriver) : null;
      }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: apply(WebDriver webDriver) -> List<WebElement>
Parameters Details: [{"name": "webDriver", "type": "WebDriver"}]
intention:      Method 'apply' (apply)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'element' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
An expectation for checking child WebElement as a part of parent element to be visible

[Current Code]
      public List<WebElement> apply(WebDriver webDriver) {
        Boolean displayed = false;
        Boolean exists = false;
        try {
          exists =
            findElements(sub_locator, webDriver).size() > 0;
          //duplicating search is to avoid dom rebuilding problems
          displayed = findElement(sub_locator, webDriver).isDisplayed();
        } catch (Exception e) {/**/}
        return (exists && displayed) ? findElements(sub_locator, webDriver) : null;
      }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -3,9 +3,9 @@
         Boolean exists = false;

         try {

           exists =

-            element.findElements(sub_locator).size()

-            > 0; //duplicating search is to avoid dom rebuilding problems

-          displayed = element.findElement(sub_locator).isDisplayed();

+            findElements(sub_locator, webDriver).size() > 0;

+          //duplicating search is to avoid dom rebuilding problems

+          displayed = findElement(sub_locator, webDriver).isDisplayed();

         } catch (Exception e) {/**/}

-        return (exists && displayed) ? element.findElements(sub_locator) : null;

+        return (exists && displayed) ? findElements(sub_locator, webDriver) : null;

       }
```

[Code Context]
- Signature: Full Signature: apply(WebDriver webDriver) -> List<WebElement>
Parameters Details: [{"name": "webDriver", "type": "WebDriver"}]
- Intent: Method 'apply' (apply)

[Rule-based Signals — HIGH PRIORITY]
- IDENTIFIER DRIFT: comment mentions 'element' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "An expectation for checking" → The code still performs a check by verifying both existence and display status of elements. YES
- SUBJECT: "child WebElement as a part of parent element" → The code now uses findElements and findElement with a webDriver parameter instead of an element parameter, but it's still checking child elements based on a sub_locator. The subject is still essentially the same. YES
- QUALIFIERS: "to be visible" → The code still checks if the element is displayed using isDisplayed(). YES

However, there's a significant structural change indicated by the IDENTIFIER DRIFT signal. The original comment mentions "element" which no longer exists in the new code. The method now takes a WebDriver parameter instead of working with a parent element. This changes the fundamental relationship between the parent and child elements being checked.

Brief conclusion: While the core action of checking visibility remains, the structural change from working with a parent element to using a WebDriver parameter makes the comment's description of the relationship between elements inaccurate.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: apply(WebDriver webDriver) -> List<WebElement>
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "An expectation for checking" → The code still performs a check by verifying bo...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [62/77] `Summary_164`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Invoke the proprietary  CometSupport` |
| ground_truth_comment | `Invoke the proprietary  AsyncSupport` |

### Step 0 · 原始数据

**old_code_snippet**

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
            if (ex.getMessage() != null && (ex.getMessage().startsWith("Tomcat failed") || ex.getMessage().startsWith("JBoss failed") )) {
                if (!isFilter) {
                    logger.warn("Failed using comet support: {}, error: {} Is the Nio or Apr Connector enabled?", cometSupport.getClass().getName(),
                            ex.getMessage());
                    logger.warn("Using BlockingIOCometSupport.");
                }
                logger.trace(ex.getMessage(), ex);

                cometSupport = new BlockingIOCometSupport(config);
                doCometSupport(req, res);
            } else {
                logger.error("AtmosphereServlet exception", ex);
                throw ex;
            }
        } finally {
            if (req != null && a != null && a.type != Action.TYPE.SUSPEND) {
                req.destroy();
                res.destroy();
            }
        }
        return null;
    }
```

**code_snippet**

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
            if (ex.getMessage() != null && (ex.getMessage().startsWith("Tomcat failed") || ex.getMessage().startsWith("JBoss failed") )) {
                if (!isFilter) {
                    logger.warn("Failed using comet support: {}, error: {} Is the Nio or Apr Connector enabled?", asyncSupport.getClass().getName(),
                            ex.getMessage());
                    logger.warn("Using BlockingIOCometSupport.");
                }
                logger.trace(ex.getMessage(), ex);

                asyncSupport = new BlockingIOCometSupport(config);
                doCometSupport(req, res);
            } else {
                logger.error("AtmosphereServlet exception", ex);
                throw ex;
            }
        } finally {
            if (req != null && a != null && a.type != Action.TYPE.SUSPEND) {
                req.destroy();
                res.destroy();
            }
        }
        return null;
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: doCometSupport(AtmosphereRequest req, AtmosphereResponse res) -> Action throws IOException, ServletException
Parameters Details: [{"name": "req", "type": "AtmosphereRequest"}, {"name": "res", "type": "AtmosphereResponse"}]
intention:      Method 'doCometSupport' (do Comet Support)
implementation: Return paths: 2, throws: IOException, ServletException
```

### Step 2 · 规则信号

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'cometSupport' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Invoke the proprietary  CometSupport

[Current Code]
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
            if (ex.getMessage() != null && (ex.getMessage().startsWith("Tomcat failed") || ex.getMessage().startsWith("JBoss failed") )) {
                if (!isFilter) {
                    logger.warn("Failed using comet support: {}, error: {} Is the Nio or Apr Connector enabled?", asyncSupport.getClass().getName(),
                            ex.getMessage());
                    logger.warn("Using BlockingIOCometSupport.");
                }
                logger.trace(ex.getMessage(), ex);

                asyncSupport = new BlockingIOCometSupport(config);
                doCometSupport(req, res);
            } else {
                logger.error("AtmosphereServlet exception", ex);
                throw ex;
            }
        } finally {
            if (req != null && a != null && a.type != Action.TYPE.SUSPEND) {
                req.destroy();
                res.destroy();
            }
        }
        return null;
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: doCometSupport(AtmosphereRequest req, AtmosphereResponse res) -> Action throws IOException, ServletException
Parameters Details: [{"name": "req", "type": "AtmosphereRequest"}, {"name": "res", "type": "AtmosphereResponse"}]
- Intent: Method 'doCometSupport' (do Comet Support)

[Rule-based Signals — HIGH PRIORITY]
- IDENTIFIER DRIFT: comment mentions 'cometSupport' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Invoke the proprietary" → The method does invoke a service (asyncSupport.service), but it's not specifically described as "proprietary" in the code. This qualifier is questionable.
- SUBJECT: "CometSupport" → The code no longer uses a variable named "cometSupport". It has been replaced with "asyncSupport". This is a significant identifier drift.
- QUALIFIERS: None specified beyond "proprietary" which is questionable.

The comment mentions "CometSupport" which no longer exists in the new code - it has been replaced with "asyncSupport". This is a clear case of IDENTIFIER DRIFT which makes the comment inconsistent with the current code.

Brief conclusion: The original comment references a variable name that no longer exists in the code, making it inconsistent with the current implementation.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: doCometSupport(AtmosphereRequest req, AtmosphereResponse res) -> Action throws I
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Invoke the proprietary" → The method does invoke a service (asyncSupport.servi...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [63/77] `Summary_169`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns a DurationField representing seconds.` |
| ground_truth_comment | `Returns a DurationField representing seconds.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public DurationField seconds() {
        return UnsupportedDurationField.INSTANCE;
    }
```

**code_snippet**

```java
public DurationField seconds() {
        return UnsupportedDurationField.getInstance("seconds");
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: seconds() -> DurationField
Parameters Details: []
intention:      Method 'seconds' (seconds)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns a DurationField representing seconds.

[Current Code]
    public DurationField seconds() {
        return UnsupportedDurationField.getInstance("seconds");
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public DurationField seconds() {

-        return UnsupportedDurationField.INSTANCE;

+        return UnsupportedDurationField.getInstance("seconds");

     }
```

[Code Context]
- Signature: Full Signature: seconds() -> DurationField
Parameters Details: []
- Intent: Method 'seconds' (seconds)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES. The method still returns a value.
- SUBJECT: "a DurationField representing seconds" → still this same thing? NO. The method now returns an UnsupportedDurationField instance specifically for "seconds", not a general DurationField representing seconds.
- QUALIFIERS: None specified in the summary.
- Brief conclusion: The summary is inconsistent because it claims to return a general DurationField representing seconds, but the code now returns a specific UnsupportedDurationField instance for seconds.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: seconds() -> DurationField
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → still done by the code? YES. The method still returns a value.
- SU...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [64/77] `Summary_170`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Given a URL, attempt to infer and return the hostname from the URL.` |
| ground_truth_comment | `Given a URL, attempt to return the host portion (not including the port).` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getHostFromUrl(String url) -> String
Parameters Details: [{"name": "url", "type": "String"}]
intention:      Method 'getHostFromUrl' (get Host From Url)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Given a URL, attempt to infer and return the hostname from the URL.

[Current Code]
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


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getHostFromUrl(String url) -> String
Parameters Details: [{"name": "url", "type": "String"}]
- Intent: Method 'getHostFromUrl' (get Host From Url)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "attempt to infer and return" → The code still attempts to extract and return a hostname from a URL. YES
- SUBJECT: "hostname from the URL" → The code still extracts the hostname from the URL. YES
- QUALIFIERS: None specified in the summary. YES
- Brief conclusion: The summary still accurately describes what the method does after the code changes.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getHostFromUrl(String url) -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [65/77] `Summary_172`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Helper method to return the constant string for a  CstInsn in human form.` |
| ground_truth_comment | `Helper method to return a constant string.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
protected static String cstString(DalvInsn insn) {
        CstInsn ci = (CstInsn) insn;
        Constant cst = ci.getConstant();

        return cst instanceof CstString ? ((CstString) cst).toQuoted() : cst.toHuman();
    }
```

**code_snippet**

```java
protected static String cstString(DalvInsn insn) {
        CstInsn ci = (CstInsn) insn;
        Constant cst = ci.getConstant();

        return cst.toHuman();
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: cstString(DalvInsn insn) -> String
Parameters Details: [{"name": "insn", "type": "DalvInsn"}]
intention:      Method 'cstString' (cst String)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Helper method to return the constant string for a  CstInsn in human form.

[Current Code]
    protected static String cstString(DalvInsn insn) {
        CstInsn ci = (CstInsn) insn;
        Constant cst = ci.getConstant();

        return cst.toHuman();
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: cstString(DalvInsn insn) -> String
Parameters Details: [{"name": "insn", "type": "DalvInsn"}]
- Intent: Method 'cstString' (cst String)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Helper method to return" → The method still returns a string value. YES
- SUBJECT: "the constant string for a CstInsn in human form" → The method still takes a CstInsn and returns a string representation of its constant. YES
- QUALIFIERS: "in human form" → The method now always uses `cst.toHuman()` instead of the previous conditional logic that sometimes used `toQuoted()` for string constants. The qualifier "in human form" is still accurate, but the implementation has been simplified. YES

Brief conclusion: The summary still accurately describes what the method does, though the implementation has been simplified to always use the human form representation.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: cstString(DalvInsn insn) -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [66/77] `Summary_174`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Does this time interval contain or equal the specified time interval.` |
| ground_truth_comment | `Does this time interval contain the specified time interval.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: contains(ReadableInterval interval) -> boolean
Parameters Details: [{"name": "interval", "type": "ReadableInterval"}]
intention:      Method 'contains' (contains)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Does this time interval contain or equal the specified time interval.

[Current Code]
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


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: contains(ReadableInterval interval) -> boolean
Parameters Details: [{"name": "interval", "type": "ReadableInterval"}]
- Intent: Method 'contains' (contains)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Does this time interval contain or equal the specified time interval" → The code checks if one time interval contains another, but the "or equal" part is no longer true. NO
- SUBJECT: "time interval" → The code still operates on time intervals. YES
- QUALIFIERS: "contain or equal" → The code now only checks for containment, not equality. NO
- Brief conclusion: The summary mentions "contain or equal" but the code now only checks for containment, not equality.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: contains(ReadableInterval interval) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Does this time interval contain or equal the specified time interval" → The co...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [67/77] `Summary_177`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Converts an old style id to a new style id.` |
| ground_truth_comment | `Converts an old style id to a new style id.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
private static int parseOffset(String str) {
        Chronology chrono;
        if (cDefault != null) {
            chrono = ISOChronology.getInstanceUTC();
        } else {
            // Can't use a real chronology if called during class
            // initialization. Offset parser doesn't need it anyhow.
            chrono = new BaseChronology() {
                public DateTimeZone getZone() {
                    return null;
                }
                public Chronology withUTC() {
                    return this;
                }
                public Chronology withZone(DateTimeZone zone) {
                    return this;
                }
                public String toString() {
                    return getClass().getName();
                }
            };
        }

        return -(int) offsetFormatter().parseMillis(str, chrono);
    }
```

**code_snippet**

```java
private static int parseOffset(String str) {
        Chronology chrono;
        if (cDefault != null) {
            chrono = ISOChronology.getInstanceUTC();
        } else {
            // Can't use a real chronology if called during class
            // initialization. Offset parser doesn't need it anyhow.
            chrono = new BaseChronology() {
                public DateTimeZone getZone() {
                    return null;
                }
                public Chronology withUTC() {
                    return this;
                }
                public Chronology withZone(DateTimeZone zone) {
                    return this;
                }
                public String toString() {
                    return getClass().getName();
                }
            };
        }

        return -(int) offsetFormatter().withChronology(chrono).parseMillis(str);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: parseOffset(String str) -> int
Parameters Details: [{"name": "str", "type": "String"}]
intention:      Method 'parseOffset' (parse Offset)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Converts an old style id to a new style id.

[Current Code]
    private static int parseOffset(String str) {
        Chronology chrono;
        if (cDefault != null) {
            chrono = ISOChronology.getInstanceUTC();
        } else {
            // Can't use a real chronology if called during class
            // initialization. Offset parser doesn't need it anyhow.
            chrono = new BaseChronology() {
                public DateTimeZone getZone() {
                    return null;
                }
                public Chronology withUTC() {
                    return this;
                }
                public Chronology withZone(DateTimeZone zone) {
                    return this;
                }
                public String toString() {
                    return getClass().getName();
                }
            };
        }

        return -(int) offsetFormatter().withChronology(chrono).parseMillis(str);
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -21,5 +21,5 @@
             };

         }

 

-        return -(int) offsetFormatter().parseMillis(str, chrono);

+        return -(int) offsetFormatter().withChronology(chrono).parseMillis(str);

     }
```

[Code Context]
- Signature: Full Signature: parseOffset(String str) -> int
Parameters Details: [{"name": "str", "type": "String"}]
- Intent: Method 'parseOffset' (parse Offset)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Converts" → The method still performs a conversion operation, taking a string and returning an integer representation of an offset. YES
- SUBJECT: "an old style id to a new style id" → The method is still parsing a string representation of an offset and converting it to an integer value. The subject remains consistent. YES
- QUALIFIERS: None specific in the summary. The implementation details have changed slightly (how the chronology is applied), but the high-level action and subject remain the same. YES

Brief conclusion: The summary accurately describes what the method does - it converts a string representation of an offset to an integer value, which is essentially converting from an "old style id" to a "new style id" representation.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: parseOffset(String str) -> int
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [68/77] `Summary_179`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Checks if this function replacement is needed.` |
| ground_truth_comment | `Checks if this function replacement is needed.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
private String functionReplacement(FunctionCall functionCall) {
    String funcName = functionCall.getName();
      if (functionCall.args.size() > 0) {
          MajorType majorType =  functionCall.args.get(0).getMajorType();
          DataMode dataMode = majorType.getMode();
          MinorType minorType = majorType.getMinorType();
          if (optionManager != null
              && optionManager.getOption(ExecConstants.CAST_TO_NULLABLE_NUMERIC).bool_val
              && CastFunctions.isReplacementNeeded(funcName, minorType)) {
              funcName = CastFunctions.getReplacingCastFunction(funcName, dataMode, minorType);
          }
      }

    return funcName;
  }
```

**code_snippet**

```java
private String functionReplacement(FunctionCall functionCall) {
    String funcName = functionCall.getName();
    if (functionCall.args.size() == 0) {
      return funcName;
    }
    boolean castToNullableNumeric = optionManager != null &&
                  optionManager.getOption(ExecConstants.CAST_TO_NULLABLE_NUMERIC_OPTION);
    if (! castToNullableNumeric) {
      return funcName;
    }
    MajorType majorType =  functionCall.args.get(0).getMajorType();
    DataMode dataMode = majorType.getMode();
    MinorType minorType = majorType.getMinorType();
    if (CastFunctions.isReplacementNeeded(funcName, minorType)) {
        funcName = CastFunctions.getReplacingCastFunction(funcName, dataMode, minorType);
    }

    return funcName;
  }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: functionReplacement(FunctionCall functionCall) -> String
Parameters Details: [{"name": "functionCall", "type": "FunctionCall"}]
intention:      Method 'functionReplacement' (function Replacement)
implementation: Return paths: 3
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Checks if this function replacement is needed.

[Current Code]
  private String functionReplacement(FunctionCall functionCall) {
    String funcName = functionCall.getName();
    if (functionCall.args.size() == 0) {
      return funcName;
    }
    boolean castToNullableNumeric = optionManager != null &&
                  optionManager.getOption(ExecConstants.CAST_TO_NULLABLE_NUMERIC_OPTION);
    if (! castToNullableNumeric) {
      return funcName;
    }
    MajorType majorType =  functionCall.args.get(0).getMajorType();
    DataMode dataMode = majorType.getMode();
    MinorType minorType = majorType.getMinorType();
    if (CastFunctions.isReplacementNeeded(funcName, minorType)) {
        funcName = CastFunctions.getReplacingCastFunction(funcName, dataMode, minorType);
    }

    return funcName;
  }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,15 +1,19 @@
 private String functionReplacement(FunctionCall functionCall) {

     String funcName = functionCall.getName();

-      if (functionCall.args.size() > 0) {

-          MajorType majorType =  functionCall.args.get(0).getMajorType();

-          DataMode dataMode = majorType.getMode();

-          MinorType minorType = majorType.getMinorType();

-          if (optionManager != null

-              && optionManager.getOption(ExecConstants.CAST_TO_NULLABLE_NUMERIC).bool_val

-              && CastFunctions.isReplacementNeeded(funcName, minorType)) {

-              funcName = CastFunctions.getReplacingCastFunction(funcName, dataMode, minorType);

-          }

-      }

+    if (functionCall.args.size() == 0) {

+      return funcName;

+    }

+    boolean castToNullableNumeric = optionManager != null &&

+                  optionManager.getOption(ExecConstants.CAST_TO_NULLABLE_NUMERIC_OPTION);

+    if (! castToNullableNumeric) {

+      return funcName;

+    }

+    MajorType majorType =  functionCall.args.get(0).getMajorType();

+    DataMode dataMode = majorType.getMode();

+    MinorType minorType = majorType.getMinorType();

+    if (CastFunctions.isReplacementNeeded(funcName, minorType)) {

+        funcName = CastFunctions.getReplacingCastFunction(funcName, dataMode, minorType);

+    }

 

     return funcName;

   }
```

[Code Context]
- Signature: Full Signature: functionReplacement(FunctionCall functionCall) -> String
Parameters Details: [{"name": "functionCall", "type": "FunctionCall"}]
- Intent: Method 'functionReplacement' (function Replacement)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Checks if this function replacement is needed" → The code now does more than just check if replacement is needed - it actually performs the replacement when needed. NO
- SUBJECT: "this function replacement" → The code now returns the potentially replaced function name, not just checking if replacement is needed. NO
- QUALIFIERS: None specified in the summary. N/A
- Brief conclusion: The summary only describes checking if replacement is needed, but the code now actually performs the replacement when needed.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: functionReplacement(FunctionCall functionCall) -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Checks if this function replacement is needed" → The code now does more than j...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [69/77] `Summary_181`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Converts a value object for an expected JDBC type of  Types#INTEGER.` |
| ground_truth_comment | `Converts a value object for an expected JDBC type of  Types#INTEGER.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
protected Object convertBigInt(Column column, Field fieldDefn, Object data) {
        if (data == null) {
            data = fieldDefn.schema().defaultValue();
        }
        if (data == null) {
            if (column.isOptional()) return null;
            return 0L;
        }
        if (data instanceof Long) return data;
        if (data instanceof Number) {
            Number value = (Number) data;
            return new Long(value.longValue());
        }
        if (data instanceof Boolean) {
            return NumberConversions.getLong((Boolean) data);
        }
        return handleUnknownData(column, fieldDefn, data);
    }
```

**code_snippet**

```java
protected Object convertBigInt(Column column, Field fieldDefn, Object data) {
        if (data == null) {
            data = fieldDefn.schema().defaultValue();
        }
        if (data == null) {
            if (column.isOptional()) return null;
            return 0L;
        }
        if (data instanceof Long) return data;
        if (data instanceof Number) {
            Number value = (Number) data;
            return Long.valueOf(value.longValue());
        }
        if (data instanceof Boolean) {
            return NumberConversions.getLong((Boolean) data);
        }
        return handleUnknownData(column, fieldDefn, data);
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: convertBigInt(Column column, Field fieldDefn, Object data) -> Object
Parameters Details: [{"name": "column", "type": "Column"}, {"name": "fieldDefn", "type": "Field"}, {"name": "data", "type": "Object"}]
intention:      Method 'convertBigInt' (convert Big Int)
implementation: Return paths: 6
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Converts a value object for an expected JDBC type of  Types#INTEGER.

[Current Code]
    protected Object convertBigInt(Column column, Field fieldDefn, Object data) {
        if (data == null) {
            data = fieldDefn.schema().defaultValue();
        }
        if (data == null) {
            if (column.isOptional()) return null;
            return 0L;
        }
        if (data instanceof Long) return data;
        if (data instanceof Number) {
            Number value = (Number) data;
            return Long.valueOf(value.longValue());
        }
        if (data instanceof Boolean) {
            return NumberConversions.getLong((Boolean) data);
        }
        return handleUnknownData(column, fieldDefn, data);
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -9,7 +9,7 @@
         if (data instanceof Long) return data;

         if (data instanceof Number) {

             Number value = (Number) data;

-            return new Long(value.longValue());

+            return Long.valueOf(value.longValue());

         }

         if (data instanceof Boolean) {

             return NumberConversions.getLong((Boolean) data);

```

[Code Context]
- Signature: Full Signature: convertBigInt(Column column, Field fieldDefn, Object data) -> Object
Parameters Details: [{"name": "column", "type": "Column"}, {"name": "fieldDefn", "type": "Field"}, {"name": "data", "type": "Object"}]
- Intent: Method 'convertBigInt' (convert Big Int)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Converts a value object" → The method still performs conversion of input data to a different type. YES
- SUBJECT: "for an expected JDBC type of Types#INTEGER" → The method is named "convertBigInt" which suggests it's for converting to a BIGINT type, not INTEGER. The method handles conversion to Long values, which would correspond to JDBC BIGINT, not INTEGER. The subject has changed. NO
- QUALIFIERS: None specified in the summary. YES

Brief conclusion: The summary incorrectly states the method converts to an INTEGER type when it actually converts to a BIGINT type.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: convertBigInt(Column column, Field fieldDefn, Object data) -> Object
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Converts a value object" → The method still performs conversion of input data ...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [70/77] `Summary_182`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Tests if the editor is in word-wrap mode.` |
| ground_truth_comment | `Tests if the text area is in word-wrap mode.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
@Override
    public boolean isWordwrap() {
        // TODO implement here once the API from TextField is removed
        return super.isWordwrap();
    }
```

**code_snippet**

```java
public boolean isWordwrap() {
        return wordwrap;
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: isWordwrap() -> boolean
Parameters Details: []
intention:      Method 'isWordwrap' (is Wordwrap)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Tests if the editor is in word-wrap mode.

[Current Code]
    public boolean isWordwrap() {
        return wordwrap;
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: isWordwrap() -> boolean
Parameters Details: []
- Intent: Method 'isWordwrap' (is Wordwrap)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Tests if" → The code now directly returns a value without any testing logic. NO
- SUBJECT: "the editor" → The code now returns a simple boolean value without any reference to an editor. NO
- QUALIFIERS: "in word-wrap mode" → The code returns a boolean value named "wordwrap" but doesn't test or check anything. NO
- Brief conclusion: The summary describes a testing/checking behavior that no longer exists in the code, which now simply returns a value.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isWordwrap() -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Tests if" → The code now directly returns a value without any testing logic. N...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [71/77] `Summary_184`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `If a ApiResponse contains a reference to an other ApiResponse with '$ref', returns the referenced ApiResponse or the actual ApiResponse in the other cases.` |
| ground_truth_comment | `If a ApiResponse contains a reference to an other ApiResponse with '$ref', returns the referenced ApiResponse if it is found or the actual ApiResponse in the other cases.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public static ApiResponse getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) {
        if (apiResponse != null && StringUtils.isNotEmpty(apiResponse.get$ref())) {
            String name = getSimpleRef(apiResponse.get$ref());
            return getApiResponse(openAPI, name);
        }
        return apiResponse;
    }
```

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) -> ApiResponse
Parameters Details: [{"name": "openAPI", "type": "OpenAPI"}, {"name": "apiResponse", "type": "ApiResponse"}]
intention:      Method 'getReferencedApiResponse' (get Referenced Api Response)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
If a ApiResponse contains a reference to an other ApiResponse with '$ref', returns the referenced ApiResponse or the actual ApiResponse in the other cases.

[Current Code]
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


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) -> ApiResponse
Parameters Details: [{"name": "openAPI", "type": "OpenAPI"}, {"name": "apiResponse", "type": "ApiResponse"}]
- Intent: Method 'getReferencedApiResponse' (get Referenced Api Response)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "returns the referenced ApiResponse or the actual ApiResponse in the other cases" → The code still returns either a referenced ApiResponse or the original ApiResponse if no reference exists. YES
- SUBJECT: "ApiResponse" → The method still operates on ApiResponse objects. YES
- QUALIFIERS: "If a ApiResponse contains a reference to an other ApiResponse with '$ref'" → The code still checks for the '$ref' field and handles it appropriately. YES
- The code change adds a null check before returning the referenced ApiResponse, but this doesn't change the fundamental behavior described in the comment.

Brief conclusion: The summary still accurately describes what the method does after the code change.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) -> ApiRespons
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [72/77] `Summary_186`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Try to get the primary  java.net.InetAddress of the primary network interface with fallback to the local loopback address (usually  127.0.0.1 or  ::1.` |
| ground_truth_comment | `Try to get the primary  InetAddress of the primary network interface with fallback to the local loopback address (usually  127.0.0.1 or  ::1.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: guessPrimaryNetworkAddress(boolean preferIPv4) -> InetAddress throws SocketException
Parameters Details: [{"name": "preferIPv4", "type": "boolean"}]
intention:      Method 'guessPrimaryNetworkAddress' (guess Primary Network Address)
implementation: Return paths: 3, throws: SocketException
```

### Step 2 · 规则信号

```text
rule_signals    = ["PARAMETERS CHANGED: added params: {'preferIPv4'}."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Try to get the primary  java.net.InetAddress of the primary network interface with fallback to the local loopback address (usually  127.0.0.1 or  ::1.

[Current Code]
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



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: guessPrimaryNetworkAddress(boolean preferIPv4) -> InetAddress throws SocketException
Parameters Details: [{"name": "preferIPv4", "type": "boolean"}]
- Intent: Method 'guessPrimaryNetworkAddress' (guess Primary Network Address)

[Rule-based Signals — HIGH PRIORITY]
- PARAMETERS CHANGED: added params: {'preferIPv4'}.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Try to get" → still done by the code? YES. The method still attempts to get a network address.
- SUBJECT: "the primary java.net.InetAddress of the primary network interface" → still this same thing? PARTIALLY. The method still tries to get an InetAddress, but the concept of "primary" is now qualified by the preferIPv4 parameter.
- QUALIFIERS: "with fallback to the local loopback address (usually 127.0.0.1 or ::1)" → still all true? YES. The fallback to loopback address is still implemented.

The comment is missing the new parameter (preferIPv4) which changes how the "primary" address is determined. The original comment doesn't mention IPv4/IPv6 preference, which is now a key part of the method's behavior.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: guessPrimaryNetworkAddress(boolean preferIPv4) -> InetAddress throws SocketExcep
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Try to get" → still done by the code? YES. The method still attempts to get a ...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [73/77] `Summary_189`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Maps offset from java code to pde code.` |
| ground_truth_comment | `Maps offset from java code to pde code.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
protected int[] JavaToPdeOffsets(int line, int offset) {
    int codeIndex = 0;

    int x = line - mainClassOffset;
    if (x < 0) {
      // log("Negative line number "
      // + problem.getSourceLineNumber() + " , offset "
      // + mainClassOffset);
      x = line - 2; // Another -1 for 0 index
      if (x < programImports.size() && x >= 0) {
        ImportStatement is = programImports.get(x);
        // log(is.importName + ", " + is.tab + ", "
        // + is.lineNumber);
        return new int[] { is.getTab(), is.getLineNumber() };
      } else {

        // Some seriously ugly stray error, just can't find the source
        // line! Simply return first line for first tab.
        return  new int[] { 0, 1 };
      }

    }

    try {
      for (SketchCode sc : editor.getSketch().getCode()) {
        if (sc.isExtension("pde")) {
          int len;
          if (editor.getSketch().getCurrentCode().equals(sc)) {
            len = Util.countLines(sc.getDocumentText()) + 1;
          } else {
            len = Util.countLines(sc.getProgram()) + 1;
          }

          // log("x,len, CI: " + x + "," + len + ","
          // + codeIndex);

          if (x >= len) {

            // We're in the last tab and the line count is greater
            // than the no.
            // of lines in the tab,
            if (codeIndex >= editor.getSketch().getCodeCount() - 1) {
              // log("Exceeds lc " + x + "," + len
              // + problem.toString());
              // x = len
              x = editor.getSketch().getCode(codeIndex)
                  .getLineCount();
              // TODO: Obtain line having last non-white space
              // character in the code.
              break;
            } else {
              x -= len;
              codeIndex++;
            }
          } else {

            if (codeIndex >= editor.getSketch().getCodeCount()) {
              codeIndex = editor.getSketch().getCodeCount() - 1;
            }
            break;
          }

        }
      }
    } catch (Exception e) {
      System.err.println("Error inside ErrorCheckerService.JavaToPdeOffset()");
      e.printStackTrace();
    }
    return new int[] { codeIndex, x };
  }
```

**code_snippet**

```java
protected int[] JavaToPdeOffsets(int line, int offset) {

    return new int[] { 0, 0 }; // TODO

    /*
    int codeIndex = 0;

    int x = line - mainClassOffset;
    if (x < 0) {
      // log("Negative line number "
      // + problem.getSourceLineNumber() + " , offset "
      // + mainClassOffset);
      x = line - 2; // Another -1 for 0 index
      if (x < programImports.size() && x >= 0) {
        ImportStatement is = programImports.get(x);
        // log(is.importName + ", " + is.tab + ", "
        // + is.lineNumber);
        return new int[] { 0, 0 }; // TODO
      } else {

        // Some seriously ugly stray error, just can't find the source
        // line! Simply return first line for first tab.
        return  new int[] { 0, 1 };
      }

    }

    try {
      for (SketchCode sc : editor.getSketch().getCode()) {
        if (sc.isExtension("pde")) {
          int len;
          if (editor.getSketch().getCurrentCode().equals(sc)) {
            len = Util.countLines(sc.getDocumentText()) + 1;
          } else {
            len = Util.countLines(sc.getProgram()) + 1;
          }

          // log("x,len, CI: " + x + "," + len + ","
          // + codeIndex);

          if (x >= len) {

            // We're in the last tab and the line count is greater
            // than the no.
            // of lines in the tab,
            if (codeIndex >= editor.getSketch().getCodeCount() - 1) {
              // log("Exceeds lc " + x + "," + len
              // + problem.toString());
              // x = len
              x = editor.getSketch().getCode(codeIndex)
                  .getLineCount();
              // TODO: Obtain line having last non-white space
              // character in the code.
              break;
            } else {
              x -= len;
              codeIndex++;
            }
          } else {

            if (codeIndex >= editor.getSketch().getCodeCount()) {
              codeIndex = editor.getSketch().getCodeCount() - 1;
            }
            break;
          }

        }
      }
    } catch (Exception e) {
      System.err.println("Error inside ErrorCheckerService.JavaToPdeOffset()");
      e.printStackTrace();
    }
    return new int[] { codeIndex, x };
    */
  }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: JavaToPdeOffsets(int line, int offset) -> int[]
Parameters Details: [{"name": "line", "type": "int"}, {"name": "offset", "type": "int"}]
intention:      Method 'JavaToPdeOffsets' (Java To Pde Offsets)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = []
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Maps offset from java code to pde code.

[Current Code]
  protected int[] JavaToPdeOffsets(int line, int offset) {

    return new int[] { 0, 0 }; // TODO

    /*
    int codeIndex = 0;

    int x = line - mainClassOffset;
    if (x < 0) {
      // log("Negative line number "
      // + problem.getSourceLineNumber() + " , offset "
      // + mainClassOffset);
      x = line - 2; // Another -1 for 0 index
      if (x < programImports.size() && x >= 0) {
        ImportStatement is = programImports.get(x);
        // log(is.importName + ", " + is.tab + ", "
        // + is.lineNumber);
        return new int[] { 0, 0 }; // TODO
      } else {

        // Some seriously ugly stray error, just can't find the source
        // line! Simply return first line for first tab.
        return  new int[] { 0, 1 };
      }

    }

    try {
      for (SketchCode sc : editor.getSketch().getCode()) {
        if (sc.isExtension("pde")) {
          int len;
          if (editor.getSketch().getCurrentCode().equals(sc)) {
            len = Util.countLines(sc.getDocumentText()) + 1;
          } else {
            len = Util.countLines(sc.getProgram()) + 1;
          }

          // log("x,len, CI: " + x + "," + len + ","
          // + codeIndex);

          if (x >= len) {

            // We're in the last tab and the line count is greater
            // than the no.
            // of lines in the tab,
            if (codeIndex >= editor.getSketch().getCodeCount() - 1) {
              // log("Exceeds lc " + x + "," + len
              // + problem.toString());
              // x = len
              x = editor.getSketch().getCode(codeIndex)
                  .getLineCount();
              // TODO: Obtain line having last non-white space
              // character in the code.
              break;
            } else {
              x -= len;
              codeIndex++;
            }
          } else {

            if (codeIndex >= editor.getSketch().getCodeCount()) {
              codeIndex = editor.getSketch().getCodeCount() - 1;
            }
            break;
          }

        }
      }
    } catch (Exception e) {
      System.err.println("Error inside ErrorCheckerService.JavaToPdeOffset()");
      e.printStackTrace();
    }
    return new int[] { codeIndex, x };
    */
  }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,4 +1,8 @@
 protected int[] JavaToPdeOffsets(int line, int offset) {

+

+    return new int[] { 0, 0 }; // TODO

+

+    /*

     int codeIndex = 0;

 

     int x = line - mainClassOffset;

@@ -11,7 +15,7 @@
         ImportStatement is = programImports.get(x);

         // log(is.importName + ", " + is.tab + ", "

         // + is.lineNumber);

-        return new int[] { is.getTab(), is.getLineNumber() };

+        return new int[] { 0, 0 }; // TODO

       } else {

 

         // Some seriously ugly stray error, just can't find the source

@@ -67,4 +71,5 @@
       e.printStackTrace();

     }

     return new int[] { codeIndex, x };

+    */

   }
```

[Code Context]
- Signature: Full Signature: JavaToPdeOffsets(int line, int offset) -> int[]
Parameters Details: [{"name": "line", "type": "int"}, {"name": "offset", "type": "int"}]
- Intent: Method 'JavaToPdeOffsets' (Java To Pde Offsets)
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Maps offset from java code to pde code" → The method still has the same name and purpose, but the implementation has been simplified to just return {0, 0} with a TODO comment. The action of mapping is no longer actually performed.
- SUBJECT: "offset from java code to pde code" → The method still takes line and offset parameters, but no longer performs the mapping logic.
- QUALIFIERS: None specified in the summary.

The summary suggests the method performs a mapping between Java and PDE code offsets, but the current implementation simply returns {0, 0} with a TODO comment, indicating the actual mapping functionality has been removed or disabled. The method signature remains the same, but the core functionality described in the summary no longer exists.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: JavaToPdeOffsets(int line, int offset) -> int[]
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Maps offset from java code to pde code" → The method still has the same name a...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [74/77] `Summary_194`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Checks if toolitem is selected` |
| ground_truth_comment | `Finds out whether specified  ToolItem is selected or not.` |

### Step 0 · 原始数据

**old_code_snippet**

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

**code_snippet**

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

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: isSelected(ToolItem toolItem) -> boolean
Parameters Details: [{"name": "toolItem", "type": "ToolItem"}]
intention:      Method 'isSelected' (is Selected)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'w'}; added params: {'toolItem'}."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Checks if toolitem is selected

[Current Code]
	public boolean isSelected(final ToolItem toolItem) {
		boolean selectionState = Display.syncExec(new ResultRunnable<Boolean>() {
			@Override
			public Boolean run() {
					return toolItem.getSelection(); 
			}
		});
		return selectionState;
	}



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

[Code Context]
- Signature: Full Signature: isSelected(ToolItem toolItem) -> boolean
Parameters Details: [{"name": "toolItem", "type": "ToolItem"}]
- Intent: Method 'isSelected' (is Selected)

[Rule-based Signals — HIGH PRIORITY]
- PARAMETERS CHANGED: removed params: {'w'}; added params: {'toolItem'}.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Checks if" → The code still performs a check by calling toolItem.getSelection() and returning the result. YES
- SUBJECT: "toolitem" → The method still operates on a ToolItem object, though the parameter name changed from 'w' to 'toolItem'. The subject remains the same. YES
- QUALIFIERS: "is selected" → The method still checks the selection state of the toolItem by calling getSelection(). YES

Brief conclusion: The summary accurately describes what the method does despite the parameter name change.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isSelected(ToolItem toolItem) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [75/77] `Summary_195`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Set the Year of a week based year component of the specified time instant.` |
| ground_truth_comment | `Set the Year of a week based year component of the specified time instant.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public long set(long millis, int year) {
        super.verifyValueBounds(Math.abs(year),
                                iChronology.getMinYear(), iChronology.getMaxYear());
        //
        // Do nothing if no real change is requested.
        //
        int thisWeekyear = get( millis );
        if ( thisWeekyear == year ) {
            return millis;
        }
        //
        // Calculate the DayOfWeek (to be preserved).
        //
        int thisDow = iChronology.dayOfWeek().get( millis );
        //
        // Calculate the maximum weeks in the target year.
        //
        int weeksInFromYear = iChronology.getWeeksInYear( thisWeekyear );
        int weeksInToYear = iChronology.getWeeksInYear( year );
        int maxOutWeeks = (weeksInToYear < weeksInFromYear) ?
            weeksInToYear : weeksInFromYear;
        //
        // Get the current week of the year. This will be preserved in
        // the output unless it is greater than the maximum possible
        // for the target weekyear.  In that case it is adjusted
        // to the maximum possible.
        //
        int setToWeek = iChronology.weekOfWeekyear().get( millis );
        if ( setToWeek > maxOutWeeks ) {
            setToWeek = maxOutWeeks;
        }
        //
        // Get a wroking copy of the current date-time.
        // This can be a convenience for debugging.
        //
        long workMillis = millis; // Get a copy
        //
        // Attempt to get close to the proper weekyear.
        // Note - we cannot currently call ourself, so we just call
        // set for the year.  This at least gets us close.
        //
        workMillis = iChronology.year().set( workMillis, year );
        //
        // Calculate the weekyear number for the get close to value
        // (which might not be equal to the year just set).
        //
        int workWoyYear = iChronology.weekyear().get( workMillis );

        // *TEMP Debugging
        /*
        MutableDateTime temp = new MutableDateTime(workMillis,
            ISOChronology.getInstance());
        System.out.println("Current mdt value 01: "
            + temp
            + " " + workWoyYear
        );
        System.out.println("->Temp: " + temp.toString()
            + " WOYYr=" + temp.getWeekyear()
            + " WOYWk=" + temp.getWeekOfWeekyear()
            + " DoW=" + temp.getDayOfWeek()
        );
        */

        //
        // At most we are off by one year, which can be "fixed" by
        // adding/subtracting a week.
        //
        if ( workWoyYear < year ) {
            // System.out.println("Year: Adding "+workWoyYear+" "+year);
            workMillis += DateTimeConstants.MILLIS_PER_WEEK;
        } else if ( workWoyYear > year ) {
            // System.out.println("Year: Subing "+workWoyYear+" "+year);
            workMillis -= DateTimeConstants.MILLIS_PER_WEEK;
        }
        //
        // Set the proper week in the current weekyear.
        //

        // BEGIN: possible set WeekOfWeekyear logic.
        int currentWoyWeek = iChronology.weekOfWeekyear().get( workMillis );
        // No range check required (we already know it is OK).
        workMillis = workMillis + (setToWeek - currentWoyWeek)
            * (long)DateTimeConstants.MILLIS_PER_WEEK;
        // END: possible set WeekOfWeekyear logic.

        //
        // Reset DayOfWeek to previous value.
        //
        workMillis = iChronology.dayOfWeek().set( workMillis, thisDow );
        //
        // Return result.
        //
        return workMillis;
    }
```

**code_snippet**

```java
public long set(long instant, int year) {
        Utils.verifyValueBounds(this, Math.abs(year),
                                iChronology.getMinYear(), iChronology.getMaxYear());
        //
        // Do nothing if no real change is requested.
        //
        int thisWeekyear = get( instant );
        if ( thisWeekyear == year ) {
            return instant;
        }
        //
        // Calculate the DayOfWeek (to be preserved).
        //
        int thisDow = iChronology.dayOfWeek().get( instant );
        //
        // Calculate the maximum weeks in the target year.
        //
        int weeksInFromYear = iChronology.getWeeksInYear( thisWeekyear );
        int weeksInToYear = iChronology.getWeeksInYear( year );
        int maxOutWeeks = (weeksInToYear < weeksInFromYear) ?
            weeksInToYear : weeksInFromYear;
        //
        // Get the current week of the year. This will be preserved in
        // the output unless it is greater than the maximum possible
        // for the target weekyear.  In that case it is adjusted
        // to the maximum possible.
        //
        int setToWeek = iChronology.weekOfWeekyear().get( instant );
        if ( setToWeek > maxOutWeeks ) {
            setToWeek = maxOutWeeks;
        }
        //
        // Get a wroking copy of the current date-time.
        // This can be a convenience for debugging.
        //
        long workInstant = instant; // Get a copy
        //
        // Attempt to get close to the proper weekyear.
        // Note - we cannot currently call ourself, so we just call
        // set for the year.  This at least gets us close.
        //
        workInstant = iChronology.year().set( workInstant, year );
        //
        // Calculate the weekyear number for the get close to value
        // (which might not be equal to the year just set).
        //
        int workWoyYear = iChronology.weekyear().get( workInstant );

        //
        // At most we are off by one year, which can be "fixed" by
        // adding/subtracting a week.
        //
        if ( workWoyYear < year ) {
            workInstant += DateTimeConstants.MILLIS_PER_WEEK;
        } else if ( workWoyYear > year ) {
            workInstant -= DateTimeConstants.MILLIS_PER_WEEK;
        }
        //
        // Set the proper week in the current weekyear.
        //

        // BEGIN: possible set WeekOfWeekyear logic.
        int currentWoyWeek = iChronology.weekOfWeekyear().get( workInstant );
        // No range check required (we already know it is OK).
        workInstant = workInstant + (setToWeek - currentWoyWeek)
            * (long)DateTimeConstants.MILLIS_PER_WEEK;
        // END: possible set WeekOfWeekyear logic.

        //
        // Reset DayOfWeek to previous value.
        //
        workInstant = iChronology.dayOfWeek().set( workInstant, thisDow );
        //
        // Return result.
        //
        return workInstant;
    }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: set(long instant, int year) -> long
Parameters Details: [{"name": "instant", "type": "long"}, {"name": "year", "type": "int"}]
intention:      Method 'set' (set)
implementation: Return paths: 2
```

### Step 2 · 规则信号

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'millis'}; added params: {'instant'}.", "IDENTIFIER DRIFT: comment mentions 'Year' which no longer exists in new code."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Set the Year of a week based year component of the specified time instant.

[Current Code]
    public long set(long instant, int year) {
        Utils.verifyValueBounds(this, Math.abs(year),
                                iChronology.getMinYear(), iChronology.getMaxYear());
        //
        // Do nothing if no real change is requested.
        //
        int thisWeekyear = get( instant );
        if ( thisWeekyear == year ) {
            return instant;
        }
        //
        // Calculate the DayOfWeek (to be preserved).
        //
        int thisDow = iChronology.dayOfWeek().get( instant );
        //
        // Calculate the maximum weeks in the target year.
        //
        int weeksInFromYear = iChronology.getWeeksInYear( thisWeekyear );
        int weeksInToYear = iChronology.getWeeksInYear( year );
        int maxOutWeeks = (weeksInToYear < weeksInFromYear) ?
            weeksInToYear : weeksInFromYear;
        //
        // Get the current week of the year. This will be preserved in
        // the output unless it is greater than the maximum possible
        // for the target weekyear.  In that case it is adjusted
        // to the maximum possible.
        //
        int setToWeek = iChronology.weekOfWeekyear().get( instant );
        if ( setToWeek > maxOutWeeks ) {
            setToWeek = maxOutWeeks;
        }
        //
        // Get a wroking copy of the current date-time.
        // This can be a convenience for debugging.
        //
        long workInstant = instant; // Get a copy
        //
        // Attempt to get close to the proper weekyear.
        // Note - we cannot currently call ourself, so we just call
        // set for the year.  This at least gets us close.
        //
        workInstant = iChronology.year().set( workInstant, year );
        //
        // Calculate the weekyear number for the get close to value
        // (which might not be equal to the year just set).
        //
        int workWoyYear = iChronology.weekyear().get( workInstant );

        //
        // At most we are off by one year, which can be "fixed" by
        // adding/subtracting a week.
        //
        if ( workWoyYear < year ) {
            workInstant += DateTimeConstants.MILLIS_PER_WEEK;
        } else if ( workWoyYear > year ) {
            workInstant -= DateTimeConstants.MILLIS_PER_WEEK;
        }
        //
        // Set the proper week in the current weekyear.
        //

        // BEGIN: possible set WeekOfWeekyear logic.
        int currentWoyWeek = iChronology.weekOfWeekyear().get( workInstant );
        // No range check required (we already know it is OK).
        workInstant = workInstant + (setToWeek - currentWoyWeek)
            * (long)DateTimeConstants.MILLIS_PER_WEEK;
        // END: possible set WeekOfWeekyear logic.

        //
        // Reset DayOfWeek to previous value.
        //
        workInstant = iChronology.dayOfWeek().set( workInstant, thisDow );
        //
        // Return result.
        //
        return workInstant;
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,17 +1,17 @@
-public long set(long millis, int year) {

-        super.verifyValueBounds(Math.abs(year),

+public long set(long instant, int year) {

+        Utils.verifyValueBounds(this, Math.abs(year),

                                 iChronology.getMinYear(), iChronology.getMaxYear());

         //

         // Do nothing if no real change is requested.

         //

-        int thisWeekyear = get( millis );

+        int thisWeekyear = get( instant );

         if ( thisWeekyear == year ) {

-            return millis;

+            return instant;

         }

         //

         // Calculate the DayOfWeek (to be preserved).

         //

-        int thisDow = iChronology.dayOfWeek().get( millis );

+        int thisDow = iChronology.dayOfWeek().get( instant );

         //

         // Calculate the maximum weeks in the target year.

         //

@@ -25,7 +25,7 @@
         // for the target weekyear.  In that case it is adjusted

         // to the maximum possible.

         //

-        int setToWeek = iChronology.weekOfWeekyear().get( millis );

+        int setToWeek = iChronology.weekOfWeekyear().get( instant );

         if ( setToWeek > maxOutWeeks ) {

             setToWeek = maxOutWeeks;

         }

@@ -33,62 +33,45 @@
         // Get a wroking copy of the current date-time.

         // This can be a convenience for debugging.

         //

-        long workMillis = millis; // Get a copy

+        long workInstant = instant; // Get a copy

         //

         // Attempt to get close to the proper weekyear.

         // Note - we cannot currently call ourself, so we just call

         // set for the year.  This at least gets us close.

         //

-        workMillis = iChronology.year().set( workMillis, year );

+        workInstant = iChronology.year().set( workInstant, year );

         //

         // Calculate the weekyear number for the get close to value

         // (which might not be equal to the year just set).

         //

-        int workWoyYear = iChronology.weekyear().get( workMillis );

-

-        // *TEMP Debugging

-        /*

-        MutableDateTime temp = new MutableDateTime(workMillis,

-            ISOChronology.getInstance());

-        System.out.println("Current mdt value 01: "

-            + temp

-            + " " + workWoyYear

```

[Code Context]
- Signature: Full Signature: set(long instant, int year) -> long
Parameters Details: [{"name": "instant", "type": "long"}, {"name": "year", "type": "int"}]
- Intent: Method 'set' (set)

[Rule-based Signals — HIGH PRIORITY]
- PARAMETERS CHANGED: removed params: {'millis'}; added params: {'instant'}.
- IDENTIFIER DRIFT: comment mentions 'Year' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Set the Year" → The method still sets a year value, but the parameter name changed from "millis" to "instant". The action remains the same.
- SUBJECT: "of a week based year component" → The method still operates on a week-based year component, as evidenced by the use of weekyear-related calculations.
- QUALIFIERS: "of the specified time instant" → The method still takes a time instant as input, though the parameter name changed from "millis" to "instant".

The core functionality remains the same - the method sets the year component of a week-based year system for a given time instant. The parameter name change from "millis" to "instant" is a renaming that doesn't affect the method's purpose. The comment accurately describes what the method does.

CONCLUSION: CONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: set(long instant, int year) -> long
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [76/77] `Summary_204`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns the encoding used to send and receive lines from the IRC server, or null if not set.` |
| ground_truth_comment | `Returns the encoding used to send and receive lines from the IRC server.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public String getEncoding() {
		return _charset;
	}
```

**code_snippet**

```java
public Charset getEncoding() {
		return _charset;
	}
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: getEncoding() -> Charset
Parameters Details: []
intention:      Method 'getEncoding' (get Encoding)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'String' -> 'Charset'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns the encoding used to send and receive lines from the IRC server, or null if not set.

[Current Code]
	public Charset getEncoding() {
		return _charset;
	}



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public String getEncoding() {

+public Charset getEncoding() {

 		return _charset;

 	}
```

[Code Context]
- Signature: Full Signature: getEncoding() -> Charset
Parameters Details: []
- Intent: Method 'getEncoding' (get Encoding)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'String' -> 'Charset'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a value)
- SUBJECT: "the encoding used to send and receive lines from the IRC server" → still this same thing? NO (the method now returns a Charset object instead of a String)
- QUALIFIERS: "or null if not set" → still all true? YES (the method can still return null if _charset is not set)

The comment is inconsistent because it describes the method as returning a String (the encoding), but the method now returns a Charset object. While the subject is related to encoding, the specific type has changed, which makes the comment inaccurate.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getEncoding() -> Charset
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a value)
- SU...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [77/77] `Summary_205`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns the label associated with the current node, or null if there is no label.` |
| ground_truth_comment | `Returns the label associated with the current node, or null if there is no label.` |

### Step 0 · 原始数据

**old_code_snippet**

```java
public CoreLabel label() {
    return label;
  }
```

**code_snippet**

```java
public CyclicCoreLabel label() {
    return label;
  }
```

### Step 1 · ContextParser 输出

```text
interface:      Full Signature: label() -> CyclicCoreLabel
Parameters Details: []
intention:      Method 'label' (label)
implementation: Return paths: 1
```

### Step 2 · 规则信号

```text
rule_signals    = ["RETURN TYPE CHANGED: 'CoreLabel' -> 'CyclicCoreLabel'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []
```

### Step 3 · Prompt 样本专属部分（分类规则见报告开头）

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Returns the label associated with the current node, or null if there is no label.

[Current Code]
  public CyclicCoreLabel label() {
    return label;
  }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
-public CoreLabel label() {

+public CyclicCoreLabel label() {

     return label;

   }
```

[Code Context]
- Signature: Full Signature: label() -> CyclicCoreLabel
Parameters Details: []
- Intent: Method 'label' (label)

[Rule-based Signals — HIGH PRIORITY]
- RETURN TYPE CHANGED: 'CoreLabel' -> 'CyclicCoreLabel'. If the comment references the old return type, it is INCONSISTENT.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.
```

### Step 4 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a value)
- SUBJECT: "the label associated with the current node" → still this same thing? YES (the method still returns a label, though the type changed)
- QUALIFIERS: "or null if there is no label" → still all true? NO (the method now returns a CyclicCoreLabel, but the comment doesn't specify if it can return null)

The comment states the method returns "the label associated with the current node, or null if there is no label." However, the code now returns a CyclicCoreLabel type, which is a more specific type than the original CoreLabel. The comment doesn't reflect this type change, and more importantly, the comment suggests the method might return null, but the code doesn't show this possibility. The comment is outdated because it doesn't reflect the return type change and potentially incorrect about the null return possibility.

CONCLUSION: INCONSISTENT
```

### Step 5 · Agent 执行日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: label() -> CyclicCoreLabel
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a value)
- SU...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

