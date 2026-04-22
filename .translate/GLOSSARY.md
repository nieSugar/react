# Translation Glossary (EN -> ZH)

Rules (strict):
1. Technical/API terms MUST stay in English: `component`, `props`, `state`, `hook`, `render`, `effect`, `ref`, `context`, `reducer`, `JSX`, `DOM`, `useState`, `useEffect`, `useRef`, `useContext`, `useReducer`, `useMemo`, `useCallback`, `useEffectEvent`, `React`, `Virtual DOM`, `Reconciliation`, `Fiber`, `props`, `children`, `key`, `ref`, `fragment`, `memo`, `HOC`, `StrictMode`.
2. Common verbs/nouns used as UI labels like "Dashboard", "Next Lesson", "Course Progress", "Pass props" stay translated if short (see below).
3. `{{SKIP_N}}` / `\u0000SKIP#N\u0000` placeholders must be preserved and moved to grammatically correct positions in the Chinese output.
4. `&nbsp;` and other HTML entities should be kept as-is.
5. HTML entities like `&amp;`, `&lt;` inside the text should be preserved.
6. Keep punctuation consistent with Chinese typography (use `，。：；！？` and English punctuation inside code phrases).

UI / Navigation:
- "Course Progress" -> "课程进度"
- "My Profile" -> "个人资料"
- "Dashboard" -> "控制台"
- "Next Lesson" -> "下一章"
- "Prev Lesson" / "Previous Lesson" -> "上一章"
- "Submit An Issue" -> "提交问题"
- "New Thread" -> "新主题"
- "Start Thread" -> "发起主题"
- "Name (required to comment)" -> "名字（评论必填）"
- "Markdown is supported" -> "支持 Markdown 语法"
- "Show N Replies" -> "查看 N 条回复"
- "media loading" -> "媒体加载中"
- "Quality" -> "画质"
- "Auto" / "Low" / "Med" / "High" -> "自动 / 低 / 中 / 高"
- "Off" -> "关闭"
- "English" -> "英文"
- "X months ago" -> "X 个月前"
- "Sandbox - CodeSandbox" -> "Sandbox - CodeSandbox" (keep as-is)

Page title pattern: `"Props - ui.dev"` -> `"Props - ui.dev"` (保留不翻译页面标题，因为浏览器标签)。
Actually per user: all English translated → but page title doesn't contain prose content; translate the lesson name only when appropriate:
  - "Getting Started" -> "开始学习"
  - "Why React?" -> "为什么用 React？"
  - "Imperative vs Declarative Programming" -> "命令式与声明式编程"
  - "Pure Functions" -> "纯函数"
  - "Components" -> "组件"
  - "JSX" -> "JSX"
  - "Props" -> "Props"
  - "Elements vs Components" -> "Elements 与 Components"
  - "Handling Events" -> "处理事件"
  - "Preserving Values with useState" -> "使用 useState 保存值"
  - "Using useState" -> "使用 useState"
  - "Why React Renders" -> "React 为什么会渲染"
  - "Reality Check" -> "现实检验"
  - "Managing Effects" -> "管理 Effect"
  - "Managing Effects - Part 2" -> "管理 Effect（第二部分）"
  - "Preserving Values with useRef" -> "使用 useRef 保存值"
  - "Teleportation with Context" -> "使用 Context 传送数据"
  - "Complex State with useReducer" -> "使用 useReducer 管理复杂状态"
  - "Referential Equality and Why It Matters" -> "引用相等及其重要性"
  - "Managing Advanced Effects" -> "管理高级 Effect"
  - "Abstracting Reactive Values with useEffectEvent" -> "使用 useEffectEvent 抽象响应式值"
  - "Creating Custom Hooks" -> "创建自定义 Hook"
  - "Rebuilding useHooks" -> "重构 useHooks"

Common phrases:
- "In this example" -> "在这个例子中"
- "Let's" -> "让我们"
- "Note that" -> "注意，"
- "For example" -> "例如"
- "As you can see" -> "如你所见"
- "Just like" -> "就像"
- "In other words" -> "换句话说"
- "Instead of" -> "与其"
- "Because of" -> "由于"
- "Similarly" -> "类似地"
- "ui.dev" stays as "ui.dev"
