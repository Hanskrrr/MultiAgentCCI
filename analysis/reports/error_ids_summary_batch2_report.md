# Summary 类别错误批次2 — 新增误判案例 — 全链路 Agent 判定报告

| 项目 | 值 |
|---|---|
| 模型 | `glm-4-plus` |
| use-diff | `True` |
| parser | `treesitter` |
| 总样本 | 26 |
| 运行报错 | 0 |
| 本次判对 | 3 / 26 |

## 汇总一览

| # | ID | 真实标签 | 预测 | 判定方式 | 注释类型 | 原始注释 |
|---|---|---|---|---|---|---|
| FAIL 1 | `Summary_103` | `True` | `False` | `llm` | `summary` | Checks if this potato is baked. |
| FAIL 2 | `Summary_104` | `False` | `True` | `llm` | `summary` | Creates a renderscript allocation from a bitmap |
| FAIL 3 | `Summary_105` | `True` | `False` | `llm` | `summary` | Computes the row type of an  Aggregate before it exists. |
| FAIL 4 | `Summary_106` | `False` | `True` | `llm` | `summary` | Returns the sibling on the right of the end of given  Treepa |
| FAIL 5 | `Summary_108` | `False` | `True` | `llm` | `summary` | Evaluate a PLAIN login challenge, returning the a result str |
| FAIL 6 | `Summary_109` | `True` | `False` | `llm` | `summary` | Gets the given  start and  end view positions offset to a he |
| FAIL 7 | `Summary_110` | `False` | `True` | `llm` | `summary` | Return XML schema for the specified type, suitable for inser |
| FAIL 8 | `Summary_115` | `True` | `False` | `llm` | `summary` | This method initializes tableAuth |
| FAIL 9 | `Summary_119` | `True` | `False` | `llm` | `summary` | Returns whether an instance of Chrome is currently connected |
| FAIL 10 | `Summary_121` | `True` | `False` | `llm` | `summary` | Creates a new UserFolder, inflated from R.layout.user_folder |
| FAIL 11 | `Summary_126` | `False` | `True` | `llm` | `summary` | Make fully qualified URI based on the default file system Sc |
| OK 12 | `Summary_127` | `True` | `True` | `llm` | `summary` | Rotate the vertex by the given orientation |
| FAIL 13 | `Summary_131` | `True` | `False` | `llm` | `summary` | Does this time interval overlap the specified time interval. |
| OK 14 | `Summary_143` | `True` | `True` | `llm` | `summary` | Used to determine if the broker can dispatch to the consumer |
| FAIL 15 | `Summary_147` | `True` | `False` | `llm` | `summary` | Get a  Struct representation of the source  #partition(Strin |
| OK 16 | `Summary_149` | `True` | `True` | `llm` | `summary` | When initializing the profile, Opera rapidly starts, stops,  |
| FAIL 17 | `Summary_153` | `True` | `False` | `llm` | `summary` | An expectation for checking child WebElement as a part of pa |
| FAIL 18 | `Summary_169` | `True` | `False` | `llm` | `summary` | Returns a DurationField representing seconds. |
| FAIL 19 | `Summary_170` | `False` | `True` | `llm` | `summary` | Given a URL, attempt to infer and return the hostname from t |
| FAIL 20 | `Summary_172` | `False` | `True` | `llm` | `summary` | Helper method to return the constant string for a  CstInsn i |
| FAIL 21 | `Summary_179` | `True` | `False` | `llm` | `summary` | Checks if this function replacement is needed. |
| FAIL 22 | `Summary_181` | `True` | `False` | `llm` | `summary` | Converts a value object for an expected JDBC type of  Types# |
| FAIL 23 | `Summary_184` | `False` | `True` | `llm` | `summary` | If a ApiResponse contains a reference to an other ApiRespons |
| FAIL 24 | `Summary_189` | `True` | `False` | `llm` | `summary` | Maps offset from java code to pde code. |
| FAIL 25 | `Summary_194` | `False` | `True` | `llm` | `summary` | Checks if toolitem is selected |
| FAIL 26 | `Summary_195` | `True` | `False` | `llm` | `summary` | Set the Year of a week based year component of the specified |

---

## FAIL [1/26] `Summary_103`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Checks if this potato is baked.` |
| ground_truth_comment | `Checks if this potato is baked.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public boolean isBaked() {
        try {
            return this.isPutIntoOven();
        } catch (OvenException e) {
            return false;
        }
    }
```

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: isBaked() -> boolean throws NotDeliciousException
Parameters Details: []

intention_context:
Method 'isBaked' (is Baked)

implementation_context:
Return paths: 2, throws: NotDeliciousException
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["THROWS CHANGED: none -> {'NotDeliciousException'}."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Checks if" → The method still performs a check by determining if the potato is in the oven. YES
- SUBJECT: "this potato" → The method still operates on the same potato object (this). YES
- QUALIFIERS: "is baked" → The method now has additional logic that checks if the bake time exceeds 1100ms and throws an exception if so. The original comment doesn't mention this new behavior or exception handling. NO
- Brief conclusion: The comment is missing key details about the bake time check and exception handling that are now part of the method's functionality.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isBaked() -> boolean throws NotDeliciousException
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Checks if" → The method still performs a check by determining if the potato is...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [2/26] `Summary_104`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Creates a renderscript allocation from a bitmap` |
| ground_truth_comment | `Creates an Allocation from a  android.graphics.Bitmap.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: createFromBitmap(RenderScript rs, Bitmap b, MipmapControl mips, int usage) -> Allocation
Parameters Details: [{"name": "rs", "type": "RenderScript"}, {"name": "b", "type": "Bitmap"}, {"name": "mips", "type": "MipmapControl"}, {"name": "usage", "type": "int"}]

intention_context:
Method 'createFromBitmap' (create From Bitmap)

implementation_context:
Return paths: 4
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Creates a renderscript allocation" → The method still creates an Allocation object, so YES.
- SUBJECT: "from a bitmap" → The method still takes a Bitmap as input and creates an Allocation from it, so YES.
- QUALIFIERS: None mentioned in the summary.

The summary is very basic and doesn't mention any specific conditions or qualifiers. While the implementation has been significantly enhanced with additional checks and optimizations, the core functionality described in the summary remains unchanged. The method still creates a renderscript allocation from a bitmap.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: createFromBitmap(RenderScript rs, Bitmap b, MipmapControl mips, int usage) -> Al
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [3/26] `Summary_105`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Computes the row type of an  Aggregate before it exists.` |
| ground_truth_comment | `Computes the row type of an  Aggregate before it exists.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public boolean isValid(Litmus litmus) {
    return super.isValid(litmus)
        && litmus.check(Util.isDistinct(getRowType().getFieldNames()), getRowType());
  }
```

**code_snippet**（当前代码）

```java
public boolean isValid(Litmus litmus) {
    return super.isValid(litmus)
        && litmus.check(Util.isDistinct(getRowType().getFieldNames()),
            "distinct field names: {}", getRowType());
  }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: isValid(Litmus litmus) -> boolean
Parameters Details: [{"name": "litmus", "type": "Litmus"}]

intention_context:
Method 'isValid' (is Valid)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Computes" → NO, the code doesn't compute anything, it validates something
- SUBJECT: "the row type of an Aggregate" → NO, the code is checking if field names in a row type are distinct
- QUALIFIERS: "before it exists" → NO, the code is using getRowType() which implies it already exists

The original comment describes a computation that doesn't match the actual validation logic in the current code. The method is checking if field names in a row type are distinct, not computing a row type before it exists.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isValid(Litmus litmus) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Computes" → NO, the code doesn't compute anything, it validates something
- SU...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [4/26] `Summary_106`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns the sibling on the right of the end of given  Treepath.` |
| ground_truth_comment | `Returns the sibling on the left of the bottom of given  Treepath.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public static Treepath getNextSibling( Treepath treepath ) {
    throw new UnsupportedOperationException( "getNextSibling" ) ;
  }
```

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: getNextSibling(Treepath treepath) -> Treepath
Parameters Details: [{"name": "treepath", "type": "Treepath"}]

intention_context:
Method 'getNextSibling' (get Next Sibling)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → The code does return a Treepath object. YES
- SUBJECT: "the sibling on the right of the end of given Treepath" → The code finds and returns the next sibling of the bottom node in the given Treepath. YES
- QUALIFIERS: None explicitly mentioned in the summary. The code does have specific conditions (minimum height of 2, must have a next sibling) but these aren't mentioned in the summary. Since the summary doesn't make claims about these qualifiers, this isn't an inconsistency.

Brief conclusion: The summary accurately describes what the method does - it returns the next sibling of the given Treepath's bottom node.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getNextSibling(Treepath treepath) -> Treepath
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [5/26] `Summary_108`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Evaluate a PLAIN login challenge, returning the a result string that should satisfy the clallenge.` |
| ground_truth_comment | `Evaluate a PLAIN login challenge, returning the a result string that should satisfy the challenge.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: evaluateChallenge(byte[] challenge) -> byte[] throws MessagingException
Parameters Details: [{"name": "challenge", "type": "byte[]"}]

intention_context:
Method 'evaluateChallenge' (evaluate Challenge)

implementation_context:
Return paths: 1, throws: MessagingException
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Evaluate a PLAIN login challenge" → The method still evaluates a login challenge, but the implementation has changed. The action is still performed.
- SUBJECT: "returning a result string that should satisfy the challenge" → The method still returns a result string (converted to bytes) that should satisfy the challenge.
- QUALIFIERS: "PLAIN login challenge" → The method still handles a PLAIN login challenge, though the implementation has been simplified.

The core functionality remains the same - the method evaluates a PLAIN login challenge by creating a result string with username and password (and optionally authzid) and returns it as bytes. The implementation has been simplified but the purpose and behavior are unchanged.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: evaluateChallenge(byte[] challenge) -> byte[] throws MessagingException
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [6/26] `Summary_109`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Gets the given  start and  end view positions offset to a header.` |
| ground_truth_comment | `Gets the given  start and  end view positions offset to a header.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public static int[] getViewToHeaderPosition(JTextArea view, int start, int end) {
        validateView(view);
        validateStartEnd(start, end, view.getDocument().getLength());
        return getViewToHeaderPositionImpl(view, start, end);
    }
```

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: getViewToHeaderPosition(JTextArea view, int start, int end) -> int[]
Parameters Details: [{"name": "view", "type": "JTextArea"}, {"name": "start", "type": "int"}, {"name": "end", "type": "int"}]

intention_context:
Method 'getViewToHeaderPosition' (get View To Header Position)

implementation_context:
Return paths: 2
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Gets the given start and end view positions offset to a header" → The method still gets positions, but now has additional validation logic. The core action remains similar.
- SUBJECT: "start and end view positions" → The method still operates on start and end positions as parameters.
- QUALIFIERS: "offset to a header" → This qualifier is still accurate as the method name and purpose remain the same.

However, there is a significant change in the implementation. The method now has additional validation logic that checks if the start and end positions are valid for the document length, and returns INVALID_POSITION if they're not. The original comment doesn't mention this new validation behavior, which is a significant part of the method's functionality now.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getViewToHeaderPosition(JTextArea view, int start, int end) -> int[]
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Gets the given start and end view positions offset to a header" → The method s...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [7/26] `Summary_110`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Return XML schema for the specified type, suitable for insertion into the &lt;types&gt; element of a WSDL document.` |
| ground_truth_comment | `Return XML schema for the specified type, suitable for insertion into the &lt;types&gt; element of a WSDL document, or underneath an &lt;element&gt; or &lt;attribute&gt; declaration.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public boolean writeSchema(Types types) throws Exception {
        return false;
    }
```

**code_snippet**（当前代码）

```java
public Element writeSchema(Class javaType, Types types) throws Exception {
        return null;
    }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: writeSchema(Class javaType, Types types) -> Element throws Exception
Parameters Details: [{"name": "javaType", "type": "Class"}, {"name": "types", "type": "Types"}]

intention_context:
Method 'writeSchema' (write Schema)

implementation_context:
Return paths: 1, throws: Exception
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["RETURN TYPE CHANGED: 'boolean' -> 'Element'. If the comment references the old return type, it is INCONSISTENT.", "PARAMETERS CHANGED: added params: {'javaType'}."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Return XML schema for the specified type, suitable for insertion into the &lt;types&gt; element of a WSDL document.

[Current Code]
    public Element writeSchema(Class javaType, Types types) throws Exception {
        return null;
    }



[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Return XML schema" → The method now returns an Element (which represents XML schema), so this part is still accurate. YES
- SUBJECT: "for the specified type" → The method now takes a javaType parameter, so it still operates on a specified type. YES
- QUALIFIERS: "suitable for insertion into the <types> element of a WSDL document" → This qualifier is still mentioned in the comment and presumably still applies to the returned Element. YES
- Brief conclusion: The summary still accurately describes what the method does, despite the implementation change from returning boolean to Element and the addition of the javaType parameter.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: writeSchema(Class javaType, Types types) -> Element throws Exception
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [8/26] `Summary_115`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `This method initializes tableAuth` |
| ground_truth_comment | `This method initializes tableAuth` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: getTableExtension() -> JXTable
Parameters Details: []

intention_context:
Method 'getTableExtension' (get Table Extension)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["RETURN TYPE CHANGED: 'JTable' -> 'JXTable'. If the comment references the old return type, it is INCONSISTENT."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "initializes" → The method still initializes a table object (now JXTable instead of JTable). YES
- SUBJECT: "tableAuth" → The method now initializes "tableExt" (not "tableAuth"). The subject has changed. NO
- QUALIFIERS: None specified in the comment. N/A

Brief conclusion: The comment mentions "tableAuth" but the code now initializes "tableExt", making the subject inconsistent with the comment.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

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

## FAIL [9/26] `Summary_119`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns whether an instance of Chrome is currently connected` |
| ground_truth_comment | `Returns whether an instance of Chrome is currently connected` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
boolean hasClient() {
    return listeningThread != null && listeningThread.hasClient;
  }
```

**code_snippet**（当前代码）

```java
boolean hasClient() {
    return listeningThread != null && listeningThread.hasClient && !listeningThread.sockets.isEmpty();
  }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: hasClient() -> boolean
Parameters Details: []

intention_context:
Method 'hasClient' (has Client)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a boolean value)
- SUBJECT: "whether an instance of Chrome is currently connected" → still this same thing? NO (the method now also checks if sockets is empty, which is a new condition not mentioned in the original comment)
- QUALIFIERS: "currently connected" → still all true? PARTIALLY (the method still checks if a client is connected, but now with an additional condition about sockets being empty)

Brief conclusion: The original comment is incomplete as it doesn't mention the new condition about checking if sockets is empty, which is a significant part of the method's logic now.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

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

## FAIL [10/26] `Summary_121`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Creates a new UserFolder, inflated from R.layout.user_folder.` |
| ground_truth_comment | `Creates a new UserFolder, inflated from R.layout.user_folder.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
static Folder fromXml(Launcher launcher) {
        return (Folder) launcher.getLayoutInflater().inflate(
                FeatureFlags.LAUNCHER3_DISABLE_ICON_NORMALIZATION
                        ? R.layout.user_folder : R.layout.user_folder_icon_normalized, null);
    }
```

**code_snippet**（当前代码）

```java
static Folder fromXml(Launcher launcher) {
        return (Folder) launcher.getLayoutInflater()
                .inflate(R.layout.user_folder_icon_normalized, null);
    }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: fromXml(Launcher launcher) -> Folder
Parameters Details: [{"name": "launcher", "type": "Launcher"}]

intention_context:
Method 'fromXml' (from Xml)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'user_folder' which no longer exists in new code."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Creates a new UserFolder" → The code still creates a new Folder object by inflating a layout. YES
- SUBJECT: "UserFolder" → The code now returns a Folder object, not specifically a UserFolder. The comment mentions "UserFolder" which is no longer accurate. NO
- QUALIFIERS: "inflated from R.layout.user_folder" → The code now inflates from R.layout.user_folder_icon_normalized, not R.layout.user_folder. NO

Brief conclusion: The comment is inconsistent because it mentions "UserFolder" and "R.layout.user_folder" which are no longer used in the current code.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: fromXml(Launcher launcher) -> Folder
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Creates a new UserFolder" → The code still creates a new Folder object by infl...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [11/26] `Summary_126`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Make fully qualified URI based on the default file system Scheme and Authority` |
| ground_truth_comment | `Make fully qualified URI if Scheme and/or Authority is missing, based on the default file system Scheme and Authority.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: makeFullQualifiedURI(String uriName) -> URI throws IOException
Parameters Details: [{"name": "uriName", "type": "String"}]

intention_context:
Method 'makeFullQualifiedURI' (make Full Qualified URI)

implementation_context:
Return paths: 2, throws: IOException
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["THROWS CHANGED: {'URISyntaxException', 'IOException'} -> {'IOException'}."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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
- THROWS CHANGED: {'URISyntaxException', 'IOException'} -> {'IOException'}.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Make fully qualified URI" → The method still creates a fully qualified URI from a string input. YES
- SUBJECT: "URI based on the default file system Scheme and Authority" → The method still creates a URI using the default file system's scheme and authority when they're missing. YES
- QUALIFIERS: "fully qualified" → The method now has additional logic to check if the URI is normalized and has an absolute path before making it qualified. The qualifier "fully qualified" still applies to the output when conditions are met. YES
- The method now has additional logic to reject relative URI paths (returning null), but this doesn't contradict the original summary.

Brief conclusion: The summary still accurately describes what the method does, though the implementation has been enhanced with additional validation.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: makeFullQualifiedURI(String uriName) -> URI throws IOException
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## OK [12/26] `Summary_127`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Rotate the vertex by the given orientation` |
| ground_truth_comment | `Rotate the vertex by the given orientation` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public Vertex rotate(int orientation)
	{
		int sin = Perspective.SINE[orientation];
		int cos = Perspective.COSINE[orientation];

		return new Vertex(
			x * cos + z * sin >> 16,
			y,
			z * cos - x * sin >> 16
		);
	}
```

**code_snippet**（当前代码）

```java
public Vertex rotate(int orientation)
	{
		// models are orientated north (1024) and there are 2048 angles total
		orientation = (orientation + 1024) % 2048;

		if (orientation == 0)
		{
			return this;
		}

		int sin = Perspective.SINE[orientation];
		int cos = Perspective.COSINE[orientation];

		return new Vertex(
			x * cos + z * sin >> 16,
			y,
			z * cos - x * sin >> 16
		);
	}
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: rotate(int orientation) -> Vertex
Parameters Details: [{"name": "orientation", "type": "int"}]

intention_context:
Method 'rotate' (rotate)

implementation_context:
Return paths: 2
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Rotate the vertex by the given orientation

[Current Code]
	public Vertex rotate(int orientation)
	{
		// models are orientated north (1024) and there are 2048 angles total
		orientation = (orientation + 1024) % 2048;

		if (orientation == 0)
		{
			return this;
		}

		int sin = Perspective.SINE[orientation];
		int cos = Perspective.COSINE[orientation];

		return new Vertex(
			x * cos + z * sin >> 16,
			y,
			z * cos - x * sin >> 16
		);
	}


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,5 +1,13 @@
 public Vertex rotate(int orientation)

 	{

+		// models are orientated north (1024) and there are 2048 angles total

+		orientation = (orientation + 1024) % 2048;

+

+		if (orientation == 0)

+		{

+			return this;

+		}

+

 		int sin = Perspective.SINE[orientation];

 		int cos = Perspective.COSINE[orientation];

 

```

[Code Context]
- Signature: Full Signature: rotate(int orientation) -> Vertex
Parameters Details: [{"name": "orientation", "type": "int"}]
- Intent: Method 'rotate' (rotate)

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Rotate" → still done by the code? YES
- SUBJECT: "the vertex" → still this same thing? YES
- QUALIFIERS: "by the given orientation" → still all true? YES

The method still rotates a vertex by an orientation parameter, though the implementation now includes additional normalization logic (adding 1024 and taking modulo 2048) and an early return for the zero orientation case. The core action, subject, and main qualifier remain unchanged.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: rotate(int orientation) -> Vertex
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [13/26] `Summary_131`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Does this time interval overlap the specified time interval.` |
| ground_truth_comment | `Does this time interval overlap the specified time interval.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public boolean overlaps(ReadableInterval interval) {
        if (interval == null) {
            throw new IllegalArgumentException("The time interval must not be null");
        }
        long otherStart = interval.getStartMillis();
        long otherEnd = interval.getEndMillis();
        long thisStart = getStartMillis();
        long thisEnd = getEndMillis();
        return (thisStart < otherEnd && otherStart < thisEnd);
    }
```

**code_snippet**（当前代码）

```java
public boolean overlaps(ReadableInterval interval) {
        if (interval == null) {
            return containsNow();
        }
        long otherStart = interval.getStartMillis();
        long otherEnd = interval.getEndMillis();
        long thisStart = getStartMillis();
        long thisEnd = getEndMillis();
        return (thisStart < otherEnd && otherStart < thisEnd);
    }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: overlaps(ReadableInterval interval) -> boolean
Parameters Details: [{"name": "interval", "type": "ReadableInterval"}]

intention_context:
Method 'overlaps' (overlaps)

implementation_context:
Return paths: 2
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'time' which no longer exists in new code."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Does this time interval overlap the specified time interval.

[Current Code]
    public boolean overlaps(ReadableInterval interval) {
        if (interval == null) {
            return containsNow();
        }
        long otherStart = interval.getStartMillis();
        long otherEnd = interval.getEndMillis();
        long thisStart = getStartMillis();
        long thisEnd = getEndMillis();
        return (thisStart < otherEnd && otherStart < thisEnd);
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,6 +1,6 @@
 public boolean overlaps(ReadableInterval interval) {

         if (interval == null) {

-            throw new IllegalArgumentException("The time interval must not be null");

+            return containsNow();

         }

         long otherStart = interval.getStartMillis();

         long otherEnd = interval.getEndMillis();

```

[Code Context]
- Signature: Full Signature: overlaps(ReadableInterval interval) -> boolean
Parameters Details: [{"name": "interval", "type": "ReadableInterval"}]
- Intent: Method 'overlaps' (overlaps)

[Rule-based Signals — HIGH PRIORITY]
- IDENTIFIER DRIFT: comment mentions 'time' which no longer exists in new code.
These are deterministic signals extracted from code analysis.
Signals starting with RETURN TYPE CHANGED, IDENTIFIER DRIFT, or PARAMETERS CHANGED indicate
structural code changes that very likely make the comment outdated. Treat them as strong evidence of INCONSISTENCY.

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Does this time interval overlap the specified time interval" → The method still checks for overlap between intervals, but the action has changed slightly because it now handles null differently.
- SUBJECT: "time interval" → The method still operates on time intervals, but the comment mentions "time" which is no longer explicitly in the code.
- QUALIFIERS: "the specified time interval" → This qualifier is no longer accurate because the method now has special handling for null input.

The comment describes checking for overlap between time intervals, but the code now has a different behavior when the input interval is null (it returns containsNow() instead of throwing an exception). Additionally, the comment mentions "time" which is no longer explicitly referenced in the code.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: overlaps(ReadableInterval interval) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Does this time interval overlap the specified time interval" → The method stil...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## OK [14/26] `Summary_143`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Used to determine if the broker can dispatch to the consumer.` |
| ground_truth_comment | `Used to determine if the broker can dispatch to the consumer.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public boolean isFull() {
        return dispatched.size() - prefetchExtension.get() >= info.getPrefetchSize();
    }
```

**code_snippet**（当前代码）

```java
public boolean isFull() {
        return getPrefetchSize() == 0 ? prefetchExtension.get() == 0 : dispatched.size() - prefetchExtension.get() >= info.getPrefetchSize();
    }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: isFull() -> boolean
Parameters Details: []

intention_context:
Method 'isFull' (is Full)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

```text
Task: Determine if the [Original Comment] is CONSISTENT with the [Current Code].

[Comment Type]
summary

[Original Comment]
Used to determine if the broker can dispatch to the consumer.

[Current Code]
    public boolean isFull() {
        return getPrefetchSize() == 0 ? prefetchExtension.get() == 0 : dispatched.size() - prefetchExtension.get() >= info.getPrefetchSize();
    }


[Code Change Diff] (old_code -> new_code)
IMPORTANT: The Original Comment was written for the OLD code and was correct at that time.
Your job is to determine if it is STILL consistent with the NEW code after the changes below.
```diff
--- old_code
+++ new_code
@@ -1,3 +1,3 @@
 public boolean isFull() {

-        return dispatched.size() - prefetchExtension.get() >= info.getPrefetchSize();

+        return getPrefetchSize() == 0 ? prefetchExtension.get() == 0 : dispatched.size() - prefetchExtension.get() >= info.getPrefetchSize();

     }
```

[Code Context]
- Signature: Full Signature: isFull() -> boolean
Parameters Details: []
- Intent: Method 'isFull' (is Full)

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Used to determine" → The method still performs a determination/evaluation. YES
- SUBJECT: "if the broker can dispatch to the consumer" → The method still checks a condition related to dispatching capacity. YES
- QUALIFIERS: None explicitly mentioned in the summary. The code now has an additional condition when prefetchSize is 0, but this doesn't contradict the original purpose.

Brief conclusion: The summary still accurately describes the method's purpose of determining dispatch capacity, even though the implementation has been enhanced with an additional condition.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isFull() -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [15/26] `Summary_147`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Get a  Struct representation of the source  #partition(String) partition and  #lastOffset(String) offset information.` |
| ground_truth_comment | `Get a  Struct representation of the source  #partition(String) partition and  #lastOffset(String) offset information.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: offsetStructForEvent(String replicaSetName, Document oplogEvent) -> Struct
Parameters Details: [{"name": "replicaSetName", "type": "String"}, {"name": "oplogEvent", "type": "Document"}]

intention_context:
Method 'offsetStructForEvent' (offset Struct For Event)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Get a Struct representation" → The method still returns a Struct, so this is YES.
- SUBJECT: "of the source #partition(String) partition and #lastOffset(String) offset information" → The method still deals with partition and offset information, but the way it handles the partition has changed. It now uses CollectionId.parse(replicaSetName + "." + namespace) instead of just passing the namespace directly.
- QUALIFIERS: None explicitly mentioned in the summary.

The key change is that the method now processes the namespace differently by parsing it with CollectionId.parse() before using it. This is a significant change in how the partition information is handled, even though the high-level purpose remains similar.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

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

## OK [16/26] `Summary_149`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `When initializing the profile, Opera rapidly starts, stops, restarts and stops again; we need to wait a bit to make sure the file lock is really gone.` |
| ground_truth_comment | `When initializing the profile, Opera rapidly starts, stops, restarts and stops again; we need to wait a bit to make sure the file lock is really gone.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

```java
private boolean makeSureFileLockRemainsGone(File lock, long timeToWait) {
        for (long start = System.currentTimeMillis(); System.currentTimeMillis() < start + timeToWait;) {
            AsyncExecute.sleepTight(500);
            if (lock.exists()) return false;
        }
        return !lock.exists();
    }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: makeSureFileLockRemainsGone(File lock, long timeToWait) -> boolean
Parameters Details: [{"name": "lock", "type": "File"}, {"name": "timeToWait", "type": "long"}]

intention_context:
Method 'makeSureFileLockRemainsGone' (make Sure File Lock Remains Gone)

implementation_context:
Return paths: 2
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "we need to wait a bit to make sure the file lock is really gone" → The code still waits in a loop with sleepTight(500) and checks if the lock file exists. YES
- SUBJECT: "file lock" → The method still operates on a File lock object. YES
- QUALIFIERS: "rapidly starts, stops, restarts and stops again" → This is a context description about Opera's behavior, not a qualifier of the method itself. The method's behavior of waiting and checking remains unchanged. YES
- Brief conclusion: The summary still accurately describes what the method does - it waits for a specified time to ensure a file lock is gone.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: makeSureFileLockRemainsGone(File lock, long timeToWait) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [17/26] `Summary_153`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `An expectation for checking child WebElement as a part of parent element to be visible` |
| ground_truth_comment | `An expectation for checking child WebElement as a part of parent element to be visible` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: apply(WebDriver webDriver) -> List<WebElement>
Parameters Details: [{"name": "webDriver", "type": "WebDriver"}]

intention_context:
Method 'apply' (apply)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["IDENTIFIER DRIFT: comment mentions 'element' which no longer exists in new code."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "An expectation for checking" → The code still performs a check by verifying both existence and display status of elements. YES
- SUBJECT: "child WebElement as a part of parent element" → The code now uses findElements and findElement with a webDriver parameter instead of an element parameter, but it's still checking child elements based on a sub_locator. The subject is essentially the same. YES
- QUALIFIERS: "to be visible" → The code still checks if the element is displayed (visible) using the isDisplayed() method. YES

However, there's a significant structural change indicated by the IDENTIFIER DRIFT signal. The original comment mentions "element" which no longer exists in the new code. The method now takes a WebDriver parameter instead of working with a parent element. This changes the fundamental relationship between the parent and child elements being checked.

Brief conclusion: While the core action of checking visibility remains, the structural change from working with a parent element to using a WebDriver makes the comment outdated.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

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

## FAIL [18/26] `Summary_169`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Returns a DurationField representing seconds.` |
| ground_truth_comment | `Returns a DurationField representing seconds.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public DurationField seconds() {
        return UnsupportedDurationField.INSTANCE;
    }
```

**code_snippet**（当前代码）

```java
public DurationField seconds() {
        return UnsupportedDurationField.getInstance("seconds");
    }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: seconds() -> DurationField
Parameters Details: []

intention_context:
Method 'seconds' (seconds)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a DurationField)
- SUBJECT: "a DurationField representing seconds" → still this same thing? NO (the method now returns an UnsupportedDurationField instance for "seconds", which is a specific type of DurationField, but the comment doesn't specify it's unsupported)
- QUALIFIERS: None in the original comment
- Brief conclusion: The summary is inconsistent because it doesn't indicate that the returned DurationField is specifically an unsupported field for seconds.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: seconds() -> DurationField
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Returns" → still done by the code? YES (the method still returns a DurationFie...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

## FAIL [19/26] `Summary_170`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Given a URL, attempt to infer and return the hostname from the URL.` |
| ground_truth_comment | `Given a URL, attempt to return the host portion (not including the port).` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: getHostFromUrl(String url) -> String
Parameters Details: [{"name": "url", "type": "String"}]

intention_context:
Method 'getHostFromUrl' (get Host From Url)

implementation_context:
Return paths: 2
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "attempt to infer and return" → The code still attempts to extract and return a hostname from a URL. YES
- SUBJECT: "hostname from the URL" → The code is still extracting a hostname from a URL. YES
- QUALIFIERS: None specified in the summary. YES
- Brief conclusion: The summary still accurately describes what the method does - it extracts a hostname from a URL.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getHostFromUrl(String url) -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [20/26] `Summary_172`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Helper method to return the constant string for a  CstInsn in human form.` |
| ground_truth_comment | `Helper method to return a constant string.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
protected static String cstString(DalvInsn insn) {
        CstInsn ci = (CstInsn) insn;
        Constant cst = ci.getConstant();

        return cst instanceof CstString ? ((CstString) cst).toQuoted() : cst.toHuman();
    }
```

**code_snippet**（当前代码）

```java
protected static String cstString(DalvInsn insn) {
        CstInsn ci = (CstInsn) insn;
        Constant cst = ci.getConstant();

        return cst.toHuman();
    }
```

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: cstString(DalvInsn insn) -> String
Parameters Details: [{"name": "insn", "type": "DalvInsn"}]

intention_context:
Method 'cstString' (cst String)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Helper method to return" → The method still returns a string value. YES
- SUBJECT: "the constant string for a CstInsn" → The method still takes a CstInsn and processes its constant. YES
- QUALIFIERS: "in human form" → The method now always calls cst.toHuman() without the conditional check for CstString that previously existed. The qualifier "in human form" is still accurate, but the implementation has been simplified. YES
- Brief conclusion: The summary still accurately describes what the method does, though the implementation has been simplified.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: cstString(DalvInsn insn) -> String
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [21/26] `Summary_179`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Checks if this function replacement is needed.` |
| ground_truth_comment | `Checks if this function replacement is needed.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: functionReplacement(FunctionCall functionCall) -> String
Parameters Details: [{"name": "functionCall", "type": "FunctionCall"}]

intention_context:
Method 'functionReplacement' (function Replacement)

implementation_context:
Return paths: 3
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Checks if this function replacement is needed" → The code now does more than just check if replacement is needed - it actually performs the replacement when conditions are met. The action has changed from checking to potentially replacing.
- SUBJECT: "this function replacement" → The subject is still function replacement, but the method now actively modifies the function name rather than just checking if it's needed.
- QUALIFIERS: None specified in the summary.

The summary suggests the method only checks if replacement is needed, but the code now actually performs the replacement when certain conditions are met. The method has evolved from a simple check to a conditional transformation.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

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

## FAIL [22/26] `Summary_181`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Converts a value object for an expected JDBC type of  Types#INTEGER.` |
| ground_truth_comment | `Converts a value object for an expected JDBC type of  Types#INTEGER.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: convertBigInt(Column column, Field fieldDefn, Object data) -> Object
Parameters Details: [{"name": "column", "type": "Column"}, {"name": "fieldDefn", "type": "Field"}, {"name": "data", "type": "Object"}]

intention_context:
Method 'convertBigInt' (convert Big Int)

implementation_context:
Return paths: 6
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Converts a value object" → The method still performs conversion of input data to a different type. YES
- SUBJECT: "for an expected JDBC type of Types#INTEGER" → The method is named "convertBigInt" which suggests it's for converting to a BIGINT type, not INTEGER. The method handles conversion to Long, not Integer. NO
- QUALIFIERS: None specified in the summary. YES

The summary mentions converting to an INTEGER type, but the method is named "convertBigInt" and returns Long values, which suggests it's for BIGINT type conversion, not INTEGER. The method name and return type don't match the JDBC type mentioned in the summary.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

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

## FAIL [23/26] `Summary_184`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `If a ApiResponse contains a reference to an other ApiResponse with '$ref', returns the referenced ApiResponse or the actual ApiResponse in the other cases.` |
| ground_truth_comment | `If a ApiResponse contains a reference to an other ApiResponse with '$ref', returns the referenced ApiResponse if it is found or the actual ApiResponse in the other cases.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

```java
public static ApiResponse getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) {
        if (apiResponse != null && StringUtils.isNotEmpty(apiResponse.get$ref())) {
            String name = getSimpleRef(apiResponse.get$ref());
            return getApiResponse(openAPI, name);
        }
        return apiResponse;
    }
```

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) -> ApiResponse
Parameters Details: [{"name": "openAPI", "type": "OpenAPI"}, {"name": "apiResponse", "type": "ApiResponse"}]

intention_context:
Method 'getReferencedApiResponse' (get Referenced Api Response)

implementation_context:
Return paths: 2
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "returns the referenced ApiResponse or the actual ApiResponse in the other cases" → still done by the code? YES
- SUBJECT: "ApiResponse" → still this same thing? YES
- QUALIFIERS: "If a ApiResponse contains a reference to an other ApiResponse with '$ref'" → still all true? YES

The code change adds a null check for the referenced ApiResponse before returning it, but this doesn't change the fundamental behavior described in the comment. The method still returns the referenced ApiResponse if found via '$ref', or the original ApiResponse in other cases.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: getReferencedApiResponse(OpenAPI openAPI, ApiResponse apiResponse) -> ApiRespons
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [24/26] `Summary_189`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Maps offset from java code to pde code.` |
| ground_truth_comment | `Maps offset from java code to pde code.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: JavaToPdeOffsets(int line, int offset) -> int[]
Parameters Details: [{"name": "line", "type": "int"}, {"name": "offset", "type": "int"}]

intention_context:
Method 'JavaToPdeOffsets' (Java To Pde Offsets)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = []
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Maps offset from java code to pde code" → The method still has the same name and purpose, but the implementation has been simplified to always return {0, 0}. The action of mapping is no longer actually performed.
- SUBJECT: "offset from java code to pde code" → The method still takes line and offset parameters, but no longer performs the mapping.
- QUALIFIERS: None specific mentioned in the summary.

The summary suggests the method performs a mapping between Java and PDE code offsets, but the current implementation simply returns {0, 0} with a TODO comment, indicating the actual mapping functionality has been removed or disabled. The method signature remains the same, but the core functionality described in the summary no longer exists.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

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

## FAIL [25/26] `Summary_194`

| 字段 | 值 |
|---|---|
| 真实标签 | `False` |
| 预测结果 | `True` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Checks if toolitem is selected` |
| ground_truth_comment | `Finds out whether specified  ToolItem is selected or not.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: isSelected(ToolItem toolItem) -> boolean
Parameters Details: [{"name": "toolItem", "type": "ToolItem"}]

intention_context:
Method 'isSelected' (is Selected)

implementation_context:
Return paths: 1
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'w'}; added params: {'toolItem'}."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Checks if" → The code still performs a check by calling toolItem.getSelection() → YES
- SUBJECT: "toolitem" → The method still operates on a ToolItem object (parameter name changed from 'w' to 'toolItem', but it's still the same type) → YES
- QUALIFIERS: "is selected" → The code still checks the selection state of the toolitem by calling getSelection() → YES

Brief conclusion: The summary accurately describes what the method does despite the parameter name change.

CONCLUSION: CONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: isSelected(ToolItem toolItem) -> boolean
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Detection Passed: Comment is consistent.
[Orchestrator] (仅检测模式) 代码与注释一致。
```

---

## FAIL [26/26] `Summary_195`

| 字段 | 值 |
|---|---|
| 真实标签 | `True` |
| 预测结果 | `False` |
| 判定方式 | `llm` |
| 注释类型 | `summary` |
| original_comment     | `Set the Year of a week based year component of the specified time instant.` |
| ground_truth_comment | `Set the Year of a week based year component of the specified time instant.` |

### Step 0 · 数据集原始数据

**old_code_snippet**（代码变更前）

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

**code_snippet**（当前代码）

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

### Step 1 · ContextParserAgent 输出

```text
interface_context:
Full Signature: set(long instant, int year) -> long
Parameters Details: [{"name": "instant", "type": "long"}, {"name": "year", "type": "int"}]

intention_context:
Method 'set' (set)

implementation_context:
Return paths: 2
```

### Step 2 · 规则检查结果

```text
rule_signals    = ["PARAMETERS CHANGED: removed params: {'millis'}; added params: {'instant'}.", "IDENTIFIER DRIFT: comment mentions 'Year' which no longer exists in new code."]
rule_hard_fails = []

注：rule_hard_fails 非空时规则直接判定，跳过 LLM。
```

### Step 3 · 注入的 Few-Shot 示例

> *无 few-shot*（Summary 类型暂无动态检索，使用 Prompt 内置示例）

### Step 4 · 发送给 LLM 的完整 Prompt

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

### Step 5 · LLM 原始 Reasoning 输出

```text
Reasoning:
- ACTION: "Set the Year" → The method is still setting a year value, but it's actually setting a "weekyear" (a specific calendar concept). The action is similar but not exactly the same.
- SUBJECT: "of a week based year component" → The method is still working with week-based year components, but the comment doesn't mention the complexity of the weekyear calculation.
- QUALIFIERS: "of the specified time instant" → The method still takes a time instant parameter (though the parameter name changed from "millis" to "instant").

The comment is now inconsistent because:
1. The parameter name changed from "millis" to "instant", which is a significant change in terminology.
2. The comment mentions "Year" but the code is actually working with "weekyear" which is a more specific calendar concept.
3. The comment doesn't capture the complexity of the weekyear calculation logic that was added to the code.

CONCLUSION: INCONSISTENT
```

### Step 6 · Agent 执行历史日志

```text
[Orchestrator] 初始化任务，工作流开始。
[ContextParserAgent] Starting code analysis (mode=treesitter)...
[ContextParserAgent] Tree-sitter Java parsing successful: set(long instant, int year) -> long
[DetectorAgent] Starting consistency detection analysis...
[DetectorAgent] Inconsistency found (Reason: Reasoning:
- ACTION: "Set the Year" → The method is still setting a year value, but it's actually se...)
[Orchestrator] (仅检测模式) 发现不一致，跳过修正与审查。
```

---

