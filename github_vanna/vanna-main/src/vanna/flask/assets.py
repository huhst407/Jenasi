html_content = '''<!doctype html>
<html lang="en" translate>
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/png" href="https://s2.loli.net/2024/11/22/x9I4JoySjMmu2VZ.png" type="image/x-icon"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@350&display=swap" rel="stylesheet">
    <script src="https://cdn.plot.ly/plotly-latest.min.js" type="text/javascript"></script>
    <title>Jenasi.AI</title>
    <script type="module" crossorigin src="/assets/index-35bab439.js"></script>
    <link rel="stylesheet" href="/assets/index-f228f78f.css">
  </head>
  <body class="bg-white dark:bg-slate-900">
    <div id="app"></div>

  </body>
</html>
'''

css_content = '''
.nav-title {
    font-family: Roboto Slab, serif
}

*,
:before,
:after {
    box-sizing: border-box;
    border-width: 0;
    border-style: solid;
    border-color: #e5e7eb
}

:before,
:after {
    --tw-content: ""
}

html {
    line-height: 1.5;
    -webkit-text-size-adjust: 100%;
    -moz-tab-size: 4;
    -o-tab-size: 4;
    tab-size: 4;
    font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", Segoe UI Symbol, "Noto Color Emoji";
    font-feature-settings: normal;
    font-variation-settings: normal
}

body {
    margin: 0;
    line-height: inherit
}

hr {
    height: 0;
    color: inherit;
    border-top-width: 1px
}

abbr:where([title]) {
    -webkit-text-decoration: underline dotted;
    text-decoration: underline dotted
}

h1,
h2,
h3,
h4,
h5,
h6 {
    font-size: inherit;
    font-weight: inherit
}

a {
    color: inherit;
    text-decoration: inherit
}

b,
strong {
    font-weight: bolder
}

code,
kbd,
samp,
pre {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace;
    font-size: 1em
}

small {
    font-size: 80%
}

sub,
sup {
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline
}

sub {
    bottom: -.25em
}

sup {
    top: -.5em
}

table {
    text-indent: 0;
    border-color: inherit;
    border-collapse: collapse
}

button,
input,
optgroup,
select,
textarea {
    font-family: inherit;
    font-feature-settings: inherit;
    font-variation-settings: inherit;
    font-size: 100%;
    font-weight: inherit;
    line-height: inherit;
    color: inherit;
    margin: 0;
    padding: 0
}

button,
select {
    text-transform: none
}

button,
[type=button],
[type=reset],
[type=submit] {
    -webkit-appearance: button;
    background-color: transparent;
    background-image: none
}

:-moz-focusring {
    outline: auto
}

:-moz-ui-invalid {
    box-shadow: none
}

progress {
    vertical-align: baseline
}

::-webkit-inner-spin-button,
::-webkit-outer-spin-button {
    height: auto
}

[type=search] {
    -webkit-appearance: textfield;
    outline-offset: -2px
}

::-webkit-search-decoration {
    -webkit-appearance: none
}

::-webkit-file-upload-button {
    -webkit-appearance: button;
    font: inherit
}

summary {
    display: list-item
}

blockquote,
dl,
dd,
h1,
h2,
h3,
h4,
h5,
h6,
hr,
figure,
p,
pre {
    margin: 0
}

fieldset {
    margin: 0;
    padding: 0
}

legend {
    padding: 0
}

ol,
ul,
menu {
    list-style: none;
    margin: 0;
    padding: 0
}

dialog {
    padding: 0
}

textarea {
    resize: vertical
}

input::-moz-placeholder,
textarea::-moz-placeholder {
    opacity: 1;
    color: #9ca3af
}

input::placeholder,
textarea::placeholder {
    opacity: 1;
    color: #9ca3af
}

button,
[role=button] {
    cursor: pointer
}

:disabled {
    cursor: default
}

img,
svg,
video,
canvas,
audio,
iframe,
embed,
object {
    display: block;
    vertical-align: middle
}

img,
video {
    max-width: 100%;
    height: auto
}

[hidden] {
    display: none
}

*,
:before,
:after {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgb(59 130 246 / .5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia:
}

::backdrop {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgb(59 130 246 / .5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia:
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0
}

.pointer-events-none {
    pointer-events: none
}

.collapse {
    visibility: collapse
}

.static {
    position: static
}

.fixed {
    position: fixed
}

.absolute {
    position: absolute
}

.relative {
    position: relative
}

.sticky {
    position: sticky
}

.inset-0 {
    top: 0;
    right: 0;
    bottom: 0;
    left: 0
}

.inset-x-px {
    left: 1px;
    right: 1px
}

.inset-y-0 {
    top: 0;
    bottom: 0
}

.bottom-0 {
    bottom: 0
}

.bottom-px {
    bottom: 1px
}

.end-0 {
    inset-inline-end: 0px
}

.left-0 {
    left: 0
}

.right-0 {
    right: 0
}

.top-0 {
    top: 0
}

.z-10 {
    z-index: 10
}

.z-50 {
    z-index: 50
}

.z-\\[60\\] {
    z-index: 60
}

.z-\\[80\\] {
    z-index: 80
}

.-m-1 {
    margin: -.25rem
}

.-m-1\\.5 {
    margin: -.375rem
}

.m-1 {
    margin: .25rem
}

.m-3 {
    margin: .75rem
}

.mx-auto {
    margin-left: auto;
    margin-right: auto
}

.mb-1 {
    margin-bottom: .25rem
}

.mb-2 {
    margin-bottom: .5rem
}

.mb-2\\.5 {
    margin-bottom: .625rem
}

.mb-3 {
    margin-bottom: .75rem
}

.mb-auto {
    margin-bottom: auto
}

.ml-3 {
    margin-left: .75rem
}

.ml-4 {
    margin-left: 1rem
}

.mr-1 {
    margin-right: .25rem
}

.mr-1\\.5 {
    margin-right: .375rem
}

.mr-3 {
    margin-right: .75rem
}

.ms-0 {
    margin-inline-start: 0px
}

.ms-3 {
    margin-inline-start: .75rem
}

.mt-0 {
    margin-top: 0
}

.mt-0\\.5 {
    margin-top: .125rem
}

.mt-1 {
    margin-top: .25rem
}

.mt-16 {
    margin-top: 4rem
}

.mt-2 {
    margin-top: .5rem
}

.mt-2\\.5 {
    margin-top: .625rem
}

.mt-3 {
    margin-top: .75rem
}

.mt-4 {
    margin-top: 1rem
}

.mt-5 {
    margin-top: 1.25rem
}

.mt-6 {
    margin-top: 1.5rem
}

.mt-7 {
    margin-top: 1.75rem
}

.mt-auto {
    margin-top: auto
}

.block {
    display: block
}

.inline-block {
    display: inline-block
}

.inline {
    display: inline
}

.flex {
    display: flex
}

.inline-flex {
    display: inline-flex
}

.table {
    display: table
}

.grid {
    display: grid
}

.hidden {
    display: none
}

.h-1 {
    height: .25rem
}

.h-1\\.5 {
    height: .375rem
}

.h-2 {
    height: .5rem
}

.h-3 {
    height: .75rem
}

.h-3\\.5 {
    height: .875rem
}

.h-4 {
    height: 1rem
}

.h-5 {
    height: 1.25rem
}

.h-52 {
    height: 13rem
}

.h-6 {
    height: 1.5rem
}

.h-7 {
    height: 1.75rem
}

.h-8 {
    height: 2rem
}

.h-\\[2\\.375rem\\] {
    height: 2.375rem
}

.h-auto {
    height: auto
}

.h-full {
    height: 100%
}

.h-px {
    height: 1px
}

.h-screen {
    height: 100vh
}

.min-h-\\[15rem\\] {
    min-height: 15rem
}

.min-h-\\[calc\\(100\\%-3\\.5rem\\)\\] {
    min-height: calc(100% - 3.5rem)
}

.w-0 {
    width: 0px
}

.w-1 {
    width: .25rem
}

.w-1\\.5 {
    width: .375rem
}

.w-2 {
    width: .5rem
}

.w-28 {
    width: 7rem
}

.w-3 {
    width: .75rem
}

.w-3\\.5 {
    width: .875rem
}

.w-4 {
    width: 1rem
}

.w-6 {
    width: 1.5rem
}

.w-64 {
    width: 16rem
}

.w-8 {
    width: 2rem
}

.w-\\[2\\.375rem\\] {
    width: 2.375rem
}

.w-\\[3\\.25rem\\] {
    width: 3.25rem
}

.w-full {
    width: 100%
}

.w-px {
    width: 1px
}

.min-w-full {
    min-width: 100%
}

.max-w-2xl {
    max-width: 42rem
}

.max-w-4xl {
    max-width: 56rem
}

.max-w-7xl {
    max-width: 80rem
}

.max-w-\\[50rem\\] {
    max-width: 50rem
}

.max-w-\\[85rem\\] {
    max-width: 85rem
}

.max-w-fit {
    max-width: -moz-fit-content;
    max-width: fit-content
}

.max-w-md {
    max-width: 28rem
}

.max-w-sm {
    max-width: 24rem
}

.max-w-xs {
    max-width: 20rem
}

.flex-1 {
    flex: 1 1 0%
}

.flex-auto {
    flex: 1 1 auto
}

.flex-none {
    flex: none
}

.flex-shrink-0,
.shrink-0 {
    flex-shrink: 0
}

.flex-grow,
.grow {
    flex-grow: 1
}

.-translate-x-full {
    --tw-translate-x: -100%;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.translate-x-0 {
    --tw-translate-x: 0px;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.translate-x-full {
    --tw-translate-x: 100%;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.transform {
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

@keyframes bounce {

    0%,
    to {
        transform: translateY(-25%);
        animation-timing-function: cubic-bezier(.8, 0, 1, 1)
    }

    50% {
        transform: none;
        animation-timing-function: cubic-bezier(0, 0, .2, 1)
    }
}

.animate-bounce {
    animation: bounce 1s infinite
}

@keyframes ping {

    75%,
    to {
        transform: scale(2);
        opacity: 0
    }
}

.animate-ping {
    animation: ping 1s cubic-bezier(0, 0, .2, 1) infinite
}

@keyframes pulse {
    50% {
        opacity: .5
    }
}

.animate-pulse {
    animation: pulse 2s cubic-bezier(.4, 0, .6, 1) infinite
}

@keyframes spin {
    to {
        transform: rotate(360deg)
    }
}

.animate-spin {
    animation: spin 1s linear infinite
}

.cursor-pointer {
    cursor: pointer
}

.resize {
    resize: both
}

.list-disc {
    list-style-type: disc
}

.appearance-none {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none
}

.grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr))
}

.flex-col {
    flex-direction: column
}

.items-start {
    align-items: flex-start
}

.items-center {
    align-items: center
}

.justify-end {
    justify-content: flex-end
}

.justify-center {
    justify-content: center
}

.justify-between {
    justify-content: space-between
}

.gap-1 {
    gap: .25rem
}

.gap-1\\.5 {
    gap: .375rem
}

.gap-2 {
    gap: .5rem
}

.gap-3 {
    gap: .75rem
}

.gap-4 {
    gap: 1rem
}

.gap-x-1 {
    -moz-column-gap: .25rem;
    column-gap: .25rem
}

.gap-x-2 {
    -moz-column-gap: .5rem;
    column-gap: .5rem
}

.gap-x-3 {
    -moz-column-gap: .75rem;
    column-gap: .75rem
}

.gap-y-4 {
    row-gap: 1rem
}

.-space-y-px>:not([hidden])~:not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: calc(-1px * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(-1px * var(--tw-space-y-reverse))
}

.space-x-2>:not([hidden])~:not([hidden]) {
    --tw-space-x-reverse: 0;
    margin-right: calc(.5rem * var(--tw-space-x-reverse));
    margin-left: calc(.5rem * calc(1 - var(--tw-space-x-reverse)))
}

.space-y-1>:not([hidden])~:not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: calc(.25rem * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(.25rem * var(--tw-space-y-reverse))
}

.space-y-1\\.5>:not([hidden])~:not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: calc(.375rem * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(.375rem * var(--tw-space-y-reverse))
}

.space-y-2>:not([hidden])~:not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: calc(.5rem * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(.5rem * var(--tw-space-y-reverse))
}

.space-y-3>:not([hidden])~:not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: calc(.75rem * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(.75rem * var(--tw-space-y-reverse))
}

.space-y-4>:not([hidden])~:not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: calc(1rem * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(1rem * var(--tw-space-y-reverse))
}

.space-y-5>:not([hidden])~:not([hidden]) {
    --tw-space-y-reverse: 0;
    margin-top: calc(1.25rem * calc(1 - var(--tw-space-y-reverse)));
    margin-bottom: calc(1.25rem * var(--tw-space-y-reverse))
}

.divide-x>:not([hidden])~:not([hidden]) {
    --tw-divide-x-reverse: 0;
    border-right-width: calc(1px * var(--tw-divide-x-reverse));
    border-left-width: calc(1px * calc(1 - var(--tw-divide-x-reverse)))
}

.divide-y>:not([hidden])~:not([hidden]) {
    --tw-divide-y-reverse: 0;
    border-top-width: calc(1px * calc(1 - var(--tw-divide-y-reverse)));
    border-bottom-width: calc(1px * var(--tw-divide-y-reverse))
}

.divide-gray-200>:not([hidden])~:not([hidden]) {
    --tw-divide-opacity: 1;
    border-color: rgb(229 231 235 / var(--tw-divide-opacity))
}

.overflow-hidden {
    overflow: hidden
}

.overflow-x-auto {
    overflow-x: auto
}

.overflow-y-auto {
    overflow-y: auto
}

.overflow-x-hidden {
    overflow-x: hidden
}

.overflow-y-hidden {
    overflow-y: hidden
}

.truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.whitespace-nowrap {
    white-space: nowrap
}

.whitespace-pre-wrap {
    white-space: pre-wrap
}

.whitespace-break-spaces {
    white-space: break-spaces
}

.rounded {
    border-radius: .25rem
}

.rounded-full {
    border-radius: 9999px
}

.rounded-lg {
    border-radius: .5rem
}

.rounded-md {
    border-radius: .375rem
}

.rounded-xl {
    border-radius: .75rem
}

.rounded-b-md {
    border-bottom-right-radius: .375rem;
    border-bottom-left-radius: .375rem
}

.rounded-t-xl {
    border-top-left-radius: .75rem;
    border-top-right-radius: .75rem
}

.rounded-ee-xl {
    border-end-end-radius: .75rem
}

.rounded-es-xl {
    border-end-start-radius: .75rem
}

.border {
    border-width: 1px
}

.border-2 {
    border-width: 2px
}

.border-4 {
    border-width: 4px
}

.border-\\[3px\\] {
    border-width: 3px
}

.border-b {
    border-bottom-width: 1px
}

.border-b-2 {
    border-bottom-width: 2px
}

.border-r {
    border-right-width: 1px
}

.border-s {
    border-inline-start-width: 1px
}

.border-t {
    border-top-width: 1px
}

.border-t-2 {
    border-top-width: 2px
}

.border-t-4 {
    border-top-width: 4px
}

.border-blue-500 {
    --tw-border-opacity: 1;
    border-color: rgb(59 130 246 / var(--tw-border-opacity))
}

.border-blue-600 {
    --tw-border-opacity: 1;
    border-color: rgb(37 99 235 / var(--tw-border-opacity))
}

.border-current {
    border-color: currentColor
}

.border-gray-200 {
    --tw-border-opacity: 1;
    border-color: rgb(229 231 235 / var(--tw-border-opacity))
}

.border-gray-300 {
    --tw-border-opacity: 1;
    border-color: rgb(209 213 219 / var(--tw-border-opacity))
}

.border-gray-600 {
    --tw-border-opacity: 1;
    border-color: rgb(75 85 99 / var(--tw-border-opacity))
}

.border-gray-700 {
    --tw-border-opacity: 1;
    border-color: rgb(55 65 81 / var(--tw-border-opacity))
}

.border-green-200 {
    --tw-border-opacity: 1;
    border-color: rgb(187 247 208 / var(--tw-border-opacity))
}

.border-neutral-700 {
    --tw-border-opacity: 1;
    border-color: rgb(64 64 64 / var(--tw-border-opacity))
}

.border-red-200 {
    --tw-border-opacity: 1;
    border-color: rgb(254 202 202 / var(--tw-border-opacity))
}

.border-red-500 {
    --tw-border-opacity: 1;
    border-color: rgb(239 68 68 / var(--tw-border-opacity))
}

.border-red-600 {
    --tw-border-opacity: 1;
    border-color: rgb(220 38 38 / var(--tw-border-opacity))
}

.border-teal-100 {
    --tw-border-opacity: 1;
    border-color: rgb(204 251 241 / var(--tw-border-opacity))
}

.border-teal-500 {
    --tw-border-opacity: 1;
    border-color: rgb(20 184 166 / var(--tw-border-opacity))
}

.border-teal-900 {
    --tw-border-opacity: 1;
    border-color: rgb(19 78 74 / var(--tw-border-opacity))
}

.border-transparent {
    border-color: transparent
}

.border-yellow-200 {
    --tw-border-opacity: 1;
    border-color: rgb(254 240 138 / var(--tw-border-opacity))
}

.border-t-blue-500 {
    --tw-border-opacity: 1;
    border-top-color: rgb(59 130 246 / var(--tw-border-opacity))
}

.border-t-blue-600 {
    --tw-border-opacity: 1;
    border-top-color: rgb(37 99 235 / var(--tw-border-opacity))
}

.border-t-green-500 {
    --tw-border-opacity: 1;
    border-top-color: rgb(34 197 94 / var(--tw-border-opacity))
}

.border-t-green-600 {
    --tw-border-opacity: 1;
    border-top-color: rgb(22 163 74 / var(--tw-border-opacity))
}

.border-t-red-500 {
    --tw-border-opacity: 1;
    border-top-color: rgb(239 68 68 / var(--tw-border-opacity))
}

.border-t-red-600 {
    --tw-border-opacity: 1;
    border-top-color: rgb(220 38 38 / var(--tw-border-opacity))
}

.border-t-transparent {
    border-top-color: transparent
}

.bg-blue-500 {
    --tw-bg-opacity: 1;
    background-color: rgb(59 130 246 / var(--tw-bg-opacity))
}

.bg-blue-600 {
    --tw-bg-opacity: 1;
    background-color: rgb(37 99 235 / var(--tw-bg-opacity))
}

.bg-gray-100 {
    --tw-bg-opacity: 1;
    background-color: rgb(243 244 246 / var(--tw-bg-opacity))
}

.bg-gray-50 {
    --tw-bg-opacity: 1;
    background-color: rgb(249 250 251 / var(--tw-bg-opacity))
}

.bg-gray-600 {
    --tw-bg-opacity: 1;
    background-color: rgb(75 85 99 / var(--tw-bg-opacity))
}

.bg-gray-700 {
    --tw-bg-opacity: 1;
    background-color: rgb(55 65 81 / var(--tw-bg-opacity))
}

.bg-gray-800 {
    --tw-bg-opacity: 1;
    background-color: rgb(31 41 55 / var(--tw-bg-opacity))
}

.bg-gray-900 {
    --tw-bg-opacity: 1;
    background-color: rgb(17 24 39 / var(--tw-bg-opacity))
}

.bg-green-600 {
    --tw-bg-opacity: 1;
    background-color: rgb(22 163 74 / var(--tw-bg-opacity))
}

.bg-neutral-800 {
    --tw-bg-opacity: 1;
    background-color: rgb(38 38 38 / var(--tw-bg-opacity))
}

.bg-neutral-900 {
    --tw-bg-opacity: 1;
    background-color: rgb(23 23 23 / var(--tw-bg-opacity))
}

.bg-red-500 {
    --tw-bg-opacity: 1;
    background-color: rgb(239 68 68 / var(--tw-bg-opacity))
}

.bg-slate-800 {
    --tw-bg-opacity: 1;
    background-color: rgb(30 41 59 / var(--tw-bg-opacity))
}

.bg-slate-900 {
    --tw-bg-opacity: 1;
    background-color: rgb(15 23 42 / var(--tw-bg-opacity))
}

.bg-teal-200 {
    --tw-bg-opacity: 1;
    background-color: rgb(153 246 228 / var(--tw-bg-opacity))
}

.bg-teal-50 {
    --tw-bg-opacity: 1;
    background-color: rgb(240 253 250 / var(--tw-bg-opacity))
}

.bg-teal-800 {
    --tw-bg-opacity: 1;
    background-color: rgb(17 94 89 / var(--tw-bg-opacity))
}

.bg-white {
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity))
}

.bg-yellow-50 {
    --tw-bg-opacity: 1;
    background-color: rgb(254 252 232 / var(--tw-bg-opacity))
}

.bg-opacity-50 {
    --tw-bg-opacity: .5
}

.bg-opacity-80 {
    --tw-bg-opacity: .8
}

.p-1 {
    padding: .25rem
}

.p-1\\.5 {
    padding: .375rem
}

.p-2 {
    padding: .5rem
}

.p-2\\.5 {
    padding: .625rem
}

.p-3 {
    padding: .75rem
}

.p-4 {
    padding: 1rem
}

.p-6 {
    padding: 1.5rem
}

.px-1 {
    padding-left: .25rem;
    padding-right: .25rem
}

.px-3 {
    padding-left: .75rem;
    padding-right: .75rem
}

.px-4 {
    padding-left: 1rem;
    padding-right: 1rem
}

.px-6 {
    padding-left: 1.5rem;
    padding-right: 1.5rem
}

.px-7 {
    padding-left: 1.75rem;
    padding-right: 1.75rem
}

.py-1 {
    padding-top: .25rem;
    padding-bottom: .25rem
}

.py-10 {
    padding-top: 2.5rem;
    padding-bottom: 2.5rem
}

.py-16 {
    padding-top: 4rem;
    padding-bottom: 4rem
}

.py-2 {
    padding-top: .5rem;
    padding-bottom: .5rem
}

.py-2\\.5 {
    padding-top: .625rem;
    padding-bottom: .625rem
}

.py-3 {
    padding-top: .75rem;
    padding-bottom: .75rem
}

.py-4 {
    padding-top: 1rem;
    padding-bottom: 1rem
}

.py-5 {
    padding-top: 1.25rem;
    padding-bottom: 1.25rem
}

.pb-12 {
    padding-bottom: 3rem
}

.pe-11 {
    padding-inline-end: 2.75rem
}

.pe-3 {
    padding-inline-end: .75rem
}

.pl-3 {
    padding-left: .75rem
}

.pl-7 {
    padding-left: 1.75rem
}

.pr-10 {
    padding-right: 2.5rem
}

.pr-4 {
    padding-right: 1rem
}

.pr-9 {
    padding-right: 2.25rem
}

.ps-5 {
    padding-inline-start: 1.25rem
}

.text-left {
    text-align: left
}

.text-center {
    text-align: center
}

.text-start {
    text-align: start
}

.align-middle {
    vertical-align: middle
}

.font-mono {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace
}

.text-2xl {
    font-size: 1.5rem;
    line-height: 2rem
}

.text-3xl {
    font-size: 1.875rem;
    line-height: 2.25rem
}

.text-7xl {
    font-size: 4.5rem;
    line-height: 1
}

.text-base {
    font-size: 1rem;
    line-height: 1.5rem
}

.text-lg {
    font-size: 1.125rem;
    line-height: 1.75rem
}

.text-sm {
    font-size: .875rem;
    line-height: 1.25rem
}

.text-xl {
    font-size: 1.25rem;
    line-height: 1.75rem
}

.text-xs {
    font-size: .75rem;
    line-height: 1rem
}

.font-bold {
    font-weight: 700
}

.font-medium {
    font-weight: 500
}

.font-semibold {
    font-weight: 600
}

.uppercase {
    text-transform: uppercase
}

.leading-none {
    line-height: 1
}

.tracking-wide {
    letter-spacing: .025em
}

.text-blue-500 {
    --tw-text-opacity: 1;
    color: rgb(59 130 246 / var(--tw-text-opacity))
}

.text-blue-600 {
    --tw-text-opacity: 1;
    color: rgb(37 99 235 / var(--tw-text-opacity))
}

.text-gray-200 {
    --tw-text-opacity: 1;
    color: rgb(229 231 235 / var(--tw-text-opacity))
}

.text-gray-300 {
    --tw-text-opacity: 1;
    color: rgb(209 213 219 / var(--tw-text-opacity))
}

.text-gray-400 {
    --tw-text-opacity: 1;
    color: rgb(156 163 175 / var(--tw-text-opacity))
}

.text-gray-500 {
    --tw-text-opacity: 1;
    color: rgb(107 114 128 / var(--tw-text-opacity))
}

.text-gray-600 {
    --tw-text-opacity: 1;
    color: rgb(75 85 99 / var(--tw-text-opacity))
}

.text-gray-700 {
    --tw-text-opacity: 1;
    color: rgb(55 65 81 / var(--tw-text-opacity))
}

.text-gray-800 {
    --tw-text-opacity: 1;
    color: rgb(31 41 55 / var(--tw-text-opacity))
}

.text-green-500 {
    --tw-text-opacity: 1;
    color: rgb(34 197 94 / var(--tw-text-opacity))
}

.text-green-600 {
    --tw-text-opacity: 1;
    color: rgb(22 163 74 / var(--tw-text-opacity))
}

.text-neutral-200 {
    --tw-text-opacity: 1;
    color: rgb(229 229 229 / var(--tw-text-opacity))
}

.text-neutral-300 {
    --tw-text-opacity: 1;
    color: rgb(212 212 212 / var(--tw-text-opacity))
}

.text-neutral-400 {
    --tw-text-opacity: 1;
    color: rgb(163 163 163 / var(--tw-text-opacity))
}

.text-neutral-500 {
    --tw-text-opacity: 1;
    color: rgb(115 115 115 / var(--tw-text-opacity))
}

.text-red-500 {
    --tw-text-opacity: 1;
    color: rgb(239 68 68 / var(--tw-text-opacity))
}

.text-red-600 {
    --tw-text-opacity: 1;
    color: rgb(220 38 38 / var(--tw-text-opacity))
}

.text-slate-400 {
    --tw-text-opacity: 1;
    color: rgb(148 163 184 / var(--tw-text-opacity))
}

.text-slate-700 {
    --tw-text-opacity: 1;
    color: rgb(51 65 85 / var(--tw-text-opacity))
}

.text-teal-400 {
    --tw-text-opacity: 1;
    color: rgb(45 212 191 / var(--tw-text-opacity))
}

.text-teal-800 {
    --tw-text-opacity: 1;
    color: rgb(17 94 89 / var(--tw-text-opacity))
}

.text-white {
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity))
}

.text-yellow-400 {
    --tw-text-opacity: 1;
    color: rgb(250 204 21 / var(--tw-text-opacity))
}

.text-yellow-700 {
    --tw-text-opacity: 1;
    color: rgb(161 98 7 / var(--tw-text-opacity))
}

.text-yellow-800 {
    --tw-text-opacity: 1;
    color: rgb(133 77 14 / var(--tw-text-opacity))
}

.decoration-2 {
    text-decoration-thickness: 2px
}

.opacity-0 {
    opacity: 0
}

.shadow {
    --tw-shadow: 0 1px 3px 0 rgb(0 0 0 / .1), 0 1px 2px -1px rgb(0 0 0 / .1);
    --tw-shadow-colored: 0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)
}

.shadow-md {
    --tw-shadow: 0 4px 6px -1px rgb(0 0 0 / .1), 0 2px 4px -2px rgb(0 0 0 / .1);
    --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)
}

.shadow-sm {
    --tw-shadow: 0 1px 2px 0 rgb(0 0 0 / .05);
    --tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)
}

.shadow-neutral-700 {
    --tw-shadow-color: #404040;
    --tw-shadow: var(--tw-shadow-colored)
}

.shadow-slate-700 {
    --tw-shadow-color: #334155;
    --tw-shadow: var(--tw-shadow-colored)
}

.ring-1 {
    --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
    --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(1px + var(--tw-ring-offset-width)) var(--tw-ring-color);
    box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000)
}

.ring-transparent {
    --tw-ring-color: transparent
}

.ring-offset-white {
    --tw-ring-offset-color: #fff
}

.blur {
    --tw-blur: blur(8px);
    filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)
}

.filter {
    filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)
}

.transition {
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter;
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter;
    transition-timing-function: cubic-bezier(.4, 0, .2, 1);
    transition-duration: .15s
}

.transition-all {
    transition-property: all;
    transition-timing-function: cubic-bezier(.4, 0, .2, 1);
    transition-duration: .15s
}

.transition-colors {
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
    transition-timing-function: cubic-bezier(.4, 0, .2, 1);
    transition-duration: .15s
}

.duration-200 {
    transition-duration: .2s
}

.duration-300 {
    transition-duration: .3s
}

.duration-500 {
    transition-duration: .5s
}

.ease-in-out {
    transition-timing-function: cubic-bezier(.4, 0, .2, 1)
}

.ease-out {
    transition-timing-function: cubic-bezier(0, 0, .2, 1)
}

.\\[--body-scroll\\:true\\] {
    --body-scroll: true
}

.marker\\:text-blue-600 *::marker {
    color: #2563eb
}

.marker\\:text-blue-600::marker {
    color: #2563eb
}

.before\\:inline-block:before {
    content: var(--tw-content);
    display: inline-block
}

.before\\:h-6:before {
    content: var(--tw-content);
    height: 1.5rem
}

.before\\:w-6:before {
    content: var(--tw-content);
    width: 1.5rem
}

.before\\:translate-x-0:before {
    content: var(--tw-content);
    --tw-translate-x: 0px;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.before\\:transform:before {
    content: var(--tw-content);
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.before\\:rounded-full:before {
    content: var(--tw-content);
    border-radius: 9999px
}

.before\\:bg-white:before {
    content: var(--tw-content);
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity))
}

.before\\:shadow:before {
    content: var(--tw-content);
    --tw-shadow: 0 1px 3px 0 rgb(0 0 0 / .1), 0 1px 2px -1px rgb(0 0 0 / .1);
    --tw-shadow-colored: 0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)
}

.before\\:ring-0:before {
    content: var(--tw-content);
    --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
    --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(0px + var(--tw-ring-offset-width)) var(--tw-ring-color);
    box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000)
}

.before\\:transition:before {
    content: var(--tw-content);
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter;
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter;
    transition-timing-function: cubic-bezier(.4, 0, .2, 1);
    transition-duration: .15s
}

.before\\:duration-200:before {
    content: var(--tw-content);
    transition-duration: .2s
}

.before\\:ease-in-out:before {
    content: var(--tw-content);
    transition-timing-function: cubic-bezier(.4, 0, .2, 1)
}

.first\\:mt-0:first-child {
    margin-top: 0
}

.first\\:rounded-t-lg:first-child {
    border-top-left-radius: .5rem;
    border-top-right-radius: .5rem
}

.last\\:rounded-b-lg:last-child {
    border-bottom-right-radius: .5rem;
    border-bottom-left-radius: .5rem
}

.checked\\:bg-blue-600:checked {
    --tw-bg-opacity: 1;
    background-color: rgb(37 99 235 / var(--tw-bg-opacity))
}

.checked\\:bg-none:checked {
    background-image: none
}

.checked\\:before\\:translate-x-full:checked:before {
    content: var(--tw-content);
    --tw-translate-x: 100%;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.checked\\:before\\:bg-blue-200:checked:before {
    content: var(--tw-content);
    --tw-bg-opacity: 1;
    background-color: rgb(191 219 254 / var(--tw-bg-opacity))
}

.hover\\:border-blue-500:hover {
    --tw-border-opacity: 1;
    border-color: rgb(59 130 246 / var(--tw-border-opacity))
}

.hover\\:border-green-500:hover {
    --tw-border-opacity: 1;
    border-color: rgb(34 197 94 / var(--tw-border-opacity))
}

.hover\\:border-red-400:hover {
    --tw-border-opacity: 1;
    border-color: rgb(248 113 113 / var(--tw-border-opacity))
}

.hover\\:border-red-500:hover {
    --tw-border-opacity: 1;
    border-color: rgb(239 68 68 / var(--tw-border-opacity))
}

.hover\\:bg-blue-50:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(239 246 255 / var(--tw-bg-opacity))
}

.hover\\:bg-blue-500:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(59 130 246 / var(--tw-bg-opacity))
}

.hover\\:bg-blue-600:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(37 99 235 / var(--tw-bg-opacity))
}

.hover\\:bg-blue-700:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(29 78 216 / var(--tw-bg-opacity))
}

.hover\\:bg-gray-100:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(243 244 246 / var(--tw-bg-opacity))
}

.hover\\:bg-gray-50:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(249 250 251 / var(--tw-bg-opacity))
}

.hover\\:bg-green-500:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(34 197 94 / var(--tw-bg-opacity))
}

.hover\\:bg-red-500:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(239 68 68 / var(--tw-bg-opacity))
}

.hover\\:text-blue-500:hover {
    --tw-text-opacity: 1;
    color: rgb(59 130 246 / var(--tw-text-opacity))
}

.hover\\:text-blue-600:hover {
    --tw-text-opacity: 1;
    color: rgb(37 99 235 / var(--tw-text-opacity))
}

.hover\\:text-blue-800:hover {
    --tw-text-opacity: 1;
    color: rgb(30 64 175 / var(--tw-text-opacity))
}

.hover\\:text-gray-400:hover {
    --tw-text-opacity: 1;
    color: rgb(156 163 175 / var(--tw-text-opacity))
}

.hover\\:text-green-800:hover {
    --tw-text-opacity: 1;
    color: rgb(22 101 52 / var(--tw-text-opacity))
}

.hover\\:text-red-400:hover {
    --tw-text-opacity: 1;
    color: rgb(248 113 113 / var(--tw-text-opacity))
}

.hover\\:text-red-500:hover {
    --tw-text-opacity: 1;
    color: rgb(239 68 68 / var(--tw-text-opacity))
}

.hover\\:text-red-600:hover {
    --tw-text-opacity: 1;
    color: rgb(220 38 38 / var(--tw-text-opacity))
}

.hover\\:text-white:hover {
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity))
}

.focus\\:z-10:focus {
    z-index: 10
}

.focus\\:border-blue-500:focus {
    --tw-border-opacity: 1;
    border-color: rgb(59 130 246 / var(--tw-border-opacity))
}

.focus\\:border-blue-600:focus {
    --tw-border-opacity: 1;
    border-color: rgb(37 99 235 / var(--tw-border-opacity))
}

.focus\\:border-indigo-500:focus {
    --tw-border-opacity: 1;
    border-color: rgb(99 102 241 / var(--tw-border-opacity))
}

.focus\\:outline-none:focus {
    outline: 2px solid transparent;
    outline-offset: 2px
}

.focus\\:ring-2:focus {
    --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
    --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
    box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000)
}

.focus\\:ring-blue-500:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(59 130 246 / var(--tw-ring-opacity))
}

.focus\\:ring-blue-600:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(37 99 235 / var(--tw-ring-opacity))
}

.focus\\:ring-gray-400:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(156 163 175 / var(--tw-ring-opacity))
}

.focus\\:ring-green-200:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(187 247 208 / var(--tw-ring-opacity))
}

.focus\\:ring-indigo-500:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(99 102 241 / var(--tw-ring-opacity))
}

.focus\\:ring-red-200:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(254 202 202 / var(--tw-ring-opacity))
}

.focus\\:ring-red-500:focus {
    --tw-ring-opacity: 1;
    --tw-ring-color: rgb(239 68 68 / var(--tw-ring-opacity))
}

.focus\\:ring-offset-2:focus {
    --tw-ring-offset-width: 2px
}

.focus\\:ring-offset-white:focus {
    --tw-ring-offset-color: #fff
}

.disabled\\:pointer-events-none:disabled {
    pointer-events: none
}

.disabled\\:opacity-50:disabled {
    opacity: .5
}

[data-hs-tab].active.hs-tab-active\\:border-blue-600 {
    --tw-border-opacity: 1;
    border-color: rgb(37 99 235 / var(--tw-border-opacity))
}

[data-hs-tab].active.hs-tab-active\\:font-semibold {
    font-weight: 600
}

[data-hs-tab].active.hs-tab-active\\:text-blue-600 {
    --tw-text-opacity: 1;
    color: rgb(37 99 235 / var(--tw-text-opacity))
}

[data-hs-tab].active .hs-tab-active\\:border-blue-600 {
    --tw-border-opacity: 1;
    border-color: rgb(37 99 235 / var(--tw-border-opacity))
}

[data-hs-tab].active .hs-tab-active\\:font-semibold {
    font-weight: 600
}

[data-hs-tab].active .hs-tab-active\\:text-blue-600 {
    --tw-text-opacity: 1;
    color: rgb(37 99 235 / var(--tw-text-opacity))
}

.open.hs-overlay-open\\:mt-7 {
    margin-top: 1.75rem
}

.open.hs-overlay-open\\:translate-x-0 {
    --tw-translate-x: 0px;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.open.hs-overlay-open\\:opacity-100 {
    opacity: 1
}

.open.hs-overlay-open\\:duration-500 {
    transition-duration: .5s
}

.open .hs-overlay-open\\:mt-7 {
    margin-top: 1.75rem
}

.open .hs-overlay-open\\:translate-x-0 {
    --tw-translate-x: 0px;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.open .hs-overlay-open\\:opacity-100 {
    opacity: 1
}

.open .hs-overlay-open\\:duration-500 {
    transition-duration: .5s
}

@media (prefers-color-scheme: dark) {
    .dark\\:divide-gray-700>:not([hidden])~:not([hidden]) {
        --tw-divide-opacity: 1;
        border-color: rgb(55 65 81 / var(--tw-divide-opacity))
    }

    .dark\\:border-blue-500 {
        --tw-border-opacity: 1;
        border-color: rgb(59 130 246 / var(--tw-border-opacity))
    }

    .dark\\:border-gray-600 {
        --tw-border-opacity: 1;
        border-color: rgb(75 85 99 / var(--tw-border-opacity))
    }

    .dark\\:border-gray-700 {
        --tw-border-opacity: 1;
        border-color: rgb(55 65 81 / var(--tw-border-opacity))
    }

    .dark\\:border-neutral-700 {
        --tw-border-opacity: 1;
        border-color: rgb(64 64 64 / var(--tw-border-opacity))
    }

    .dark\\:border-red-500 {
        --tw-border-opacity: 1;
        border-color: rgb(239 68 68 / var(--tw-border-opacity))
    }

    .dark\\:border-teal-900 {
        --tw-border-opacity: 1;
        border-color: rgb(19 78 74 / var(--tw-border-opacity))
    }

    .dark\\:border-t-blue-500 {
        --tw-border-opacity: 1;
        border-top-color: rgb(59 130 246 / var(--tw-border-opacity))
    }

    .dark\\:border-t-green-500 {
        --tw-border-opacity: 1;
        border-top-color: rgb(34 197 94 / var(--tw-border-opacity))
    }

    .dark\\:border-t-red-500 {
        --tw-border-opacity: 1;
        border-top-color: rgb(239 68 68 / var(--tw-border-opacity))
    }

    .dark\\:bg-gray-700 {
        --tw-bg-opacity: 1;
        background-color: rgb(55 65 81 / var(--tw-bg-opacity))
    }

    .dark\\:bg-gray-800 {
        --tw-bg-opacity: 1;
        background-color: rgb(31 41 55 / var(--tw-bg-opacity))
    }

    .dark\\:bg-neutral-800 {
        --tw-bg-opacity: 1;
        background-color: rgb(38 38 38 / var(--tw-bg-opacity))
    }

    .dark\\:bg-neutral-900 {
        --tw-bg-opacity: 1;
        background-color: rgb(23 23 23 / var(--tw-bg-opacity))
    }

    .dark\\:bg-slate-800 {
        --tw-bg-opacity: 1;
        background-color: rgb(30 41 59 / var(--tw-bg-opacity))
    }

    .dark\\:bg-slate-900 {
        --tw-bg-opacity: 1;
        background-color: rgb(15 23 42 / var(--tw-bg-opacity))
    }

    .dark\\:bg-teal-800 {
        --tw-bg-opacity: 1;
        background-color: rgb(17 94 89 / var(--tw-bg-opacity))
    }

    .dark\\:bg-teal-800\\/30 {
        background-color: #115e594d
    }

    .dark\\:bg-opacity-80 {
        --tw-bg-opacity: .8
    }

    .dark\\:text-blue-500 {
        --tw-text-opacity: 1;
        color: rgb(59 130 246 / var(--tw-text-opacity))
    }

    .dark\\:text-gray-200 {
        --tw-text-opacity: 1;
        color: rgb(229 231 235 / var(--tw-text-opacity))
    }

    .dark\\:text-gray-300 {
        --tw-text-opacity: 1;
        color: rgb(209 213 219 / var(--tw-text-opacity))
    }

    .dark\\:text-gray-400 {
        --tw-text-opacity: 1;
        color: rgb(156 163 175 / var(--tw-text-opacity))
    }

    .dark\\:text-gray-500 {
        --tw-text-opacity: 1;
        color: rgb(107 114 128 / var(--tw-text-opacity))
    }

    .dark\\:text-green-500 {
        --tw-text-opacity: 1;
        color: rgb(34 197 94 / var(--tw-text-opacity))
    }

    .dark\\:text-neutral-200 {
        --tw-text-opacity: 1;
        color: rgb(229 229 229 / var(--tw-text-opacity))
    }

    .dark\\:text-neutral-400 {
        --tw-text-opacity: 1;
        color: rgb(163 163 163 / var(--tw-text-opacity))
    }

    .dark\\:text-neutral-500 {
        --tw-text-opacity: 1;
        color: rgb(115 115 115 / var(--tw-text-opacity))
    }

    .dark\\:text-red-500 {
        --tw-text-opacity: 1;
        color: rgb(239 68 68 / var(--tw-text-opacity))
    }

    .dark\\:text-slate-400 {
        --tw-text-opacity: 1;
        color: rgb(148 163 184 / var(--tw-text-opacity))
    }

    .dark\\:text-teal-400 {
        --tw-text-opacity: 1;
        color: rgb(45 212 191 / var(--tw-text-opacity))
    }

    .dark\\:text-white {
        --tw-text-opacity: 1;
        color: rgb(255 255 255 / var(--tw-text-opacity))
    }

    .dark\\:placeholder-gray-400::-moz-placeholder {
        --tw-placeholder-opacity: 1;
        color: rgb(156 163 175 / var(--tw-placeholder-opacity))
    }

    .dark\\:placeholder-gray-400::placeholder {
        --tw-placeholder-opacity: 1;
        color: rgb(156 163 175 / var(--tw-placeholder-opacity))
    }

    .dark\\:placeholder-neutral-500::-moz-placeholder {
        --tw-placeholder-opacity: 1;
        color: rgb(115 115 115 / var(--tw-placeholder-opacity))
    }

    .dark\\:placeholder-neutral-500::placeholder {
        --tw-placeholder-opacity: 1;
        color: rgb(115 115 115 / var(--tw-placeholder-opacity))
    }

    .dark\\:shadow-neutral-700\\/70 {
        --tw-shadow-color: rgb(64 64 64 / .7);
        --tw-shadow: var(--tw-shadow-colored)
    }

    .dark\\:shadow-slate-700\\/\\[\\.7\\] {
        --tw-shadow-color: rgb(51 65 85 / .7);
        --tw-shadow: var(--tw-shadow-colored)
    }

    .dark\\:before\\:bg-gray-400:before {
        content: var(--tw-content);
        --tw-bg-opacity: 1;
        background-color: rgb(156 163 175 / var(--tw-bg-opacity))
    }

    .dark\\:checked\\:border-blue-500:checked {
        --tw-border-opacity: 1;
        border-color: rgb(59 130 246 / var(--tw-border-opacity))
    }

    .dark\\:checked\\:bg-blue-500:checked {
        --tw-bg-opacity: 1;
        background-color: rgb(59 130 246 / var(--tw-bg-opacity))
    }

    .dark\\:checked\\:bg-blue-600:checked {
        --tw-bg-opacity: 1;
        background-color: rgb(37 99 235 / var(--tw-bg-opacity))
    }

    .dark\\:checked\\:before\\:bg-blue-200:checked:before {
        content: var(--tw-content);
        --tw-bg-opacity: 1;
        background-color: rgb(191 219 254 / var(--tw-bg-opacity))
    }

    .dark\\:hover\\:border-blue-400:hover {
        --tw-border-opacity: 1;
        border-color: rgb(96 165 250 / var(--tw-border-opacity))
    }

    .dark\\:hover\\:border-red-400:hover {
        --tw-border-opacity: 1;
        border-color: rgb(248 113 113 / var(--tw-border-opacity))
    }

    .dark\\:hover\\:bg-gray-900:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(17 24 39 / var(--tw-bg-opacity))
    }

    .dark\\:hover\\:bg-neutral-700:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(64 64 64 / var(--tw-bg-opacity))
    }

    .dark\\:hover\\:bg-slate-800:hover {
        --tw-bg-opacity: 1;
        background-color: rgb(30 41 59 / var(--tw-bg-opacity))
    }

    .dark\\:hover\\:text-blue-400:hover {
        --tw-text-opacity: 1;
        color: rgb(96 165 250 / var(--tw-text-opacity))
    }

    .dark\\:hover\\:text-blue-500:hover {
        --tw-text-opacity: 1;
        color: rgb(59 130 246 / var(--tw-text-opacity))
    }

    .dark\\:hover\\:text-green-400:hover {
        --tw-text-opacity: 1;
        color: rgb(74 222 128 / var(--tw-text-opacity))
    }

    .dark\\:hover\\:text-red-400:hover {
        --tw-text-opacity: 1;
        color: rgb(248 113 113 / var(--tw-text-opacity))
    }

    .dark\\:hover\\:text-red-500:hover {
        --tw-text-opacity: 1;
        color: rgb(239 68 68 / var(--tw-text-opacity))
    }

    .dark\\:hover\\:text-slate-300:hover {
        --tw-text-opacity: 1;
        color: rgb(203 213 225 / var(--tw-text-opacity))
    }

    .dark\\:hover\\:text-white:hover {
        --tw-text-opacity: 1;
        color: rgb(255 255 255 / var(--tw-text-opacity))
    }

    .dark\\:focus\\:border-blue-500:focus {
        --tw-border-opacity: 1;
        border-color: rgb(59 130 246 / var(--tw-border-opacity))
    }

    .dark\\:focus\\:outline-none:focus {
        outline: 2px solid transparent;
        outline-offset: 2px
    }

    .dark\\:focus\\:ring-1:focus {
        --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
        --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(1px + var(--tw-ring-offset-width)) var(--tw-ring-color);
        box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000)
    }

    .dark\\:focus\\:ring-blue-500:focus {
        --tw-ring-opacity: 1;
        --tw-ring-color: rgb(59 130 246 / var(--tw-ring-opacity))
    }

    .dark\\:focus\\:ring-gray-600:focus {
        --tw-ring-opacity: 1;
        --tw-ring-color: rgb(75 85 99 / var(--tw-ring-opacity))
    }

    .dark\\:focus\\:ring-gray-700:focus {
        --tw-ring-opacity: 1;
        --tw-ring-color: rgb(55 65 81 / var(--tw-ring-opacity))
    }

    .dark\\:focus\\:ring-neutral-600:focus {
        --tw-ring-opacity: 1;
        --tw-ring-color: rgb(82 82 82 / var(--tw-ring-opacity))
    }

    .dark\\:focus\\:ring-red-600:focus {
        --tw-ring-opacity: 1;
        --tw-ring-color: rgb(220 38 38 / var(--tw-ring-opacity))
    }

    .dark\\:focus\\:ring-offset-gray-800:focus {
        --tw-ring-offset-color: #1f2937
    }
}

@media (min-width: 640px) {
    .sm\\:mx-auto {
        margin-left: auto;
        margin-right: auto
    }

    .sm\\:mb-3 {
        margin-bottom: .75rem
    }

    .sm\\:mt-10 {
        margin-top: 2.5rem
    }

    .sm\\:w-auto {
        width: auto
    }

    .sm\\:w-full {
        width: 100%
    }

    .sm\\:max-w-lg {
        max-width: 32rem
    }

    .sm\\:flex-row {
        flex-direction: row
    }

    .sm\\:gap-3 {
        gap: .75rem
    }

    .sm\\:gap-x-4 {
        -moz-column-gap: 1rem;
        column-gap: 1rem
    }

    .sm\\:space-y-6>:not([hidden])~:not([hidden]) {
        --tw-space-y-reverse: 0;
        margin-top: calc(1.5rem * calc(1 - var(--tw-space-y-reverse)));
        margin-bottom: calc(1.5rem * var(--tw-space-y-reverse))
    }

    .sm\\:p-4 {
        padding: 1rem
    }

    .sm\\:px-6 {
        padding-left: 1.5rem;
        padding-right: 1.5rem
    }

    .sm\\:py-4 {
        padding-top: 1rem;
        padding-bottom: 1rem
    }

    .sm\\:py-6 {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem
    }

    .sm\\:text-3xl {
        font-size: 1.875rem;
        line-height: 2.25rem
    }

    .sm\\:text-4xl {
        font-size: 2.25rem;
        line-height: 2.5rem
    }

    .sm\\:text-9xl {
        font-size: 8rem;
        line-height: 1
    }

    .sm\\:text-sm {
        font-size: .875rem;
        line-height: 1.25rem
    }
}

@media (min-width: 768px) {
    .md\\:flex {
        display: flex
    }

    .md\\:items-center {
        align-items: center
    }

    .md\\:justify-between {
        justify-content: space-between
    }

    .md\\:p-10 {
        padding: 2.5rem
    }

    .md\\:p-5 {
        padding: 1.25rem
    }
}

@media (min-width: 1024px) {
    .lg\\:bottom-0 {
        bottom: 0
    }

    .lg\\:right-auto {
        right: auto
    }

    .lg\\:block {
        display: block
    }

    .lg\\:hidden {
        display: none
    }

    .lg\\:translate-x-0 {
        --tw-translate-x: 0px;
        transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
    }

    .lg\\:px-8 {
        padding-left: 2rem;
        padding-right: 2rem
    }

    .lg\\:py-14 {
        padding-top: 3.5rem;
        padding-bottom: 3.5rem
    }

    .lg\\:pl-64 {
        padding-left: 16rem
    }
}
'''

js_content = '''
var Rn = Object.defineProperty;
var nn = (E, e, T) => e in E ? Rn(E, e, {
	enumerable: !0,
	configurable: !0,
	writable: !0,
	value: T
}) : E[e] = T;
var wt = (E, e, T) => (nn(E, typeof e != "symbol" ? e + "" : e, T), T);
(function() {
	const e = document.createElement("link")
		.relList;
	if (e && e.supports && e.supports("modulepreload")) return;
	for (const r of document.querySelectorAll('link[rel="modulepreload"]'))
		t(r);
	new MutationObserver(r => {
			for (const R of r)
				if (R.type === "childList")
					for (const n of R.addedNodes) n.tagName === "LINK" &&
						n.rel === "modulepreload" && t(n)
		})
		.observe(document, {
			childList: !0,
			subtree: !0
		});

	function T(r) {
		const R = {};
		return r.integrity && (R.integrity = r.integrity), r.referrerPolicy &&
			(R.referrerPolicy = r.referrerPolicy), r.crossOrigin ===
			"use-credentials" ? R.credentials = "include" : r.crossOrigin ===
			"anonymous" ? R.credentials = "omit" : R.credentials =
			"same-origin", R
	}

	function t(r) {
		if (r.ep) return;
		r.ep = !0;
		const R = T(r);
		fetch(r.href, R)
	}
})();

function j() {}

function An(E, e) {
	for (const T in e) E[T] = e[T];
	return E
}

function cR(E) {
	return E()
}

function YT() {
	return Object.create(null)
}

function NE(E) {
	E.forEach(cR)
}

function zE(E) {
	return typeof E == "function"
}

function _e(E, e) {
	return E != E ? e == e : E !== e || E && typeof E == "object" || typeof E ==
		"function"
}
let ut;

function VT(E, e) {
	return E === e ? !0 : (ut || (ut = document.createElement("a")), ut.href =
		e, E === ut.href)
}

function sn(E) {
	return Object.keys(E)
		.length === 0
}

function fR(E, ...e) {
	if (E == null) {
		for (const t of e) t(void 0);
		return j
	}
	const T = E.subscribe(...e);
	return T.unsubscribe ? () => T.unsubscribe() : T
}

function uE(E) {
	let e;
	return fR(E, T => e = T)(), e
}

function eE(E, e, T) {
	E.$$.on_destroy.push(fR(e, T))
}

function Ut(E, e, T, t) {
	if (E) {
		const r = PR(E, e, T, t);
		return E[0](r)
	}
}

function PR(E, e, T, t) {
	return E[1] && t ? An(T.ctx.slice(), E[1](t(e))) : T.ctx
}

function mt(E, e, T, t) {
	if (E[2] && t) {
		const r = E[2](t(T));
		if (e.dirty === void 0) return r;
		if (typeof r == "object") {
			const R = [],
				n = Math.max(e.dirty.length, r.length);
			for (let s = 0; s < n; s += 1) R[s] = e.dirty[s] | r[s];
			return R
		}
		return e.dirty | r
	}
	return e.dirty
}

function ht(E, e, T, t, r, R) {
	if (r) {
		const n = PR(e, T, t, R);
		E.p(n, r)
	}
}

function Gt(E) {
	if (E.ctx.length > 32) {
		const e = [],
			T = E.ctx.length / 32;
		for (let t = 0; t < T; t++) e[t] = -1;
		return e
	}
	return -1
}

function OT(E, e, T) {
	return E.set(T), e
}

function l(E, e) {
	E.appendChild(e)
}

function V(E, e, T) {
	E.insertBefore(e, T || null)
}

function Y(E) {
	E.parentNode && E.parentNode.removeChild(E)
}

function nE(E, e) {
	for (let T = 0; T < E.length; T += 1) E[T] && E[T].d(e)
}

function f(E) {
	return document.createElement(E)
}

function OE(E) {
	return document.createElementNS("http://www.w3.org/2000/svg", E)
}

function te(E) {
	return document.createTextNode(E)
}

function $() {
	return te(" ")
}

function je() {
	return te("")
}

function Ne(E, e, T, t) {
	return E.addEventListener(e, T, t), () => E.removeEventListener(e, T, t)
}

function a(E, e, T) {
	T == null ? E.removeAttribute(e) : E.getAttribute(e) !== T && E.setAttribute(
		e, T)
}

function Sn(E) {
	let e;
	return {
		p(...T) {
			e = T, e.forEach(t => E.push(t))
		},
		r() {
			e.forEach(T => E.splice(E.indexOf(T), 1))
		}
	}
}

function on(E) {
	return Array.from(E.childNodes)
}

function Le(E, e) {
	e = "" + e, E.data !== e && (E.data = e)
}

function Ye(E, e) {
	E.value = e ? ? ""
}

function ct(E, e, T, t) {
	T == null ? E.style.removeProperty(e) : E.style.setProperty(e, T, t ?
		"important" : "")
}

function WT(E, e, T) {
	for (let t = 0; t < E.options.length; t += 1) {
		const r = E.options[t];
		if (r.__value === e) {
			r.selected = !0;
			return
		}
	}(!T || e !== void 0) && (E.selectedIndex = -1)
}

function On(E) {
	const e = E.querySelector(":checked");
	return e && e.__value
}
let Ot;

function st(E) {
	Ot = E
}

function an() {
	if (!Ot) throw new Error("Function called outside component initialization");
	return Ot
}

function DR(E) {
	an()
		.$$.on_mount.push(E)
}
const jE = [],
	iT = [];
let et = [];
const aT = [],
	In = Promise.resolve();
let IT = !1;

function Nn() {
	IT || (IT = !0, In.then(dR))
}

function dt(E) {
	et.push(E)
}

function ln(E) {
	aT.push(E)
}
const $t = new Set;
let JE = 0;

function dR() {
	if (JE !== 0) return;
	const E = Ot;
	do {
		try {
			for (; JE < jE.length;) {
				const e = jE[JE];
				JE++, st(e), _n(e.$$)
			}
		} catch (e) {
			throw jE.length = 0, JE = 0, e
		}
		for (st(null), jE.length = 0, JE = 0; iT.length;) iT.pop()();
		for (let e = 0; e < et.length; e += 1) {
			const T = et[e];
			$t.has(T) || ($t.add(T), T())
		}
		et.length = 0
	} while (jE.length);
	for (; aT.length;) aT.pop()();
	IT = !1, $t.clear(), st(E)
}

function _n(E) {
	if (E.fragment !== null) {
		E.update(), NE(E.before_update);
		const e = E.dirty;
		E.dirty = [-1], E.fragment && E.fragment.p(E.ctx, e), E.after_update.forEach(
			dt)
	}
}

function Ln(E) {
	const e = [],
		T = [];
	et.forEach(t => E.indexOf(t) === -1 ? e.push(t) : T.push(t)), T.forEach(t =>
		t()), et = e
}
const ft = new Set;
let vE;

function Ge() {
	vE = {
		r: 0,
		c: [],
		p: vE
	}
}

function ge() {
	vE.r || NE(vE.c), vE = vE.p
}

function m(E, e) {
	E && E.i && (ft.delete(E), E.i(e))
}

function y(E, e, T, t) {
	if (E && E.o) {
		if (ft.has(E)) return;
		ft.add(E), vE.c.push(() => {
			ft.delete(E), t && (T && E.d(1), t())
		}), E.o(e)
	} else t && t()
}

function De(E) {
	return (E == null ? void 0 : E.length) !== void 0 ? E : Array.from(E)
}

function Cn(E, e) {
	E.d(1), e.delete(E.key)
}

function un(E, e, T, t, r, R, n, s, S, A, o, i) {
	let _ = E.length,
		c = R.length,
		P = _;
	const p = {};
	for (; P--;) p[E[P].key] = P;
	const C = [],
		L = new Map,
		I = new Map,
		u = [];
	for (P = c; P--;) {
		const O = i(r, R, P),
			N = T(O);
		let D = n.get(N);
		D ? t && u.push(() => D.p(O, e)) : (D = A(N, O), D.c()), L.set(N, C[P] =
			D), N in p && I.set(N, Math.abs(P - p[N]))
	}
	const H = new Set,
		b = new Set;

	function M(O) {
		m(O, 1), O.m(s, o), n.set(O.key, O), o = O.first, c--
	}
	for (; _ && c;) {
		const O = C[c - 1],
			N = E[_ - 1],
			D = O.key,
			B = N.key;
		O === N ? (o = O.first, _--, c--) : L.has(B) ? !n.has(D) || H.has(D) ?
			M(O) : b.has(B) ? _-- : I.get(D) > I.get(B) ? (b.add(D), M(O)) : (H
				.add(B), _--) : (S(N, n), _--)
	}
	for (; _--;) {
		const O = E[_];
		L.has(O.key) || S(O, n)
	}
	for (; c;) M(C[c - 1]);
	return NE(u), C
}

function cn(E, e, T) {
	const t = E.$$.props[e];
	t !== void 0 && (E.$$.bound[t] = T, T(E.$$.ctx[t]))
}

function K(E) {
	E && E.c()
}

function X(E, e, T) {
	const {
		fragment: t,
		after_update: r
	} = E.$$;
	t && t.m(e, T), dt(() => {
		const R = E.$$.on_mount.map(cR)
			.filter(zE);
		E.$$.on_destroy ? E.$$.on_destroy.push(...R) : NE(R), E.$$.on_mount = []
	}), r.forEach(dt)
}

function k(E, e) {
	const T = E.$$;
	T.fragment !== null && (Ln(T.after_update), NE(T.on_destroy), T.fragment &&
		T.fragment.d(e), T.on_destroy = T.fragment = null, T.ctx = [])
}

function fn(E, e) {
	E.$$.dirty[0] === -1 && (jE.push(E), Nn(), E.$$.dirty.fill(0)), E.$$.dirty[
		e / 31 | 0] |= 1 << e % 31
}

function Ce(E, e, T, t, r, R, n, s = [-1]) {
	const S = Ot;
	st(E);
	const A = E.$$ = {
		fragment: null,
		ctx: [],
		props: R,
		update: j,
		not_equal: r,
		bound: YT(),
		on_mount: [],
		on_destroy: [],
		on_disconnect: [],
		before_update: [],
		after_update: [],
		context: new Map(e.context || (S ? S.$$.context : [])),
		callbacks: YT(),
		dirty: s,
		skip_bound: !1,
		root: e.target || S.$$.root
	};
	n && n(A.root);
	let o = !1;
	if (A.ctx = T ? T(E, e.props || {}, (i, _, ...c) => {
			const P = c.length ? c[0] : _;
			return A.ctx && r(A.ctx[i], A.ctx[i] = P) && (!A.skip_bound &&
				A.bound[i] && A.bound[i](P), o && fn(E, i)), _
		}) : [], A.update(), o = !0, NE(A.before_update), A.fragment = t ? t(A.ctx) :
		!1, e.target) {
		if (e.hydrate) {
			const i = on(e.target);
			A.fragment && A.fragment.l(i), i.forEach(Y)
		} else A.fragment && A.fragment.c();
		e.intro && m(E.$$.fragment), X(E, e.target, e.anchor), dR()
	}
	st(S)
}
class ue {
	constructor() {
		wt(this, "$$");
		wt(this, "$$set")
	}
	$destroy() {
		k(this, 1), this.$destroy = j
	}
	$on(e, T) {
		if (!zE(T)) return j;
		const t = this.$$.callbacks[e] || (this.$$.callbacks[e] = []);
		return t.push(T), () => {
			const r = t.indexOf(T);
			r !== -1 && t.splice(r, 1)
		}
	}
	$set(e) {
		this.$$set && !sn(e) && (this.$$.skip_bound = !0, this.$$set(e),
			this.$$.skip_bound = !1)
	}
}
const Pn = "4";
typeof window < "u" && (window.__svelte || (window.__svelte = {
		v: new Set
	}))
	.v.add(Pn);
const qE = [];

function iE(E, e = j) {
	let T;
	const t = new Set;

	function r(s) {
		if (_e(E, s) && (E = s, T)) {
			const S = !qE.length;
			for (const A of t) A[1](), qE.push(A, E);
			if (S) {
				for (let A = 0; A < qE.length; A += 2) qE[A][0](qE[A + 1]);
				qE.length = 0
			}
		}
	}

	function R(s) {
		r(s(E))
	}

	function n(s, S = j) {
		const A = [s, S];
		return t.add(A), t.size === 1 && (T = e(r, R) || j), s(E), () => {
			t.delete(A), t.size === 0 && T && (T(), T = null)
		}
	}
	return {
		set: r,
		update: R,
		subscribe: n
	}
}
let GE = iE(""),
	YE = iE([]),
	LT = iE(null),
	gt = iE(null),
	Ht = iE(!1),
	St = iE(!1),
	DE = iE("chat"),
	CT = iE([]),
	Et = iE(""),
	pR = iE(!1),
	BE = iE(""),
	VE = iE({
		debug: !0,
		logo: "",
		title: "Welcome to Jenasi.AI",
		subtitle: "Loading...",
		show_training_data: !0,
		suggested_questions: !0,
		sql: !0,
		table: !0,
		csv_download: !0,
		chart: !0,
		redraw_chart: !0,
		auto_fix_sql: !0,
		ask_results_correct: !0,
		followup_questions: !0,
		summarization: !0,
		function_generation: !0,
		version: ""
	}),
	bt = iE(null),
	MR = iE([]);

function UR() {
	YE.set([]), Ht.set(!1), St.set(!1)
}
async function uT(E) {
	let e = uE(VE),
		T = yn();
	if (Se({
		type: "user_question",
		question: E
	}), Ht.set(!0), T) {
		const n = await Pe("generate_rewritten_question", "GET", {
			last_question: T,
			new_question: E
		});
		n.type === "rewritten_question" && n.question !== E && (Se(n), E =
			n.question)
	}
	const t = await Pe("get_function", "GET", {
		question: E
	});
	let r;
	if (e.function_generation && t.type === "function") Se(t), r = t.id, GE
		.set(t.id), Et.set(t.function.instantiated_sql);
	else {
		const n = await Pe("generate_sql", "GET", {
			question: E
		});
		if (Se(n), n.type !== "sql") return;
		window.location.hash = n.id, GE.set(n.id), Et.set(n.text), r = n.id
	}
	const R = await Pe("run_sql", "GET", {
		id: r
	});
	if (Se(R), R.type === "df") {
		if (R.should_generate_chart) {
			const n = await Pe("generate_plotly_figure", "GET", {
				id: R.id
			});
			if (Se(n), n.type !== "plotly_figure") return;
			CT.update(s => [...s, {
				question: E,
				id: n.id
			}])
		}
		if (e.summarization) {
			const n = await Pe("generate_summary", "GET", {
				id: r
			});
			Se(n)
		}
		Se({
			type: "feedback_question"
		}), Se({
			type: "feedback_buttons"
		})
	}
}
async function Dn(E) {
	let e = uE(VE);
	if (Se(E), E.type !== "sql") return;
	window.location.hash = E.id, GE.set(E.id), Et.set(E.text);
	const T = await Pe("run_sql", "GET", {
		id: E.id
	});
	if (Se(T), T.type !== "df") return;
	const t = await Pe("generate_plotly_figure", "GET", {
		id: T.id
	});
	if (Se(t), t.type === "plotly_figure") {
		if (e.summarization) {
			const r = await Pe("generate_summary", "GET", {
				id: t.id
			});
			Se(r)
		}
		Se({
			type: "feedback_question"
		}), Se({
			type: "feedback_buttons"
		})
	}
}

function dn(E) {
	Se({
			type: "user_question",
			question: "Re-run the SQL"
		}), Pe("run_sql", "GET", {
			id: E
		})
		.then(Se)
		.then(e => {
			e.type === "df" && Pe("generate_plotly_figure", "GET", {
					id: e.id
				})
				.then(Se)
				.then(T => {
					T.type === "plotly_figure" && Pe(
							"generate_followup_questions", "GET", {
								id: T.id
							})
						.then(Se)
				})
		})
}

function mR() {
	Pe("get_question_history", "GET", [])
		.then(gn)
}

function pn() {
	Pe("get_config", "GET", [])
		.then(Gn)
}

function cT() {
	window.location.hash = "functions", DE.set("functions"), Pe(
			"get_all_functions", "GET", [])
		.then(mn)
}

function hR() {
	window.location.hash = "training-data", DE.set("training-data"), Pe(
			"get_training_data", "GET", [])
		.then(pt)
}

function it() {
	window.location.hash = "", DE.set("chat"), UR(), uE(LT) === null && Pe(
			"generate_questions", "GET", [])
		.then(hn), mR()
}

function Mn(E) {
	window.location.hash = E, DE.set("chat"), UR(), Ht.set(!0), Pe(
			"load_question", "GET", {
				id: E
			})
		.then(Se)
}

function Un(E) {
	gt.set(null), Pe("remove_training_data", "POST", {
			id: E
		})
		.then(e => {
			Pe("get_training_data", "GET", [])
				.then(pt)
		})
}

function Se(E) {
	return E.type === "not_logged_in" ? (bt.set(E.html), DE.set("login"), E) :
		(YE.update(e => [...e, E]), bn(), E)
}

function pt(E) {
	return gt.set(E), E.type === "df" ? JSON.parse(E.df)
		.length === 0 && DE.set("no-training-data") : E.type ===
		"not_logged_in" && (bt.set(E.html), DE.set("login")), E
}

function mn(E) {
	return E.type === "functions" && MR.set(E.functions), E
}

function hn(E) {
	return LT.set(E), E
}

function Gn(E) {
	return E.type === "config" ? (VE.set(E.config), E.config.debug && xn()) : E
		.type === "not_logged_in" && (bt.set(E.html), DE.set("login")), E
}

function gn(E) {
	return E.type === "question_history" && CT.set(E.questions), E
}

function Hn(E, e) {
	gt.set(null);
	let T = {};
	T[e] = E, Pe("train", "POST", T)
		.then(pt)
		.then(t => {
			t.type !== "error" && Pe("get_training_data", "GET", [])
				.then(pt)
		})
}
async function Pe(E, e, T) {
	try {
		St.set(!0);
		let t = "",
			r;
		if (e === "GET") t = Object.entries(T)
			.filter(([n, s]) => n !== "endpoint" && n !== "addMessage")
			.map(([n, s]) =>
				`${encodeURIComponent(n)}=${encodeURIComponent(s)}`)
			.join("&"), r = await fetch(`/api/v0/${E}?${t}`);
		else {
			let n = JSON.stringify(T);
			r = await fetch(`/api/v0/${E}`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: n
			})
		}
		if (!r.ok) throw new Error(
			"The server returned an error. See the server logs for more details. If you are running in Colab, this function is probably not supported. Please try running in a local environment."
		);
		const R = await r.json();
		return St.set(!1), R
	} catch (t) {
		return St.set(!1), {
			type: "error",
			error: String(t)
		}
	}
}

function bn() {
	setTimeout(() => {
		window.scrollTo({
			top: document.body.scrollHeight,
			behavior: "smooth"
		})
	}, 100)
}

function yn() {
	let E = uE(YE),
		e = E.findLast(T => T.type === "rewritten_question");
	return e || (e = E.findLast(T => T.type === "user_question")), e && (e.type ===
			"rewritten_question" || e.type === "user_question") ? e.question :
		null
}

function fT() {
	let E = uE(YE),
		e = E.find(T => T.type === "user_question");
	if (e && e.type === "user_question") {
		let T = E.findLast(t => t.type === "sql");
		if (T && T.type === "sql") return {
			question: e.question,
			sql: T.text
		}
	}
	return null
}

function at(E) {
	YE.update(e => e.filter(T => T.type !== E))
}

function Bn(E) {
	Pe("fix_sql", "POST", {
			id: uE(GE),
			error: E
		})
		.then(Dn)
}

function vn(E) {
	let T = uE(YE)
		.find(t => t.type === "user_question");
	T && T.type === "user_question" && (Pe("update_sql", "POST", {
			id: uE(GE),
			sql: E
		})
		.then(Se)
		.then(t => {
			t.type === "sql" && (Et.set(t.text), Pe("run_sql", "GET", {
					id: t.id
				})
				.then(Se)
				.then(r => {
					r.type === "df" ? JSON.parse(r.df)
						.length > 1 ? Pe(
							"generate_plotly_figure", "GET", {
								id: r.id
							})
						.then(Se)
						.then(n => {
							Se({
								type: "feedback_question"
							}), Se({
								type: "feedback_buttons"
							})
						}) : (Se({
							type: "feedback_question"
						}), Se({
							type: "feedback_buttons"
						})) : (Se({
							type: "feedback_question"
						}), Se({
							type: "feedback_buttons"
						}))
				}))
		}), at("user_sql"))
}

function Fn() {
	Se({
		type: "chart_modification"
	})
}

function Yn() {
	at("feedback_buttons"), Se({
			type: "feedback_correct"
		}), fT() ? Pe("create_function", "GET", {
			id: uE(GE)
		})
		.then(Se) : console.log("No Question-SQL Found")
}

function Vn(E, e) {
	Pe("update_function", "POST", {
		old_function_name: E,
		updated_function: e
	})
}

function Wn(E) {
	Pe("delete_function", "POST", {
			function_name: E
		})
		.finally(() => {
			cT()
		})
}

function wn() {
	at("feedback_buttons"), Se({
		type: "feedback_correct"
	});
	let E = fT();
	E && (Pe("train", "POST", E), Pe("generate_followup_questions", "GET", {
			id: uE(GE)
		})
		.then(Se))
}

function wT() {
	at("feedback_buttons"), Se({
		type: "feedback_incorrect"
	}), Se({
		type: "user_sql"
	})
}

function $n(E) {
	at("chart_modification"), Se({
			type: "user_question",
			question: "Update the chart with these instructions: " + E
		}), Pe("generate_plotly_figure", "GET", {
			id: uE(GE),
			chart_instructions: E
		})
		.then(Se)
}

function xn() {
	var E = new WebSocket("ws://" + window.location.host + "/api/v0/log");
	E.onopen = function() {
		console.log("Connected to WebSocket server at /log.")
	}, E.onmessage = function(e) {
		console.log("Received message:", e.data);
		try {
			var T = JSON.parse(e.data)
		} catch (r) {
			console.error("Error parsing JSON:", r);
			return
		}
		var t = document.getElementById("log-contents");
		t && (t.innerHTML += "<details> <summary>" + T.title +
			"</summary> " + JSON.stringify(T.message) +
			"</details> <br>")
	}, E.onclose = function(e) {
		console.log("WebSocket connection closed:", e)
	}, E.onerror = function(e) {
		console.error("WebSocket error:", e)
	}
}

function $T(E, e, T) {
	const t = E.slice();
	return t[3] = e[T], t
}

function xT(E) {
	let e, T, t, r;
	return {
		c() {
			e = f("li"), T = f("button"), T.innerHTML =
				`<svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5"></path></svg>
              Functions`,
				a(T, "class",
					"flex items-center gap-x-3 py-2 px-3 text-sm text-slate-700 rounded-md hover:bg-gray-100 dark:hover:bg-gray-900 dark:text-slate-400 dark:hover:text-slate-300 border border-gray-200 dark:border-gray-700 w-full"
				)
		},
		m(R, n) {
			V(R, e, n), l(e, T), t || (r = Ne(T, "click", cT), t = !0)
		},
		d(R) {
			R && Y(e), t = !1, r()
		}
	}
}

function XT(E) {
	let e, T, t, r;
	return {
		c() {
			e = f("li"), T = f("button"), T.innerHTML =
				`<svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5"></path></svg>
              Training Data`,
				a(T, "class",
					"flex items-center gap-x-3 py-2 px-3 text-sm text-slate-700 rounded-md hover:bg-gray-100 dark:hover:bg-gray-900 dark:text-slate-400 dark:hover:text-slate-300 border border-gray-200 dark:border-gray-700 w-full"
				)
		},
		m(R, n) {
			V(R, e, n), l(e, T), t || (r = Ne(T, "click", hR), t = !0)
		},
		d(R) {
			R && Y(e), t = !1, r()
		}
	}
}

function kT(E) {
	let e, T, t, r, R, n = E[3].question + "",
		s, S, A, o;

	function i() {
		return E[2](E[3])
	}
	return {
		c() {
			e = f("li"), T = f("button"), t = OE("svg"), r = OE("path"), R = $(),
				s = te(n), S = $(), a(r, "stroke-linecap", "round"), a(r,
					"stroke-linejoin", "round"), a(r, "d",
					"M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 01.865-.501 48.172 48.172 0 003.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z"
				), a(t, "class", "w-3.5 h-3.5"), a(t, "fill", "none"), a(t,
					"stroke", "currentColor"), a(t, "stroke-width", "1.5"), a(t,
					"viewBox", "0 0 24 24"), a(t, "xmlns",
					"http://www.w3.org/2000/svg"), a(t, "aria-hidden", "true"),
				a(T, "class",
					"flex items-center text-left gap-x-3 py-2 px-3 text-sm text-slate-700 rounded-md hover:bg-gray-100 dark:hover:bg-gray-900 dark:text-slate-400 dark:hover:text-slate-300"
				)
		},
		m(_, c) {
			V(_, e, c), l(e, T), l(T, t), l(t, r), l(T, R), l(T, s), l(e, S), A ||
				(o = Ne(T, "click", i), A = !0)
		},
		p(_, c) {
			E = _, c & 2 && n !== (n = E[3].question + "") && Le(s, n)
		},
		d(_) {
			_ && Y(e), A = !1, o()
		}
	}
}

function Xn(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _, c, P, p, C, L, I, u, H, b, M = E[0]
		.version + "",
		O, N, D, B, h, G = E[0].function_generation && xT(),
		F = E[0].show_training_data && XT(),
		W = De(E[1]),
		x = [];
	for (let J = 0; J < W.length; J += 1) x[J] = kT($T(E, W, J));
	return {
		c() {
			e = f("div"), T = f("nav"), t = f("div"), r = f("img"), n = $(), s =
				f("div"), s.innerHTML =
				'<button type="button" class="w-8 h-8 inline-flex justify-center items-center gap-2 rounded-md text-gray-700 align-middle focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 transition-all dark:text-gray-400 dark:focus:ring-offset-gray-800" data-hs-overlay="#application-sidebar" aria-controls="application-sidebar" aria-label="Toggle navigation"><svg class="w-4 h-4" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"></path></svg> <span class="sr-only">Sidebar</span></button>',
				S = $(), A = f("div"), o = f("ul"), G && G.c(), i = $(), F && F
				.c(), _ = $(), c = f("li"), P = f("button"), P.innerHTML =
				`<svg class="w-3.5 h-3.5" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" clip-rule="evenodd" d="M8 2C8.47339 2 8.85714 2.38376 8.85714 2.85714V7.14286L13.1429 7.14286C13.6162 7.14286 14 7.52661 14 8C14 8.47339 13.6162 8.85714 13.1429 8.85714L8.85714 8.85715V13.1429C8.85714 13.6162 8.47339 14 8 14C7.52661 14 7.14286 13.6162 7.14286 13.1429V8.85715L2.85714 8.85715C2.38376 8.85715 2 8.4734 2 8.00001C2 7.52662 2.38376 7.14287 2.85714 7.14287L7.14286 7.14286V2.85714C7.14286 2.38376 7.52661 2 8 2Z" fill="currentColor"></path></svg>
              New question`,
				p = $();
			for (let J = 0; J < x.length; J += 1) x[J].c();
			C = $(), L = f("div"), I = f("div"), u = f("p"), H = f("span"), b =
				te(`
            v`), O = te(M), N = $(), D = f("div"), D.innerHTML =
				`<a class="flex justify-between items-center gap-x-3 py-2 px-3 text-sm text-slate-700 rounded-md hover:bg-gray-100 dark:hover:bg-gray-900 dark:text-slate-400 dark:hover:text-slate-300" href="/auth/logout">Sign out
            <svg class="w-3.5 h-3.5" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M10 3.5a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v9a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-2a.5.5 0 0 1 1 0v2A1.5 1.5 0 0 1 9.5 14h-8A1.5 1.5 0 0 1 0 12.5v-9A1.5 1.5 0 0 1 1.5 2h8A1.5 1.5 0 0 1 11 3.5v2a.5.5 0 0 1-1 0v-2z"></path><path fill-rule="evenodd" d="M4.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H14.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"></path></svg></a>`,
				a(r, "class", "w-28 h-auto"), VT(r.src, R = E[0].logo) || a(r,
					"src", R), a(r, "alt", "Vanna Logo"), a(s, "class",
					"lg:hidden"), a(t, "class",
					"flex items-center justify-between py-4 pr-4 pl-7"), a(P,
					"class",
					"w-full py-2 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none"
				), a(o, "class", "space-y-1.5 p-4"), a(A, "class", "h-full"), a(
					H, "class", "block w-1.5 h-1.5 rounded-full bg-green-600"),
				a(u, "class",
					"inline-flex items-center gap-x-2 text-xs text-green-600"),
				a(I, "class", "py-2.5 px-7"), a(D, "class",
					"p-4 border-t border-gray-200 dark:border-gray-700"), a(L,
					"class", "mt-auto"), a(T, "class",
					"hs-accordion-group w-full h-full flex flex-col"), a(T,
					"data-hs-accordion-always-open", ""), a(e, "id",
					"application-sidebar"), a(e, "class",
					"hs-overlay hs-overlay-open:translate-x-0 -translate-x-full transition-all duration-300 transform hidden fixed top-0 left-0 bottom-0 z-[60] w-64 bg-white border-r border-gray-200 overflow-y-auto scrollbar-y lg:block lg:translate-x-0 lg:right-auto lg:bottom-0 dark:scrollbar-y dark:bg-slate-900 dark:border-gray-700"
				)
		},
		m(J, oe) {
			V(J, e, oe), l(e, T), l(T, t), l(t, r), l(t, n), l(t, s), l(T, S),
				l(T, A), l(A, o), G && G.m(o, null), l(o, i), F && F.m(o, null),
				l(o, _), l(o, c), l(c, P), l(o, p);
			for (let z = 0; z < x.length; z += 1) x[z] && x[z].m(o, null);
			l(T, C), l(T, L), l(L, I), l(I, u), l(u, H), l(u, b), l(u, O), l(L,
				N), l(L, D), B || (h = Ne(P, "click", it), B = !0)
		},
		p(J, [oe]) {
			if (oe & 1 && !VT(r.src, R = J[0].logo) && a(r, "src", R), J[0].function_generation ?
				G || (G = xT(), G.c(), G.m(o, i)) : G && (G.d(1), G = null), J[
					0].show_training_data ? F || (F = XT(), F.c(), F.m(o, _)) :
				F && (F.d(1), F = null), oe & 2) {
				W = De(J[1]);
				let z;
				for (z = 0; z < W.length; z += 1) {
					const Oe = $T(J, W, z);
					x[z] ? x[z].p(Oe, oe) : (x[z] = kT(Oe), x[z].c(), x[z].m(o,
						null))
				}
				for (; z < x.length; z += 1) x[z].d(1);
				x.length = W.length
			}
			oe & 1 && M !== (M = J[0].version + "") && Le(O, M)
		},
		i: j,
		o: j,
		d(J) {
			J && Y(e), G && G.d(), F && F.d(), nE(x, J), B = !1, h()
		}
	}
}

function kn(E, e, T) {
	let t, r;
	return eE(E, VE, n => T(0, t = n)), eE(E, CT, n => T(1, r = n)), [t, r, n => {
		Mn(n.id)
	}]
}
class Kn extends ue {
	constructor(e) {
		super(), Ce(this, e, kn, Xn, _e, {})
	}
}
var Jn = typeof globalThis < "u" ? globalThis : typeof window < "u" ? window :
	typeof global < "u" ? global : typeof self < "u" ? self : {};

function qn(E) {
	return E && E.__esModule && Object.prototype.hasOwnProperty.call(E,
		"default") ? E.default : E
}
var Qn = {
	exports: {}
}; /*! For license information please see preline.js.LICENSE.txt */
(function(E, e) {
	(function(T, t) {
		E.exports = t()
	})(self, function() {
		return (() => {
			var T = {
					661: (n, s, S) => {
						function A(p) {
							return A = typeof Symbol ==
								"function" && typeof Symbol
								.iterator == "symbol" ?
								function(C) {
									return typeof C
								} : function(C) {
									return C && typeof Symbol ==
										"function" && C.constructor ===
										Symbol && C !==
										Symbol.prototype ?
										"symbol" : typeof C
								}, A(p)
						}

						function o(p, C) {
							for (var L = 0; L < C.length; L++) {
								var I = C[L];
								I.enumerable = I.enumerable ||
									!1, I.configurable = !0,
									"value" in I && (I.writable = !
										0), Object.defineProperty(
										p, I.key, I)
							}
						}

						function i(p, C) {
							return i = Object.setPrototypeOf ||
								function(L, I) {
									return L.__proto__ = I,
										L
								}, i(p, C)
						}

						function _(p, C) {
							if (C && (A(C) === "object" ||
								typeof C == "function"))
								return C;
							if (C !== void 0) throw new TypeError(
								"Derived constructors may only return object or undefined"
							);
							return function(L) {
								if (L === void 0) throw new ReferenceError(
									"this hasn't been initialised - super() hasn't been called"
								);
								return L
							}(p)
						}

						function c(p) {
							return c = Object.setPrototypeOf ?
								Object.getPrototypeOf :
								function(C) {
									return C.__proto__ ||
										Object.getPrototypeOf(
											C)
								}, c(p)
						}
						var P = function(p) {
							(function(M, O) {
								if (typeof O !=
									"function" && O !==
									null) throw new TypeError(
									"Super expression must either be null or a function"
								);
								M.prototype =
									Object.create(O &&
										O.prototype, {
											constructor: {
												value: M,
												writable:
													!
													0,
												configurable:
													!
													0
											}
										}), Object.defineProperty(
										M,
										"prototype", {
											writable:
												!1
										}), O && i(
										M, O)
							})(b, p);
							var C, L, I, u, H = (I = b,
								u = function() {
									if (typeof Reflect >
										"u" || !
										Reflect.construct ||
										Reflect.construct
										.sham)
										return !1;
									if (typeof Proxy ==
										"function")
										return !0;
									try {
										return Boolean
											.prototype
											.valueOf
											.call(
												Reflect
												.construct(
													Boolean,
													[],
													function() {}
												)),
											!0
									} catch {
										return !1
									}
								}(),
								function() {
									var M, O = c(I);
									if (u) {
										var N = c(
												this
											)
											.constructor;
										M = Reflect
											.construct(
												O,
												arguments,
												N)
									} else M = O.apply(
										this,
										arguments
									);
									return _(this,
										M)
								});

							function b() {
								return function(M, O) {
									if (!(M instanceof O))
										throw new TypeError(
											"Cannot call a class as a function"
										)
								}(this, b), H.call(
									this,
									".hs-accordion"
								)
							}
							return C = b, (L = [{
									key: "init",
									value: function() {
										var
											M =
											this;
										document
											.addEventListener(
												"click",
												function(
													O
												) {
													var
														N =
														O
														.target,
														D =
														N
														.closest(
															M
															.selector
														),
														B =
														N
														.closest(
															".hs-accordion-toggle"
														),
														h =
														N
														.closest(
															".hs-accordion-group"
														);
													D
														&&
														h &&
														B &&
														(
															M
															._hideAll(
																D
															),
															M
															.show(
																D
															)
														)
												}
											)
									}
								}, {
									key: "show",
									value: function(
										M) {
										var
											O =
											this;
										if (
											M
											.classList
											.contains(
												"active"
											)
										)
											return this
												.hide(
													M
												);
										M.classList
											.add(
												"active"
											);
										var
											N =
											M
											.querySelector(
												".hs-accordion-content"
											);
										N.style
											.display =
											"block",
											N
											.style
											.height =
											0,
											setTimeout(
												function() {
													N
														.style
														.height =
														""
														.concat(
															N
															.scrollHeight,
															"px"
														)
												}
											),
											this
											.afterTransition(
												N,
												function() {
													M
														.classList
														.contains(
															"active"
														) &&
														(
															N
															.style
															.height =
															"",
															O
															._fireEvent(
																"open",
																M
															),
															O
															._dispatch(
																"open.hs.accordion",
																M,
																M
															)
														)
												}
											)
									}
								}, {
									key: "hide",
									value: function(
										M) {
										var
											O =
											this,
											N =
											M
											.querySelector(
												".hs-accordion-content"
											);
										N.style
											.height =
											""
											.concat(
												N
												.scrollHeight,
												"px"
											),
											setTimeout(
												function() {
													N
														.style
														.height =
														0
												}
											),
											this
											.afterTransition(
												N,
												function() {
													M
														.classList
														.contains(
															"active"
														) ||
														(
															N
															.style
															.display =
															"",
															O
															._fireEvent(
																"hide",
																M
															),
															O
															._dispatch(
																"hide.hs.accordion",
																M,
																M
															)
														)
												}
											),
											M
											.classList
											.remove(
												"active"
											)
									}
								}, {
									key: "_hideAll",
									value: function(
										M) {
										var
											O =
											this,
											N =
											M
											.closest(
												".hs-accordion-group"
											);
										N.hasAttribute(
												"data-hs-accordion-always-open"
											) ||
											N
											.querySelectorAll(
												this
												.selector
											)
											.forEach(
												function(
													D
												) {
													M
														!==
														D &&
														O
														.hide(
															D
														)
												}
											)
									}
								}]) && o(C.prototype, L),
								Object.defineProperty(C,
									"prototype", {
										writable: !1
									}), b
						}(S(765)
							.Z);
						window.HSAccordion = new P,
							document.addEventListener(
								"load", window.HSAccordion.init()
							)
					},
					795: (n, s, S) => {
						function A(C) {
							return A = typeof Symbol ==
								"function" && typeof Symbol
								.iterator == "symbol" ?
								function(L) {
									return typeof L
								} : function(L) {
									return L && typeof Symbol ==
										"function" && L.constructor ===
										Symbol && L !==
										Symbol.prototype ?
										"symbol" : typeof L
								}, A(C)
						}

						function o(C, L) {
							(L == null || L > C.length) &&
							(L = C.length);
							for (var I = 0, u = new Array(L); I <
								L; I++) u[I] = C[I];
							return u
						}

						function i(C, L) {
							for (var I = 0; I < L.length; I++) {
								var u = L[I];
								u.enumerable = u.enumerable ||
									!1, u.configurable = !0,
									"value" in u && (u.writable = !
										0), Object.defineProperty(
										C, u.key, u)
							}
						}

						function _(C, L) {
							return _ = Object.setPrototypeOf ||
								function(I, u) {
									return I.__proto__ = u,
										I
								}, _(C, L)
						}

						function c(C, L) {
							if (L && (A(L) === "object" ||
								typeof L == "function"))
								return L;
							if (L !== void 0) throw new TypeError(
								"Derived constructors may only return object or undefined"
							);
							return function(I) {
								if (I === void 0) throw new ReferenceError(
									"this hasn't been initialised - super() hasn't been called"
								);
								return I
							}(C)
						}

						function P(C) {
							return P = Object.setPrototypeOf ?
								Object.getPrototypeOf :
								function(L) {
									return L.__proto__ ||
										Object.getPrototypeOf(
											L)
								}, P(C)
						}
						var p = function(C) {
							(function(O, N) {
								if (typeof N !=
									"function" && N !==
									null) throw new TypeError(
									"Super expression must either be null or a function"
								);
								O.prototype =
									Object.create(N &&
										N.prototype, {
											constructor: {
												value: O,
												writable:
													!
													0,
												configurable:
													!
													0
											}
										}), Object.defineProperty(
										O,
										"prototype", {
											writable:
												!1
										}), N && _(
										O, N)
							})(M, C);
							var L, I, u, H, b = (u = M,
								H = function() {
									if (typeof Reflect >
										"u" || !
										Reflect.construct ||
										Reflect.construct
										.sham)
										return !1;
									if (typeof Proxy ==
										"function")
										return !0;
									try {
										return Boolean
											.prototype
											.valueOf
											.call(
												Reflect
												.construct(
													Boolean,
													[],
													function() {}
												)),
											!0
									} catch {
										return !1
									}
								}(),
								function() {
									var O, N = P(u);
									if (H) {
										var D = P(
												this
											)
											.constructor;
										O = Reflect
											.construct(
												N,
												arguments,
												D)
									} else O = N.apply(
										this,
										arguments
									);
									return c(this,
										O)
								});

							function M() {
								return function(O, N) {
									if (!(O instanceof N))
										throw new TypeError(
											"Cannot call a class as a function"
										)
								}(this, M), b.call(
									this,
									"[data-hs-collapse]"
								)
							}
							return L = M, (I = [{
									key: "init",
									value: function() {
										var
											O =
											this;
										document
											.addEventListener(
												"click",
												function(
													N
												) {
													var
														D =
														N
														.target
														.closest(
															O
															.selector
														);
													if (
														D
													) {
														var
															B =
															document
															.querySelectorAll(
																D
																.getAttribute(
																	"data-hs-collapse"
																)
															);
														O
															.toggle(
																B
															)
													}
												}
											)
									}
								}, {
									key: "toggle",
									value: function(
										O) {
										var
											N,
											D =
											this;
										O.length &&
											(
												N =
												O,
												function(
													B
												) {
													if (
														Array
														.isArray(
															B
														)
													)
														return o(
															B
														)
												}
												(
													N
												) ||
												function(
													B
												) {
													if (
														typeof Symbol <
														"u" &&
														B[
															Symbol
															.iterator
														] !=
														null ||
														B[
															"@@iterator"
														] !=
														null
													)
														return Array
															.from(
																B
															)
												}
												(
													N
												) ||
												function(
													B,
													h
												) {
													if (
														B
													) {
														if (
															typeof B ==
															"string"
														)
															return o(
																B,
																h
															);
														var
															G =
															Object
															.prototype
															.toString
															.call(
																B
															)
															.slice(
																8,
																-
																1
															);
														return G ===
															"Object" &&
															B
															.constructor &&
															(
																G =
																B
																.constructor
																.name
															),
															G ===
															"Map" ||
															G ===
															"Set" ?
															Array
															.from(
																B
															) :
															G ===
															"Arguments" ||
															/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/
															.test(
																G
															) ?
															o(
																B,
																h
															) :
															void 0
													}
												}
												(
													N
												) ||
												function() {
													throw new TypeError(
														`Invalid attempt to spread non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`
													)
												}
												()
											)
											.forEach(
												function(
													B
												) {
													B
														.classList
														.contains(
															"hidden"
														) ?
														D
														.show(
															B
														) :
														D
														.hide(
															B
														)
												}
											)
									}
								}, {
									key: "show",
									value: function(
										O) {
										var
											N =
											this;
										O.classList
											.add(
												"open"
											),
											O
											.classList
											.remove(
												"hidden"
											),
											O
											.style
											.height =
											0,
											document
											.querySelectorAll(
												this
												.selector
											)
											.forEach(
												function(
													D
												) {
													O
														.closest(
															D
															.getAttribute(
																"data-hs-collapse"
															)
														) &&
														D
														.classList
														.add(
															"open"
														)
												}
											),
											O
											.style
											.height =
											""
											.concat(
												O
												.scrollHeight,
												"px"
											),
											this
											.afterTransition(
												O,
												function() {
													O
														.classList
														.contains(
															"open"
														) &&
														(
															O
															.style
															.height =
															"",
															N
															._fireEvent(
																"open",
																O
															),
															N
															._dispatch(
																"open.hs.collapse",
																O,
																O
															)
														)
												}
											)
									}
								}, {
									key: "hide",
									value: function(
										O) {
										var
											N =
											this;
										O.style
											.height =
											""
											.concat(
												O
												.scrollHeight,
												"px"
											),
											setTimeout(
												function() {
													O
														.style
														.height =
														0
												}
											),
											O
											.classList
											.remove(
												"open"
											),
											this
											.afterTransition(
												O,
												function() {
													O
														.classList
														.contains(
															"open"
														) ||
														(
															O
															.classList
															.add(
																"hidden"
															),
															O
															.style
															.height =
															null,
															N
															._fireEvent(
																"hide",
																O
															),
															N
															._dispatch(
																"hide.hs.collapse",
																O,
																O
															),
															O
															.querySelectorAll(
																".hs-mega-menu-content.block"
															)
															.forEach(
																function(
																	D
																) {
																	D
																		.classList
																		.remove(
																			"block"
																		),
																		D
																		.classList
																		.add(
																			"hidden"
																		)
																}
															)
														)
												}
											),
											document
											.querySelectorAll(
												this
												.selector
											)
											.forEach(
												function(
													D
												) {
													O
														.closest(
															D
															.getAttribute(
																"data-hs-collapse"
															)
														) &&
														D
														.classList
														.remove(
															"open"
														)
												}
											)
									}
								}]) && i(L.prototype, I),
								Object.defineProperty(L,
									"prototype", {
										writable: !1
									}), M
						}(S(765)
							.Z);
						window.HSCollapse = new p, document
							.addEventListener("load",
								window.HSCollapse.init())
					},
					682: (n, s, S) => {
						var A = S(714),
							o = S(765);
						const i = {
							historyIndex: -1,
							addHistory: function(H) {
								this.historyIndex =
									H
							},
							existsInHistory: function(H) {
								return H > this.historyIndex
							},
							clearHistory: function() {
								this.historyIndex = -
									1
							}
						};

						function _(H) {
							return _ = typeof Symbol ==
								"function" && typeof Symbol
								.iterator == "symbol" ?
								function(b) {
									return typeof b
								} : function(b) {
									return b && typeof Symbol ==
										"function" && b.constructor ===
										Symbol && b !==
										Symbol.prototype ?
										"symbol" : typeof b
								}, _(H)
						}

						function c(H) {
							return function(b) {
								if (Array.isArray(b))
									return P(b)
							}(H) || function(b) {
								if (typeof Symbol < "u" &&
									b[Symbol.iterator] !=
									null || b[
										"@@iterator"] !=
									null) return Array.from(
									b)
							}(H) || function(b, M) {
								if (b) {
									if (typeof b ==
										"string") return P(
										b, M);
									var O = Object.prototype
										.toString.call(
											b)
										.slice(8, -1);
									return O ===
										"Object" && b.constructor &&
										(O = b.constructor
											.name), O ===
										"Map" || O ===
										"Set" ? Array.from(
											b) : O ===
										"Arguments" ||
										/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/
										.test(O) ? P(b,
											M) : void 0
								}
							}(H) || function() {
								throw new TypeError(
									`Invalid attempt to spread non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`
								)
							}()
						}

						function P(H, b) {
							(b == null || b > H.length) &&
							(b = H.length);
							for (var M = 0, O = new Array(b); M <
								b; M++) O[M] = H[M];
							return O
						}

						function p(H, b) {
							for (var M = 0; M < b.length; M++) {
								var O = b[M];
								O.enumerable = O.enumerable ||
									!1, O.configurable = !0,
									"value" in O && (O.writable = !
										0), Object.defineProperty(
										H, O.key, O)
							}
						}

						function C(H, b) {
							return C = Object.setPrototypeOf ||
								function(M, O) {
									return M.__proto__ = O,
										M
								}, C(H, b)
						}

						function L(H, b) {
							if (b && (_(b) === "object" ||
								typeof b == "function"))
								return b;
							if (b !== void 0) throw new TypeError(
								"Derived constructors may only return object or undefined"
							);
							return function(M) {
								if (M === void 0) throw new ReferenceError(
									"this hasn't been initialised - super() hasn't been called"
								);
								return M
							}(H)
						}

						function I(H) {
							return I = Object.setPrototypeOf ?
								Object.getPrototypeOf :
								function(b) {
									return b.__proto__ ||
										Object.getPrototypeOf(
											b)
								}, I(H)
						}
						var u = function(H) {
							(function(h, G) {
								if (typeof G !=
									"function" && G !==
									null) throw new TypeError(
									"Super expression must either be null or a function"
								);
								h.prototype =
									Object.create(G &&
										G.prototype, {
											constructor: {
												value: h,
												writable:
													!
													0,
												configurable:
													!
													0
											}
										}), Object.defineProperty(
										h,
										"prototype", {
											writable:
												!1
										}), G && C(
										h, G)
							})(B, H);
							var b, M, O, N, D = (O = B,
								N = function() {
									if (typeof Reflect >
										"u" || !
										Reflect.construct ||
										Reflect.construct
										.sham)
										return !1;
									if (typeof Proxy ==
										"function")
										return !0;
									try {
										return Boolean
											.prototype
											.valueOf
											.call(
												Reflect
												.construct(
													Boolean,
													[],
													function() {}
												)),
											!0
									} catch {
										return !1
									}
								}(),
								function() {
									var h, G = I(O);
									if (N) {
										var F = I(
												this
											)
											.constructor;
										h = Reflect
											.construct(
												G,
												arguments,
												F)
									} else h = G.apply(
										this,
										arguments
									);
									return L(this,
										h)
								});

							function B() {
								var h;
								return function(G, F) {
										if (!(G instanceof F))
											throw new TypeError(
												"Cannot call a class as a function"
											)
									}(this, B), (h = D.call(
										this,
										".hs-dropdown"
									))
									.positions = {
										top: "top",
										"top-left": "top-start",
										"top-right": "top-end",
										bottom: "bottom",
										"bottom-left": "bottom-start",
										"bottom-right": "bottom-end",
										right: "right",
										"right-top": "right-start",
										"right-bottom": "right-end",
										left: "left",
										"left-top": "left-start",
										"left-bottom": "left-end"
									}, h.absoluteStrategyModifiers =
									function(G) {
										return [{
											name: "applyStyles",
											fn: function(
												F
											) {
												var
													W =
													(
														window
														.getComputedStyle(
															G
														)
														.getPropertyValue(
															"--strategy"
														) ||
														"absolute"
													)
													.replace(
														" ",
														""
													),
													x =
													(
														window
														.getComputedStyle(
															G
														)
														.getPropertyValue(
															"--adaptive"
														) ||
														"adaptive"
													)
													.replace(
														" ",
														""
													);
												F
													.state
													.elements
													.popper
													.style
													.position =
													W,
													F
													.state
													.elements
													.popper
													.style
													.transform =
													x ===
													"adaptive" ?
													F
													.state
													.styles
													.popper
													.transform :
													null,
													F
													.state
													.elements
													.popper
													.style
													.top =
													null,
													F
													.state
													.elements
													.popper
													.style
													.bottom =
													null,
													F
													.state
													.elements
													.popper
													.style
													.left =
													null,
													F
													.state
													.elements
													.popper
													.style
													.right =
													null,
													F
													.state
													.elements
													.popper
													.style
													.margin =
													0
											}
										}, {
											name: "computeStyles",
											options: {
												adaptive:
													!
													1
											}
										}]
									}, h._history = i,
									h
							}
							return b = B, M = [{
								key: "init",
								value: function() {
									var h =
										this;
									document
										.addEventListener(
											"click",
											function(
												G
											) {
												var
													F =
													G
													.target,
													W =
													F
													.closest(
														h
														.selector
													),
													x =
													F
													.closest(
														".hs-dropdown-menu"
													);
												if (
													W &&
													W
													.classList
													.contains(
														"open"
													) ||
													h
													._closeOthers(
														W
													),
													x
												) {
													var
														J =
														(
															window
															.getComputedStyle(
																W
															)
															.getPropertyValue(
																"--auto-close"
															) ||
															""
														)
														.replace(
															" ",
															""
														);
													if (
														(
															J ==
															"false" ||
															J ==
															"inside"
														) &&
														!
														W
														.parentElement
														.closest(
															h
															.selector
														)
													)
														return
												}
												W
													&&
													(
														W
														.classList
														.contains(
															"open"
														) ?
														h
														.close(
															W
														) :
														h
														.open(
															W
														)
													)
											}
										),
										document
										.addEventListener(
											"mousemove",
											function(
												G
											) {
												var
													F =
													G
													.target,
													W =
													F
													.closest(
														h
														.selector
													);
												if (
													F
													.closest(
														".hs-dropdown-menu"
													),
													W
												) {
													var
														x =
														(
															window
															.getComputedStyle(
																W
															)
															.getPropertyValue(
																"--trigger"
															) ||
															"click"
														)
														.replace(
															" ",
															""
														);
													if (
														x !==
														"hover"
													)
														return;
													W
														&&
														W
														.classList
														.contains(
															"open"
														) ||
														h
														._closeOthers(
															W
														),
														x !==
														"hover" ||
														W
														.classList
														.contains(
															"open"
														) ||
														/iPad|iPhone|iPod/
														.test(
															navigator
															.platform
														) ||
														navigator
														.maxTouchPoints &&
														navigator
														.maxTouchPoints >
														2 &&
														/MacIntel/
														.test(
															navigator
															.platform
														) ||
														navigator
														.maxTouchPoints &&
														navigator
														.maxTouchPoints >
														2 &&
														/MacIntel/
														.test(
															navigator
															.platform
														) ||
														h
														._hover(
															F
														)
												}
											}
										),
										document
										.addEventListener(
											"keydown",
											this
											._keyboardSupport
											.bind(
												this
											)
										),
										window
										.addEventListener(
											"resize",
											function() {
												document
													.querySelectorAll(
														".hs-dropdown.open"
													)
													.forEach(
														function(
															G
														) {
															h
																.close(
																	G,
																	!
																	0
																)
														}
													)
											}
										)
								}
							}, {
								key: "_closeOthers",
								value: function() {
									var h =
										this,
										G =
										arguments
										.length >
										0 &&
										arguments[
											0
										] !==
										void 0 ?
										arguments[
											0
										] :
										null,
										F =
										document
										.querySelectorAll(
											""
											.concat(
												this
												.selector,
												".open"
											)
										);
									F.forEach(
										function(
											W
										) {
											if (
												!
												G ||
												G
												.closest(
													".hs-dropdown.open"
												) !==
												W
											) {
												var
													x =
													(
														window
														.getComputedStyle(
															W
														)
														.getPropertyValue(
															"--auto-close"
														) ||
														""
													)
													.replace(
														" ",
														""
													);
												x
													!=
													"false" &&
													x !=
													"outside" &&
													h
													.close(
														W
													)
											}
										}
									)
								}
							}, {
								key: "_hover",
								value: function(
									h) {
									var G =
										this,
										F =
										h.closest(
											this
											.selector
										);
									this.open(
											F
										),
										document
										.addEventListener(
											"mousemove",
											function W(
												x
											) {
												x
													.target
													.closest(
														G
														.selector
													) &&
													x
													.target
													.closest(
														G
														.selector
													) !==
													F
													.parentElement
													.closest(
														G
														.selector
													) ||
													(
														G
														.close(
															F
														),
														document
														.removeEventListener(
															"mousemove",
															W,
															!
															0
														)
													)
											},
											!
											0
										)
								}
							}, {
								key: "close",
								value: function(
									h) {
									var G =
										this,
										F =
										arguments
										.length >
										1 &&
										arguments[
											1
										] !==
										void 0 &&
										arguments[
											1
										],
										W =
										h.querySelector(
											".hs-dropdown-menu"
										),
										x =
										function() {
											h
												.classList
												.contains(
													"open"
												) ||
												(
													W
													.classList
													.remove(
														"block"
													),
													W
													.classList
													.add(
														"hidden"
													),
													W
													.style
													.inset =
													null,
													W
													.style
													.position =
													null,
													h
													._popper &&
													h
													._popper
													.destroy()
												)
										};
									F ||
										this
										.afterTransition(
											h
											.querySelector(
												"[data-hs-dropdown-transition]"
											) ||
											W,
											function() {
												x
													()
											}
										),
										W.style
										.margin =
										null,
										h.classList
										.remove(
											"open"
										),
										F &&
										x(),
										this
										._fireEvent(
											"close",
											h
										),
										this
										._dispatch(
											"close.hs.dropdown",
											h,
											h
										);
									var J =
										W.querySelectorAll(
											".hs-dropdown.open"
										);
									J.forEach(
										function(
											oe
										) {
											G
												.close(
													oe,
													!
													0
												)
										}
									)
								}
							}, {
								key: "open",
								value: function(
									h) {
									var G =
										h.querySelector(
											".hs-dropdown-menu"
										),
										F =
										(
											window
											.getComputedStyle(
												h
											)
											.getPropertyValue(
												"--placement"
											) ||
											""
										)
										.replace(
											" ",
											""
										),
										W =
										(
											window
											.getComputedStyle(
												h
											)
											.getPropertyValue(
												"--strategy"
											) ||
											"fixed"
										)
										.replace(
											" ",
											""
										),
										x =
										((
												window
												.getComputedStyle(
													h
												)
												.getPropertyValue(
													"--adaptive"
												) ||
												"adaptive"
											)
											.replace(
												" ",
												""
											),
											parseInt(
												(
													window
													.getComputedStyle(
														h
													)
													.getPropertyValue(
														"--offset"
													) ||
													"10"
												)
												.replace(
													" ",
													""
												)
											)
										);
									if (W !==
										"static"
									) {
										h._popper &&
											h
											._popper
											.destroy();
										var
											J =
											(
												0,
												A
												.fi
											)
											(
												h,
												G, {
													placement: this
														.positions[
															F
														] ||
														"bottom-start",
													strategy: W,
													modifiers: []
														.concat(
															c(
																W !==
																"fixed" ?
																this
																.absoluteStrategyModifiers(
																	h
																) : []
															),
															[{
																name: "offset",
																options: {
																	offset: [
																		0,
																		x
																	]
																}
															}]
														)
												}
											);
										h._popper =
											J
									}
									G.style
										.margin =
										null,
										G.classList
										.add(
											"block"
										),
										G.classList
										.remove(
											"hidden"
										),
										setTimeout(
											function() {
												h
													.classList
													.add(
														"open"
													)
											}
										),
										this
										._fireEvent(
											"open",
											h
										),
										this
										._dispatch(
											"open.hs.dropdown",
											h,
											h
										)
								}
							}, {
								key: "_keyboardSupport",
								value: function(
									h) {
									var G =
										document
										.querySelector(
											".hs-dropdown.open"
										);
									if (G)
										return h
											.keyCode ===
											27 ?
											(
												h
												.preventDefault(),
												this
												._esc(
													G
												)
											) :
											h
											.keyCode ===
											40 ?
											(
												h
												.preventDefault(),
												this
												._down(
													G
												)
											) :
											h
											.keyCode ===
											38 ?
											(
												h
												.preventDefault(),
												this
												._up(
													G
												)
											) :
											h
											.keyCode ===
											36 ?
											(
												h
												.preventDefault(),
												this
												._start(
													G
												)
											) :
											h
											.keyCode ===
											35 ?
											(
												h
												.preventDefault(),
												this
												._end(
													G
												)
											) :
											void this
											._byChar(
												G,
												h
												.key
											)
								}
							}, {
								key: "_esc",
								value: function(
									h) {
									this.close(
										h
									)
								}
							}, {
								key: "_up",
								value: function(
									h) {
									var G =
										h.querySelector(
											".hs-dropdown-menu"
										),
										F =
										c(G
											.querySelectorAll(
												"a"
											)
										)
										.reverse()
										.filter(
											function(
												J
											) {
												return !
													J
													.disabled
											}
										),
										W =
										G.querySelector(
											"a:focus"
										),
										x =
										F.findIndex(
											function(
												J
											) {
												return J ===
													W
											}
										);
									x + 1 <
										F.length &&
										x++,
										F[x]
										.focus()
								}
							}, {
								key: "_down",
								value: function(
									h) {
									var G =
										h.querySelector(
											".hs-dropdown-menu"
										),
										F =
										c(G
											.querySelectorAll(
												"a"
											)
										)
										.filter(
											function(
												J
											) {
												return !
													J
													.disabled
											}
										),
										W =
										G.querySelector(
											"a:focus"
										),
										x =
										F.findIndex(
											function(
												J
											) {
												return J ===
													W
											}
										);
									x + 1 <
										F.length &&
										x++,
										F[x]
										.focus()
								}
							}, {
								key: "_start",
								value: function(
									h) {
									var G =
										c(h
											.querySelector(
												".hs-dropdown-menu"
											)
											.querySelectorAll(
												"a"
											)
										)
										.filter(
											function(
												F
											) {
												return !
													F
													.disabled
											}
										);
									G.length &&
										G[0]
										.focus()
								}
							}, {
								key: "_end",
								value: function(
									h) {
									var G =
										c(h
											.querySelector(
												".hs-dropdown-menu"
											)
											.querySelectorAll(
												"a"
											)
										)
										.reverse()
										.filter(
											function(
												F
											) {
												return !
													F
													.disabled
											}
										);
									G.length &&
										G[0]
										.focus()
								}
							}, {
								key: "_byChar",
								value: function(
									h, G) {
									var F =
										this,
										W =
										c(h
											.querySelector(
												".hs-dropdown-menu"
											)
											.querySelectorAll(
												"a"
											)
										),
										x =
										function() {
											return W
												.findIndex(
													function(
														oe,
														z
													) {
														return oe
															.innerText
															.toLowerCase()
															.charAt(
																0
															) ===
															G
															.toLowerCase() &&
															F
															._history
															.existsInHistory(
																z
															)
													}
												)
										},
										J =
										x();
									J ===
										-1 &&
										(
											this
											._history
											.clearHistory(),
											J =
											x()
										),
										J !==
										-1 &&
										(W[
												J
											]
											.focus(),
											this
											._history
											.addHistory(
												J
											)
										)
								}
							}, {
								key: "toggle",
								value: function(
									h) {
									h.classList
										.contains(
											"open"
										) ?
										this
										.close(
											h
										) :
										this
										.open(
											h
										)
								}
							}], M && p(b.prototype,
								M), Object.defineProperty(
								b, "prototype", {
									writable: !1
								}), B
						}(o.Z);
						window.HSDropdown = new u, document
							.addEventListener("load",
								window.HSDropdown.init())
					},
					284: (n, s, S) => {
						function A(C) {
							return A = typeof Symbol ==
								"function" && typeof Symbol
								.iterator == "symbol" ?
								function(L) {
									return typeof L
								} : function(L) {
									return L && typeof Symbol ==
										"function" && L.constructor ===
										Symbol && L !==
										Symbol.prototype ?
										"symbol" : typeof L
								}, A(C)
						}

						function o(C, L) {
							(L == null || L > C.length) &&
							(L = C.length);
							for (var I = 0, u = new Array(L); I <
								L; I++) u[I] = C[I];
							return u
						}

						function i(C, L) {
							for (var I = 0; I < L.length; I++) {
								var u = L[I];
								u.enumerable = u.enumerable ||
									!1, u.configurable = !0,
									"value" in u && (u.writable = !
										0), Object.defineProperty(
										C, u.key, u)
							}
						}

						function _(C, L) {
							return _ = Object.setPrototypeOf ||
								function(I, u) {
									return I.__proto__ = u,
										I
								}, _(C, L)
						}

						function c(C, L) {
							if (L && (A(L) === "object" ||
								typeof L == "function"))
								return L;
							if (L !== void 0) throw new TypeError(
								"Derived constructors may only return object or undefined"
							);
							return function(I) {
								if (I === void 0) throw new ReferenceError(
									"this hasn't been initialised - super() hasn't been called"
								);
								return I
							}(C)
						}

						function P(C) {
							return P = Object.setPrototypeOf ?
								Object.getPrototypeOf :
								function(L) {
									return L.__proto__ ||
										Object.getPrototypeOf(
											L)
								}, P(C)
						}
						var p = function(C) {
							(function(O, N) {
								if (typeof N !=
									"function" && N !==
									null) throw new TypeError(
									"Super expression must either be null or a function"
								);
								O.prototype =
									Object.create(N &&
										N.prototype, {
											constructor: {
												value: O,
												writable:
													!
													0,
												configurable:
													!
													0
											}
										}), Object.defineProperty(
										O,
										"prototype", {
											writable:
												!1
										}), N && _(
										O, N)
							})(M, C);
							var L, I, u, H, b = (u = M,
								H = function() {
									if (typeof Reflect >
										"u" || !
										Reflect.construct ||
										Reflect.construct
										.sham)
										return !1;
									if (typeof Proxy ==
										"function")
										return !0;
									try {
										return Boolean
											.prototype
											.valueOf
											.call(
												Reflect
												.construct(
													Boolean,
													[],
													function() {}
												)),
											!0
									} catch {
										return !1
									}
								}(),
								function() {
									var O, N = P(u);
									if (H) {
										var D = P(
												this
											)
											.constructor;
										O = Reflect
											.construct(
												N,
												arguments,
												D)
									} else O = N.apply(
										this,
										arguments
									);
									return c(this,
										O)
								});

							function M() {
								var O;
								return function(N, D) {
										if (!(N instanceof D))
											throw new TypeError(
												"Cannot call a class as a function"
											)
									}(this, M), (O = b.call(
										this,
										"[data-hs-overlay]"
									))
									.openNextOverlay = !
									1, O
							}
							return L = M, (I = [{
									key: "init",
									value: function() {
										var
											O =
											this;
										document
											.addEventListener(
												"click",
												function(
													N
												) {
													var
														D =
														N
														.target
														.closest(
															O
															.selector
														),
														B =
														N
														.target
														.closest(
															"[data-hs-overlay-close]"
														),
														h =
														N
														.target
														.getAttribute(
															"aria-overlay"
														) ===
														"true";
													return B ?
														O
														.close(
															B
															.closest(
																".hs-overlay.open"
															)
														) :
														D ?
														O
														.toggle(
															document
															.querySelector(
																D
																.getAttribute(
																	"data-hs-overlay"
																)
															)
														) :
														void(
															h &&
															O
															._onBackdropClick(
																N
																.target
															)
														)
												}
											),
											document
											.addEventListener(
												"keydown",
												function(
													N
												) {
													if (
														N
														.keyCode ===
														27
													) {
														var
															D =
															document
															.querySelector(
																".hs-overlay.open"
															);
														if (
															!
															D
														)
															return;
														setTimeout
															(
																function() {
																	D
																		.getAttribute(
																			"data-hs-overlay-keyboard"
																		) !==
																		"false" &&
																		O
																		.close(
																			D
																		)
																}
															)
													}
												}
											)
									}
								}, {
									key: "toggle",
									value: function(
										O) {
										O &&
											(
												O
												.classList
												.contains(
													"hidden"
												) ?
												this
												.open(
													O
												) :
												this
												.close(
													O
												)
											)
									}
								}, {
									key: "open",
									value: function(
										O) {
										var
											N =
											this;
										if (
											O
										) {
											var
												D =
												document
												.querySelector(
													".hs-overlay.open"
												),
												B =
												this
												.getClassProperty(
													O,
													"--body-scroll",
													"false"
												) !==
												"true";
											if (
												D
											)
												return this
													.openNextOverlay = !
													0,
													this
													.close(
														D
													)
													.then(
														function() {
															N
																.open(
																	O
																),
																N
																.openNextOverlay = !
																1
														}
													);
											B
												&&
												(
													document
													.body
													.style
													.overflow =
													"hidden"
												),
												this
												._buildBackdrop(
													O
												),
												this
												._checkTimer(
													O
												),
												this
												._autoHide(
													O
												),
												O
												.classList
												.remove(
													"hidden"
												),
												O
												.setAttribute(
													"aria-overlay",
													"true"
												),
												O
												.setAttribute(
													"tabindex",
													"-1"
												),
												setTimeout(
													function() {
														O
															.classList
															.contains(
																"hidden"
															) ||
															(
																O
																.classList
																.add(
																	"open"
																),
																N
																._fireEvent(
																	"open",
																	O
																),
																N
																._dispatch(
																	"open.hs.overlay",
																	O,
																	O
																),
																N
																._focusInput(
																	O
																)
															)
													},
													50
												)
										}
									}
								}, {
									key: "close",
									value: function(
										O) {
										var
											N =
											this;
										return new Promise(
											function(
												D
											) {
												O
													&&
													(
														O
														.classList
														.remove(
															"open"
														),
														O
														.removeAttribute(
															"aria-overlay"
														),
														O
														.removeAttribute(
															"tabindex",
															"-1"
														),
														N
														.afterTransition(
															O,
															function() {
																O
																	.classList
																	.contains(
																		"open"
																	) ||
																	(
																		O
																		.classList
																		.add(
																			"hidden"
																		),
																		N
																		._destroyBackdrop(),
																		N
																		._fireEvent(
																			"close",
																			O
																		),
																		N
																		._dispatch(
																			"close.hs.overlay",
																			O,
																			O
																		),
																		document
																		.body
																		.style
																		.overflow =
																		"",
																		D(
																			O
																		)
																	)
															}
														)
													)
											}
										)
									}
								}, {
									key: "_autoHide",
									value: function(
										O) {
										var
											N =
											this,
											D =
											parseInt(
												this
												.getClassProperty(
													O,
													"--auto-hide",
													"0"
												)
											);
										D &&
											(
												O
												.autoHide =
												setTimeout(
													function() {
														N
															.close(
																O
															)
													},
													D
												)
											)
									}
								}, {
									key: "_checkTimer",
									value: function(
										O) {
										O.autoHide &&
											(
												clearTimeout(
													O
													.autoHide
												),
												delete O
												.autoHide
											)
									}
								}, {
									key: "_onBackdropClick",
									value: function(
										O) {
										this
											.getClassProperty(
												O,
												"--overlay-backdrop",
												"true"
											) !==
											"static" &&
											this
											.close(
												O
											)
									}
								}, {
									key: "_buildBackdrop",
									value: function(
										O) {
										var
											N,
											D =
											this,
											B =
											O
											.getAttribute(
												"data-hs-overlay-backdrop-container"
											) ||
											!
											1,
											h =
											document
											.createElement(
												"div"
											),
											G =
											"transition duration fixed inset-0 z-50 bg-gray-900 bg-opacity-50 dark:bg-opacity-80 hs-overlay-backdrop",
											F =
											function(
												J,
												oe
											) {
												var
													z =
													typeof Symbol <
													"u" &&
													J[
														Symbol
														.iterator
													] ||
													J[
														"@@iterator"
													];
												if (
													!
													z
												) {
													if (
														Array
														.isArray(
															J
														) ||
														(
															z =
															function(
																me,
																fE
															) {
																if (
																	me
																) {
																	if (
																		typeof me ==
																		"string"
																	)
																		return o(
																			me,
																			fE
																		);
																	var
																		rE =
																		Object
																		.prototype
																		.toString
																		.call(
																			me
																		)
																		.slice(
																			8,
																			-
																			1
																		);
																	return rE ===
																		"Object" &&
																		me
																		.constructor &&
																		(
																			rE =
																			me
																			.constructor
																			.name
																		),
																		rE ===
																		"Map" ||
																		rE ===
																		"Set" ?
																		Array
																		.from(
																			me
																		) :
																		rE ===
																		"Arguments" ||
																		/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/
																		.test(
																			rE
																		) ?
																		o(
																			me,
																			fE
																		) :
																		void 0
																}
															}
															(
																J
															)
														) ||
														oe &&
														J &&
														typeof J
														.length ==
														"number"
													) {
														z
															&&
															(
																J =
																z
															);
														var
															Oe =
															0,
															Ue =
															function() {};
														return {
															s: Ue,
															n: function() {
																return Oe >=
																	J
																	.length ? {
																		done:
																			!
																			0
																	} : {
																		done:
																			!
																			1,
																		value: J[
																			Oe++
																		]
																	}
															},
															e: function(
																me
															) {
																throw me
															},
															f: Ue
														}
													}
													throw new TypeError(
														`Invalid attempt to iterate non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`
													)
												}
												var
													ye,
													TE = !
													0,
													dE = !
													1;
												return {
													s: function() {
														z
															=
															z
															.call(
																J
															)
													},
													n: function() {
														var
															me =
															z
															.next();
														return TE =
															me
															.done,
															me
													},
													e: function(
														me
													) {
														dE
															= !
															0,
															ye =
															me
													},
													f: function() {
														try {
															TE
																||
																z
																.return ==
																null ||
																z
																.return()
														} finally {
															if (
																dE
															)
																throw ye
														}
													}
												}
											}
											(
												O
												.classList
												.values()
											);
										try {
											for (
												F
												.s(); !
												(
													N =
													F
													.n()
												)
												.done;
											) {
												var
													W =
													N
													.value;
												W
													.startsWith(
														"hs-overlay-backdrop-open:"
													) &&
													(
														G +=
														" "
														.concat(
															W
														)
													)
											}
										} catch (
											J
										) {
											F
												.e(
													J
												)
										} finally {
											F
												.f()
										}
										var
											x =
											this
											.getClassProperty(
												O,
												"--overlay-backdrop",
												"true"
											) !==
											"static";
										this
											.getClassProperty(
												O,
												"--overlay-backdrop",
												"true"
											) ===
											"false" ||
											(
												B &&
												(
													(
														h =
														document
														.querySelector(
															B
														)
														.cloneNode(
															!
															0
														)
													)
													.classList
													.remove(
														"hidden"
													),
													G =
													h
													.classList,
													h
													.classList =
													""
												),
												x &&
												h
												.addEventListener(
													"click",
													function() {
														return D
															.close(
																O
															)
													},
													!
													0
												),
												h
												.setAttribute(
													"data-hs-overlay-backdrop-template",
													""
												),
												document
												.body
												.appendChild(
													h
												),
												setTimeout(
													function() {
														h
															.classList =
															G
													}
												)
											)
									}
								}, {
									key: "_destroyBackdrop",
									value: function() {
										var
											O =
											document
											.querySelector(
												"[data-hs-overlay-backdrop-template]"
											);
										O &&
											(
												this
												.openNextOverlay &&
												(
													O
													.style
													.transitionDuration =
													""
													.concat(
														1.8 *
														parseFloat(
															window
															.getComputedStyle(
																O
															)
															.transitionDuration
															.replace(
																/[^\\d.-]/g,
																""
															)
														),
														"s"
													)
												),
												O
												.classList
												.add(
													"opacity-0"
												),
												this
												.afterTransition(
													O,
													function() {
														O
															.remove()
													}
												)
											)
									}
								}, {
									key: "_focusInput",
									value: function(
										O) {
										var
											N =
											O
											.querySelector(
												"[autofocus]"
											);
										N &&
											N
											.focus()
									}
								}]) && i(L.prototype, I),
								Object.defineProperty(L,
									"prototype", {
										writable: !1
									}), M
						}(S(765)
							.Z);
						window.HSOverlay = new p, document.addEventListener(
							"load", window.HSOverlay.init()
						)
					},
					181: (n, s, S) => {
						function A(p) {
							return A = typeof Symbol ==
								"function" && typeof Symbol
								.iterator == "symbol" ?
								function(C) {
									return typeof C
								} : function(C) {
									return C && typeof Symbol ==
										"function" && C.constructor ===
										Symbol && C !==
										Symbol.prototype ?
										"symbol" : typeof C
								}, A(p)
						}

						function o(p, C) {
							for (var L = 0; L < C.length; L++) {
								var I = C[L];
								I.enumerable = I.enumerable ||
									!1, I.configurable = !0,
									"value" in I && (I.writable = !
										0), Object.defineProperty(
										p, I.key, I)
							}
						}

						function i(p, C) {
							return i = Object.setPrototypeOf ||
								function(L, I) {
									return L.__proto__ = I,
										L
								}, i(p, C)
						}

						function _(p, C) {
							if (C && (A(C) === "object" ||
								typeof C == "function"))
								return C;
							if (C !== void 0) throw new TypeError(
								"Derived constructors may only return object or undefined"
							);
							return function(L) {
								if (L === void 0) throw new ReferenceError(
									"this hasn't been initialised - super() hasn't been called"
								);
								return L
							}(p)
						}

						function c(p) {
							return c = Object.setPrototypeOf ?
								Object.getPrototypeOf :
								function(C) {
									return C.__proto__ ||
										Object.getPrototypeOf(
											C)
								}, c(p)
						}
						var P = function(p) {
							(function(M, O) {
								if (typeof O !=
									"function" && O !==
									null) throw new TypeError(
									"Super expression must either be null or a function"
								);
								M.prototype =
									Object.create(O &&
										O.prototype, {
											constructor: {
												value: M,
												writable:
													!
													0,
												configurable:
													!
													0
											}
										}), Object.defineProperty(
										M,
										"prototype", {
											writable:
												!1
										}), O && i(
										M, O)
							})(b, p);
							var C, L, I, u, H = (I = b,
								u = function() {
									if (typeof Reflect >
										"u" || !
										Reflect.construct ||
										Reflect.construct
										.sham)
										return !1;
									if (typeof Proxy ==
										"function")
										return !0;
									try {
										return Boolean
											.prototype
											.valueOf
											.call(
												Reflect
												.construct(
													Boolean,
													[],
													function() {}
												)),
											!0
									} catch {
										return !1
									}
								}(),
								function() {
									var M, O = c(I);
									if (u) {
										var N = c(
												this
											)
											.constructor;
										M = Reflect
											.construct(
												O,
												arguments,
												N)
									} else M = O.apply(
										this,
										arguments
									);
									return _(this,
										M)
								});

							function b() {
								return function(M, O) {
									if (!(M instanceof O))
										throw new TypeError(
											"Cannot call a class as a function"
										)
								}(this, b), H.call(
									this,
									"[data-hs-remove-element]"
								)
							}
							return C = b, (L = [{
									key: "init",
									value: function() {
										var
											M =
											this;
										document
											.addEventListener(
												"click",
												function(
													O
												) {
													var
														N =
														O
														.target
														.closest(
															M
															.selector
														);
													if (
														N
													) {
														var
															D =
															document
															.querySelector(
																N
																.getAttribute(
																	"data-hs-remove-element"
																)
															);
														D
															&&
															(
																D
																.classList
																.add(
																	"hs-removing"
																),
																M
																.afterTransition(
																	D,
																	function() {
																		D
																			.remove()
																	}
																)
															)
													}
												}
											)
									}
								}]) && o(C.prototype, L),
								Object.defineProperty(C,
									"prototype", {
										writable: !1
									}), b
						}(S(765)
							.Z);
						window.HSRemoveElement = new P,
							document.addEventListener(
								"load", window.HSRemoveElement
								.init())
					},
					778: (n, s, S) => {
						function A(p) {
							return A = typeof Symbol ==
								"function" && typeof Symbol
								.iterator == "symbol" ?
								function(C) {
									return typeof C
								} : function(C) {
									return C && typeof Symbol ==
										"function" && C.constructor ===
										Symbol && C !==
										Symbol.prototype ?
										"symbol" : typeof C
								}, A(p)
						}

						function o(p, C) {
							for (var L = 0; L < C.length; L++) {
								var I = C[L];
								I.enumerable = I.enumerable ||
									!1, I.configurable = !0,
									"value" in I && (I.writable = !
										0), Object.defineProperty(
										p, I.key, I)
							}
						}

						function i(p, C) {
							return i = Object.setPrototypeOf ||
								function(L, I) {
									return L.__proto__ = I,
										L
								}, i(p, C)
						}

						function _(p, C) {
							if (C && (A(C) === "object" ||
								typeof C == "function"))
								return C;
							if (C !== void 0) throw new TypeError(
								"Derived constructors may only return object or undefined"
							);
							return function(L) {
								if (L === void 0) throw new ReferenceError(
									"this hasn't been initialised - super() hasn't been called"
								);
								return L
							}(p)
						}

						function c(p) {
							return c = Object.setPrototypeOf ?
								Object.getPrototypeOf :
								function(C) {
									return C.__proto__ ||
										Object.getPrototypeOf(
											C)
								}, c(p)
						}
						var P = function(p) {
							(function(M, O) {
								if (typeof O !=
									"function" && O !==
									null) throw new TypeError(
									"Super expression must either be null or a function"
								);
								M.prototype =
									Object.create(O &&
										O.prototype, {
											constructor: {
												value: M,
												writable:
													!
													0,
												configurable:
													!
													0
											}
										}), Object.defineProperty(
										M,
										"prototype", {
											writable:
												!1
										}), O && i(
										M, O)
							})(b, p);
							var C, L, I, u, H = (I = b,
								u = function() {
									if (typeof Reflect >
										"u" || !
										Reflect.construct ||
										Reflect.construct
										.sham)
										return !1;
									if (typeof Proxy ==
										"function")
										return !0;
									try {
										return Boolean
											.prototype
											.valueOf
											.call(
												Reflect
												.construct(
													Boolean,
													[],
													function() {}
												)),
											!0
									} catch {
										return !1
									}
								}(),
								function() {
									var M, O = c(I);
									if (u) {
										var N = c(
												this
											)
											.constructor;
										M = Reflect
											.construct(
												O,
												arguments,
												N)
									} else M = O.apply(
										this,
										arguments
									);
									return _(this,
										M)
								});

							function b() {
								var M;
								return function(O, N) {
										if (!(O instanceof N))
											throw new TypeError(
												"Cannot call a class as a function"
											)
									}(this, b), (M = H.call(
										this,
										"[data-hs-scrollspy] "
									))
									.activeSection =
									null, M
							}
							return C = b, (L = [{
									key: "init",
									value: function() {
										var
											M =
											this;
										document
											.querySelectorAll(
												this
												.selector
											)
											.forEach(
												function(
													O
												) {
													var
														N =
														document
														.querySelector(
															O
															.getAttribute(
																"data-hs-scrollspy"
															)
														),
														D =
														O
														.querySelectorAll(
															"[href]"
														),
														B =
														N
														.children,
														h =
														O
														.getAttribute(
															"data-hs-scrollspy-scrollable-parent"
														) ?
														document
														.querySelector(
															O
															.getAttribute(
																"data-hs-scrollspy-scrollable-parent"
															)
														) :
														document;
													Array
														.from(
															B
														)
														.forEach(
															function(
																G
															) {
																G
																	.getAttribute(
																		"id"
																	) &&
																	h
																	.addEventListener(
																		"scroll",
																		function(
																			F
																		) {
																			return M
																				._update({
																					$scrollspyEl: O,
																					$scrollspyContentEl: N,
																					links: D,
																					$sectionEl: G,
																					sections: B,
																					ev: F
																				})
																		}
																	)
															}
														),
														D
														.forEach(
															function(
																G
															) {
																G
																	.addEventListener(
																		"click",
																		function(
																			F
																		) {
																			F
																				.preventDefault(),
																				G
																				.getAttribute(
																					"href"
																				) !==
																				"javascript:;" &&
																				M
																				._scrollTo({
																					$scrollspyEl: O,
																					$scrollableEl: h,
																					$link: G
																				})
																		}
																	)
															}
														)
												}
											)
									}
								}, {
									key: "_update",
									value: function(
										M) {
										var
											O =
											M
											.ev,
											N =
											M
											.$scrollspyEl,
											D =
											(
												M
												.sections,
												M
												.links
											),
											B =
											M
											.$sectionEl,
											h =
											parseInt(
												this
												.getClassProperty(
													N,
													"--scrollspy-offset",
													"0"
												)
											),
											G =
											this
											.getClassProperty(
												B,
												"--scrollspy-offset"
											) ||
											h,
											F =
											O
											.target ===
											document ?
											0 :
											parseInt(
												O
												.target
												.getBoundingClientRect()
												.top
											),
											W =
											parseInt(
												B
												.getBoundingClientRect()
												.top
											) -
											G -
											F,
											x =
											B
											.offsetHeight;
										if (
											W <=
											0 &&
											W +
											x >
											0
										) {
											if (
												this
												.activeSection ===
												B
											)
												return;
											D
												.forEach(
													function(
														Oe
													) {
														Oe
															.classList
															.remove(
																"active"
															)
													}
												);
											var
												J =
												N
												.querySelector(
													'[href="#'
													.concat(
														B
														.getAttribute(
															"id"
														),
														'"]'
													)
												);
											if (
												J
											) {
												J
													.classList
													.add(
														"active"
													);
												var
													oe =
													J
													.closest(
														"[data-hs-scrollspy-group]"
													);
												if (
													oe
												) {
													var
														z =
														oe
														.querySelector(
															"[href]"
														);
													z
														&&
														z
														.classList
														.add(
															"active"
														)
												}
											}
											this
												.activeSection =
												B
										}
									}
								}, {
									key: "_scrollTo",
									value: function(
										M) {
										var
											O =
											M
											.$scrollspyEl,
											N =
											M
											.$scrollableEl,
											D =
											M
											.$link,
											B =
											document
											.querySelector(
												D
												.getAttribute(
													"href"
												)
											),
											h =
											parseInt(
												this
												.getClassProperty(
													O,
													"--scrollspy-offset",
													"0"
												)
											),
											G =
											this
											.getClassProperty(
												B,
												"--scrollspy-offset"
											) ||
											h,
											F =
											N ===
											document ?
											0 :
											N
											.offsetTop,
											W =
											B
											.offsetTop -
											G -
											F,
											x =
											N ===
											document ?
											window :
											N;
										this
											._fireEvent(
												"scroll",
												O
											),
											this
											._dispatch(
												"scroll.hs.scrollspy",
												O,
												O
											),
											window
											.history
											.replaceState(
												null,
												null,
												D
												.getAttribute(
													"href"
												)
											),
											x
											.scrollTo({
												top: W,
												left: 0,
												behavior: "smooth"
											})
									}
								}]) && o(C.prototype, L),
								Object.defineProperty(C,
									"prototype", {
										writable: !1
									}), b
						}(S(765)
							.Z);
						window.HSScrollspy = new P,
							document.addEventListener(
								"load", window.HSScrollspy.init()
							)
					},
					51: (n, s, S) => {
						function A(L) {
							return A = typeof Symbol ==
								"function" && typeof Symbol
								.iterator == "symbol" ?
								function(I) {
									return typeof I
								} : function(I) {
									return I && typeof Symbol ==
										"function" && I.constructor ===
										Symbol && I !==
										Symbol.prototype ?
										"symbol" : typeof I
								}, A(L)
						}

						function o(L) {
							return function(I) {
								if (Array.isArray(I))
									return i(I)
							}(L) || function(I) {
								if (typeof Symbol < "u" &&
									I[Symbol.iterator] !=
									null || I[
										"@@iterator"] !=
									null) return Array.from(
									I)
							}(L) || function(I, u) {
								if (I) {
									if (typeof I ==
										"string") return i(
										I, u);
									var H = Object.prototype
										.toString.call(
											I)
										.slice(8, -1);
									return H ===
										"Object" && I.constructor &&
										(H = I.constructor
											.name), H ===
										"Map" || H ===
										"Set" ? Array.from(
											I) : H ===
										"Arguments" ||
										/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/
										.test(H) ? i(I,
											u) : void 0
								}
							}(L) || function() {
								throw new TypeError(
									`Invalid attempt to spread non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`
								)
							}()
						}

						function i(L, I) {
							(I == null || I > L.length) &&
							(I = L.length);
							for (var u = 0, H = new Array(I); u <
								I; u++) H[u] = L[u];
							return H
						}

						function _(L, I) {
							for (var u = 0; u < I.length; u++) {
								var H = I[u];
								H.enumerable = H.enumerable ||
									!1, H.configurable = !0,
									"value" in H && (H.writable = !
										0), Object.defineProperty(
										L, H.key, H)
							}
						}

						function c(L, I) {
							return c = Object.setPrototypeOf ||
								function(u, H) {
									return u.__proto__ = H,
										u
								}, c(L, I)
						}

						function P(L, I) {
							if (I && (A(I) === "object" ||
								typeof I == "function"))
								return I;
							if (I !== void 0) throw new TypeError(
								"Derived constructors may only return object or undefined"
							);
							return function(u) {
								if (u === void 0) throw new ReferenceError(
									"this hasn't been initialised - super() hasn't been called"
								);
								return u
							}(L)
						}

						function p(L) {
							return p = Object.setPrototypeOf ?
								Object.getPrototypeOf :
								function(I) {
									return I.__proto__ ||
										Object.getPrototypeOf(
											I)
								}, p(L)
						}
						var C = function(L) {
							(function(N, D) {
								if (typeof D !=
									"function" && D !==
									null) throw new TypeError(
									"Super expression must either be null or a function"
								);
								N.prototype =
									Object.create(D &&
										D.prototype, {
											constructor: {
												value: N,
												writable:
													!
													0,
												configurable:
													!
													0
											}
										}), Object.defineProperty(
										N,
										"prototype", {
											writable:
												!1
										}), D && c(
										N, D)
							})(O, L);
							var I, u, H, b, M = (H = O,
								b = function() {
									if (typeof Reflect >
										"u" || !
										Reflect.construct ||
										Reflect.construct
										.sham)
										return !1;
									if (typeof Proxy ==
										"function")
										return !0;
									try {
										return Boolean
											.prototype
											.valueOf
											.call(
												Reflect
												.construct(
													Boolean,
													[],
													function() {}
												)),
											!0
									} catch {
										return !1
									}
								}(),
								function() {
									var N, D = p(H);
									if (b) {
										var B = p(
												this
											)
											.constructor;
										N = Reflect
											.construct(
												D,
												arguments,
												B)
									} else N = D.apply(
										this,
										arguments
									);
									return P(this,
										N)
								});

							function O() {
								return function(N, D) {
									if (!(N instanceof D))
										throw new TypeError(
											"Cannot call a class as a function"
										)
								}(this, O), M.call(
									this,
									"[data-hs-tab]"
								)
							}
							return I = O, (u = [{
									key: "init",
									value: function() {
										var
											N =
											this;
										document
											.addEventListener(
												"keydown",
												this
												._keyboardSupport
												.bind(
													this
												)
											),
											document
											.addEventListener(
												"click",
												function(
													D
												) {
													var
														B =
														D
														.target
														.closest(
															N
															.selector
														);
													B
														&&
														N
														.open(
															B
														)
												}
											),
											document
											.querySelectorAll(
												"[hs-data-tab-select]"
											)
											.forEach(
												function(
													D
												) {
													var
														B =
														document
														.querySelector(
															D
															.getAttribute(
																"hs-data-tab-select"
															)
														);
													B
														&&
														B
														.addEventListener(
															"change",
															function(
																h
															) {
																var
																	G =
																	document
																	.querySelector(
																		'[data-hs-tab="'
																		.concat(
																			h
																			.target
																			.value,
																			'"]'
																		)
																	);
																G
																	&&
																	N
																	.open(
																		G
																	)
															}
														)
												}
											)
									}
								}, {
									key: "open",
									value: function(
										N) {
										var
											D =
											document
											.querySelector(
												N
												.getAttribute(
													"data-hs-tab"
												)
											),
											B =
											o(
												N
												.parentElement
												.children
											),
											h =
											o(
												D
												.parentElement
												.children
											),
											G =
											N
											.closest(
												"[hs-data-tab-select]"
											),
											F =
											G ?
											document
											.querySelector(
												G
												.getAttribute(
													"data-hs-tab"
												)
											) :
											null;
										B.forEach(
												function(
													W
												) {
													return W
														.classList
														.remove(
															"active"
														)
												}
											),
											h
											.forEach(
												function(
													W
												) {
													return W
														.classList
														.add(
															"hidden"
														)
												}
											),
											N
											.classList
											.add(
												"active"
											),
											D
											.classList
											.remove(
												"hidden"
											),
											this
											._fireEvent(
												"change",
												N
											),
											this
											._dispatch(
												"change.hs.tab",
												N,
												N
											),
											F &&
											(
												F
												.value =
												N
												.getAttribute(
													"data-hs-tab"
												)
											)
									}
								}, {
									key: "_keyboardSupport",
									value: function(
										N) {
										var
											D =
											N
											.target
											.closest(
												this
												.selector
											);
										if (
											D
										) {
											var
												B =
												D
												.closest(
													'[role="tablist"]'
												)
												.getAttribute(
													"data-hs-tabs-vertical"
												) ===
												"true";
											return (
													B ?
													N
													.keyCode ===
													38 :
													N
													.keyCode ===
													37
												) ?
												(
													N
													.preventDefault(),
													this
													._left(
														D
													)
												) :
												(
													B ?
													N
													.keyCode ===
													40 :
													N
													.keyCode ===
													39
												) ?
												(
													N
													.preventDefault(),
													this
													._right(
														D
													)
												) :
												N
												.keyCode ===
												36 ?
												(
													N
													.preventDefault(),
													this
													._start(
														D
													)
												) :
												N
												.keyCode ===
												35 ?
												(
													N
													.preventDefault(),
													this
													._end(
														D
													)
												) :
												void 0
										}
									}
								}, {
									key: "_right",
									value: function(
										N) {
										var
											D =
											N
											.closest(
												'[role="tablist"]'
											);
										if (
											D
										) {
											var
												B =
												o(
													D
													.querySelectorAll(
														this
														.selector
													)
												)
												.filter(
													function(
														F
													) {
														return !
															F
															.disabled
													}
												),
												h =
												D
												.querySelector(
													"button:focus"
												),
												G =
												B
												.findIndex(
													function(
														F
													) {
														return F ===
															h
													}
												);
											G
												+
												1 <
												B
												.length ?
												G++
												:
												G =
												0,
												B[
													G
												]
												.focus(),
												this
												.open(
													B[
														G
													]
												)
										}
									}
								}, {
									key: "_left",
									value: function(
										N) {
										var
											D =
											N
											.closest(
												'[role="tablist"]'
											);
										if (
											D
										) {
											var
												B =
												o(
													D
													.querySelectorAll(
														this
														.selector
													)
												)
												.filter(
													function(
														F
													) {
														return !
															F
															.disabled
													}
												)
												.reverse(),
												h =
												D
												.querySelector(
													"button:focus"
												),
												G =
												B
												.findIndex(
													function(
														F
													) {
														return F ===
															h
													}
												);
											G
												+
												1 <
												B
												.length ?
												G++
												:
												G =
												0,
												B[
													G
												]
												.focus(),
												this
												.open(
													B[
														G
													]
												)
										}
									}
								}, {
									key: "_start",
									value: function(
										N) {
										var
											D =
											N
											.closest(
												'[role="tablist"]'
											);
										if (
											D
										) {
											var
												B =
												o(
													D
													.querySelectorAll(
														this
														.selector
													)
												)
												.filter(
													function(
														h
													) {
														return !
															h
															.disabled
													}
												);
											B
												.length &&
												(
													B[
														0
													]
													.focus(),
													this
													.open(
														B[
															0
														]
													)
												)
										}
									}
								}, {
									key: "_end",
									value: function(
										N) {
										var
											D =
											N
											.closest(
												'[role="tablist"]'
											);
										if (
											D
										) {
											var
												B =
												o(
													D
													.querySelectorAll(
														this
														.selector
													)
												)
												.reverse()
												.filter(
													function(
														h
													) {
														return !
															h
															.disabled
													}
												);
											B
												.length &&
												(
													B[
														0
													]
													.focus(),
													this
													.open(
														B[
															0
														]
													)
												)
										}
									}
								}]) && _(I.prototype, u),
								Object.defineProperty(I,
									"prototype", {
										writable: !1
									}), O
						}(S(765)
							.Z);
						window.HSTabs = new C, document.addEventListener(
							"load", window.HSTabs.init()
						)
					},
					185: (n, s, S) => {
						var A = S(765),
							o = S(714);

						function i(L) {
							return i = typeof Symbol ==
								"function" && typeof Symbol
								.iterator == "symbol" ?
								function(I) {
									return typeof I
								} : function(I) {
									return I && typeof Symbol ==
										"function" && I.constructor ===
										Symbol && I !==
										Symbol.prototype ?
										"symbol" : typeof I
								}, i(L)
						}

						function _(L, I) {
							for (var u = 0; u < I.length; u++) {
								var H = I[u];
								H.enumerable = H.enumerable ||
									!1, H.configurable = !0,
									"value" in H && (H.writable = !
										0), Object.defineProperty(
										L, H.key, H)
							}
						}

						function c(L, I) {
							return c = Object.setPrototypeOf ||
								function(u, H) {
									return u.__proto__ = H,
										u
								}, c(L, I)
						}

						function P(L, I) {
							if (I && (i(I) === "object" ||
								typeof I == "function"))
								return I;
							if (I !== void 0) throw new TypeError(
								"Derived constructors may only return object or undefined"
							);
							return function(u) {
								if (u === void 0) throw new ReferenceError(
									"this hasn't been initialised - super() hasn't been called"
								);
								return u
							}(L)
						}

						function p(L) {
							return p = Object.setPrototypeOf ?
								Object.getPrototypeOf :
								function(I) {
									return I.__proto__ ||
										Object.getPrototypeOf(
											I)
								}, p(L)
						}
						var C = function(L) {
							(function(N, D) {
								if (typeof D !=
									"function" && D !==
									null) throw new TypeError(
									"Super expression must either be null or a function"
								);
								N.prototype =
									Object.create(D &&
										D.prototype, {
											constructor: {
												value: N,
												writable:
													!
													0,
												configurable:
													!
													0
											}
										}), Object.defineProperty(
										N,
										"prototype", {
											writable:
												!1
										}), D && c(
										N, D)
							})(O, L);
							var I, u, H, b, M = (H = O,
								b = function() {
									if (typeof Reflect >
										"u" || !
										Reflect.construct ||
										Reflect.construct
										.sham)
										return !1;
									if (typeof Proxy ==
										"function")
										return !0;
									try {
										return Boolean
											.prototype
											.valueOf
											.call(
												Reflect
												.construct(
													Boolean,
													[],
													function() {}
												)),
											!0
									} catch {
										return !1
									}
								}(),
								function() {
									var N, D = p(H);
									if (b) {
										var B = p(
												this
											)
											.constructor;
										N = Reflect
											.construct(
												D,
												arguments,
												B)
									} else N = D.apply(
										this,
										arguments
									);
									return P(this,
										N)
								});

							function O() {
								return function(N, D) {
									if (!(N instanceof D))
										throw new TypeError(
											"Cannot call a class as a function"
										)
								}(this, O), M.call(
									this,
									".hs-tooltip")
							}
							return I = O, (u = [{
									key: "init",
									value: function() {
										var
											N =
											this;
										document
											.addEventListener(
												"click",
												function(
													D
												) {
													var
														B =
														D
														.target
														.closest(
															N
															.selector
														);
													B
														&&
														N
														.getClassProperty(
															B,
															"--trigger"
														) ===
														"focus" &&
														N
														._focus(
															B
														),
														B &&
														N
														.getClassProperty(
															B,
															"--trigger"
														) ===
														"click" &&
														N
														._click(
															B
														)
												}
											),
											document
											.addEventListener(
												"mousemove",
												function(
													D
												) {
													var
														B =
														D
														.target
														.closest(
															N
															.selector
														);
													B
														&&
														N
														.getClassProperty(
															B,
															"--trigger"
														) !==
														"focus" &&
														N
														.getClassProperty(
															B,
															"--trigger"
														) !==
														"click" &&
														N
														._hover(
															B
														)
												}
											)
									}
								}, {
									key: "_hover",
									value: function(
										N) {
										var
											D =
											this;
										if (
											!
											N
											.classList
											.contains(
												"show"
											)
										) {
											var
												B =
												N
												.querySelector(
													".hs-tooltip-toggle"
												),
												h =
												N
												.querySelector(
													".hs-tooltip-content"
												),
												G =
												this
												.getClassProperty(
													N,
													"--placement"
												);
											(
												0,
												o
												.fi
											)
											(
												B,
												h, {
													placement: G ||
														"top",
													strategy: "fixed",
													modifiers: [{
														name: "offset",
														options: {
															offset: [
																0,
																5
															]
														}
													}]
												}
											),
											this
												.show(
													N
												),
												N
												.addEventListener(
													"mouseleave",
													function F(
														W
													) {
														W
															.relatedTarget
															.closest(
																D
																.selector
															) &&
															W
															.relatedTarget
															.closest(
																D
																.selector
															) ==
															N ||
															(
																D
																.hide(
																	N
																),
																N
																.removeEventListener(
																	"mouseleave",
																	F,
																	!
																	0
																)
															)
													},
													!
													0
												)
										}
									}
								}, {
									key: "_focus",
									value: function(
										N) {
										var
											D =
											this,
											B =
											N
											.querySelector(
												".hs-tooltip-toggle"
											),
											h =
											N
											.querySelector(
												".hs-tooltip-content"
											),
											G =
											this
											.getClassProperty(
												N,
												"--placement"
											),
											F =
											this
											.getClassProperty(
												N,
												"--strategy"
											);
										(0,
											o
											.fi
										)(B,
											h, {
												placement: G ||
													"top",
												strategy: F ||
													"fixed",
												modifiers: [{
													name: "offset",
													options: {
														offset: [
															0,
															5
														]
													}
												}]
											}
										),
										this
											.show(
												N
											),
											N
											.addEventListener(
												"blur",
												function W() {
													D
														.hide(
															N
														),
														N
														.removeEventListener(
															"blur",
															W,
															!
															0
														)
												},
												!
												0
											)
									}
								}, {
									key: "_click",
									value: function(
										N) {
										var
											D =
											this;
										if (
											!
											N
											.classList
											.contains(
												"show"
											)
										) {
											var
												B =
												N
												.querySelector(
													".hs-tooltip-toggle"
												),
												h =
												N
												.querySelector(
													".hs-tooltip-content"
												),
												G =
												this
												.getClassProperty(
													N,
													"--placement"
												),
												F =
												this
												.getClassProperty(
													N,
													"--strategy"
												);
											(
												0,
												o
												.fi
											)
											(
												B,
												h, {
													placement: G ||
														"top",
													strategy: F ||
														"fixed",
													modifiers: [{
														name: "offset",
														options: {
															offset: [
																0,
																5
															]
														}
													}]
												}
											),
											this
												.show(
													N
												);
											var
												W =
												function x(
													J
												) {
													setTimeout
														(
															function() {
																D
																	.hide(
																		N
																	),
																	N
																	.removeEventListener(
																		"click",
																		x,
																		!
																		0
																	),
																	N
																	.removeEventListener(
																		"blur",
																		x,
																		!
																		0
																	)
															}
														)
												};
											N
												.addEventListener(
													"blur",
													W,
													!
													0
												),
												N
												.addEventListener(
													"click",
													W,
													!
													0
												)
										}
									}
								}, {
									key: "show",
									value: function(
										N) {
										var
											D =
											this;
										N.querySelector(
												".hs-tooltip-content"
											)
											.classList
											.remove(
												"hidden"
											),
											setTimeout(
												function() {
													N
														.classList
														.add(
															"show"
														),
														D
														._fireEvent(
															"show",
															N
														),
														D
														._dispatch(
															"show.hs.tooltip",
															N,
															N
														)
												}
											)
									}
								}, {
									key: "hide",
									value: function(
										N) {
										var
											D =
											N
											.querySelector(
												".hs-tooltip-content"
											);
										N.classList
											.remove(
												"show"
											),
											this
											._fireEvent(
												"hide",
												N
											),
											this
											._dispatch(
												"hide.hs.tooltip",
												N,
												N
											),
											this
											.afterTransition(
												D,
												function() {
													N
														.classList
														.contains(
															"show"
														) ||
														D
														.classList
														.add(
															"hidden"
														)
												}
											)
									}
								}]) && _(I.prototype, u),
								Object.defineProperty(I,
									"prototype", {
										writable: !1
									}), O
						}(A.Z);
						window.HSTooltip = new C, document.addEventListener(
							"load", window.HSTooltip.init()
						)
					},
					765: (n, s, S) => {
						function A(i, _) {
							for (var c = 0; c < _.length; c++) {
								var P = _[c];
								P.enumerable = P.enumerable ||
									!1, P.configurable = !0,
									"value" in P && (P.writable = !
										0), Object.defineProperty(
										i, P.key, P)
							}
						}
						S.d(s, {
							Z: () => o
						});
						var o = function() {
							function i(P, p) {
								(function(C, L) {
									if (!(C instanceof L))
										throw new TypeError(
											"Cannot call a class as a function"
										)
								})(this, i), this.$collection = [],
									this.selector = P,
									this.config = p,
									this.events = {}
							}
							var _, c;
							return _ = i, c = [{
								key: "_fireEvent",
								value: function(
									P) {
									var p =
										arguments
										.length >
										1 &&
										arguments[
											1
										] !==
										void 0 ?
										arguments[
											1
										] :
										null;
									this.events
										.hasOwnProperty(
											P
										) &&
										this
										.events[
											P
										](p)
								}
							}, {
								key: "_dispatch",
								value: function(
									P, p) {
									var C =
										arguments
										.length >
										2 &&
										arguments[
											2
										] !==
										void 0 ?
										arguments[
											2
										] :
										null,
										L =
										new CustomEvent(
											P, {
												detail: {
													payload: C
												},
												bubbles:
													!
													0,
												cancelable:
													!
													0,
												composed:
													!
													1
											}
										);
									p.dispatchEvent(
										L
									)
								}
							}, {
								key: "on",
								value: function(
									P, p) {
									this.events[
											P
										] =
										p
								}
							}, {
								key: "afterTransition",
								value: function(
									P, p) {
									window.getComputedStyle(
											P,
											null
										)
										.getPropertyValue(
											"transition"
										) !==
										"all 0s ease 0s" ?
										P.addEventListener(
											"transitionend",
											function C() {
												p
													(),
													P
													.removeEventListener(
														"transitionend",
														C,
														!
														0
													)
											},
											!
											0
										) :
										p()
								}
							}, {
								key: "getClassProperty",
								value: function(
									P, p) {
									var C =
										arguments
										.length >
										2 &&
										arguments[
											2
										] !==
										void 0 ?
										arguments[
											2
										] :
										"",
										L =
										(
											window
											.getComputedStyle(
												P
											)
											.getPropertyValue(
												p
											) ||
											C
										)
										.replace(
											" ",
											""
										);
									return L
								}
							}], c && A(_.prototype,
								c), Object.defineProperty(
								_, "prototype", {
									writable: !1
								}), i
						}()
					},
					714: (n, s, S) => {
						function A(U) {
							if (U == null) return window;
							if (U.toString() !==
								"[object Window]") {
								var d = U.ownerDocument;
								return d && d.defaultView ||
									window
							}
							return U
						}

						function o(U) {
							return U instanceof A(U)
								.Element || U instanceof Element
						}

						function i(U) {
							return U instanceof A(U)
								.HTMLElement || U instanceof HTMLElement
						}

						function _(U) {
							return typeof ShadowRoot < "u" &&
								(U instanceof A(U)
									.ShadowRoot || U instanceof ShadowRoot
								)
						}
						S.d(s, {
							fi: () => tn
						});
						var c = Math.max,
							P = Math.min,
							p = Math.round;

						function C(U, d) {
							d === void 0 && (d = !1);
							var g = U.getBoundingClientRect(),
								w = 1,
								Z = 1;
							if (i(U) && d) {
								var q = U.offsetHeight,
									Q = U.offsetWidth;
								Q > 0 && (w = p(g.width) /
									Q || 1), q > 0 && (
									Z = p(g.height) / q ||
									1)
							}
							return {
								width: g.width / w,
								height: g.height / Z,
								top: g.top / Z,
								right: g.right / w,
								bottom: g.bottom / Z,
								left: g.left / w,
								x: g.left / w,
								y: g.top / Z
							}
						}

						function L(U) {
							var d = A(U);
							return {
								scrollLeft: d.pageXOffset,
								scrollTop: d.pageYOffset
							}
						}

						function I(U) {
							return U ? (U.nodeName || "")
								.toLowerCase() : null
						}

						function u(U) {
							return ((o(U) ? U.ownerDocument :
										U.document) ||
									window.document)
								.documentElement
						}

						function H(U) {
							return C(u(U))
								.left + L(U)
								.scrollLeft
						}

						function b(U) {
							return A(U)
								.getComputedStyle(U)
						}

						function M(U) {
							var d = b(U),
								g = d.overflow,
								w = d.overflowX,
								Z = d.overflowY;
							return /auto|scroll|overlay|hidden/
								.test(g + Z + w)
						}

						function O(U, d, g) {
							g === void 0 && (g = !1);
							var w, Z, q = i(d),
								Q = i(d) && function(re) {
									var We = re.getBoundingClientRect(),
										ae = p(We.width) /
										re.offsetWidth || 1,
										Me = p(We.height) /
										re.offsetHeight ||
										1;
									return ae !== 1 || Me !==
										1
								}(d),
								ee = u(d),
								Ee = C(U, Q),
								ne = {
									scrollLeft: 0,
									scrollTop: 0
								},
								Ae = {
									x: 0,
									y: 0
								};
							return (q || !q && !g) && ((I(d) !==
									"body" || M(ee)) &&
								(ne = (w = d) !== A(w) &&
									i(w) ? {
										scrollLeft: (Z =
												w)
											.scrollLeft,
										scrollTop: Z.scrollTop
									} : L(w)), i(d) ? (
									(Ae = C(d, !0))
									.x += d.clientLeft,
									Ae.y += d.clientTop
								) : ee && (Ae.x = H(ee))
							), {
								x: Ee.left + ne.scrollLeft -
									Ae.x,
								y: Ee.top + ne.scrollTop -
									Ae.y,
								width: Ee.width,
								height: Ee.height
							}
						}

						function N(U) {
							var d = C(U),
								g = U.offsetWidth,
								w = U.offsetHeight;
							return Math.abs(d.width - g) <=
								1 && (g = d.width), Math.abs(
									d.height - w) <= 1 && (
									w = d.height), {
									x: U.offsetLeft,
									y: U.offsetTop,
									width: g,
									height: w
								}
						}

						function D(U) {
							return I(U) === "html" ? U : U.assignedSlot ||
								U.parentNode || (_(U) ? U.host :
									null) || u(U)
						}

						function B(U) {
							return ["html", "body",
									"#document"
								].indexOf(I(U)) >= 0 ? U.ownerDocument
								.body : i(U) && M(U) ? U :
								B(D(U))
						}

						function h(U, d) {
							var g;
							d === void 0 && (d = []);
							var w = B(U),
								Z = w === ((g = U.ownerDocument) ==
									null ? void 0 : g.body),
								q = A(w),
								Q = Z ? [q].concat(q.visualViewport || [], M(w) ? w : []) : w,
								ee = d.concat(Q);
							return Z ? ee : ee.concat(h(D(Q)))
						}

						function G(U) {
							return ["table", "td", "th"].indexOf(
								I(U)) >= 0
						}

						function F(U) {
							return i(U) && b(U)
								.position !== "fixed" ? U.offsetParent :
								null
						}

						function W(U) {
							for (var d = A(U), g = F(U); g &&
								G(g) && b(g)
								.position === "static";) g =
								F(g);
							return g && (I(g) === "html" ||
									I(g) === "body" && b(g)
									.position === "static") ?
								d : g || function(w) {
									var Z = navigator.userAgent
										.toLowerCase()
										.indexOf("firefox") !==
										-1;
									if (navigator.userAgent
										.indexOf("Trident") !==
										-1 && i(w) && b(w)
										.position ===
										"fixed") return null;
									for (var q = D(w); i(q) && ["html", "body"].indexOf(
										I(q)) < 0;) {
										var Q = b(q);
										if (Q.transform !==
											"none" || Q.perspective !==
											"none" || Q.contain ===
											"paint" || [
												"transform",
												"perspective"
											].indexOf(Q.willChange) !==
											-1 || Z && Q.willChange ===
											"filter" || Z &&
											Q.filter && Q.filter !==
											"none") return q;
										q = q.parentNode
									}
									return null
								}(U) || d
						}
						var x = "top",
							J = "bottom",
							oe = "right",
							z = "left",
							Oe = "auto",
							Ue = [x, J, oe, z],
							ye = "start",
							TE = "end",
							dE = "viewport",
							me = "popper",
							fE = Ue.reduce(function(U, d) {
								return U.concat([d +
									"-" + ye, d +
									"-" + TE
								])
							}, []),
							rE = [].concat(Ue, [Oe])
							.reduce(function(U, d) {
								return U.concat([d, d +
									"-" + ye, d +
									"-" + TE
								])
							}, []),
							pE = ["beforeRead", "read",
								"afterRead", "beforeMain",
								"main", "afterMain",
								"beforeWrite", "write",
								"afterWrite"
							];

						function Tt(U) {
							var d = new Map,
								g = new Set,
								w = [];

							function Z(q) {
								g.add(q.name), [].concat(q.requires || [], q.requiresIfExists || [])
									.forEach(function(Q) {
										if (!g.has(Q)) {
											var ee = d.get(
												Q);
											ee && Z(ee)
										}
									}), w.push(q)
							}
							return U.forEach(function(q) {
								d.set(q.name, q)
							}), U.forEach(function(q) {
								g.has(q.name) || Z(
									q)
							}), w
						}
						var rt = {
							placement: "bottom",
							modifiers: [],
							strategy: "absolute"
						};

						function Ve() {
							for (var U = arguments.length,
									d = new Array(U), g = 0; g <
								U; g++) d[g] = arguments[g];
							return !d.some(function(w) {
								return !(w &&
									typeof w.getBoundingClientRect ==
									"function")
							})
						}

						function ME(U) {
							U === void 0 && (U = {});
							var d = U,
								g = d.defaultModifiers,
								w = g === void 0 ? [] : g,
								Z = d.defaultOptions,
								q = Z === void 0 ? rt : Z;
							return function(Q, ee, Ee) {
								Ee === void 0 && (Ee =
									q);
								var ne, Ae, re = {
										placement: "bottom",
										orderedModifiers: [],
										options: Object
											.assign({},
												rt, q),
										modifiersData: {},
										elements: {
											reference: Q,
											popper: ee
										},
										attributes: {},
										styles: {}
									},
									We = [],
									ae = !1,
									Me = {
										state: re,
										setOptions: function(
											ie) {
											var we =
												typeof ie ==
												"function" ?
												ie(
													re
													.options
												) :
												ie;
											de(),
												re.options =
												Object
												.assign({},
													q,
													re
													.options,
													we
												),
												re.scrollParents = {
													reference: o(
															Q
														) ?
														h(
															Q
														) : Q
														.contextElement ?
														h(
															Q
															.contextElement
														) : [],
													popper: h(
														ee
													)
												};
											var be,
												ce,
												he =
												function(
													Ie
												) {
													var
														le =
														Tt(
															Ie
														);
													return pE
														.reduce(
															function(
																fe,
																pe
															) {
																return fe
																	.concat(
																		le
																		.filter(
																			function(
																				He
																			) {
																				return He
																					.phase ===
																					pe
																			}
																		)
																	)
															},
															[]
														)
												}((
													be = []
													.concat(
														w,
														re
														.options
														.modifiers
													),
													ce =
													be
													.reduce(
														function(
															Ie,
															le
														) {
															var
																fe =
																Ie[
																	le
																	.name
																];
															return Ie[
																	le
																	.name
																] =
																fe ?
																Object
																.assign({},
																	fe,
																	le, {
																		options: Object
																			.assign({},
																				fe
																				.options,
																				le
																				.options
																			),
																		data: Object
																			.assign({},
																				fe
																				.data,
																				le
																				.data
																			)
																	}
																) :
																le,
																Ie
														}, {}
													),
													Object
													.keys(
														ce
													)
													.map(
														function(
															Ie
														) {
															return ce[
																Ie
															]
														}
													)
												));
											return re
												.orderedModifiers =
												he.filter(
													function(
														Ie
													) {
														return Ie
															.enabled
													}
												),
												re.orderedModifiers
												.forEach(
													function(
														Ie
													) {
														var
															le =
															Ie
															.name,
															fe =
															Ie
															.options,
															pe =
															fe ===
															void 0 ? {} :
															fe,
															He =
															Ie
															.effect;
														if (
															typeof He ==
															"function"
														) {
															var
																ke =
																He({
																	state: re,
																	name: le,
																	instance: Me,
																	options: pe
																});
															We
																.push(
																	ke ||
																	function() {}
																)
														}
													}
												),
												Me.update()
										},
										forceUpdate: function() {
											if (!ae) {
												var
													ie =
													re
													.elements,
													we =
													ie
													.reference,
													be =
													ie
													.popper;
												if (
													Ve(
														we,
														be
													)
												) {
													re
														.rects = {
															reference: O(
																we,
																W(
																	be
																),
																re
																.options
																.strategy ===
																"fixed"
															),
															popper: N(
																be
															)
														},
														re
														.reset = !
														1,
														re
														.placement =
														re
														.options
														.placement,
														re
														.orderedModifiers
														.forEach(
															function(
																He
															) {
																return re
																	.modifiersData[
																		He
																		.name
																	] =
																	Object
																	.assign({},
																		He
																		.data
																	)
															}
														);
													for (
														var
															ce =
															0; ce <
														re
														.orderedModifiers
														.length; ce++
													)
														if (
															re
															.reset !==
															!
															0
														) {
															var
																he =
																re
																.orderedModifiers[
																	ce
																],
																Ie =
																he
																.fn,
																le =
																he
																.options,
																fe =
																le ===
																void 0 ? {} :
																le,
																pe =
																he
																.name;
															typeof Ie
																==
																"function" &&
																(
																	re =
																	Ie({
																		state: re,
																		options: fe,
																		name: pe,
																		instance: Me
																	}) ||
																	re
																)
														} else
															re
															.reset = !
															1,
															ce = -
															1
												}
											}
										},
										update: (ne =
											function() {
												return new Promise(
													function(
														ie
													) {
														Me
															.forceUpdate(),
															ie(
																re
															)
													}
												)
											},
											function() {
												return Ae ||
													(
														Ae =
														new Promise(
															function(
																ie
															) {
																Promise
																	.resolve()
																	.then(
																		function() {
																			Ae
																				=
																				void 0,
																				ie(
																					ne()
																				)
																		}
																	)
															}
														)
													),
													Ae
											}),
										destroy: function() {
											de(),
												ae = !
												0
										}
									};
								if (!Ve(Q, ee)) return Me;

								function de() {
									We.forEach(function(
										ie) {
										return ie()
									}), We = []
								}
								return Me.setOptions(Ee)
									.then(function(ie) {
										!ae && Ee.onFirstUpdate &&
											Ee.onFirstUpdate(
												ie)
									}), Me
							}
						}
						var $e = {
							passive: !0
						};

						function ze(U) {
							return U.split("-")[0]
						}

						function ve(U) {
							return U.split("-")[1]
						}

						function Fe(U) {
							return ["top", "bottom"].indexOf(
								U) >= 0 ? "x" : "y"
						}

						function Te(U) {
							var d, g = U.reference,
								w = U.element,
								Z = U.placement,
								q = Z ? ze(Z) : null,
								Q = Z ? ve(Z) : null,
								ee = g.x + g.width / 2 - w.width /
								2,
								Ee = g.y + g.height / 2 - w
								.height / 2;
							switch (q) {
								case x:
									d = {
										x: ee,
										y: g.y - w.height
									};
									break;
								case J:
									d = {
										x: ee,
										y: g.y + g.height
									};
									break;
								case oe:
									d = {
										x: g.x + g.width,
										y: Ee
									};
									break;
								case z:
									d = {
										x: g.x - w.width,
										y: Ee
									};
									break;
								default:
									d = {
										x: g.x,
										y: g.y
									}
							}
							var ne = q ? Fe(q) : null;
							if (ne != null) {
								var Ae = ne === "y" ?
									"height" : "width";
								switch (Q) {
									case ye:
										d[ne] = d[ne] - (g[
												Ae] / 2 -
											w[Ae] / 2);
										break;
									case TE:
										d[ne] = d[ne] + (g[
												Ae] / 2 -
											w[Ae] / 2)
								}
							}
							return d
						}
						var Xe = {
							top: "auto",
							right: "auto",
							bottom: "auto",
							left: "auto"
						};

						function se(U) {
							var d, g = U.popper,
								w = U.popperRect,
								Z = U.placement,
								q = U.variation,
								Q = U.offsets,
								ee = U.position,
								Ee = U.gpuAcceleration,
								ne = U.adaptive,
								Ae = U.roundOffsets,
								re = U.isFixed,
								We = Q.x,
								ae = We === void 0 ? 0 : We,
								Me = Q.y,
								de = Me === void 0 ? 0 : Me,
								ie = typeof Ae ==
								"function" ? Ae({
									x: ae,
									y: de
								}) : {
									x: ae,
									y: de
								};
							ae = ie.x, de = ie.y;
							var we = Q.hasOwnProperty("x"),
								be = Q.hasOwnProperty("y"),
								ce = z,
								he = x,
								Ie = window;
							if (ne) {
								var le = W(g),
									fe = "clientHeight",
									pe = "clientWidth";
								le === A(g) && b(le = u(g))
									.position !== "static" &&
									ee === "absolute" && (
										fe = "scrollHeight",
										pe = "scrollWidth"),
									le = le, (Z === x || (Z ===
											z || Z === oe) &&
										q === TE) && (he =
										J, de -= (re && Ie.visualViewport ?
											Ie.visualViewport
											.height : le[fe]
										) - w.height, de *=
										Ee ? 1 : -1), Z !==
									z && (Z !== x && Z !==
										J || q !== TE) || (
										ce = oe, ae -= (re &&
											Ie.visualViewport ?
											Ie.visualViewport
											.width : le[pe]
										) - w.width, ae *=
										Ee ? 1 : -1)
							}
							var He, ke = Object.assign({
									position: ee
								}, ne && Xe),
								Ke = Ae === !0 ? function(
									sE) {
									var lE = sE.x,
										PE = sE.y,
										SE = window.devicePixelRatio ||
										1;
									return {
										x: p(lE * SE) / SE ||
											0,
										y: p(PE * SE) / SE ||
											0
									}
								}({
									x: ae,
									y: de
								}) : {
									x: ae,
									y: de
								};
							return ae = Ke.x, de = Ke.y, Ee ?
								Object.assign({}, ke, ((He = {})[
										he] = be ? "0" :
									"", He[ce] = we ?
									"0" : "", He.transform =
									(Ie.devicePixelRatio ||
										1) <= 1 ?
									"translate(" + ae +
									"px, " + de + "px)" :
									"translate3d(" + ae +
									"px, " + de +
									"px, 0)", He)) : Object
								.assign({}, ke, ((d = {})[
										he] = be ? de +
									"px" : "", d[ce] =
									we ? ae + "px" : "",
									d.transform = "", d
								))
						}
						var gE = {
							left: "right",
							right: "left",
							bottom: "top",
							top: "bottom"
						};

						function Nt(U) {
							return U.replace(
								/left|right|bottom|top/g,
								function(d) {
									return gE[d]
								})
						}
						var En = {
							start: "end",
							end: "start"
						};

						function dT(U) {
							return U.replace(/start|end/g,
								function(d) {
									return En[d]
								})
						}

						function pT(U, d) {
							var g = d.getRootNode && d.getRootNode();
							if (U.contains(d)) return !0;
							if (g && _(g)) {
								var w = d;
								do {
									if (w && U.isSameNode(w))
										return !0;
									w = w.parentNode || w.host
								} while (w)
							}
							return !1
						}

						function Bt(U) {
							return Object.assign({}, U, {
								left: U.x,
								top: U.y,
								right: U.x + U.width,
								bottom: U.y + U.height
							})
						}

						function MT(U, d) {
							return d === dE ? Bt(function(g) {
								var w = A(g),
									Z = u(g),
									q = w.visualViewport,
									Q = Z.clientWidth,
									ee = Z.clientHeight,
									Ee = 0,
									ne = 0;
								return q && (Q = q.width,
									ee = q.height,
									/^((?!chrome|android).)*safari/i
									.test(
										navigator
										.userAgent
									) || (Ee =
										q.offsetLeft,
										ne = q.offsetTop
									)), {
									width: Q,
									height: ee,
									x: Ee + H(g),
									y: ne
								}
							}(U)) : o(d) ? function(g) {
								var w = C(g);
								return w.top = w.top +
									g.clientTop, w.left =
									w.left + g.clientLeft,
									w.bottom = w.top +
									g.clientHeight, w.right =
									w.left + g.clientWidth,
									w.width = g.clientWidth,
									w.height = g.clientHeight,
									w.x = w.left, w.y =
									w.top, w
							}(d) : Bt(function(g) {
								var w, Z = u(g),
									q = L(g),
									Q = (w = g.ownerDocument) ==
									null ? void 0 :
									w.body,
									ee = c(Z.scrollWidth,
										Z.clientWidth,
										Q ? Q.scrollWidth :
										0, Q ? Q.clientWidth :
										0),
									Ee = c(Z.scrollHeight,
										Z.clientHeight,
										Q ? Q.scrollHeight :
										0, Q ? Q.clientHeight :
										0),
									ne = -q.scrollLeft +
									H(g),
									Ae = -q.scrollTop;
								return b(Q || Z)
									.direction ===
									"rtl" && (ne +=
										c(Z.clientWidth,
											Q ? Q.clientWidth :
											0) - ee
									), {
										width: ee,
										height: Ee,
										x: ne,
										y: Ae
									}
							}(u(U)))
						}

						function UT(U) {
							return Object.assign({}, {
								top: 0,
								right: 0,
								bottom: 0,
								left: 0
							}, U)
						}

						function mT(U, d) {
							return d.reduce(function(g, w) {
								return g[w] = U, g
							}, {})
						}

						function Rt(U, d) {
							d === void 0 && (d = {});
							var g = d,
								w = g.placement,
								Z = w === void 0 ? U.placement :
								w,
								q = g.boundary,
								Q = q === void 0 ?
								"clippingParents" : q,
								ee = g.rootBoundary,
								Ee = ee === void 0 ? dE :
								ee,
								ne = g.elementContext,
								Ae = ne === void 0 ? me :
								ne,
								re = g.altBoundary,
								We = re !== void 0 && re,
								ae = g.padding,
								Me = ae === void 0 ? 0 : ae,
								de = UT(typeof Me !=
									"number" ? Me : mT(Me,
										Ue)),
								ie = Ae === me ?
								"reference" : me,
								we = U.rects.popper,
								be = U.elements[We ? ie :
									Ae],
								ce = function(Ke, sE, lE) {
									var PE = sE ===
										"clippingParents" ?
										function(Be) {
											var UE = h(D(Be)),
												oE = [
													"absolute",
													"fixed"
												].indexOf(b(
														Be)
													.position
												) >= 0 && i(
													Be) ? W(
													Be) :
												Be;
											return o(oE) ?
												UE.filter(
													function(
														RE) {
														return o(
																RE
															) &&
															pT(
																RE,
																oE
															) &&
															I(
																RE
															) !==
															"body"
													}) : []
										}(Ke) : [].concat(
											sE),
										SE = [].concat(PE,
											[lE]),
										tE = SE[0],
										xe = SE.reduce(
											function(Be, UE) {
												var oE = MT(
													Ke,
													UE);
												return Be.top =
													c(oE.top,
														Be.top
													), Be.right =
													P(oE.right,
														Be.right
													), Be.bottom =
													P(oE.bottom,
														Be.bottom
													), Be.left =
													c(oE.left,
														Be.left
													), Be
											}, MT(Ke, tE));
									return xe.width = xe.right -
										xe.left, xe.height =
										xe.bottom - xe.top,
										xe.x = xe.left, xe.y =
										xe.top, xe
								}(o(be) ? be : be.contextElement ||
									u(U.elements.popper), Q,
									Ee),
								he = C(U.elements.reference),
								Ie = Te({
									reference: he,
									element: we,
									strategy: "absolute",
									placement: Z
								}),
								le = Bt(Object.assign({},
									we, Ie)),
								fe = Ae === me ? le : he,
								pe = {
									top: ce.top - fe.top +
										de.top,
									bottom: fe.bottom - ce.bottom +
										de.bottom,
									left: ce.left - fe.left +
										de.left,
									right: fe.right - ce.right +
										de.right
								},
								He = U.modifiersData.offset;
							if (Ae === me && He) {
								var ke = He[Z];
								Object.keys(pe)
									.forEach(function(Ke) {
										var sE = [oe, J]
											.indexOf(Ke) >=
											0 ? 1 : -1,
											lE = [x, J]
											.indexOf(Ke) >=
											0 ? "y" :
											"x";
										pe[Ke] += ke[lE] *
											sE
									})
							}
							return pe
						}

						function nt(U, d, g) {
							return c(U, P(d, g))
						}

						function hT(U, d, g) {
							return g === void 0 && (g = {
								x: 0,
								y: 0
							}), {
								top: U.top - d.height -
									g.y,
								right: U.right - d.width +
									g.x,
								bottom: U.bottom - d.height +
									g.y,
								left: U.left - d.width -
									g.x
							}
						}

						function GT(U) {
							return [x, oe, J, z].some(
								function(d) {
									return U[d] >= 0
								})
						}
						var tn = ME({
							defaultModifiers: [{
								name: "eventListeners",
								enabled: !0,
								phase: "write",
								fn: function() {},
								effect: function(
									U) {
									var
										d =
										U
										.state,
										g =
										U
										.instance,
										w =
										U
										.options,
										Z =
										w
										.scroll,
										q =
										Z ===
										void 0 ||
										Z,
										Q =
										w
										.resize,
										ee =
										Q ===
										void 0 ||
										Q,
										Ee =
										A(
											d
											.elements
											.popper
										),
										ne = []
										.concat(
											d
											.scrollParents
											.reference,
											d
											.scrollParents
											.popper
										);
									return q &&
										ne
										.forEach(
											function(
												Ae
											) {
												Ae
													.addEventListener(
														"scroll",
														g
														.update,
														$e
													)
											}
										),
										ee &&
										Ee
										.addEventListener(
											"resize",
											g
											.update,
											$e
										),
										function() {
											q
												&&
												ne
												.forEach(
													function(
														Ae
													) {
														Ae
															.removeEventListener(
																"scroll",
																g
																.update,
																$e
															)
													}
												),
												ee &&
												Ee
												.removeEventListener(
													"resize",
													g
													.update,
													$e
												)
										}
								},
								data: {}
							}, {
								name: "popperOffsets",
								enabled: !0,
								phase: "read",
								fn: function(
									U) {
									var
										d =
										U
										.state,
										g =
										U
										.name;
									d.modifiersData[
											g
										] =
										Te({
											reference: d
												.rects
												.reference,
											element: d
												.rects
												.popper,
											strategy: "absolute",
											placement: d
												.placement
										})
								},
								data: {}
							}, {
								name: "computeStyles",
								enabled: !0,
								phase: "beforeWrite",
								fn: function(
									U) {
									var
										d =
										U
										.state,
										g =
										U
										.options,
										w =
										g
										.gpuAcceleration,
										Z =
										w ===
										void 0 ||
										w,
										q =
										g
										.adaptive,
										Q =
										q ===
										void 0 ||
										q,
										ee =
										g
										.roundOffsets,
										Ee =
										ee ===
										void 0 ||
										ee,
										ne = {
											placement: ze(
												d
												.placement
											),
											variation: ve(
												d
												.placement
											),
											popper: d
												.elements
												.popper,
											popperRect: d
												.rects
												.popper,
											gpuAcceleration: Z,
											isFixed: d
												.options
												.strategy ===
												"fixed"
										};
									d.modifiersData
										.popperOffsets !=
										null &&
										(
											d
											.styles
											.popper =
											Object
											.assign({},
												d
												.styles
												.popper,
												se(
													Object
													.assign({},
														ne, {
															offsets: d
																.modifiersData
																.popperOffsets,
															position: d
																.options
																.strategy,
															adaptive: Q,
															roundOffsets: Ee
														}
													)
												)
											)
										),
										d
										.modifiersData
										.arrow !=
										null &&
										(
											d
											.styles
											.arrow =
											Object
											.assign({},
												d
												.styles
												.arrow,
												se(
													Object
													.assign({},
														ne, {
															offsets: d
																.modifiersData
																.arrow,
															position: "absolute",
															adaptive:
																!
																1,
															roundOffsets: Ee
														}
													)
												)
											)
										),
										d
										.attributes
										.popper =
										Object
										.assign({},
											d
											.attributes
											.popper, {
												"data-popper-placement": d
													.placement
											}
										)
								},
								data: {}
							}, {
								name: "applyStyles",
								enabled: !0,
								phase: "write",
								fn: function(
									U) {
									var
										d =
										U
										.state;
									Object
										.keys(
											d
											.elements
										)
										.forEach(
											function(
												g
											) {
												var
													w =
													d
													.styles[
														g
													] || {},
													Z =
													d
													.attributes[
														g
													] || {},
													q =
													d
													.elements[
														g
													];
												i
													(
														q
													) &&
													I(
														q
													) &&
													(
														Object
														.assign(
															q
															.style,
															w
														),
														Object
														.keys(
															Z
														)
														.forEach(
															function(
																Q
															) {
																var
																	ee =
																	Z[
																		Q
																	];
																ee
																	===
																	!
																	1 ?
																	q
																	.removeAttribute(
																		Q
																	) :
																	q
																	.setAttribute(
																		Q,
																		ee ===
																		!
																		0 ?
																		"" :
																		ee
																	)
															}
														)
													)
											}
										)
								},
								effect: function(
									U) {
									var
										d =
										U
										.state,
										g = {
											popper: {
												position: d
													.options
													.strategy,
												left: "0",
												top: "0",
												margin: "0"
											},
											arrow: {
												position: "absolute"
											},
											reference: {}
										};
									return Object
										.assign(
											d
											.elements
											.popper
											.style,
											g
											.popper
										),
										d
										.styles =
										g,
										d
										.elements
										.arrow &&
										Object
										.assign(
											d
											.elements
											.arrow
											.style,
											g
											.arrow
										),
										function() {
											Object
												.keys(
													d
													.elements
												)
												.forEach(
													function(
														w
													) {
														var
															Z =
															d
															.elements[
																w
															],
															q =
															d
															.attributes[
																w
															] || {},
															Q =
															Object
															.keys(
																d
																.styles
																.hasOwnProperty(
																	w
																) ?
																d
																.styles[
																	w
																] :
																g[
																	w
																]
															)
															.reduce(
																function(
																	ee,
																	Ee
																) {
																	return ee[
																			Ee
																		] =
																		"",
																		ee
																}, {}
															);
														i
															(
																Z
															) &&
															I(
																Z
															) &&
															(
																Object
																.assign(
																	Z
																	.style,
																	Q
																),
																Object
																.keys(
																	q
																)
																.forEach(
																	function(
																		ee
																	) {
																		Z
																			.removeAttribute(
																				ee
																			)
																	}
																)
															)
													}
												)
										}
								},
								requires: [
									"computeStyles"
								]
							}, {
								name: "offset",
								enabled: !0,
								phase: "main",
								requires: [
									"popperOffsets"
								],
								fn: function(
									U) {
									var
										d =
										U
										.state,
										g =
										U
										.options,
										w =
										U
										.name,
										Z =
										g
										.offset,
										q =
										Z ===
										void 0 ? [
											0,
											0
										] :
										Z,
										Q =
										rE
										.reduce(
											function(
												Ae,
												re
											) {
												return Ae[
														re
													] =
													function(
														We,
														ae,
														Me
													) {
														var
															de =
															ze(
																We
															),
															ie = [
																z,
																x
															]
															.indexOf(
																de
															) >=
															0 ?
															-
															1 :
															1,
															we =
															typeof Me ==
															"function" ?
															Me(
																Object
																.assign({},
																	ae, {
																		placement: We
																	}
																)
															) :
															Me,
															be =
															we[
																0
															],
															ce =
															we[
																1
															];
														return be =
															be ||
															0,
															ce =
															(
																ce ||
																0
															) *
															ie,
															[
																z,
																oe
															]
															.indexOf(
																de
															) >=
															0 ? {
																x: ce,
																y: be
															} : {
																x: be,
																y: ce
															}
													}
													(
														re,
														d
														.rects,
														q
													),
													Ae
											}, {}
										),
										ee =
										Q[
											d
											.placement
										],
										Ee =
										ee
										.x,
										ne =
										ee
										.y;
									d.modifiersData
										.popperOffsets !=
										null &&
										(
											d
											.modifiersData
											.popperOffsets
											.x +=
											Ee,
											d
											.modifiersData
											.popperOffsets
											.y +=
											ne
										),
										d
										.modifiersData[
											w
										] =
										Q
								}
							}, {
								name: "flip",
								enabled: !0,
								phase: "main",
								fn: function(
									U) {
									var
										d =
										U
										.state,
										g =
										U
										.options,
										w =
										U
										.name;
									if (
										!
										d
										.modifiersData[
											w
										]
										._skip
									) {
										for (
											var
												Z =
												g
												.mainAxis,
												q =
												Z ===
												void 0 ||
												Z,
												Q =
												g
												.altAxis,
												ee =
												Q ===
												void 0 ||
												Q,
												Ee =
												g
												.fallbackPlacements,
												ne =
												g
												.padding,
												Ae =
												g
												.boundary,
												re =
												g
												.rootBoundary,
												We =
												g
												.altBoundary,
												ae =
												g
												.flipVariations,
												Me =
												ae ===
												void 0 ||
												ae,
												de =
												g
												.allowedAutoPlacements,
												ie =
												d
												.options
												.placement,
												we =
												ze(
													ie
												),
												be =
												Ee ||
												(
													we !==
													ie &&
													Me ?
													function(
														RE
													) {
														if (
															ze(
																RE
															) ===
															Oe
														)
															return [];
														var
															_E =
															Nt(
																RE
															);
														return [
															dT(
																RE
															),
															_E,
															dT(
																_E
															)
														]
													}
													(
														ie
													) : [
														Nt(
															ie
														)
													]
												),
												ce = [
													ie
												]
												.concat(
													be
												)
												.reduce(
													function(
														RE,
														_E
													) {
														return RE
															.concat(
																ze(
																	_E
																) ===
																Oe ?
																function(
																	$E,
																	mE
																) {
																	mE
																		===
																		void 0 &&
																		(
																			mE = {}
																		);
																	var
																		LE =
																		mE,
																		lt =
																		LE
																		.placement,
																		_t =
																		LE
																		.boundary,
																		xE =
																		LE
																		.rootBoundary,
																		vt =
																		LE
																		.padding,
																		Ft =
																		LE
																		.flipVariations,
																		XE =
																		LE
																		.allowedAutoPlacements,
																		Yt =
																		XE ===
																		void 0 ?
																		rE :
																		XE,
																		At =
																		ve(
																			lt
																		),
																		Lt =
																		At ?
																		Ft ?
																		fE :
																		fE
																		.filter(
																			function(
																				cE
																			) {
																				return ve(
																						cE
																					) ===
																					At
																			}
																		) :
																		Ue,
																		kE =
																		Lt
																		.filter(
																			function(
																				cE
																			) {
																				return Yt
																					.indexOf(
																						cE
																					) >=
																					0
																			}
																		);
																	kE
																		.length ===
																		0 &&
																		(
																			kE =
																			Lt
																		);
																	var
																		KE =
																		kE
																		.reduce(
																			function(
																				cE,
																				HE
																			) {
																				return cE[
																						HE
																					] =
																					Rt(
																						$E, {
																							placement: HE,
																							boundary: _t,
																							rootBoundary: xE,
																							padding: vt
																						}
																					)[
																						ze(
																							HE
																						)
																					],
																					cE
																			}, {}
																		);
																	return Object
																		.keys(
																			KE
																		)
																		.sort(
																			function(
																				cE,
																				HE
																			) {
																				return KE[
																						cE
																					] -
																					KE[
																						HE
																					]
																			}
																		)
																}
																(
																	d, {
																		placement: _E,
																		boundary: Ae,
																		rootBoundary: re,
																		padding: ne,
																		flipVariations: Me,
																		allowedAutoPlacements: de
																	}
																) :
																_E
															)
													},
													[]
												),
												he =
												d
												.rects
												.reference,
												Ie =
												d
												.rects
												.popper,
												le =
												new Map,
												fe = !
												0,
												pe =
												ce[
													0
												],
												He =
												0; He <
											ce
											.length; He++
										) {
											var
												ke =
												ce[
													He
												],
												Ke =
												ze(
													ke
												),
												sE =
												ve(
													ke
												) ===
												ye,
												lE = [
													x,
													J
												]
												.indexOf(
													Ke
												) >=
												0,
												PE =
												lE ?
												"width" :
												"height",
												SE =
												Rt(
													d, {
														placement: ke,
														boundary: Ae,
														rootBoundary: re,
														altBoundary: We,
														padding: ne
													}
												),
												tE =
												lE ?
												sE ?
												oe :
												z :
												sE ?
												J :
												x;
											he
												[
													PE
												] >
												Ie[
													PE
												] &&
												(
													tE =
													Nt(
														tE
													)
												);
											var
												xe =
												Nt(
													tE
												),
												Be = [];
											if (
												q &&
												Be
												.push(
													SE[
														Ke
													] <=
													0
												),
												ee &&
												Be
												.push(
													SE[
														tE
													] <=
													0,
													SE[
														xe
													] <=
													0
												),
												Be
												.every(
													function(
														RE
													) {
														return RE
													}
												)
											) {
												pe
													=
													ke,
													fe = !
													1;
												break
											}
											le
												.set(
													ke,
													Be
												)
										}
										if (
											fe
										)
											for (
												var
													UE =
													function(
														RE
													) {
														var
															_E =
															ce
															.find(
																function(
																	$E
																) {
																	var
																		mE =
																		le
																		.get(
																			$E
																		);
																	if (
																		mE
																	)
																		return mE
																			.slice(
																				0,
																				RE
																			)
																			.every(
																				function(
																					LE
																				) {
																					return LE
																				}
																			)
																}
															);
														if (
															_E
														)
															return pe =
																_E,
																"break"
													},
													oE =
													Me ?
													3 :
													1; oE >
												0 &&
												UE(
													oE
												) !==
												"break"; oE--
											)
										;
										d
											.placement !==
											pe &&
											(
												d
												.modifiersData[
													w
												]
												._skip = !
												0,
												d
												.placement =
												pe,
												d
												.reset = !
												0
											)
									}
								},
								requiresIfExists: [
									"offset"
								],
								data: {
									_skip:
										!1
								}
							}, {
								name: "preventOverflow",
								enabled: !0,
								phase: "main",
								fn: function(
									U) {
									var
										d =
										U
										.state,
										g =
										U
										.options,
										w =
										U
										.name,
										Z =
										g
										.mainAxis,
										q =
										Z ===
										void 0 ||
										Z,
										Q =
										g
										.altAxis,
										ee =
										Q !==
										void 0 &&
										Q,
										Ee =
										g
										.boundary,
										ne =
										g
										.rootBoundary,
										Ae =
										g
										.altBoundary,
										re =
										g
										.padding,
										We =
										g
										.tether,
										ae =
										We ===
										void 0 ||
										We,
										Me =
										g
										.tetherOffset,
										de =
										Me ===
										void 0 ?
										0 :
										Me,
										ie =
										Rt(
											d, {
												boundary: Ee,
												rootBoundary: ne,
												padding: re,
												altBoundary: Ae
											}
										),
										we =
										ze(
											d
											.placement
										),
										be =
										ve(
											d
											.placement
										),
										ce = !
										be,
										he =
										Fe(
											we
										),
										Ie =
										he ===
										"x" ?
										"y" :
										"x",
										le =
										d
										.modifiersData
										.popperOffsets,
										fe =
										d
										.rects
										.reference,
										pe =
										d
										.rects
										.popper,
										He =
										typeof de ==
										"function" ?
										de(
											Object
											.assign({},
												d
												.rects, {
													placement: d
														.placement
												}
											)
										) :
										de,
										ke =
										typeof He ==
										"number" ? {
											mainAxis: He,
											altAxis: He
										} :
										Object
										.assign({
												mainAxis: 0,
												altAxis: 0
											},
											He
										),
										Ke =
										d
										.modifiersData
										.offset ?
										d
										.modifiersData
										.offset[
											d
											.placement
										] :
										null,
										sE = {
											x: 0,
											y: 0
										};
									if (
										le
									) {
										if (
											q
										) {
											var
												lE,
												PE =
												he ===
												"y" ?
												x :
												z,
												SE =
												he ===
												"y" ?
												J :
												oe,
												tE =
												he ===
												"y" ?
												"height" :
												"width",
												xe =
												le[
													he
												],
												Be =
												xe +
												ie[
													PE
												],
												UE =
												xe -
												ie[
													SE
												],
												oE =
												ae ?
												-
												pe[
													tE
												] /
												2 :
												0,
												RE =
												be ===
												ye ?
												fe[
													tE
												] :
												pe[
													tE
												],
												_E =
												be ===
												ye ?
												-
												pe[
													tE
												] :
												-
												fe[
													tE
												],
												$E =
												d
												.elements
												.arrow,
												mE =
												ae &&
												$E ?
												N(
													$E
												) : {
													width: 0,
													height: 0
												},
												LE =
												d
												.modifiersData[
													"arrow#persistent"
												] ?
												d
												.modifiersData[
													"arrow#persistent"
												]
												.padding : {
													top: 0,
													right: 0,
													bottom: 0,
													left: 0
												},
												lt =
												LE[
													PE
												],
												_t =
												LE[
													SE
												],
												xE =
												nt(
													0,
													fe[
														tE
													],
													mE[
														tE
													]
												),
												vt =
												ce ?
												fe[
													tE
												] /
												2 -
												oE -
												xE -
												lt -
												ke
												.mainAxis :
												RE -
												xE -
												lt -
												ke
												.mainAxis,
												Ft =
												ce ?
												-
												fe[
													tE
												] /
												2 +
												oE +
												xE +
												_t +
												ke
												.mainAxis :
												_E +
												xE +
												_t +
												ke
												.mainAxis,
												XE =
												d
												.elements
												.arrow &&
												W(
													d
													.elements
													.arrow
												),
												Yt =
												XE ?
												he ===
												"y" ?
												XE
												.clientTop ||
												0 :
												XE
												.clientLeft ||
												0 :
												0,
												At =
												(
													lE =
													Ke ==
													null ?
													void 0 :
													Ke[
														he
													]
												) !=
												null ?
												lE :
												0,
												Lt =
												xe +
												Ft -
												At,
												kE =
												nt(
													ae ?
													P(
														Be,
														xe +
														vt -
														At -
														Yt
													) :
													Be,
													xe,
													ae ?
													c(
														UE,
														Lt
													) :
													UE
												);
											le
												[
													he
												] =
												kE,
												sE[
													he
												] =
												kE -
												xe
										}
										if (
											ee
										) {
											var
												KE,
												cE =
												he ===
												"x" ?
												x :
												z,
												HE =
												he ===
												"x" ?
												J :
												oe,
												bE =
												le[
													Ie
												],
												Ct =
												Ie ===
												"y" ?
												"height" :
												"width",
												gT =
												bE +
												ie[
													cE
												],
												HT =
												bE -
												ie[
													HE
												],
												Vt = [
													x,
													z
												]
												.indexOf(
													we
												) !==
												-
												1,
												bT =
												(
													KE =
													Ke ==
													null ?
													void 0 :
													Ke[
														Ie
													]
												) !=
												null ?
												KE :
												0,
												yT =
												Vt ?
												gT :
												bE -
												fe[
													Ct
												] -
												pe[
													Ct
												] -
												bT +
												ke
												.altAxis,
												BT =
												Vt ?
												bE +
												fe[
													Ct
												] +
												pe[
													Ct
												] -
												bT -
												ke
												.altAxis :
												HT,
												vT =
												ae &&
												Vt ?
												function(
													Tn,
													rn,
													Wt
												) {
													var
														FT =
														nt(
															Tn,
															rn,
															Wt
														);
													return FT >
														Wt ?
														Wt :
														FT
												}
												(
													yT,
													bE,
													BT
												) :
												nt(
													ae ?
													yT :
													gT,
													bE,
													ae ?
													BT :
													HT
												);
											le
												[
													Ie
												] =
												vT,
												sE[
													Ie
												] =
												vT -
												bE
										}
										d
											.modifiersData[
												w
											] =
											sE
									}
								},
								requiresIfExists: [
									"offset"
								]
							}, {
								name: "arrow",
								enabled: !0,
								phase: "main",
								fn: function(
									U) {
									var
										d,
										g =
										U
										.state,
										w =
										U
										.name,
										Z =
										U
										.options,
										q =
										g
										.elements
										.arrow,
										Q =
										g
										.modifiersData
										.popperOffsets,
										ee =
										ze(
											g
											.placement
										),
										Ee =
										Fe(
											ee
										),
										ne = [
											z,
											oe
										]
										.indexOf(
											ee
										) >=
										0 ?
										"height" :
										"width";
									if (
										q &&
										Q
									) {
										var
											Ae =
											function(
												pe,
												He
											) {
												return UT(
													typeof(
														pe =
														typeof pe ==
														"function" ?
														pe(
															Object
															.assign({},
																He
																.rects, {
																	placement: He
																		.placement
																}
															)
														) :
														pe
													) !=
													"number" ?
													pe :
													mT(
														pe,
														Ue
													)
												)
											}
											(
												Z
												.padding,
												g
											),
											re =
											N(
												q
											),
											We =
											Ee ===
											"y" ?
											x :
											z,
											ae =
											Ee ===
											"y" ?
											J :
											oe,
											Me =
											g
											.rects
											.reference[
												ne
											] +
											g
											.rects
											.reference[
												Ee
											] -
											Q[
												Ee
											] -
											g
											.rects
											.popper[
												ne
											],
											de =
											Q[
												Ee
											] -
											g
											.rects
											.reference[
												Ee
											],
											ie =
											W(
												q
											),
											we =
											ie ?
											Ee ===
											"y" ?
											ie
											.clientHeight ||
											0 :
											ie
											.clientWidth ||
											0 :
											0,
											be =
											Me /
											2 -
											de /
											2,
											ce =
											Ae[
												We
											],
											he =
											we -
											re[
												ne
											] -
											Ae[
												ae
											],
											Ie =
											we /
											2 -
											re[
												ne
											] /
											2 +
											be,
											le =
											nt(
												ce,
												Ie,
												he
											),
											fe =
											Ee;
										g
											.modifiersData[
												w
											] =
											(
												(
													d = {}
												)[
													fe
												] =
												le,
												d
												.centerOffset =
												le -
												Ie,
												d
											)
									}
								},
								effect: function(
									U) {
									var
										d =
										U
										.state,
										g =
										U
										.options
										.element,
										w =
										g ===
										void 0 ?
										"[data-popper-arrow]" :
										g;
									w !=
										null &&
										(
											typeof w !=
											"string" ||
											(
												w =
												d
												.elements
												.popper
												.querySelector(
													w
												)
											)
										) &&
										pT(
											d
											.elements
											.popper,
											w
										) &&
										(
											d
											.elements
											.arrow =
											w
										)
								},
								requires: [
									"popperOffsets"
								],
								requiresIfExists: [
									"preventOverflow"
								]
							}, {
								name: "hide",
								enabled: !0,
								phase: "main",
								requiresIfExists: [
									"preventOverflow"
								],
								fn: function(
									U) {
									var
										d =
										U
										.state,
										g =
										U
										.name,
										w =
										d
										.rects
										.reference,
										Z =
										d
										.rects
										.popper,
										q =
										d
										.modifiersData
										.preventOverflow,
										Q =
										Rt(
											d, {
												elementContext: "reference"
											}
										),
										ee =
										Rt(
											d, {
												altBoundary:
													!
													0
											}
										),
										Ee =
										hT(
											Q,
											w
										),
										ne =
										hT(
											ee,
											Z,
											q
										),
										Ae =
										GT(
											Ee
										),
										re =
										GT(
											ne
										);
									d.modifiersData[
											g
										] = {
											referenceClippingOffsets: Ee,
											popperEscapeOffsets: ne,
											isReferenceHidden: Ae,
											hasPopperEscaped: re
										},
										d
										.attributes
										.popper =
										Object
										.assign({},
											d
											.attributes
											.popper, {
												"data-popper-reference-hidden": Ae,
												"data-popper-escaped": re
											}
										)
								}
							}]
						})
					}
				},
				t = {};

			function r(n) {
				var s = t[n];
				if (s !== void 0) return s.exports;
				var S = t[n] = {
					exports: {}
				};
				return T[n](S, S.exports, r), S.exports
			}
			r.d = (n, s) => {
					for (var S in s) r.o(s, S) && !r.o(n, S) &&
						Object.defineProperty(n, S, {
							enumerable: !0,
							get: s[S]
						})
				}, r.o = (n, s) => Object.prototype.hasOwnProperty
				.call(n, s), r.r = n => {
					typeof Symbol < "u" && Symbol.toStringTag &&
						Object.defineProperty(n, Symbol.toStringTag, {
							value: "Module"
						}), Object.defineProperty(n,
							"__esModule", {
								value: !0
							})
				};
			var R = {};
			return r.r(R), r(661), r(795), r(682), r(284), r(
				181), r(778), r(51), r(185), R
		})()
	})
})(Qn);

function Zn(E) {
	let e = E[0].title + "",
		T;
	return {
		c() {
			T = te(e)
		},
		m(t, r) {
			V(t, T, r)
		},
		p(t, r) {
			r & 1 && e !== (e = t[0].title + "") && Le(T, e)
		},
		d(t) {
			t && Y(T)
		}
	}
}

function jn(E) {
	let e, T;
	return {
		c() {
			e = te("Welcome to "), T = f("span"), T.textContent = "Jenasi.AI",
				a(T, "class", "nav-title")
		},
		m(t, r) {
			V(t, e, r), V(t, T, r)
		},
		p: j,
		d(t) {
			t && (Y(e), Y(T))
		}
	}
}

function zn(E) {
	let e, T, t, r, R = E[0].subtitle + "",
		n;

	function s(o, i) {
		return o[0].title == "Welcome to Jenasi.AI" ? jn : Zn
	}
	let S = s(E),
		A = S(E);
	return {
		c() {
			e = f("div"), T = f("h1"), A.c(), t = $(), r = f("p"), n = te(R), a(
				T, "class",
				"text-3xl font-bold text-gray-800 sm:text-4xl dark:text-white"
			), a(r, "class", "mt-3 text-gray-600 dark:text-gray-400"), a(e,
				"class",
				"max-w-4xl px-4 sm:px-6 lg:px-8 mx-auto text-center")
		},
		m(o, i) {
			V(o, e, i), l(e, T), A.m(T, null), l(e, t), l(e, r), l(r, n)
		},
		p(o, [i]) {
			S === (S = s(o)) && A ? A.p(o, i) : (A.d(1), A = S(o), A && (A.c(),
					A.m(T, null))), i & 1 && R !== (R = o[0].subtitle + "") &&
				Le(n, R)
		},
		i: j,
		o: j,
		d(o) {
			o && Y(e), A.d()
		}
	}
}

function eA(E, e, T) {
	let t;
	return eE(E, VE, r => T(0, t = r)), [t]
}
class EA extends ue {
	constructor(e) {
		super(), Ce(this, e, eA, zn, _e, {})
	}
}

function tA(E) {
	let e, T;
	const t = E[1].default,
		r = Ut(t, E, E[0], null);
	return {
		c() {
			e = f("p"), r && r.c(), a(e, "class",
				"text-gray-800 dark:text-gray-200")
		},
		m(R, n) {
			V(R, e, n), r && r.m(e, null), T = !0
		},
		p(R, [n]) {
			r && r.p && (!T || n & 1) && ht(r, t, R, R[0], T ? mt(t, R[0], n,
				null) : Gt(R[0]), null)
		},
		i(R) {
			T || (m(r, R), T = !0)
		},
		o(R) {
			y(r, R), T = !1
		},
		d(R) {
			R && Y(e), r && r.d(R)
		}
	}
}

function TA(E, e, T) {
	let {
		$$slots: t = {},
		$$scope: r
	} = e;
	return E.$$set = R => {
		"$$scope" in R && T(0, r = R.$$scope)
	}, [r, t]
}
class aE extends ue {
	constructor(e) {
		super(), Ce(this, e, TA, tA, _e, {})
	}
}

function rA(E) {
	let e;
	return {
		c() {
			e = te(E[0])
		},
		m(T, t) {
			V(T, e, t)
		},
		p(T, t) {
			t & 1 && Le(e, T[0])
		},
		d(T) {
			T && Y(e)
		}
	}
}

function RA(E) {
	let e, T, t, r, R, n, s, S, A;
	s = new aE({
		props: {
			$$slots: {
				default: [rA]
			},
			$$scope: {
				ctx: E
			}
		}
	});
	const o = E[1].default,
		i = Ut(o, E, E[2], null);
	return {
		c() {
			e = f("li"), T = f("div"), t = f("div"), r = f("span"), r.innerHTML =
				'<span class="text-sm font-medium text-white leading-none">You</span>',
				R = $(), n = f("div"), K(s.$$.fragment), S = $(), i && i.c(), a(
					r, "class",
					"flex-shrink-0 inline-flex items-center justify-center h-[2.375rem] w-[2.375rem] rounded-full bg-gray-600"
				), a(n, "class", "grow mt-2 space-y-3"), a(t, "class",
					"max-w-2xl flex gap-x-2 sm:gap-x-4"), a(T, "class",
					"max-w-4xl px-4 sm:px-6 lg:px-8 mx-auto"), a(e, "class",
					"py-2 sm:py-4")
		},
		m(_, c) {
			V(_, e, c), l(e, T), l(T, t), l(t, r), l(t, R), l(t, n), X(s, n,
				null), l(n, S), i && i.m(n, null), A = !0
		},
		p(_, [c]) {
			const P = {};
			c & 5 && (P.$$scope = {
				dirty: c,
				ctx: _
			}), s.$set(P), i && i.p && (!A || c & 4) && ht(i, o, _, _[2], A ?
				mt(o, _[2], c, null) : Gt(_[2]), null)
		},
		i(_) {
			A || (m(s.$$.fragment, _), m(i, _), A = !0)
		},
		o(_) {
			y(s.$$.fragment, _), y(i, _), A = !1
		},
		d(_) {
			_ && Y(e), k(s), i && i.d(_)
		}
	}
}

function nA(E, e, T) {
	let {
		$$slots: t = {},
		$$scope: r
	} = e, {
		message: R
	} = e;
	return E.$$set = n => {
		"message" in n && T(0, R = n.message), "$$scope" in n && T(2, r = n
			.$$scope)
	}, [R, t, r]
}
class WE extends ue {
	constructor(e) {
		super(), Ce(this, e, nA, RA, _e, {
			message: 0
		})
	}
}

function AA(E) {
	let e, T, t;
	return {
		c() {
			e = f("button"), e.innerHTML =
				'<svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" x2="12" y1="19" y2="22"></line></svg>',
				a(e, "type", "button"), a(e, "class",
					"inline-flex flex-shrink-0 justify-center items-center size-8 rounded-lg text-gray-500 hover:text-blue-600 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:hover:text-blue-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
				)
		},
		m(r, R) {
			V(r, e, R), T || (t = Ne(e, "click", E[1]), T = !0)
		},
		p: j,
		d(r) {
			r && Y(e), T = !1, t()
		}
	}
}

function sA(E) {
	let e;
	return {
		c() {
			e = f("button"), e.innerHTML =
				'<svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" x2="12" y1="19" y2="22"></line></svg>',
				a(e, "type", "button"), a(e, "class",
					"animate-ping animate-pulse inline-flex flex-shrink-0 justify-center items-center size-8 rounded-lg text-red-500 hover:text-red-600 focus:z-10 focus:outline-none focus:ring-2 focus:ring-red-500 dark:hover:text-red-500 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-red-600"
				)
		},
		m(T, t) {
			V(T, e, t)
		},
		p: j,
		d(T) {
			T && Y(e)
		}
	}
}

function SA(E) {
	let e;

	function T(R, n) {
		return R[0] ? sA : AA
	}
	let t = T(E),
		r = t(E);
	return {
		c() {
			r.c(), e = je()
		},
		m(R, n) {
			r.m(R, n), V(R, e, n)
		},
		p(R, [n]) {
			t === (t = T(R)) && r ? r.p(R, n) : (r.d(1), r = t(R), r && (r.c(),
				r.m(e.parentNode, e)))
		},
		i: j,
		o: j,
		d(R) {
			R && Y(e), r.d(R)
		}
	}
}

function oA(E, e, T) {
	let {
		newMessage: t
	} = e, r = !1;

	function R() {
		if (T(0, r = !0), pR.set(!0), "webkitSpeechRecognition" in window) var n =
			new window.webkitSpeechRecognition;
		else var n = new window.SpeechRecognition;
		n.lang = "en-US", n.start(), n.onresult = s => {
			const S = s.results[0][0].transcript;
			console.log(S), T(2, t = S), T(0, r = !1)
		}, n.onend = () => {
			T(0, r = !1)
		}, n.onerror = () => {
			T(0, r = !1)
		}
	}
	return E.$$set = n => {
		"newMessage" in n && T(2, t = n.newMessage)
	}, [r, R, t]
}
class OA extends ue {
	constructor(e) {
		super(), Ce(this, e, oA, SA, _e, {
			newMessage: 2
		})
	}
}

function iA(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _, c, P, p;

	function C(I) {
		E[5](I)
	}
	let L = {};
	return E[0] !== void 0 && (L.newMessage = E[0]), A = new OA({
		props: L
	}), iT.push(() => cn(A, "newMessage", C)), {
		c() {
			e = f("div"), T = f("input"), t = $(), r = f("div"), R = f(
					"div"), n = f("div"), n.innerHTML = "", s = $(), S = f(
					"div"), K(A.$$.fragment), i = $(), _ = f("button"), _.innerHTML =
				'<svg class="h-3.5 w-3.5" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471-.47 1.178Z"></path></svg>',
				a(T, "type", "text"), a(T, "class",
					"p-4 pb-12 block w-full bg-gray-100 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-800 dark:border-gray-700 dark:text-gray-400"
				), a(T, "placeholder",
					"Ask me a question about your data that I can turn into SQL."
				), a(n, "class", "flex items-center"), a(_, "type",
					"button"), a(_, "class",
					"inline-flex flex-shrink-0 justify-center items-center h-8 w-8 rounded-md text-white bg-blue-600 hover:bg-blue-500 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
				), a(S, "class", "flex items-center gap-x-1"), a(R, "class",
					"flex justify-between items-center"), a(r, "class",
					"absolute bottom-px inset-x-px p-2 rounded-b-md bg-gray-100 dark:bg-slate-800"
				), a(e, "class", "relative")
		},
		m(I, u) {
			V(I, e, u), l(e, T), Ye(T, E[0]), l(e, t), l(e, r), l(r, R), l(
					R, n), l(R, s), l(R, S), X(A, S, null), l(S, i), l(S, _),
				c = !0, P || (p = [Ne(T, "input", E[4]), Ne(T, "keydown", E[
					1]), Ne(_, "click", E[2])], P = !0)
		},
		p(I, [u]) {
			u & 1 && T.value !== I[0] && Ye(T, I[0]);
			const H = {};
			!o && u & 1 && (o = !0, H.newMessage = I[0], ln(() => o = !1)),
				A.$set(H)
		},
		i(I) {
			c || (m(A.$$.fragment, I), c = !0)
		},
		o(I) {
			y(A.$$.fragment, I), c = !1
		},
		d(I) {
			I && Y(e), k(A), P = !1, NE(p)
		}
	}
}

function aA(E, e, T) {
	let t;
	eE(E, BE, A => T(0, t = A));
	let {
		onSubmit: r
	} = e;

	function R(A) {
		A.key === "Enter" && (r(t), OT(BE, t = "", t), A.preventDefault())
	}

	function n() {
		r(t), OT(BE, t = "", t)
	}

	function s() {
		t = this.value, BE.set(t)
	}

	function S(A) {
		t = A, BE.set(t)
	}
	return E.$$set = A => {
		"onSubmit" in A && T(3, r = A.onSubmit)
	}, [t, R, n, r, s, S]
}
class IA extends ue {
	constructor(e) {
		super(), Ce(this, e, aA, iA, _e, {
			onSubmit: 3
		})
	}
}

function NA(E) {
	let e;
	return {
		c() {
			e = f("div"), e.innerHTML =
				'<button type="button" class="p-2 inline-flex justify-center items-center gap-1.5 rounded-md border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 transition-all text-xs dark:bg-slate-900 dark:hover:bg-slate-800 dark:border-gray-700 dark:text-gray-400 dark:hover:text-white dark:focus:ring-offset-gray-800" data-hs-overlay="#application-sidebar" aria-controls="application-sidebar" aria-label="Toggle navigation"><svg class="w-3.5 h-3.5" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"></path></svg> <span>Sidebar</span></button>',
				a(e, "class", "lg:hidden flex justify-end mb-2 sm:mb-3")
		},
		m(T, t) {
			V(T, e, t)
		},
		p: j,
		i: j,
		o: j,
		d(T) {
			T && Y(e)
		}
	}
}
class lA extends ue {
	constructor(e) {
		super(), Ce(this, e, null, NA, _e, {})
	}
}

function _A(E) {
	let e, T, t, r;
	return {
		c() {
			e = f("button"), T = te(E[0]), a(e, "type", "button"), a(e, "class",
				"mb-2.5 mr-1.5 py-2 px-3 inline-flex justify-center items-center gap-x-2 rounded-md border border-blue-600 bg-white text-blue-600 align-middle hover:bg-blue-50 text-sm dark:bg-slate-900 dark:text-blue-500 dark:border-blue-500 dark:hover:text-blue-400 dark:hover:border-blue-400"
			)
		},
		m(R, n) {
			V(R, e, n), l(e, T), t || (r = Ne(e, "click", E[1]), t = !0)
		},
		p(R, [n]) {
			n & 1 && Le(T, R[0])
		},
		i: j,
		o: j,
		d(R) {
			R && Y(e), t = !1, r()
		}
	}
}

function LA(E, e, T) {
	let {
		message: t
	} = e, {
		onSubmit: r
	} = e;

	function R() {
		r(t)
	}
	return E.$$set = n => {
		"message" in n && T(0, t = n.message), "onSubmit" in n && T(2, r =
			n.onSubmit)
	}, [t, R, r]
}
class IE extends ue {
	constructor(e) {
		super(), Ce(this, e, LA, _A, _e, {
			message: 0,
			onSubmit: 2
		})
	}
}

function CA(E) {
	let e, T, t, r, R, n, s, S, A, o, i;
	return {
		c() {
			e = f("span"), T = OE("svg"), t = OE("defs"), r = OE(
					"linearGradient"), R = OE("stop"), n = OE("stop"), s = OE(
					"g"), S = OE("g"), A = OE("path"), o = OE("path"), a(R,
					"offset", "0"), a(R, "stop-color", "#009efd"), a(n,
					"offset", "1"), a(n, "stop-color", "#2af598"), a(r,
					"gradientTransform",
					"matrix(1.09331 0 0 1.09331 -47.1838 -88.8946)"), a(r,
					"gradientUnits", "userSpaceOnUse"), a(r, "id",
					"LinearGradient"), a(r, "x1", "237.82"), a(r, "x2",
					"785.097"), a(r, "y1", "549.609"), a(r, "y2", "549.609"), a(
					A, "d",
					"M117.718 228.798C117.718 119.455 206.358 30.8151 315.701 30.8151L708.299 30.8151C817.642 30.8151 906.282 119.455 906.282 228.798L906.282 795.202C906.282 904.545 817.642 993.185 708.299 993.185L315.701 993.185C206.358 993.185 117.718 904.545 117.718 795.202L117.718 228.798Z"
				), a(A, "fill", "#0f172a"), a(A, "fill-rule", "nonzero"), a(A,
					"opacity", "1"), a(A, "stroke", "#374151"), a(A,
					"stroke-linecap", "butt"), a(A, "stroke-linejoin", "round"),
				a(A, "stroke-width", "20"), a(o, "d",
					"M212.828 215.239C213.095 281.169 213.629 413.028 213.629 413.028C213.629 413.028 511.51 808.257 513.993 809.681C612.915 677.809 810.759 414.065 810.759 414.065C810.759 414.065 811.034 280.901 811.172 214.319C662.105 362.973 662.105 362.973 513.038 511.627C362.933 363.433 362.933 363.433 212.828 215.239Z"
				), a(o, "fill", "url(#LinearGradient)"), a(o, "fill-rule",
					"nonzero"), a(o, "opacity", "1"), a(o, "stroke", "none"), a(
					S, "opacity", "1"), a(s, "id", "Layer-1"), a(T, "height",
					"100%"), a(T, "stroke-miterlimit", "10"), ct(T, "fill-rule",
					"nonzero"), ct(T, "clip-rule", "evenodd"), ct(T,
					"stroke-linecap", "round"), ct(T, "stroke-linejoin",
					"round"), a(T, "version", "1.1"), a(T, "viewBox",
					"0 0 1024 1024"), a(T, "width", "100%"), a(T, "xml:space",
					"preserve"), a(T, "xmlns", "http://www.w3.org/2000/svg"), a(
					e, "class", i = "flex-shrink-0 w-[2.375rem] h-[2.375rem] " +
					E[0])
		},
		m(_, c) {
			V(_, e, c), l(e, T), l(T, t), l(t, r), l(r, R), l(r, n), l(T, s), l(
				s, S), l(S, A), l(S, o)
		},
		p(_, [c]) {
			c & 1 && i !== (i = "flex-shrink-0 w-[2.375rem] h-[2.375rem] " + _[
				0]) && a(e, "class", i)
		},
		i: j,
		o: j,
		d(_) {
			_ && Y(e)
		}
	}
}

function uA(E, e, T) {
	let t, {
		animate: r = !1
	} = e;
	return E.$$set = R => {
		"animate" in R && T(1, r = R.animate)
	}, E.$$.update = () => {
		E.$$.dirty & 2 && T(0, t = r ? "animate-bounce" : "")
	}, [t, r]
}
class GR extends ue {
	constructor(e) {
		super(), Ce(this, e, uA, CA, _e, {
			animate: 1
		})
	}
}

function cA(E) {
	let e, T, t, r, R;
	T = new GR({});
	const n = E[1].default,
		s = Ut(n, E, E[0], null);
	return {
		c() {
			e = f("li"), K(T.$$.fragment), t = $(), r = f("div"), s && s.c(), a(
				r, "class",
				"space-y-3 overflow-x-auto overflow-y-hidden whitespace-break-spaces w-full"
			), a(e, "class",
				"max-w-4xl py-2 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 sm:gap-x-4"
			)
		},
		m(S, A) {
			V(S, e, A), X(T, e, null), l(e, t), l(e, r), s && s.m(r, null), R = !
				0
		},
		p(S, [A]) {
			s && s.p && (!R || A & 1) && ht(s, n, S, S[0], R ? mt(n, S[0], A,
				null) : Gt(S[0]), null)
		},
		i(S) {
			R || (m(T.$$.fragment, S), m(s, S), R = !0)
		},
		o(S) {
			y(T.$$.fragment, S), y(s, S), R = !1
		},
		d(S) {
			S && Y(e), k(T), s && s.d(S)
		}
	}
}

function fA(E, e, T) {
	let {
		$$slots: t = {},
		$$scope: r
	} = e;
	return E.$$set = R => {
		"$$scope" in R && T(0, r = R.$$scope)
	}, [r, t]
}
class Ze extends ue {
	constructor(e) {
		super(), Ce(this, e, fA, cA, _e, {})
	}
}

function PA(E) {
	let e;
	return {
		c() {
			e = te("Thinking...")
		},
		m(T, t) {
			V(T, e, t)
		},
		d(T) {
			T && Y(e)
		}
	}
}

function DA(E) {
	let e, T, t, r, R, n;
	return T = new GR({
		props: {
			animate: !0
		}
	}), R = new aE({
		props: {
			$$slots: {
				default: [PA]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			e = f("li"), K(T.$$.fragment), t = $(), r = f("div"), K(R.$$.fragment),
				a(r, "class", "space-y-3"), a(e, "class",
					"max-w-4xl py-2 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 sm:gap-x-4"
				)
		},
		m(s, S) {
			V(s, e, S), X(T, e, null), l(e, t), l(e, r), X(R, r, null), n = !
				0
		},
		p(s, [S]) {
			const A = {};
			S & 1 && (A.$$scope = {
				dirty: S,
				ctx: s
			}), R.$set(A)
		},
		i(s) {
			n || (m(T.$$.fragment, s), m(R.$$.fragment, s), n = !0)
		},
		o(s) {
			y(T.$$.fragment, s), y(R.$$.fragment, s), n = !1
		},
		d(s) {
			s && Y(e), k(T), k(R)
		}
	}
}
class dA extends ue {
	constructor(e) {
		super(), Ce(this, e, null, DA, _e, {})
	}
}

function pA(E) {
	let e, T, t, r, R, n, s, S, A, o, i;
	return {
		c() {
			e = f("ul"), T = f("li"), t = f("div"), r = f("span"), r.textContent =
				"CSV", R = $(), n = f("a"), s = OE("svg"), S = OE("path"), A =
				OE("path"), o = te(`
          Download`), a(r, "class",
					"mr-3 flex-1 w-0 truncate"), a(S, "d",
					"M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"
				), a(A, "d",
					"M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"
				), a(s, "class", "flex-shrink-0 w-3 h-3"), a(s, "width", "16"),
				a(s, "height", "16"), a(s, "viewBox", "0 0 16 16"), a(s, "fill",
					"currentColor"), a(n, "class",
					"flex items-center gap-x-2 text-gray-500 hover:text-blue-500 whitespace-nowrap"
				), a(n, "href", i = "/api/v0/download_csv?id=" + E[0]), a(t,
					"class", "w-full flex justify-between truncate"), a(T,
					"class",
					"flex items-center gap-x-2 p-3 text-sm bg-white border text-gray-800 first:rounded-t-lg first:mt-0 last:rounded-b-lg dark:bg-slate-900 dark:border-gray-700 dark:text-gray-200"
				), a(e, "class",
					"flex flex-col justify-end text-start -space-y-px")
		},
		m(_, c) {
			V(_, e, c), l(e, T), l(T, t), l(t, r), l(t, R), l(t, n), l(n, s), l(
				s, S), l(s, A), l(n, o)
		},
		p(_, [c]) {
			c & 1 && i !== (i = "/api/v0/download_csv?id=" + _[0]) && a(n,
				"href", i)
		},
		i: j,
		o: j,
		d(_) {
			_ && Y(e)
		}
	}
}

function MA(E, e, T) {
	let {
		id: t
	} = e;
	return E.$$set = r => {
		"id" in r && T(0, t = r.id)
	}, [t]
}
class UA extends ue {
	constructor(e) {
		super(), Ce(this, e, MA, pA, _e, {
			id: 0
		})
	}
}

function KT(E, e, T) {
	const t = E.slice();
	return t[5] = e[T], t
}

function JT(E, e, T) {
	const t = E.slice();
	return t[8] = e[T], t
}

function qT(E, e, T) {
	const t = E.slice();
	return t[8] = e[T], t
}

function QT(E) {
	let e, T, t, r;
	return {
		c() {
			e = f("th"), T = f("div"), t = f("span"), t.textContent = `${E[8]}`,
				r = $(), a(t, "class",
					"text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200"
				), a(T, "class", "flex items-center gap-x-2"), a(e, "scope",
					"col"), a(e, "class", "px-6 py-3 text-left")
		},
		m(R, n) {
			V(R, e, n), l(e, T), l(T, t), l(e, r)
		},
		p: j,
		d(R) {
			R && Y(e)
		}
	}
}

function ZT(E) {
	let e, T, t;
	return {
		c() {
			e = f("td"), T = f("div"), t = f("span"), t.textContent =
				`${E[5][E[8]]}`, a(t, "class",
					"text-gray-800 dark:text-gray-200"), a(T, "class",
					"px-6 py-3"), a(e, "class", "h-px w-px whitespace-nowrap")
		},
		m(r, R) {
			V(r, e, R), l(e, T), l(T, t)
		},
		p: j,
		d(r) {
			r && Y(e)
		}
	}
}

function jT(E) {
	let e, T, t = De(E[3]),
		r = [];
	for (let R = 0; R < t.length; R += 1) r[R] = ZT(JT(E, t, R));
	return {
		c() {
			e = f("tr");
			for (let R = 0; R < r.length; R += 1) r[R].c();
			T = $()
		},
		m(R, n) {
			V(R, e, n);
			for (let s = 0; s < r.length; s += 1) r[s] && r[s].m(e, null);
			l(e, T)
		},
		p(R, n) {
			if (n & 12) {
				t = De(R[3]);
				let s;
				for (s = 0; s < t.length; s += 1) {
					const S = JT(R, t, s);
					r[s] ? r[s].p(S, n) : (r[s] = ZT(S), r[s].c(), r[s].m(e, T))
				}
				for (; s < r.length; s += 1) r[s].d(1);
				r.length = t.length
			}
		},
		d(R) {
			R && Y(e), nE(r, R)
		}
	}
}

function zT(E) {
	let e, T;
	return e = new UA({
		props: {
			id: E[0]
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 1 && (R.id = t[0]), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function mA(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _ = De(E[3]),
		c = [];
	for (let L = 0; L < _.length; L += 1) c[L] = QT(qT(E, _, L));
	let P = De(E[2]),
		p = [];
	for (let L = 0; L < P.length; L += 1) p[L] = jT(KT(E, P, L));
	let C = E[1].csv_download && zT(E);
	return {
		c() {
			e = f("div"), T = f("div"), t = f("div"), r = f("table"), R = f(
				"thead"), n = f("tr");
			for (let L = 0; L < c.length; L += 1) c[L].c();
			s = $(), S = f("tbody");
			for (let L = 0; L < p.length; L += 1) p[L].c();
			A = $(), C && C.c(), o = je(), a(R, "class",
					"bg-gray-50 dark:bg-slate-800"), a(S, "class",
					"divide-y divide-gray-200 dark:divide-gray-700"), a(r,
					"class",
					"min-w-full divide-y divide-gray-200 dark:divide-gray-700"),
				a(t, "class", "p-1.5 min-w-full inline-block align-middle"), a(
					T, "class", "-m-1.5 overflow-x-auto"), a(e, "class",
					"bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden dark:bg-slate-900 dark:border-gray-700"
				)
		},
		m(L, I) {
			V(L, e, I), l(e, T), l(T, t), l(t, r), l(r, R), l(R, n);
			for (let u = 0; u < c.length; u += 1) c[u] && c[u].m(n, null);
			l(r, s), l(r, S);
			for (let u = 0; u < p.length; u += 1) p[u] && p[u].m(S, null);
			V(L, A, I), C && C.m(L, I), V(L, o, I), i = !0
		},
		p(L, [I]) {
			if (I & 8) {
				_ = De(L[3]);
				let u;
				for (u = 0; u < _.length; u += 1) {
					const H = qT(L, _, u);
					c[u] ? c[u].p(H, I) : (c[u] = QT(H), c[u].c(), c[u].m(n,
						null))
				}
				for (; u < c.length; u += 1) c[u].d(1);
				c.length = _.length
			}
			if (I & 12) {
				P = De(L[2]);
				let u;
				for (u = 0; u < P.length; u += 1) {
					const H = KT(L, P, u);
					p[u] ? p[u].p(H, I) : (p[u] = jT(H), p[u].c(), p[u].m(S,
						null))
				}
				for (; u < p.length; u += 1) p[u].d(1);
				p.length = P.length
			}
			L[1].csv_download ? C ? (C.p(L, I), I & 2 && m(C, 1)) : (C = zT(L),
				C.c(), m(C, 1), C.m(o.parentNode, o)) : C && (Ge(), y(C, 1,
				1, () => {
					C = null
				}), ge())
		},
		i(L) {
			i || (m(C), i = !0)
		},
		o(L) {
			y(C), i = !1
		},
		d(L) {
			L && (Y(e), Y(A), Y(o)), nE(c, L), nE(p, L), C && C.d(L)
		}
	}
}

function hA(E, e, T) {
	let t;
	eE(E, VE, S => T(1, t = S));
	let {
		id: r
	} = e, {
		df: R
	} = e, n = JSON.parse(R), s = n.length > 0 ? Object.keys(n[0]) : [];
	return E.$$set = S => {
		"id" in S && T(0, r = S.id), "df" in S && T(4, R = S.df)
	}, [r, t, n, s, R]
}
class gR extends ue {
	constructor(e) {
		super(), Ce(this, e, hA, mA, _e, {
			id: 0,
			df: 4
		})
	}
}

function GA(E) {
	let e;
	return {
		c() {
			e = f("div"), a(e, "id", E[0])
		},
		m(T, t) {
			V(T, e, t)
		},
		p: j,
		i: j,
		o: j,
		d(T) {
			T && Y(e)
		}
	}
}

function gA(E, e, T) {
	let {
		fig: t
	} = e, r = JSON.parse(t), R = Math.random()
		.toString(36)
		.substring(2, 15) + Math.random()
		.toString(36)
		.substring(2, 15);
	return DR(() => {
		Plotly.newPlot(document.getElementById(R), r, {
			responsive: !0
		})
	}), E.$$set = n => {
		"fig" in n && T(1, t = n.fig)
	}, [R, t]
}
class HR extends ue {
	constructor(e) {
		super(), Ce(this, e, gA, GA, _e, {
			fig: 1
		})
	}
}

function HA(E) {
	let e, T, t, r;
	return {
		c() {
			e = f("button"), T = te(E[0]), a(e, "type", "button"), a(e, "class",
				"mb-2.5 mr-1.5 py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border-2 border-green-200 font-semibold text-green-500 hover:text-white hover:bg-green-500 hover:border-green-500 focus:outline-none focus:ring-2 focus:ring-green-200 focus:ring-offset-2 transition-all text-sm dark:focus:ring-offset-gray-800"
			)
		},
		m(R, n) {
			V(R, e, n), l(e, T), t || (r = Ne(e, "click", E[1]), t = !0)
		},
		p(R, [n]) {
			n & 1 && Le(T, R[0])
		},
		i: j,
		o: j,
		d(R) {
			R && Y(e), t = !1, r()
		}
	}
}

function bA(E, e, T) {
	let {
		message: t
	} = e, {
		onSubmit: r
	} = e;

	function R() {
		r(t)
	}
	return E.$$set = n => {
		"message" in n && T(0, t = n.message), "onSubmit" in n && T(2, r =
			n.onSubmit)
	}, [t, R, r]
}
class yA extends ue {
	constructor(e) {
		super(), Ce(this, e, bA, HA, _e, {
			message: 0,
			onSubmit: 2
		})
	}
}

function BA(E) {
	let e, T, t, r, R, n, s, S, A;
	return {
		c() {
			e = f("div"), T = f("div"), t = f("div"), t.innerHTML =
				'<svg class="h-4 w-4 text-yellow-400 mt-0.5" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path></svg>',
				r = $(), R = f("div"), n = f("h3"), n.textContent = "Error", s =
				$(), S = f("div"), A = te(E[0]), a(t, "class", "flex-shrink-0"),
				a(n, "class", "text-sm text-yellow-800 font-semibold"), a(S,
					"class", "mt-1 text-sm text-yellow-700"), a(R, "class",
					"ml-4"), a(T, "class", "flex"), a(e, "class",
					"bg-yellow-50 border border-yellow-200 rounded-md p-4"), a(
					e, "role", "alert")
		},
		m(o, i) {
			V(o, e, i), l(e, T), l(T, t), l(T, r), l(T, R), l(R, n), l(R, s), l(
				R, S), l(S, A)
		},
		p(o, [i]) {
			i & 1 && Le(A, o[0])
		},
		i: j,
		o: j,
		d(o) {
			o && Y(e)
		}
	}
}

function vA(E, e, T) {
	let {
		message: t
	} = e;
	return E.$$set = r => {
		"message" in r && T(0, t = r.message)
	}, [t]
}
let PT = class extends ue {
	constructor(e) {
		super(), Ce(this, e, vA, BA, _e, {
			message: 0
		})
	}
};

function FA(E) {
	let e, T;
	const t = E[1].default,
		r = Ut(t, E, E[0], null);
	return {
		c() {
			e = f("div"), r && r.c(), a(e, "class",
				"font-mono whitespace-pre-wrap")
		},
		m(R, n) {
			V(R, e, n), r && r.m(e, null), T = !0
		},
		p(R, [n]) {
			r && r.p && (!T || n & 1) && ht(r, t, R, R[0], T ? mt(t, R[0], n,
				null) : Gt(R[0]), null)
		},
		i(R) {
			T || (m(r, R), T = !0)
		},
		o(R) {
			y(r, R), T = !1
		},
		d(R) {
			R && Y(e), r && r.d(R)
		}
	}
}

function YA(E, e, T) {
	let {
		$$slots: t = {},
		$$scope: r
	} = e;
	return E.$$set = R => {
		"$$scope" in R && T(0, r = R.$$scope)
	}, [r, t]
}
class bR extends ue {
	constructor(e) {
		super(), Ce(this, e, YA, FA, _e, {})
	}
}

function VA(E) {
	let e;
	return {
		c() {
			e = te(E[1])
		},
		m(T, t) {
			V(T, e, t)
		},
		p(T, t) {
			t & 2 && Le(e, T[1])
		},
		d(T) {
			T && Y(e)
		}
	}
}

function WA(E) {
	let e, T, t, r, R, n, s, S;
	return t = new IE({
		props: {
			message: "Run SQL",
			onSubmit: E[3]
		}
	}), R = new aE({
		props: {
			$$slots: {
				default: [VA]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			e = f("textarea"), T = $(), K(t.$$.fragment), r = $(), K(R.$$.fragment),
				a(e, "rows", "6"), a(e, "class",
					"block p-2.5 w-full text-blue-600 hover:text-blue-500 dark:text-blue-500 dark:hover:text-blue-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 font-mono"
				), a(e, "placeholder", "SELECT col1, col2, col3 FROM ...")
		},
		m(A, o) {
			V(A, e, o), Ye(e, E[1]), V(A, T, o), X(t, A, o), V(A, r, o), X(
				R, A, o), n = !0, s || (S = Ne(e, "input", E[2]), s = !
				0)
		},
		p(A, [o]) {
			o & 2 && Ye(e, A[1]);
			const i = {};
			o & 3 && (i.onSubmit = A[3]), t.$set(i);
			const _ = {};
			o & 18 && (_.$$scope = {
				dirty: o,
				ctx: A
			}), R.$set(_)
		},
		i(A) {
			n || (m(t.$$.fragment, A), m(R.$$.fragment, A), n = !0)
		},
		o(A) {
			y(t.$$.fragment, A), y(R.$$.fragment, A), n = !1
		},
		d(A) {
			A && (Y(e), Y(T), Y(r)), k(t, A), k(R, A), s = !1, S()
		}
	}
}

function wA(E, e, T) {
	let t;
	eE(E, Et, s => T(1, t = s));
	let {
		onSubmit: r
	} = e;

	function R() {
		t = this.value, Et.set(t)
	}
	const n = () => r(t);
	return E.$$set = s => {
		"onSubmit" in s && T(0, r = s.onSubmit)
	}, [r, t, R, n]
}
class $A extends ue {
	constructor(e) {
		super(), Ce(this, e, wA, WA, _e, {
			onSubmit: 0
		})
	}
}

function xA(E) {
	let e, T, t, r, R, n;
	return t = new IE({
		props: {
			message: E[3],
			onSubmit: E[5]
		}
	}), {
		c() {
			e = f("textarea"), T = $(), K(t.$$.fragment), a(e, "rows", "6"),
				a(e, "class",
					"block p-2.5 w-full text-blue-600 hover:text-blue-500 dark:text-blue-500 dark:hover:text-blue-400 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 font-mono"
				), a(e, "placeholder", E[2])
		},
		m(s, S) {
			V(s, e, S), Ye(e, E[0]), V(s, T, S), X(t, s, S), r = !0, R || (
				n = Ne(e, "input", E[4]), R = !0)
		},
		p(s, [S]) {
			(!r || S & 4) && a(e, "placeholder", s[2]), S & 1 && Ye(e, s[0]);
			const A = {};
			S & 8 && (A.message = s[3]), S & 3 && (A.onSubmit = s[5]), t.$set(
				A)
		},
		i(s) {
			r || (m(t.$$.fragment, s), r = !0)
		},
		o(s) {
			y(t.$$.fragment, s), r = !1
		},
		d(s) {
			s && (Y(e), Y(T)), k(t, s), R = !1, n()
		}
	}
}

function XA(E, e, T) {
	let {
		onSubmit: t
	} = e, {
		currentValue: r
	} = e, {
		placeholder: R
	} = e, {
		buttonText: n
	} = e;

	function s() {
		r = this.value, T(0, r)
	}
	const S = () => t(r);
	return E.$$set = A => {
		"onSubmit" in A && T(1, t = A.onSubmit), "currentValue" in A && T(0,
				r = A.currentValue), "placeholder" in A && T(2, R = A.placeholder),
			"buttonText" in A && T(3, n = A.buttonText)
	}, [r, t, R, n, s, S]
}
class kA extends ue {
	constructor(e) {
		super(), Ce(this, e, XA, xA, _e, {
			onSubmit: 1,
			currentValue: 0,
			placeholder: 2,
			buttonText: 3
		})
	}
}

function KA(E) {
	let e, T;
	return e = new IE({
		props: {
			message: "Play",
			onSubmit: E[2]
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, [r]) {
			const R = {};
			r & 1 && (R.onSubmit = t[2]), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function er(E) {
	if ("speechSynthesis" in window) {
		const e = new SpeechSynthesisUtterance(E);
		e.lang = "en-US", e.volume = 1, e.rate = 1, e.pitch = 1, window.speechSynthesis
			.speak(e)
	} else console.error(
		"SpeechSynthesis API is not supported in this browser.")
}

function JA(E, e, T) {
	let t;
	eE(E, pR, n => T(1, t = n));
	let {
		message: r
	} = e;
	const R = () => er(r);
	return E.$$set = n => {
		"message" in n && T(0, r = n.message)
	}, E.$$.update = () => {
		E.$$.dirty & 3 && t && er(r)
	}, [r, t, R]
}
class qA extends ue {
	constructor(e) {
		super(), Ce(this, e, JA, KA, _e, {
			message: 0
		})
	}
}

function QA(E) {
	let e, T, t;
	return {
		c() {
			e = f("button"), e.textContent = "Open Debugger", T = $(), t = f(
					"div"), t.innerHTML =
				'<div class="flex justify-between items-center py-3 px-4 border-b dark:border-neutral-700"><h3 class="font-bold text-gray-800 dark:text-white">Server Logs</h3> <button type="button" class="flex justify-center items-center size-7 text-sm font-semibold rounded-full border border-transparent text-gray-800 hover:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:text-white dark:hover:bg-neutral-700" data-hs-overlay="#hs-overlay-right"><span class="sr-only">Close modal</span> <svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"></path><path d="m6 6 12 12"></path></svg></button></div> <div class="p-4"><p id="log-contents" class="text-gray-800 dark:text-neutral-400"></p></div>',
				a(e, "type", "button"), a(e, "class",
					"absolute top-0 right-0 m-1 ms-0 py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none"
				), a(e, "data-hs-overlay", "#hs-overlay-right"), a(t, "id",
					"hs-overlay-right"), a(t, "class",
					"hs-overlay hs-overlay-open:translate-x-0 hidden translate-x-full fixed top-0 end-0 transition-all duration-300 transform h-full max-w-xs w-full z-[80] bg-white border-s dark:bg-neutral-800 dark:border-neutral-700 [--body-scroll:true] overflow-y-auto"
				), a(t, "tabindex", "-1")
		},
		m(r, R) {
			V(r, e, R), V(r, T, R), V(r, t, R)
		},
		p: j,
		i: j,
		o: j,
		d(r) {
			r && (Y(e), Y(T), Y(t))
		}
	}
}
class ZA extends ue {
	constructor(e) {
		super(), Ce(this, e, null, QA, _e, {})
	}
}
var yR = {
	exports: {}
};
(function(E) {
	(function(e, T) {
		E.exports ? E.exports = T() : e.nearley = T()
	})(Jn, function() {
		function e(A, o, i) {
			return this.id = ++e.highestId, this.name = A, this.symbols =
				o, this.postprocess = i, this
		}
		e.highestId = 0, e.prototype.toString = function(A) {
			var o = typeof A > "u" ? this.symbols.map(S)
				.join(" ") : this.symbols.slice(0, A)
				.map(S)
				.join(" ") + " ● " + this.symbols.slice(A)
				.map(S)
				.join(" ");
			return this.name + " → " + o
		};

		function T(A, o, i, _) {
			this.rule = A, this.dot = o, this.reference = i, this.data = [],
				this.wantedBy = _, this.isComplete = this.dot === A.symbols
				.length
		}
		T.prototype.toString = function() {
			return "{" + this.rule.toString(this.dot) + "}, from: " +
				(this.reference || 0)
		}, T.prototype.nextState = function(A) {
			var o = new T(this.rule, this.dot + 1, this.reference,
				this.wantedBy);
			return o.left = this, o.right = A, o.isComplete && (o.data =
				o.build(), o.right = void 0), o
		}, T.prototype.build = function() {
			var A = [],
				o = this;
			do A.push(o.right.data), o = o.left; while (o.left);
			return A.reverse(), A
		}, T.prototype.finish = function() {
			this.rule.postprocess && (this.data = this.rule.postprocess(
				this.data, this.reference, n.fail))
		};

		function t(A, o) {
			this.grammar = A, this.index = o, this.states = [], this.wants = {},
				this.scannable = [], this.completed = {}
		}
		t.prototype.process = function(A) {
			for (var o = this.states, i = this.wants, _ = this.completed,
				c = 0; c < o.length; c++) {
				var P = o[c];
				if (P.isComplete) {
					if (P.finish(), P.data !== n.fail) {
						for (var p = P.wantedBy, C = p.length; C--;) {
							var L = p[C];
							this.complete(L, P)
						}
						if (P.reference === this.index) {
							var I = P.rule.name;
							(this.completed[I] = this.completed[I] || [])
							.push(P)
						}
					}
				} else {
					var I = P.rule.symbols[P.dot];
					if (typeof I != "string") {
						this.scannable.push(P);
						continue
					}
					if (i[I]) {
						if (i[I].push(P), _.hasOwnProperty(I))
							for (var u = _[I], C = 0; C < u.length; C++) {
								var H = u[C];
								this.complete(P, H)
							}
					} else i[I] = [P], this.predict(I)
				}
			}
		}, t.prototype.predict = function(A) {
			for (var o = this.grammar.byName[A] || [], i = 0; i < o
				.length; i++) {
				var _ = o[i],
					c = this.wants[A],
					P = new T(_, 0, this.index, c);
				this.states.push(P)
			}
		}, t.prototype.complete = function(A, o) {
			var i = A.nextState(o);
			this.states.push(i)
		};

		function r(A, o) {
			this.rules = A, this.start = o || this.rules[0].name;
			var i = this.byName = {};
			this.rules.forEach(function(_) {
				i.hasOwnProperty(_.name) || (i[_.name] = []), i[
					_.name].push(_)
			})
		}
		r.fromCompiled = function(_, o) {
			var i = _.Lexer;
			_.ParserStart && (o = _.ParserStart, _ = _.ParserRules);
			var _ = _.map(function(P) {
					return new e(P.name, P.symbols, P.postprocess)
				}),
				c = new r(_, o);
			return c.lexer = i, c
		};

		function R() {
			this.reset("")
		}
		R.prototype.reset = function(A, o) {
			this.buffer = A, this.index = 0, this.line = o ? o.line :
				1, this.lastLineBreak = o ? -o.col : 0
		}, R.prototype.next = function() {
			if (this.index < this.buffer.length) {
				var A = this.buffer[this.index++];
				return A === `
` && (this.line += 1, this.lastLineBreak =
					this.index), {
					value: A
				}
			}
		}, R.prototype.save = function() {
			return {
				line: this.line,
				col: this.index - this.lastLineBreak
			}
		}, R.prototype.formatError = function(A, o) {
			var i = this.buffer;
			if (typeof i == "string") {
				var _ = i.split(`
`)
					.slice(Math.max(0, this.line - 5), this.line),
					c = i.indexOf(`
`, this.index);
				c === -1 && (c = i.length);
				var P = this.index - this.lastLineBreak,
					p = String(this.line)
					.length;
				return o += " at line " + this.line + " col " + P +
					`:

`, o += _.map(function(L, I) {
						return C(this.line - _.length + I + 1,
							p) + " " + L
					}, this)
					.join(`
`), o += `
` + C("", p + P) + `^
`, o
			} else return o + " at index " + (this.index - 1);

			function C(L, I) {
				var u = String(L);
				return Array(I - u.length + 1)
					.join(" ") + u
			}
		};

		function n(A, o, i) {
			if (A instanceof r) var _ = A,
				i = o;
			else var _ = r.fromCompiled(A, o);
			this.grammar = _, this.options = {
				keepHistory: !1,
				lexer: _.lexer || new R
			};
			for (var c in i || {}) this.options[c] = i[c];
			this.lexer = this.options.lexer, this.lexerState = void 0;
			var P = new t(_, 0);
			this.table = [P], P.wants[_.start] = [], P.predict(_.start),
				P.process(), this.current = 0
		}
		n.fail = {}, n.prototype.feed = function(A) {
			var o = this.lexer;
			o.reset(A, this.lexerState);
			for (var i;;) {
				try {
					if (i = o.next(), !i) break
				} catch (O) {
					var p = new t(this.grammar, this.current + 1);
					this.table.push(p);
					var _ = new Error(this.reportLexerError(O));
					throw _.offset = this.current, _.token = O.token,
						_
				}
				var c = this.table[this.current];
				this.options.keepHistory || delete this.table[this.current -
					1];
				var P = this.current + 1,
					p = new t(this.grammar, P);
				this.table.push(p);
				for (var C = i.text !== void 0 ? i.text : i.value,
					L = o.constructor === R ? i.value : i, I =
					c.scannable, u = I.length; u--;) {
					var H = I[u],
						b = H.rule.symbols[H.dot];
					if (b.test ? b.test(L) : b.type ? b.type === i.type :
						b.literal === C) {
						var M = H.nextState({
							data: L,
							token: i,
							isToken: !0,
							reference: P - 1
						});
						p.states.push(M)
					}
				}
				if (p.process(), p.states.length === 0) {
					var _ = new Error(this.reportError(i));
					throw _.offset = this.current, _.token = i, _
				}
				this.options.keepHistory && (c.lexerState = o.save()),
					this.current++
			}
			return c && (this.lexerState = o.save()), this.results =
				this.finish(), this
		}, n.prototype.reportLexerError = function(A) {
			var o, i, _ = A.token;
			return _ ? (o = "input " + JSON.stringify(_.text[0]) +
				" (lexer error)", i = this.lexer.formatError(_,
					"Syntax error")) : (o =
				"input (lexer error)", i = A.message), this.reportErrorCommon(
				i, o)
		}, n.prototype.reportError = function(A) {
			var o = (A.type ? A.type + " token: " : "") + JSON.stringify(
					A.value !== void 0 ? A.value : A),
				i = this.lexer.formatError(A, "Syntax error");
			return this.reportErrorCommon(i, o)
		}, n.prototype.reportErrorCommon = function(A, o) {
			var i = [];
			i.push(A);
			var _ = this.table.length - 2,
				c = this.table[_],
				P = c.states.filter(function(C) {
					var L = C.rule.symbols[C.dot];
					return L && typeof L != "string"
				});
			if (P.length === 0) i.push("Unexpected " + o +
				`. I did not expect any more input. Here is the state of my parse table:
`
			), this.displayStateStack(c.states, i);
			else {
				i.push("Unexpected " + o +
					`. Instead, I was expecting to see one of the following:
`
				);
				var p = P.map(function(C) {
					return this.buildFirstStateStack(C, []) || [C]
				}, this);
				p.forEach(function(C) {
					var L = C[0],
						I = L.rule.symbols[L.dot],
						u = this.getSymbolDisplay(I);
					i.push("A " + u + " based on:"), this.displayStateStack(
						C, i)
				}, this)
			}
			return i.push(""), i.join(`
`)
		}, n.prototype.displayStateStack = function(A, o) {
			for (var i, _ = 0, c = 0; c < A.length; c++) {
				var P = A[c],
					p = P.rule.toString(P.dot);
				p === i ? _++ : (_ > 0 && o.push("    ^ " + _ +
						" more lines identical to this"), _ = 0,
					o.push("    " + p)), i = p
			}
		}, n.prototype.getSymbolDisplay = function(A) {
			return s(A)
		}, n.prototype.buildFirstStateStack = function(A, o) {
			if (o.indexOf(A) !== -1) return null;
			if (A.wantedBy.length === 0) return [A];
			var i = A.wantedBy[0],
				_ = [A].concat(o),
				c = this.buildFirstStateStack(i, _);
			return c === null ? null : [A].concat(c)
		}, n.prototype.save = function() {
			var A = this.table[this.current];
			return A.lexerState = this.lexerState, A
		}, n.prototype.restore = function(A) {
			var o = A.index;
			this.current = o, this.table[o] = A, this.table.splice(
					o + 1), this.lexerState = A.lexerState, this.results =
				this.finish()
		}, n.prototype.rewind = function(A) {
			if (!this.options.keepHistory) throw new Error(
				"set option `keepHistory` to enable rewinding"
			);
			this.restore(this.table[A])
		}, n.prototype.finish = function() {
			var A = [],
				o = this.grammar.start,
				i = this.table[this.table.length - 1];
			return i.states.forEach(function(_) {
				_.rule.name === o && _.dot === _.rule.symbols
					.length && _.reference === 0 && _.data !==
					n.fail && A.push(_)
			}), A.map(function(_) {
				return _.data
			})
		};

		function s(A) {
			var o = typeof A;
			if (o === "string") return A;
			if (o === "object") {
				if (A.literal) return JSON.stringify(A.literal);
				if (A instanceof RegExp) return "character matching " +
					A;
				if (A.type) return A.type + " token";
				if (A.test) return "token matching " + String(A.test);
				throw new Error("Unknown symbol type: " + A)
			}
		}

		function S(A) {
			var o = typeof A;
			if (o === "string") return A;
			if (o === "object") {
				if (A.literal) return JSON.stringify(A.literal);
				if (A instanceof RegExp) return A.toString();
				if (A.type) return "%" + A.type;
				if (A.test) return "<" + String(A.test) + ">";
				throw new Error("Unknown symbol type: " + A)
			}
		}
		return {
			Parser: n,
			Grammar: r,
			Rule: e
		}
	})
})(yR);
var jA = yR.exports;
const zA = qn(jA);
var BR = Object.defineProperty,
	es = Object.defineProperties,
	Es = Object.getOwnPropertyDescriptors,
	Mt = Object.getOwnPropertySymbols,
	vR = Object.prototype.hasOwnProperty,
	FR = Object.prototype.propertyIsEnumerable,
	Er = (E, e, T) => e in E ? BR(E, e, {
		enumerable: !0,
		configurable: !0,
		writable: !0,
		value: T
	}) : E[e] = T,
	EE = (E, e) => {
		for (var T in e || (e = {})) vR.call(e, T) && Er(E, T, e[T]);
		if (Mt)
			for (var T of Mt(e)) FR.call(e, T) && Er(E, T, e[T]);
		return E
	},
	AE = (E, e) => es(E, Es(e)),
	ts = (E, e) => {
		var T = {};
		for (var t in E) vR.call(E, t) && e.indexOf(t) < 0 && (T[t] = E[t]);
		if (E != null && Mt)
			for (var t of Mt(E)) e.indexOf(t) < 0 && FR.call(E, t) && (T[t] = E[
				t]);
		return T
	},
	Ts = (E, e) => {
		for (var T in e) BR(E, T, {
			get: e[T],
			enumerable: !0
		})
	},
	YR = {};
Ts(YR, {
	bigquery: () => cs,
	db2: () => bs,
	db2i: () => $s,
	hive: () => js,
	mariadb: () => AS,
	mysql: () => lS,
	n1ql: () => bS,
	plsql: () => $S,
	postgresql: () => zS,
	redshift: () => so,
	singlestoredb: () => oO,
	snowflake: () => CO,
	spark: () => _o,
	sql: () => vo,
	sqlite: () => Uo,
	tidb: () => dS,
	transactsql: () => EO,
	trino: () => ko
});
var v = E => E.flatMap(rs),
	rs = E => Pt(ns(E))
	.map(Rs),
	Rs = E => E.replace(/ +/g, " ")
	.trim(),
	ns = E => ({
		type: "mandatory_block",
		items: DT(E, 0)[0]
	}),
	DT = (E, e, T) => {
		const t = [];
		for (; E[e];) {
			const [r, R] = As(E, e);
			if (t.push(r), e = R, E[e] === "|") e++;
			else if (E[e] === "}" || E[e] === "]") {
				if (T !== E[e]) throw new Error(
					`Unbalanced parenthesis in: ${E}`);
				return e++, [t, e]
			} else if (e === E.length) {
				if (T) throw new Error(`Unbalanced parenthesis in: ${E}`);
				return [t, e]
			} else throw new Error(`Unexpected "${E[e]}"`)
		}
		return [t, e]
	},
	As = (E, e) => {
		const T = [];
		for (;;) {
			const [t, r] = ss(E, e);
			if (t) T.push(t), e = r;
			else break
		}
		return T.length === 1 ? [T[0], e] : [{
			type: "concatenation",
			items: T
		}, e]
	},
	ss = (E, e) => {
		if (E[e] === "{") return Ss(E, e + 1);
		if (E[e] === "[") return os(E, e + 1); {
			let T = "";
			for (; E[e] && /[A-Za-z0-9_ ]/.test(E[e]);) T += E[e], e++;
			return [T, e]
		}
	},
	Ss = (E, e) => {
		const [T, t] = DT(E, e, "}");
		return [{
			type: "mandatory_block",
			items: T
		}, t]
	},
	os = (E, e) => {
		const [T, t] = DT(E, e, "]");
		return [{
			type: "optional_block",
			items: T
		}, t]
	},
	Pt = E => {
		if (typeof E == "string") return [E];
		if (E.type === "concatenation") return E.items.map(Pt)
			.reduce(Os, [""]);
		if (E.type === "mandatory_block") return E.items.flatMap(Pt);
		if (E.type === "optional_block") return ["", ...E.items.flatMap(Pt)];
		throw new Error(`Unknown node type: ${E}`)
	},
	Os = (E, e) => {
		const T = [];
		for (const t of E)
			for (const r of e) T.push(t + r);
		return T
	},
	VR = (E => (E.QUOTED_IDENTIFIER = "QUOTED_IDENTIFIER", E.IDENTIFIER =
		"IDENTIFIER", E.STRING = "STRING", E.VARIABLE = "VARIABLE", E.RESERVED_DATA_TYPE =
		"RESERVED_DATA_TYPE", E.RESERVED_PARAMETERIZED_DATA_TYPE =
		"RESERVED_PARAMETERIZED_DATA_TYPE", E.RESERVED_KEYWORD =
		"RESERVED_KEYWORD", E.RESERVED_FUNCTION_NAME =
		"RESERVED_FUNCTION_NAME", E.RESERVED_PHRASE = "RESERVED_PHRASE", E.RESERVED_SET_OPERATION =
		"RESERVED_SET_OPERATION", E.RESERVED_CLAUSE = "RESERVED_CLAUSE", E.RESERVED_SELECT =
		"RESERVED_SELECT", E.RESERVED_JOIN = "RESERVED_JOIN", E.ARRAY_IDENTIFIER =
		"ARRAY_IDENTIFIER", E.ARRAY_KEYWORD = "ARRAY_KEYWORD", E.CASE =
		"CASE", E.END = "END", E.WHEN = "WHEN", E.ELSE = "ELSE", E.THEN =
		"THEN", E.LIMIT = "LIMIT", E.BETWEEN = "BETWEEN", E.AND = "AND", E.OR =
		"OR", E.XOR = "XOR", E.OPERATOR = "OPERATOR", E.COMMA = "COMMA", E.ASTERISK =
		"ASTERISK", E.PROPERTY_ACCESS_OPERATOR = "PROPERTY_ACCESS_OPERATOR",
		E.OPEN_PAREN = "OPEN_PAREN", E.CLOSE_PAREN = "CLOSE_PAREN", E.LINE_COMMENT =
		"LINE_COMMENT", E.BLOCK_COMMENT = "BLOCK_COMMENT", E.DISABLE_COMMENT =
		"DISABLE_COMMENT", E.NUMBER = "NUMBER", E.NAMED_PARAMETER =
		"NAMED_PARAMETER", E.QUOTED_PARAMETER = "QUOTED_PARAMETER", E.NUMBERED_PARAMETER =
		"NUMBERED_PARAMETER", E.POSITIONAL_PARAMETER =
		"POSITIONAL_PARAMETER", E.CUSTOM_PARAMETER = "CUSTOM_PARAMETER", E.DELIMITER =
		"DELIMITER", E.EOF = "EOF", E))(VR || {}),
	WR = E => ({
		type: "EOF",
		raw: "«EOF»",
		text: "«EOF»",
		start: E
	}),
	tt = WR(1 / 0),
	QE = E => e => e.type === E.type && e.text === E.text,
	FE = {
		ARRAY: QE({
			text: "ARRAY",
			type: "RESERVED_DATA_TYPE"
		}),
		BY: QE({
			text: "BY",
			type: "RESERVED_KEYWORD"
		}),
		SET: QE({
			text: "SET",
			type: "RESERVED_CLAUSE"
		}),
		STRUCT: QE({
			text: "STRUCT",
			type: "RESERVED_DATA_TYPE"
		}),
		WINDOW: QE({
			text: "WINDOW",
			type: "RESERVED_CLAUSE"
		}),
		VALUES: QE({
			text: "VALUES",
			type: "RESERVED_CLAUSE"
		})
	},
	wR = E => E === "RESERVED_DATA_TYPE" || E === "RESERVED_KEYWORD" || E ===
	"RESERVED_FUNCTION_NAME" || E === "RESERVED_PHRASE" || E ===
	"RESERVED_CLAUSE" || E === "RESERVED_SELECT" || E ===
	"RESERVED_SET_OPERATION" || E === "RESERVED_JOIN" || E === "ARRAY_KEYWORD" ||
	E === "CASE" || E === "END" || E === "WHEN" || E === "ELSE" || E === "THEN" ||
	E === "LIMIT" || E === "BETWEEN" || E === "AND" || E === "OR" || E ===
	"XOR",
	is = E => E === "AND" || E === "OR" || E === "XOR",
	as = ["KEYS.NEW_KEYSET", "KEYS.ADD_KEY_FROM_RAW_BYTES",
		"AEAD.DECRYPT_BYTES", "AEAD.DECRYPT_STRING", "AEAD.ENCRYPT",
		"KEYS.KEYSET_CHAIN", "KEYS.KEYSET_FROM_JSON", "KEYS.KEYSET_TO_JSON",
		"KEYS.ROTATE_KEYSET", "KEYS.KEYSET_LENGTH", "ANY_VALUE", "ARRAY_AGG",
		"AVG", "CORR", "COUNT", "COUNTIF", "COVAR_POP", "COVAR_SAMP", "MAX",
		"MIN", "ST_CLUSTERDBSCAN", "STDDEV_POP", "STDDEV_SAMP", "STRING_AGG",
		"SUM", "VAR_POP", "VAR_SAMP", "ANY_VALUE", "ARRAY_AGG",
		"ARRAY_CONCAT_AGG", "AVG", "BIT_AND", "BIT_OR", "BIT_XOR", "COUNT",
		"COUNTIF", "LOGICAL_AND", "LOGICAL_OR", "MAX", "MIN", "STRING_AGG",
		"SUM", "APPROX_COUNT_DISTINCT", "APPROX_QUANTILES", "APPROX_TOP_COUNT",
		"APPROX_TOP_SUM", "ARRAY_CONCAT", "ARRAY_LENGTH", "ARRAY_TO_STRING",
		"GENERATE_ARRAY", "GENERATE_DATE_ARRAY", "GENERATE_TIMESTAMP_ARRAY",
		"ARRAY_REVERSE", "OFFSET", "SAFE_OFFSET", "ORDINAL", "SAFE_ORDINAL",
		"BIT_COUNT", "PARSE_BIGNUMERIC", "PARSE_NUMERIC", "SAFE_CAST",
		"CURRENT_DATE", "EXTRACT", "DATE", "DATE_ADD", "DATE_SUB", "DATE_DIFF",
		"DATE_TRUNC", "DATE_FROM_UNIX_DATE", "FORMAT_DATE", "LAST_DAY",
		"PARSE_DATE", "UNIX_DATE", "CURRENT_DATETIME", "DATETIME", "EXTRACT",
		"DATETIME_ADD", "DATETIME_SUB", "DATETIME_DIFF", "DATETIME_TRUNC",
		"FORMAT_DATETIME", "LAST_DAY", "PARSE_DATETIME", "ERROR",
		"EXTERNAL_QUERY", "S2_CELLIDFROMPOINT", "S2_COVERINGCELLIDS",
		"ST_ANGLE", "ST_AREA", "ST_ASBINARY", "ST_ASGEOJSON", "ST_ASTEXT",
		"ST_AZIMUTH", "ST_BOUNDARY", "ST_BOUNDINGBOX", "ST_BUFFER",
		"ST_BUFFERWITHTOLERANCE", "ST_CENTROID", "ST_CENTROID_AGG",
		"ST_CLOSESTPOINT", "ST_CLUSTERDBSCAN", "ST_CONTAINS", "ST_CONVEXHULL",
		"ST_COVEREDBY", "ST_COVERS", "ST_DIFFERENCE", "ST_DIMENSION",
		"ST_DISJOINT", "ST_DISTANCE", "ST_DUMP", "ST_DWITHIN", "ST_ENDPOINT",
		"ST_EQUALS", "ST_EXTENT", "ST_EXTERIORRING", "ST_GEOGFROM",
		"ST_GEOGFROMGEOJSON", "ST_GEOGFROMTEXT", "ST_GEOGFROMWKB",
		"ST_GEOGPOINT", "ST_GEOGPOINTFROMGEOHASH", "ST_GEOHASH",
		"ST_GEOMETRYTYPE", "ST_INTERIORRINGS", "ST_INTERSECTION",
		"ST_INTERSECTS", "ST_INTERSECTSBOX", "ST_ISCOLLECTION", "ST_ISEMPTY",
		"ST_LENGTH", "ST_MAKELINE", "ST_MAKEPOLYGON", "ST_MAKEPOLYGONORIENTED",
		"ST_MAXDISTANCE", "ST_NPOINTS", "ST_NUMGEOMETRIES", "ST_NUMPOINTS",
		"ST_PERIMETER", "ST_POINTN", "ST_SIMPLIFY", "ST_SNAPTOGRID",
		"ST_STARTPOINT", "ST_TOUCHES", "ST_UNION", "ST_UNION_AGG", "ST_WITHIN",
		"ST_X", "ST_Y", "FARM_FINGERPRINT", "MD5", "SHA1", "SHA256", "SHA512",
		"HLL_COUNT.INIT", "HLL_COUNT.MERGE", "HLL_COUNT.MERGE_PARTIAL",
		"HLL_COUNT.EXTRACT", "MAKE_INTERVAL", "EXTRACT", "JUSTIFY_DAYS",
		"JUSTIFY_HOURS", "JUSTIFY_INTERVAL", "JSON_EXTRACT", "JSON_QUERY",
		"JSON_EXTRACT_SCALAR", "JSON_VALUE", "JSON_EXTRACT_ARRAY",
		"JSON_QUERY_ARRAY", "JSON_EXTRACT_STRING_ARRAY", "JSON_VALUE_ARRAY",
		"TO_JSON_STRING", "ABS", "SIGN", "IS_INF", "IS_NAN", "IEEE_DIVIDE",
		"RAND", "SQRT", "POW", "POWER", "EXP", "LN", "LOG", "LOG10", "GREATEST",
		"LEAST", "DIV", "SAFE_DIVIDE", "SAFE_MULTIPLY", "SAFE_NEGATE",
		"SAFE_ADD", "SAFE_SUBTRACT", "MOD", "ROUND", "TRUNC", "CEIL", "CEILING",
		"FLOOR", "COS", "COSH", "ACOS", "ACOSH", "SIN", "SINH", "ASIN", "ASINH",
		"TAN", "TANH", "ATAN", "ATANH", "ATAN2", "RANGE_BUCKET", "FIRST_VALUE",
		"LAST_VALUE", "NTH_VALUE", "LEAD", "LAG", "PERCENTILE_CONT",
		"PERCENTILE_DISC", "NET.IP_FROM_STRING", "NET.SAFE_IP_FROM_STRING",
		"NET.IP_TO_STRING", "NET.IP_NET_MASK", "NET.IP_TRUNC",
		"NET.IPV4_FROM_INT64", "NET.IPV4_TO_INT64", "NET.HOST",
		"NET.PUBLIC_SUFFIX", "NET.REG_DOMAIN", "RANK", "DENSE_RANK",
		"PERCENT_RANK", "CUME_DIST", "NTILE", "ROW_NUMBER", "SESSION_USER",
		"CORR", "COVAR_POP", "COVAR_SAMP", "STDDEV_POP", "STDDEV_SAMP",
		"STDDEV", "VAR_POP", "VAR_SAMP", "VARIANCE", "ASCII", "BYTE_LENGTH",
		"CHAR_LENGTH", "CHARACTER_LENGTH", "CHR", "CODE_POINTS_TO_BYTES",
		"CODE_POINTS_TO_STRING", "CONCAT", "CONTAINS_SUBSTR", "ENDS_WITH",
		"FORMAT", "FROM_BASE32", "FROM_BASE64", "FROM_HEX", "INITCAP", "INSTR",
		"LEFT", "LENGTH", "LPAD", "LOWER", "LTRIM", "NORMALIZE",
		"NORMALIZE_AND_CASEFOLD", "OCTET_LENGTH", "REGEXP_CONTAINS",
		"REGEXP_EXTRACT", "REGEXP_EXTRACT_ALL", "REGEXP_INSTR",
		"REGEXP_REPLACE", "REGEXP_SUBSTR", "REPLACE", "REPEAT", "REVERSE",
		"RIGHT", "RPAD", "RTRIM", "SAFE_CONVERT_BYTES_TO_STRING", "SOUNDEX",
		"SPLIT", "STARTS_WITH", "STRPOS", "SUBSTR", "SUBSTRING", "TO_BASE32",
		"TO_BASE64", "TO_CODE_POINTS", "TO_HEX", "TRANSLATE", "TRIM", "UNICODE",
		"UPPER", "CURRENT_TIME", "TIME", "EXTRACT", "TIME_ADD", "TIME_SUB",
		"TIME_DIFF", "TIME_TRUNC", "FORMAT_TIME", "PARSE_TIME",
		"CURRENT_TIMESTAMP", "EXTRACT", "STRING", "TIMESTAMP", "TIMESTAMP_ADD",
		"TIMESTAMP_SUB", "TIMESTAMP_DIFF", "TIMESTAMP_TRUNC",
		"FORMAT_TIMESTAMP", "PARSE_TIMESTAMP", "TIMESTAMP_SECONDS",
		"TIMESTAMP_MILLIS", "TIMESTAMP_MICROS", "UNIX_SECONDS", "UNIX_MILLIS",
		"UNIX_MICROS", "GENERATE_UUID", "COALESCE", "IF", "IFNULL", "NULLIF",
		"AVG", "BIT_AND", "BIT_OR", "BIT_XOR", "CORR", "COUNT", "COVAR_POP",
		"COVAR_SAMP", "EXACT_COUNT_DISTINCT", "FIRST", "GROUP_CONCAT",
		"GROUP_CONCAT_UNQUOTED", "LAST", "MAX", "MIN", "NEST", "NTH",
		"QUANTILES", "STDDEV", "STDDEV_POP", "STDDEV_SAMP", "SUM", "TOP",
		"UNIQUE", "VARIANCE", "VAR_POP", "VAR_SAMP", "BIT_COUNT", "BOOLEAN",
		"BYTES", "CAST", "FLOAT", "HEX_STRING", "INTEGER", "STRING", "COALESCE",
		"GREATEST", "IFNULL", "IS_INF", "IS_NAN", "IS_EXPLICITLY_DEFINED",
		"LEAST", "NVL", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP",
		"DATE", "DATE_ADD", "DATEDIFF", "DAY", "DAYOFWEEK", "DAYOFYEAR",
		"FORMAT_UTC_USEC", "HOUR", "MINUTE", "MONTH", "MSEC_TO_TIMESTAMP",
		"NOW", "PARSE_UTC_USEC", "QUARTER", "SEC_TO_TIMESTAMP", "SECOND",
		"STRFTIME_UTC_USEC", "TIME", "TIMESTAMP", "TIMESTAMP_TO_MSEC",
		"TIMESTAMP_TO_SEC", "TIMESTAMP_TO_USEC", "USEC_TO_TIMESTAMP",
		"UTC_USEC_TO_DAY", "UTC_USEC_TO_HOUR", "UTC_USEC_TO_MONTH",
		"UTC_USEC_TO_WEEK", "UTC_USEC_TO_YEAR", "WEEK", "YEAR", "FORMAT_IP",
		"PARSE_IP", "FORMAT_PACKED_IP", "PARSE_PACKED_IP", "JSON_EXTRACT",
		"JSON_EXTRACT_SCALAR", "ABS", "ACOS", "ACOSH", "ASIN", "ASINH", "ATAN",
		"ATANH", "ATAN2", "CEIL", "COS", "COSH", "DEGREES", "EXP", "FLOOR",
		"LN", "LOG", "LOG2", "LOG10", "PI", "POW", "RADIANS", "RAND", "ROUND",
		"SIN", "SINH", "SQRT", "TAN", "TANH", "REGEXP_MATCH", "REGEXP_EXTRACT",
		"REGEXP_REPLACE", "CONCAT", "INSTR", "LEFT", "LENGTH", "LOWER", "LPAD",
		"LTRIM", "REPLACE", "RIGHT", "RPAD", "RTRIM", "SPLIT", "SUBSTR",
		"UPPER", "TABLE_DATE_RANGE", "TABLE_DATE_RANGE_STRICT", "TABLE_QUERY",
		"HOST", "DOMAIN", "TLD", "AVG", "COUNT", "MAX", "MIN", "STDDEV", "SUM",
		"CUME_DIST", "DENSE_RANK", "FIRST_VALUE", "LAG", "LAST_VALUE", "LEAD",
		"NTH_VALUE", "NTILE", "PERCENT_RANK", "PERCENTILE_CONT",
		"PERCENTILE_DISC", "RANK", "RATIO_TO_REPORT", "ROW_NUMBER",
		"CURRENT_USER", "EVERY", "FROM_BASE64", "HASH", "FARM_FINGERPRINT",
		"IF", "POSITION", "SHA1", "SOME", "TO_BASE64", "BQ.JOBS.CANCEL",
		"BQ.REFRESH_MATERIALIZED_VIEW", "OPTIONS", "PIVOT", "UNPIVOT"
	],
	Is = ["ALL", "AND", "ANY", "AS", "ASC", "ASSERT_ROWS_MODIFIED", "AT",
		"BETWEEN", "BY", "CASE", "CAST", "COLLATE", "CONTAINS", "CREATE",
		"CROSS", "CUBE", "CURRENT", "DEFAULT", "DEFINE", "DESC", "DISTINCT",
		"ELSE", "END", "ENUM", "ESCAPE", "EXCEPT", "EXCLUDE", "EXISTS",
		"EXTRACT", "FALSE", "FETCH", "FOLLOWING", "FOR", "FROM", "FULL",
		"GROUP", "GROUPING", "GROUPS", "HASH", "HAVING", "IF", "IGNORE", "IN",
		"INNER", "INTERSECT", "INTO", "IS", "JOIN", "LATERAL", "LEFT", "LIMIT",
		"LOOKUP", "MERGE", "NATURAL", "NEW", "NO", "NOT", "NULL", "NULLS", "OF",
		"ON", "OR", "ORDER", "OUTER", "OVER", "PARTITION", "PRECEDING", "PROTO",
		"RANGE", "RECURSIVE", "RESPECT", "RIGHT", "ROLLUP", "ROWS", "SELECT",
		"SET", "SOME", "TABLE", "TABLESAMPLE", "THEN", "TO", "TREAT", "TRUE",
		"UNBOUNDED", "UNION", "UNNEST", "USING", "WHEN", "WHERE", "WINDOW",
		"WITH", "WITHIN", "SAFE", "LIKE", "COPY", "CLONE", "IN", "OUT", "INOUT",
		"RETURNS", "LANGUAGE", "CASCADE", "RESTRICT", "DETERMINISTIC"
	],
	Ns = ["ARRAY", "BOOL", "BYTES", "DATE", "DATETIME", "GEOGRAPHY", "INTERVAL",
		"INT64", "INT", "SMALLINT", "INTEGER", "BIGINT", "TINYINT", "BYTEINT",
		"NUMERIC", "DECIMAL", "BIGNUMERIC", "BIGDECIMAL", "FLOAT64", "STRING",
		"STRUCT", "TIME", "TIMEZONE"
	],
	ls = v(["SELECT [ALL | DISTINCT] [AS STRUCT | AS VALUE]"]),
	_s = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY", "HAVING",
		"QUALIFY", "WINDOW", "PARTITION BY", "ORDER BY", "LIMIT", "OFFSET",
		"OMIT RECORD IF", "INSERT [INTO]", "VALUES", "SET", "MERGE [INTO]",
		"WHEN [NOT] MATCHED [BY SOURCE | BY TARGET] [THEN]", "UPDATE SET",
		"CLUSTER BY", "FOR SYSTEM_TIME AS OF", "WITH CONNECTION",
		"WITH PARTITION COLUMNS", "REMOTE WITH CONNECTION"
	]),
	tr = v([
		"CREATE [OR REPLACE] [TEMP|TEMPORARY|SNAPSHOT|EXTERNAL] TABLE [IF NOT EXISTS]"
	]),
	xt = v(["CREATE [OR REPLACE] [MATERIALIZED] VIEW [IF NOT EXISTS]", "UPDATE",
		"DELETE [FROM]", "DROP [SNAPSHOT | EXTERNAL] TABLE [IF EXISTS]",
		"ALTER TABLE [IF EXISTS]", "ADD COLUMN [IF NOT EXISTS]",
		"DROP COLUMN [IF EXISTS]", "RENAME TO", "ALTER COLUMN [IF EXISTS]",
		"SET DEFAULT COLLATE", "SET OPTIONS", "DROP NOT NULL",
		"SET DATA TYPE", "ALTER SCHEMA [IF EXISTS]",
		"ALTER [MATERIALIZED] VIEW [IF EXISTS]", "ALTER BI_CAPACITY",
		"TRUNCATE TABLE", "CREATE SCHEMA [IF NOT EXISTS]",
		"DEFAULT COLLATE",
		"CREATE [OR REPLACE] [TEMP|TEMPORARY|TABLE] FUNCTION [IF NOT EXISTS]",
		"CREATE [OR REPLACE] PROCEDURE [IF NOT EXISTS]",
		"CREATE [OR REPLACE] ROW ACCESS POLICY [IF NOT EXISTS]", "GRANT TO",
		"FILTER USING", "CREATE CAPACITY", "AS JSON", "CREATE RESERVATION",
		"CREATE ASSIGNMENT", "CREATE SEARCH INDEX [IF NOT EXISTS]",
		"DROP SCHEMA [IF EXISTS]", "DROP [MATERIALIZED] VIEW [IF EXISTS]",
		"DROP [TABLE] FUNCTION [IF EXISTS]", "DROP PROCEDURE [IF EXISTS]",
		"DROP ROW ACCESS POLICY", "DROP ALL ROW ACCESS POLICIES",
		"DROP CAPACITY [IF EXISTS]", "DROP RESERVATION [IF EXISTS]",
		"DROP ASSIGNMENT [IF EXISTS]", "DROP SEARCH INDEX [IF EXISTS]",
		"DROP [IF EXISTS]", "GRANT", "REVOKE", "DECLARE",
		"EXECUTE IMMEDIATE", "LOOP", "END LOOP", "REPEAT", "END REPEAT",
		"WHILE", "END WHILE", "BREAK", "LEAVE", "CONTINUE", "ITERATE",
		"FOR", "END FOR", "BEGIN", "BEGIN TRANSACTION",
		"COMMIT TRANSACTION", "ROLLBACK TRANSACTION", "RAISE", "RETURN",
		"CALL", "ASSERT", "EXPORT DATA"
	]),
	Ls = v(["UNION {ALL | DISTINCT}", "EXCEPT DISTINCT", "INTERSECT DISTINCT"]),
	Cs = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN"
	]),
	us = v(["TABLESAMPLE SYSTEM", "ANY TYPE", "ALL COLUMNS",
		"NOT DETERMINISTIC", "{ROWS | RANGE} BETWEEN",
		"IS [NOT] DISTINCT FROM"
	]),
	cs = {
		name: "bigquery",
		tokenizerOptions: {
			reservedSelect: ls,
			reservedClauses: [..._s, ...xt, ...tr],
			reservedSetOperations: Ls,
			reservedJoins: Cs,
			reservedPhrases: us,
			reservedKeywords: Is,
			reservedDataTypes: Ns,
			reservedFunctionNames: as,
			extraParens: ["[]"],
			stringTypes: [{
				quote: '""".."""',
				prefixes: ["R", "B", "RB", "BR"]
			}, {
				quote: "\'\'\'..\'\'\'",
				prefixes: ["R", "B", "RB", "BR"]
			}, '""-bs', "''-bs", {
				quote: '""-raw',
				prefixes: ["R", "B", "RB", "BR"],
				requirePrefix: !0
			}, {
				quote: "''-raw",
				prefixes: ["R", "B", "RB", "BR"],
				requirePrefix: !0
			}],
			identTypes: ["``"],
			identChars: {
				dashes: !0
			},
			paramTypes: {
				positional: !0,
				named: ["@"],
				quoted: ["@"]
			},
			variableTypes: [{
				regex: String.raw `@@\\w+`
			}],
			lineCommentTypes: ["--", "#"],
			operators: ["&", "|", "^", "~", ">>", "<<", "||", "=>"],
			postProcess: fs
		},
		formatOptions: {
			onelineClauses: [...tr, ...xt],
			tabularOnelineClauses: xt
		}
	};

function fs(E) {
	return Ps(Ds(E))
}

function Ps(E) {
	let e = tt;
	return E.map(T => T.text === "OFFSET" && e.text === "[" ? (e = T, AE(EE({},
		T), {
		type: "RESERVED_FUNCTION_NAME"
	})) : (e = T, T))
}

function Ds(E) {
	var e;
	const T = [];
	for (let t = 0; t < E.length; t++) {
		const r = E[t];
		if ((FE.ARRAY(r) || FE.STRUCT(r)) && ((e = E[t + 1]) == null ? void 0 :
			e.text) === "<") {
			const R = ds(E, t + 1),
				n = E.slice(t, R + 1);
			T.push({
				type: "IDENTIFIER",
				raw: n.map(Tr("raw"))
					.join(""),
				text: n.map(Tr("text"))
					.join(""),
				start: r.start
			}), t = R
		} else T.push(r)
	}
	return T
}
var Tr = E => e => e.type === "IDENTIFIER" || e.type === "COMMA" ? e[E] + " " :
	e[E];

function ds(E, e) {
	let T = 0;
	for (let t = e; t < E.length; t++) {
		const r = E[t];
		if (r.text === "<" ? T++ : r.text === ">" ? T-- : r.text === ">>" && (T -=
			2), T === 0) return t
	}
	return E.length - 1
}
var ps = ["ARRAY_AGG", "AVG", "CORRELATION", "COUNT", "COUNT_BIG", "COVARIANCE",
		"COVARIANCE_SAMP", "CUME_DIST", "GROUPING", "LISTAGG", "MAX", "MEDIAN",
		"MIN", "PERCENTILE_CONT", "PERCENTILE_DISC", "PERCENT_RANK",
		"REGR_AVGX", "REGR_AVGY", "REGR_COUNT", "REGR_INTERCEPT", "REGR_ICPT",
		"REGR_R2", "REGR_SLOPE", "REGR_SXX", "REGR_SXY", "REGR_SYY", "STDDEV",
		"STDDEV_SAMP", "SUM", "VARIANCE", "VARIANCE_SAMP", "XMLAGG", "XMLGROUP",
		"ABS", "ABSVAL", "ACOS", "ADD_DAYS", "ADD_HOURS", "ADD_MINUTES",
		"ADD_MONTHS", "ADD_SECONDS", "ADD_YEARS", "AGE", "ARRAY_DELETE",
		"ARRAY_FIRST", "ARRAY_LAST", "ARRAY_NEXT", "ARRAY_PRIOR", "ASCII",
		"ASCII_STR", "ASIN", "ATAN", "ATAN2", "ATANH", "BITAND", "BITANDNOT",
		"BITOR", "BITXOR", "BITNOT", "BPCHAR", "BSON_TO_JSON", "BTRIM",
		"CARDINALITY", "CEILING", "CEIL", "CHARACTER_LENGTH", "CHR", "COALESCE",
		"COLLATION_KEY", "COLLATION_KEY_BIT", "COMPARE_DECFLOAT", "CONCAT",
		"COS", "COSH", "COT", "CURSOR_ROWCOUNT", "DATAPARTITIONNUM",
		"DATE_PART", "DATE_TRUNC", "DAY", "DAYNAME", "DAYOFMONTH", "DAYOFWEEK",
		"DAYOFWEEK_ISO", "DAYOFYEAR", "DAYS", "DAYS_BETWEEN",
		"DAYS_TO_END_OF_MONTH", "DBPARTITIONNUM", "DECFLOAT", "DECFLOAT_FORMAT",
		"DECODE", "DECRYPT_BIN", "DECRYPT_CHAR", "DEGREES", "DEREF",
		"DIFFERENCE", "DIGITS", "DOUBLE_PRECISION", "EMPTY_BLOB", "EMPTY_CLOB",
		"EMPTY_DBCLOB", "EMPTY_NCLOB", "ENCRYPT", "EVENT_MON_STATE", "EXP",
		"EXTRACT", "FIRST_DAY", "FLOOR", "FROM_UTC_TIMESTAMP",
		"GENERATE_UNIQUE", "GETHINT", "GREATEST", "HASH", "HASH4", "HASH8",
		"HASHEDVALUE", "HEX", "HEXTORAW", "HOUR", "HOURS_BETWEEN",
		"IDENTITY_VAL_LOCAL", "IFNULL", "INITCAP", "INSERT", "INSTR", "INSTR2",
		"INSTR4", "INSTRB", "INTNAND", "INTNOR", "INTNXOR", "INTNNOT", "ISNULL",
		"JSON_ARRAY", "JSON_OBJECT", "JSON_QUERY", "JSON_TO_BSON", "JSON_VALUE",
		"JULIAN_DAY", "LAST_DAY", "LCASE", "LEAST", "LEFT", "LENGTH", "LENGTH2",
		"LENGTH4", "LENGTHB", "LN", "LOCATE", "LOCATE_IN_STRING", "LOG10",
		"LONG_VARCHAR", "LONG_VARGRAPHIC", "LOWER", "LPAD", "LTRIM", "MAX",
		"MAX_CARDINALITY", "MICROSECOND", "MIDNIGHT_SECONDS", "MIN", "MINUTE",
		"MINUTES_BETWEEN", "MOD", "MONTH", "MONTHNAME", "MONTHS_BETWEEN",
		"MULTIPLY_ALT", "NEXT_DAY", "NEXT_MONTH", "NEXT_QUARTER", "NEXT_WEEK",
		"NEXT_YEAR", "NORMALIZE_DECFLOAT", "NOW", "NULLIF", "NVL", "NVL2",
		"OCTET_LENGTH", "OVERLAY", "PARAMETER", "POSITION", "POSSTR", "POW",
		"POWER", "QUANTIZE", "QUARTER", "QUOTE_IDENT", "QUOTE_LITERAL",
		"RADIANS", "RAISE_ERROR", "RAND", "RANDOM", "RAWTOHEX", "REC2XML",
		"REGEXP_COUNT", "REGEXP_EXTRACT", "REGEXP_INSTR", "REGEXP_LIKE",
		"REGEXP_MATCH_COUNT", "REGEXP_REPLACE", "REGEXP_SUBSTR", "REPEAT",
		"REPLACE", "RID", "RID_BIT", "RIGHT", "ROUND", "ROUND_TIMESTAMP",
		"RPAD", "RTRIM", "SECLABEL", "SECLABEL_BY_NAME", "SECLABEL_TO_CHAR",
		"SECOND", "SECONDS_BETWEEN", "SIGN", "SIN", "SINH", "SOUNDEX", "SPACE",
		"SQRT", "STRIP", "STRLEFT", "STRPOS", "STRRIGHT", "SUBSTR", "SUBSTR2",
		"SUBSTR4", "SUBSTRB", "SUBSTRING", "TABLE_NAME", "TABLE_SCHEMA", "TAN",
		"TANH", "THIS_MONTH", "THIS_QUARTER", "THIS_WEEK", "THIS_YEAR",
		"TIMESTAMP_FORMAT", "TIMESTAMP_ISO", "TIMESTAMPDIFF", "TIMEZONE",
		"TO_CHAR", "TO_CLOB", "TO_DATE", "TO_HEX", "TO_MULTI_BYTE", "TO_NCHAR",
		"TO_NCLOB", "TO_NUMBER", "TO_SINGLE_BYTE", "TO_TIMESTAMP",
		"TO_UTC_TIMESTAMP", "TOTALORDER", "TRANSLATE", "TRIM", "TRIM_ARRAY",
		"TRUNC_TIMESTAMP", "TRUNCATE", "TRUNC", "TYPE_ID", "TYPE_NAME",
		"TYPE_SCHEMA", "UCASE", "UNICODE_STR", "UPPER", "VALUE",
		"VARCHAR_BIT_FORMAT", "VARCHAR_FORMAT", "VARCHAR_FORMAT_BIT",
		"VERIFY_GROUP_FOR_USER", "VERIFY_ROLE_FOR_USER",
		"VERIFY_TRUSTED_CONTEXT_ROLE_FOR_USER", "WEEK", "WEEK_ISO",
		"WEEKS_BETWEEN", "WIDTH_BUCKET", "XMLATTRIBUTES", "XMLCOMMENT",
		"XMLCONCAT", "XMLDOCUMENT", "XMLELEMENT", "XMLFOREST", "XMLNAMESPACES",
		"XMLPARSE", "XMLPI", "XMLQUERY", "XMLROW", "XMLSERIALIZE", "XMLTEXT",
		"XMLVALIDATE", "XMLXSROBJECTID", "XSLTRANSFORM", "YEAR",
		"YEARS_BETWEEN", "YMD_BETWEEN", "BASE_TABLE", "JSON_TABLE", "UNNEST",
		"XMLTABLE", "RANK", "DENSE_RANK", "NTILE", "LAG", "LEAD", "ROW_NUMBER",
		"FIRST_VALUE", "LAST_VALUE", "NTH_VALUE", "RATIO_TO_REPORT", "CAST"
	],
	Ms = ["ACTIVATE", "ADD", "AFTER", "ALIAS", "ALL", "ALLOCATE", "ALLOW",
		"ALTER", "AND", "ANY", "AS", "ASENSITIVE", "ASSOCIATE", "ASUTIME", "AT",
		"ATTRIBUTES", "AUDIT", "AUTHORIZATION", "AUX", "AUXILIARY", "BEFORE",
		"BEGIN", "BETWEEN", "BINARY", "BUFFERPOOL", "BY", "CACHE", "CALL",
		"CALLED", "CAPTURE", "CARDINALITY", "CASCADED", "CASE", "CAST", "CHECK",
		"CLONE", "CLOSE", "CLUSTER", "COLLECTION", "COLLID", "COLUMN",
		"COMMENT", "COMMIT", "CONCAT", "CONDITION", "CONNECT", "CONNECTION",
		"CONSTRAINT", "CONTAINS", "CONTINUE", "COUNT", "COUNT_BIG", "CREATE",
		"CROSS", "CURRENT", "CURRENT_DATE", "CURRENT_LC_CTYPE", "CURRENT_PATH",
		"CURRENT_SCHEMA", "CURRENT_SERVER", "CURRENT_TIME", "CURRENT_TIMESTAMP",
		"CURRENT_TIMEZONE", "CURRENT_USER", "CURSOR", "CYCLE", "DATA",
		"DATABASE", "DATAPARTITIONNAME", "DATAPARTITIONNUM", "DAY", "DAYS",
		"DB2GENERAL", "DB2GENRL", "DB2SQL", "DBINFO", "DBPARTITIONNAME",
		"DBPARTITIONNUM", "DEALLOCATE", "DECLARE", "DEFAULT", "DEFAULTS",
		"DEFINITION", "DELETE", "DENSERANK", "DENSE_RANK", "DESCRIBE",
		"DESCRIPTOR", "DETERMINISTIC", "DIAGNOSTICS", "DISABLE", "DISALLOW",
		"DISCONNECT", "DISTINCT", "DO", "DOCUMENT", "DROP", "DSSIZE", "DYNAMIC",
		"EACH", "EDITPROC", "ELSE", "ELSEIF", "ENABLE", "ENCODING",
		"ENCRYPTION", "END", "END-EXEC", "ENDING", "ERASE", "ESCAPE", "EVERY",
		"EXCEPT", "EXCEPTION", "EXCLUDING", "EXCLUSIVE", "EXECUTE", "EXISTS",
		"EXIT", "EXPLAIN", "EXTENDED", "EXTERNAL", "EXTRACT", "FENCED", "FETCH",
		"FIELDPROC", "FILE", "FINAL", "FIRST1", "FOR", "FOREIGN", "FREE",
		"FROM", "FULL", "FUNCTION", "GENERAL", "GENERATED", "GET", "GLOBAL",
		"GO", "GOTO", "GRANT", "GRAPHIC", "GROUP", "HANDLER", "HASH",
		"HASHED_VALUE", "HAVING", "HINT", "HOLD", "HOUR", "HOURS", "IDENTITY",
		"IF", "IMMEDIATE", "IMPORT", "IN", "INCLUDING", "INCLUSIVE",
		"INCREMENT", "INDEX", "INDICATOR", "INDICATORS", "INF", "INFINITY",
		"INHERIT", "INNER", "INOUT", "INSENSITIVE", "INSERT", "INTEGRITY",
		"INTERSECT", "INTO", "IS", "ISNULL", "ISOBID", "ISOLATION", "ITERATE",
		"JAR", "JAVA", "JOIN", "KEEP", "KEY", "LABEL", "LANGUAGE", "LAST3",
		"LATERAL", "LC_CTYPE", "LEAVE", "LEFT", "LIKE", "LIMIT", "LINKTYPE",
		"LOCAL", "LOCALDATE", "LOCALE", "LOCALTIME", "LOCALTIMESTAMP",
		"LOCATOR", "LOCATORS", "LOCK", "LOCKMAX", "LOCKSIZE", "LOOP",
		"MAINTAINED", "MATERIALIZED", "MAXVALUE", "MICROSECOND", "MICROSECONDS",
		"MINUTE", "MINUTES", "MINVALUE", "MODE", "MODIFIES", "MONTH", "MONTHS",
		"NAN", "NEW", "NEW_TABLE", "NEXTVAL", "NO", "NOCACHE", "NOCYCLE",
		"NODENAME", "NODENUMBER", "NOMAXVALUE", "NOMINVALUE", "NONE", "NOORDER",
		"NORMALIZED", "NOT2", "NOTNULL", "NULL", "NULLS", "NUMPARTS", "OBID",
		"OF", "OFF", "OFFSET", "OLD", "OLD_TABLE", "ON", "OPEN", "OPTIMIZATION",
		"OPTIMIZE", "OPTION", "OR", "ORDER", "OUT", "OUTER", "OVER",
		"OVERRIDING", "PACKAGE", "PADDED", "PAGESIZE", "PARAMETER", "PART",
		"PARTITION", "PARTITIONED", "PARTITIONING", "PARTITIONS", "PASSWORD",
		"PATH", "PERCENT", "PIECESIZE", "PLAN", "POSITION", "PRECISION",
		"PREPARE", "PREVVAL", "PRIMARY", "PRIQTY", "PRIVILEGES", "PROCEDURE",
		"PROGRAM", "PSID", "PUBLIC", "QUERY", "QUERYNO", "RANGE", "RANK",
		"READ", "READS", "RECOVERY", "REFERENCES", "REFERENCING", "REFRESH",
		"RELEASE", "RENAME", "REPEAT", "RESET", "RESIGNAL", "RESTART",
		"RESTRICT", "RESULT", "RESULT_SET_LOCATOR", "RETURN", "RETURNS",
		"REVOKE", "RIGHT", "ROLE", "ROLLBACK", "ROUND_CEILING", "ROUND_DOWN",
		"ROUND_FLOOR", "ROUND_HALF_DOWN", "ROUND_HALF_EVEN", "ROUND_HALF_UP",
		"ROUND_UP", "ROUTINE", "ROW", "ROWNUMBER", "ROWS", "ROWSET",
		"ROW_NUMBER", "RRN", "RUN", "SAVEPOINT", "SCHEMA", "SCRATCHPAD",
		"SCROLL", "SEARCH", "SECOND", "SECONDS", "SECQTY", "SECURITY", "SELECT",
		"SENSITIVE", "SEQUENCE", "SESSION", "SESSION_USER", "SET", "SIGNAL",
		"SIMPLE", "SNAN", "SOME", "SOURCE", "SPECIFIC", "SQL", "SQLID",
		"STACKED", "STANDARD", "START", "STARTING", "STATEMENT", "STATIC",
		"STATMENT", "STAY", "STOGROUP", "STORES", "STYLE", "SUBSTRING",
		"SUMMARY", "SYNONYM", "SYSFUN", "SYSIBM", "SYSPROC", "SYSTEM",
		"SYSTEM_USER", "TABLE", "TABLESPACE", "THEN", "TO", "TRANSACTION",
		"TRIGGER", "TRIM", "TRUNCATE", "TYPE", "UNDO", "UNION", "UNIQUE",
		"UNTIL", "UPDATE", "USAGE", "USER", "USING", "VALIDPROC", "VALUE",
		"VALUES", "VARIABLE", "VARIANT", "VCAT", "VERSION", "VIEW", "VOLATILE",
		"VOLUMES", "WHEN", "WHENEVER", "WHERE", "WHILE", "WITH", "WITHOUT",
		"WLM", "WRITE", "XMLELEMENT", "XMLEXISTS", "XMLNAMESPACES", "YEAR",
		"YEARS"
	],
	Us = ["ARRAY", "BIGINT", "BINARY", "BLOB", "BOOLEAN", "CCSID", "CHAR",
		"CHARACTER", "CLOB", "DATE", "DATETIME", "DBCLOB", "DEC", "DECIMAL",
		"DOUBLE", "DOUBLE PRECISION", "FLOAT", "FLOAT4", "FLOAT8", "GRAPHIC",
		"INT", "INT2", "INT4", "INT8", "INTEGER", "INTERVAL", "LONG VARCHAR",
		"LONG VARGRAPHIC", "NCHAR", "NCHR", "NCLOB", "NVARCHAR", "NUMERIC",
		"SMALLINT", "REAL", "TIME", "TIMESTAMP", "VARBINARY", "VARCHAR",
		"VARGRAPHIC"
	],
	ms = v(["SELECT [ALL | DISTINCT]"]),
	hs = v(["WITH", "FROM", "WHERE", "GROUP BY", "HAVING", "PARTITION BY",
		"ORDER BY [INPUT SEQUENCE]", "LIMIT", "OFFSET", "FETCH NEXT",
		"FOR UPDATE [OF]", "FOR {READ | FETCH} ONLY",
		"FOR {RR | CS | UR | RS} [USE AND KEEP {SHARE | UPDATE | EXCLUSIVE} LOCKS]",
		"WAIT FOR OUTCOME", "SKIP LOCKED DATA", "INTO", "INSERT INTO",
		"VALUES", "SET", "MERGE INTO", "WHEN [NOT] MATCHED [THEN]",
		"UPDATE SET", "INSERT"
	]),
	rr = v(["CREATE [GLOBAL TEMPORARY | EXTERNAL] TABLE [IF NOT EXISTS]"]),
	Xt = v(["CREATE [OR REPLACE] VIEW", "UPDATE", "WHERE CURRENT OF",
		"WITH {RR | RS | CS | UR}", "DELETE FROM", "DROP TABLE [IF EXISTS]",
		"ALTER TABLE", "ADD [COLUMN]", "DROP [COLUMN]", "RENAME COLUMN",
		"ALTER [COLUMN]", "SET DATA TYPE", "SET NOT NULL",
		"DROP {DEFAULT | GENERATED | NOT NULL}", "TRUNCATE [TABLE]",
		"ALLOCATE", "ALTER AUDIT POLICY", "ALTER BUFFERPOOL",
		"ALTER DATABASE PARTITION GROUP", "ALTER DATABASE",
		"ALTER EVENT MONITOR", "ALTER FUNCTION", "ALTER HISTOGRAM TEMPLATE",
		"ALTER INDEX", "ALTER MASK", "ALTER METHOD", "ALTER MODULE",
		"ALTER NICKNAME", "ALTER PACKAGE", "ALTER PERMISSION",
		"ALTER PROCEDURE", "ALTER SCHEMA", "ALTER SECURITY LABEL COMPONENT",
		"ALTER SECURITY POLICY", "ALTER SEQUENCE", "ALTER SERVER",
		"ALTER SERVICE CLASS", "ALTER STOGROUP", "ALTER TABLESPACE",
		"ALTER THRESHOLD", "ALTER TRIGGER", "ALTER TRUSTED CONTEXT",
		"ALTER TYPE", "ALTER USAGE LIST", "ALTER USER MAPPING",
		"ALTER VIEW", "ALTER WORK ACTION SET", "ALTER WORK CLASS SET",
		"ALTER WORKLOAD", "ALTER WRAPPER", "ALTER XSROBJECT",
		"ALTER STOGROUP", "ALTER TABLESPACE", "ALTER TRIGGER",
		"ALTER TRUSTED CONTEXT", "ALTER VIEW",
		"ASSOCIATE [RESULT SET] {LOCATOR | LOCATORS}", "AUDIT",
		"BEGIN DECLARE SECTION", "CALL", "CLOSE", "COMMENT ON",
		"COMMIT [WORK]", "CONNECT", "CREATE [OR REPLACE] [PUBLIC] ALIAS",
		"CREATE AUDIT POLICY", "CREATE BUFFERPOOL",
		"CREATE DATABASE PARTITION GROUP", "CREATE EVENT MONITOR",
		"CREATE [OR REPLACE] FUNCTION", "CREATE FUNCTION MAPPING",
		"CREATE HISTOGRAM TEMPLATE", "CREATE [UNIQUE] INDEX",
		"CREATE INDEX EXTENSION", "CREATE [OR REPLACE] MASK",
		"CREATE [SPECIFIC] METHOD", "CREATE [OR REPLACE] MODULE",
		"CREATE [OR REPLACE] NICKNAME", "CREATE [OR REPLACE] PERMISSION",
		"CREATE [OR REPLACE] PROCEDURE", "CREATE ROLE", "CREATE SCHEMA",
		"CREATE SECURITY LABEL [COMPONENT]", "CREATE SECURITY POLICY",
		"CREATE [OR REPLACE] SEQUENCE", "CREATE SERVICE CLASS",
		"CREATE SERVER", "CREATE STOGROUP", "CREATE SYNONYM",
		"CREATE [LARGE | REGULAR | {SYSTEM | USER} TEMPORARY] TABLESPACE",
		"CREATE THRESHOLD", "CREATE {TRANSFORM | TRANSFORMS} FOR",
		"CREATE [OR REPLACE] TRIGGER", "CREATE TRUSTED CONTEXT",
		"CREATE [OR REPLACE] TYPE", "CREATE TYPE MAPPING",
		"CREATE USAGE LIST", "CREATE USER MAPPING FOR",
		"CREATE [OR REPLACE] VARIABLE", "CREATE WORK ACTION SET",
		"CREATE WORK CLASS SET", "CREATE WORKLOAD", "CREATE WRAPPER",
		"DECLARE", "DECLARE GLOBAL TEMPORARY TABLE",
		"DESCRIBE [INPUT | OUTPUT]", "DISCONNECT", "DROP [PUBLIC] ALIAS",
		"DROP AUDIT POLICY", "DROP BUFFERPOOL",
		"DROP DATABASE PARTITION GROUP", "DROP EVENT MONITOR",
		"DROP [SPECIFIC] FUNCTION", "DROP FUNCTION MAPPING",
		"DROP HISTOGRAM TEMPLATE", "DROP INDEX [EXTENSION]", "DROP MASK",
		"DROP [SPECIFIC] METHOD", "DROP MODULE", "DROP NICKNAME",
		"DROP PACKAGE", "DROP PERMISSION", "DROP [SPECIFIC] PROCEDURE",
		"DROP ROLE", "DROP SCHEMA", "DROP SECURITY LABEL [COMPONENT]",
		"DROP SECURITY POLICY", "DROP SEQUENCE", "DROP SERVER",
		"DROP SERVICE CLASS", "DROP STOGROUP", "DROP TABLE HIERARCHY",
		"DROP {TABLESPACE | TABLESPACES}", "DROP {TRANSFORM | TRANSFORMS}",
		"DROP THRESHOLD", "DROP TRIGGER", "DROP TRUSTED CONTEXT",
		"DROP TYPE [MAPPING]", "DROP USAGE LIST", "DROP USER MAPPING FOR",
		"DROP VARIABLE", "DROP VIEW [HIERARCHY]",
		"DROP WORK {ACTION | CLASS} SET", "DROP WORKLOAD", "DROP WRAPPER",
		"DROP XSROBJECT", "END DECLARE SECTION", "EXECUTE [IMMEDIATE]",
		"EXPLAIN {PLAN [SECTION] | ALL}", "FETCH [FROM]",
		"FLUSH {BUFFERPOOL | BUFFERPOOLS} ALL", "FLUSH EVENT MONITOR",
		"FLUSH FEDERATED CACHE", "FLUSH OPTIMIZATION PROFILE CACHE",
		"FLUSH PACKAGE CACHE [DYNAMIC]",
		"FLUSH AUTHENTICATION CACHE [FOR ALL]", "FREE LOCATOR",
		"GET DIAGNOSTICS", "GOTO", "GRANT", "INCLUDE", "ITERATE", "LEAVE",
		"LOCK TABLE", "LOOP", "OPEN", "PIPE", "PREPARE", "REFRESH TABLE",
		"RELEASE", "RELEASE [TO] SAVEPOINT",
		"RENAME [TABLE | INDEX | STOGROUP | TABLESPACE]", "REPEAT",
		"RESIGNAL", "RETURN", "REVOKE", "ROLLBACK [WORK] [TO SAVEPOINT]",
		"SAVEPOINT", "SET COMPILATION ENVIRONMENT", "SET CONNECTION",
		"SET CURRENT", "SET ENCRYPTION PASSWORD", "SET EVENT MONITOR STATE",
		"SET INTEGRITY", "SET PASSTHRU", "SET PATH", "SET ROLE",
		"SET SCHEMA", "SET SERVER OPTION",
		"SET {SESSION AUTHORIZATION | SESSION_USER}", "SET USAGE LIST",
		"SIGNAL", "TRANSFER OWNERSHIP OF",
		"WHENEVER {NOT FOUND | SQLERROR | SQLWARNING}", "WHILE"
	]),
	Gs = v(["UNION [ALL]", "EXCEPT [ALL]", "INTERSECT [ALL]"]),
	gs = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN"
	]),
	Hs = v(["ON DELETE", "ON UPDATE", "SET NULL", "{ROWS | RANGE} BETWEEN"]),
	bs = {
		name: "db2",
		tokenizerOptions: {
			reservedSelect: ms,
			reservedClauses: [...hs, ...rr, ...Xt],
			reservedSetOperations: Gs,
			reservedJoins: gs,
			reservedPhrases: Hs,
			reservedKeywords: Ms,
			reservedDataTypes: Us,
			reservedFunctionNames: ps,
			extraParens: ["[]"],
			stringTypes: [{
				quote: "''-qq",
				prefixes: ["G", "N", "U&"]
			}, {
				quote: "''-raw",
				prefixes: ["X", "BX", "GX", "UX"],
				requirePrefix: !0
			}],
			identTypes: ['""-qq'],
			identChars: {
				first: "@#$",
				rest: "@#$"
			},
			paramTypes: {
				positional: !0,
				named: [":"]
			},
			paramChars: {
				first: "@#$",
				rest: "@#$"
			},
			operators: ["**", "%", "|", "&", "^", "~", "¬=", "¬>", "¬<", "!>",
				"!<", "^=", "^>", "^<", "||", "->", "=>"
			]
		},
		formatOptions: {
			onelineClauses: [...rr, ...Xt],
			tabularOnelineClauses: Xt
		}
	},
	ys = ["ARRAY_AGG", "AVG", "CORR", "CORRELATION", "COUNT", "COUNT_BIG",
		"COVAR_POP", "COVARIANCE", "COVAR", "COVAR_SAMP", "COVARIANCE_SAMP",
		"EVERY", "GROUPING", "JSON_ARRAYAGG", "JSON_OBJECTAGG", "LISTAGG",
		"MAX", "MEDIAN", "MIN", "PERCENTILE_CONT", "PERCENTILE_DISC",
		"REGR_AVGX", "REGR_AVGY", "REGR_COUNT", "REGR_INTERCEPT", "REGR_R2",
		"REGR_SLOPE", "REGR_SXX", "REGR_SXY", "REGR_SYY", "SOME", "STDDEV_POP",
		"STDDEV", "STDDEV_SAMP", "SUM", "VAR_POP", "VARIANCE", "VAR",
		"VAR_SAMP", "VARIANCE_SAMP", "XMLAGG", "XMLGROUP", "ABS", "ABSVAL",
		"ACOS", "ADD_DAYS", "ADD_HOURS", "ADD_MINUTES", "ADD_MONTHS",
		"ADD_SECONDS", "ADD_YEARS", "ANTILOG", "ARRAY_MAX_CARDINALITY",
		"ARRAY_TRIM", "ASCII", "ASIN", "ATAN", "ATAN2", "ATANH",
		"BASE64_DECODE", "BASE64_ENCODE", "BIT_LENGTH", "BITAND", "BITANDNOT",
		"BITNOT", "BITOR", "BITXOR", "BSON_TO_JSON", "CARDINALITY", "CEIL",
		"CEILING", "CHAR_LENGTH", "CHARACTER_LENGTH", "CHR", "COALESCE",
		"COMPARE_DECFLOAT", "CONCAT", "CONTAINS", "COS", "COSH", "COT",
		"CURDATE", "CURTIME", "DATABASE", "DATAPARTITIONNAME",
		"DATAPARTITIONNUM", "DAY", "DAYNAME", "DAYOFMONTH", "DAYOFWEEK_ISO",
		"DAYOFWEEK", "DAYOFYEAR", "DAYS", "DBPARTITIONNAME", "DBPARTITIONNUM",
		"DECFLOAT_FORMAT", "DECFLOAT_SORTKEY", "DECRYPT_BINARY", "DECRYPT_BIT",
		"DECRYPT_CHAR", "DECRYPT_DB", "DEGREES", "DIFFERENCE", "DIGITS",
		"DLCOMMENT", "DLLINKTYPE", "DLURLCOMPLETE", "DLURLPATH",
		"DLURLPATHONLY", "DLURLSCHEME", "DLURLSERVER", "DLVALUE",
		"DOUBLE_PRECISION", "DOUBLE", "ENCRPYT", "ENCRYPT_AES",
		"ENCRYPT_AES256", "ENCRYPT_RC2", "ENCRYPT_TDES", "EXP", "EXTRACT",
		"FIRST_DAY", "FLOOR", "GENERATE_UNIQUE", "GET_BLOB_FROM_FILE",
		"GET_CLOB_FROM_FILE", "GET_DBCLOB_FROM_FILE", "GET_XML_FILE", "GETHINT",
		"GREATEST", "HASH_MD5", "HASH_ROW", "HASH_SHA1", "HASH_SHA256",
		"HASH_SHA512", "HASH_VALUES", "HASHED_VALUE", "HEX", "HEXTORAW", "HOUR",
		"HTML_ENTITY_DECODE", "HTML_ENTITY_ENCODE", "HTTP_DELETE_BLOB",
		"HTTP_DELETE", "HTTP_GET_BLOB", "HTTP_GET", "HTTP_PATCH_BLOB",
		"HTTP_PATCH", "HTTP_POST_BLOB", "HTTP_POST", "HTTP_PUT_BLOB",
		"HTTP_PUT", "IDENTITY_VAL_LOCAL", "IFNULL", "INSERT", "INSTR",
		"INTERPRET", "ISFALSE", "ISNOTFALSE", "ISNOTTRUE", "ISTRUE",
		"JSON_ARRAY", "JSON_OBJECT", "JSON_QUERY", "JSON_TO_BSON",
		"JSON_UPDATE", "JSON_VALUE", "JULIAN_DAY", "LAND", "LAST_DAY", "LCASE",
		"LEAST", "LEFT", "LENGTH", "LN", "LNOT", "LOCATE_IN_STRING", "LOCATE",
		"LOG10", "LOR", "LOWER", "LPAD", "LTRIM", "MAX_CARDINALITY", "MAX",
		"MICROSECOND", "MIDNIGHT_SECONDS", "MIN", "MINUTE", "MOD", "MONTH",
		"MONTHNAME", "MONTHS_BETWEEN", "MQREAD", "MQREADCLOB", "MQRECEIVE",
		"MQRECEIVECLOB", "MQSEND", "MULTIPLY_ALT", "NEXT_DAY",
		"NORMALIZE_DECFLOAT", "NOW", "NULLIF", "NVL", "OCTET_LENGTH", "OVERLAY",
		"PI", "POSITION", "POSSTR", "POW", "POWER", "QUANTIZE", "QUARTER",
		"RADIANS", "RAISE_ERROR", "RANDOM", "RAND", "REGEXP_COUNT",
		"REGEXP_INSTR", "REGEXP_REPLACE", "REGEXP_SUBSTR", "REPEAT", "REPLACE",
		"RID", "RIGHT", "ROUND_TIMESTAMP", "ROUND", "RPAD", "RRN", "RTRIM",
		"SCORE", "SECOND", "SIGN", "SIN", "SINH", "SOUNDEX", "SPACE", "SQRT",
		"STRIP", "STRLEFT", "STRPOS", "STRRIGHT", "SUBSTR", "SUBSTRING",
		"TABLE_NAME", "TABLE_SCHEMA", "TAN", "TANH", "TIMESTAMP_FORMAT",
		"TIMESTAMP_ISO", "TIMESTAMPDIFF_BIG", "TIMESTAMPDIFF", "TO_CHAR",
		"TO_CLOB", "TO_DATE", "TO_NUMBER", "TO_TIMESTAMP", "TOTALORDER",
		"TRANSLATE", "TRIM_ARRAY", "TRIM", "TRUNC_TIMESTAMP", "TRUNC",
		"TRUNCATE", "UCASE", "UPPER", "URL_DECODE", "URL_ENCODE", "VALUE",
		"VARBINARY_FORMAT", "VARCHAR_BIT_FORMAT", "VARCHAR_FORMAT_BINARY",
		"VARCHAR_FORMAT", "VERIFY_GROUP_FOR_USER", "WEEK_ISO", "WEEK", "WRAP",
		"XMLATTRIBUTES", "XMLCOMMENT", "XMLCONCAT", "XMLDOCUMENT", "XMLELEMENT",
		"XMLFOREST", "XMLNAMESPACES", "XMLPARSE", "XMLPI", "XMLROW",
		"XMLSERIALIZE", "XMLTEXT", "XMLVALIDATE", "XOR", "XSLTRANSFORM", "YEAR",
		"ZONED", "BASE_TABLE", "HTTP_DELETE_BLOB_VERBOSE",
		"HTTP_DELETE_VERBOSE", "HTTP_GET_BLOB_VERBOSE", "HTTP_GET_VERBOSE",
		"HTTP_PATCH_BLOB_VERBOSE", "HTTP_PATCH_VERBOSE",
		"HTTP_POST_BLOB_VERBOSE", "HTTP_POST_VERBOSE", "HTTP_PUT_BLOB_VERBOSE",
		"HTTP_PUT_VERBOSE", "JSON_TABLE", "MQREADALL", "MQREADALLCLOB",
		"MQRECEIVEALL", "MQRECEIVEALLCLOB", "XMLTABLE", "UNPACK", "CUME_DIST",
		"DENSE_RANK", "FIRST_VALUE", "LAG", "LAST_VALUE", "LEAD", "NTH_VALUE",
		"NTILE", "PERCENT_RANK", "RANK", "RATIO_TO_REPORT", "ROW_NUMBER",
		"CAST"
	],
	Bs = ["ABSENT", "ACCORDING", "ACCTNG", "ACTION", "ACTIVATE", "ADD", "ALIAS",
		"ALL", "ALLOCATE", "ALLOW", "ALTER", "AND", "ANY", "APPEND", "APPLNAME",
		"ARRAY", "ARRAY_AGG", "ARRAY_TRIM", "AS", "ASC", "ASENSITIVE",
		"ASSOCIATE", "ATOMIC", "ATTACH", "ATTRIBUTES", "AUTHORIZATION",
		"AUTONOMOUS", "BEFORE", "BEGIN", "BETWEEN", "BIND", "BSON",
		"BUFFERPOOL", "BY", "CACHE", "CALL", "CALLED", "CARDINALITY", "CASE",
		"CAST", "CHECK", "CL", "CLOSE", "CLUSTER", "COLLECT", "COLLECTION",
		"COLUMN", "COMMENT", "COMMIT", "COMPACT", "COMPARISONS", "COMPRESS",
		"CONCAT", "CONCURRENT", "CONDITION", "CONNECT", "CONNECT_BY_ROOT",
		"CONNECTION", "CONSTANT", "CONSTRAINT", "CONTAINS", "CONTENT",
		"CONTINUE", "COPY", "COUNT", "COUNT_BIG", "CREATE", "CREATEIN", "CROSS",
		"CUBE", "CUME_DIST", "CURRENT", "CURRENT_DATE", "CURRENT_PATH",
		"CURRENT_SCHEMA", "CURRENT_SERVER", "CURRENT_TIME", "CURRENT_TIMESTAMP",
		"CURRENT_TIMEZONE", "CURRENT_USER", "CURSOR", "CYCLE", "DATABASE",
		"DATAPARTITIONNAME", "DATAPARTITIONNUM", "DAY", "DAYS", "DB2GENERAL",
		"DB2GENRL", "DB2SQL", "DBINFO", "DBPARTITIONNAME", "DBPARTITIONNUM",
		"DEACTIVATE", "DEALLOCATE", "DECLARE", "DEFAULT", "DEFAULTS", "DEFER",
		"DEFINE", "DEFINITION", "DELETE", "DELETING", "DENSE_RANK", "DENSERANK",
		"DESC", "DESCRIBE", "DESCRIPTOR", "DETACH", "DETERMINISTIC",
		"DIAGNOSTICS", "DISABLE", "DISALLOW", "DISCONNECT", "DISTINCT", "DO",
		"DOCUMENT", "DROP", "DYNAMIC", "EACH", "ELSE", "ELSEIF", "EMPTY",
		"ENABLE", "ENCODING", "ENCRYPTION", "END", "END-EXEC", "ENDING",
		"ENFORCED", "ERROR", "ESCAPE", "EVERY", "EXCEPT", "EXCEPTION",
		"EXCLUDING", "EXCLUSIVE", "EXECUTE", "EXISTS", "EXIT", "EXTEND",
		"EXTERNAL", "EXTRACT", "FALSE", "FENCED", "FETCH", "FIELDPROC", "FILE",
		"FINAL", "FIRST_VALUE", "FOR", "FOREIGN", "FORMAT", "FREE", "FREEPAGE",
		"FROM", "FULL", "FUNCTION", "GBPCACHE", "GENERAL", "GENERATED", "GET",
		"GLOBAL", "GO", "GOTO", "GRANT", "GROUP", "HANDLER", "HASH", "HASH_ROW",
		"HASHED_VALUE", "HAVING", "HINT", "HOLD", "HOUR", "HOURS", "IDENTITY",
		"IF", "IGNORE", "IMMEDIATE", "IMPLICITLY", "IN", "INCLUDE", "INCLUDING",
		"INCLUSIVE", "INCREMENT", "INDEX", "INDEXBP", "INDICATOR", "INF",
		"INFINITY", "INHERIT", "INLINE", "INNER", "INOUT", "INSENSITIVE",
		"INSERT", "INSERTING", "INTEGRITY", "INTERPRET", "INTERSECT", "INTO",
		"IS", "ISNULL", "ISOLATION", "ITERATE", "JAVA", "JOIN", "JSON",
		"JSON_ARRAY", "JSON_ARRAYAGG", "JSON_EXISTS", "JSON_OBJECT",
		"JSON_OBJECTAGG", "JSON_QUERY", "JSON_TABLE", "JSON_VALUE", "KEEP",
		"KEY", "KEYS", "LABEL", "LAG", "LANGUAGE", "LAST_VALUE", "LATERAL",
		"LEAD", "LEAVE", "LEFT", "LEVEL2", "LIKE", "LIMIT", "LINKTYPE",
		"LISTAGG", "LOCAL", "LOCALDATE", "LOCALTIME", "LOCALTIMESTAMP",
		"LOCATION", "LOCATOR", "LOCK", "LOCKSIZE", "LOG", "LOGGED", "LOOP",
		"MAINTAINED", "MASK", "MATCHED", "MATERIALIZED", "MAXVALUE", "MERGE",
		"MICROSECOND", "MICROSECONDS", "MINPCTUSED", "MINUTE", "MINUTES",
		"MINVALUE", "MIRROR", "MIXED", "MODE", "MODIFIES", "MONTH", "MONTHS",
		"NAMESPACE", "NAN", "NATIONAL", "NCHAR", "NCLOB", "NESTED", "NEW",
		"NEW_TABLE", "NEXTVAL", "NO", "NOCACHE", "NOCYCLE", "NODENAME",
		"NODENUMBER", "NOMAXVALUE", "NOMINVALUE", "NONE", "NOORDER",
		"NORMALIZED", "NOT", "NOTNULL", "NTH_VALUE", "NTILE", "NULL", "NULLS",
		"NVARCHAR", "OBID", "OBJECT", "OF", "OFF", "OFFSET", "OLD", "OLD_TABLE",
		"OMIT", "ON", "ONLY", "OPEN", "OPTIMIZE", "OPTION", "OR", "ORDER",
		"ORDINALITY", "ORGANIZE", "OUT", "OUTER", "OVER", "OVERLAY",
		"OVERRIDING", "PACKAGE", "PADDED", "PAGE", "PAGESIZE", "PARAMETER",
		"PART", "PARTITION", "PARTITIONED", "PARTITIONING", "PARTITIONS",
		"PASSING", "PASSWORD", "PATH", "PCTFREE", "PERCENT_RANK",
		"PERCENTILE_CONT", "PERCENTILE_DISC", "PERIOD", "PERMISSION",
		"PIECESIZE", "PIPE", "PLAN", "POSITION", "PREPARE", "PREVVAL",
		"PRIMARY", "PRIOR", "PRIQTY", "PRIVILEGES", "PROCEDURE", "PROGRAM",
		"PROGRAMID", "QUERY", "RANGE", "RANK", "RATIO_TO_REPORT", "RCDFMT",
		"READ", "READS", "RECOVERY", "REFERENCES", "REFERENCING", "REFRESH",
		"REGEXP_LIKE", "RELEASE", "RENAME", "REPEAT", "RESET", "RESIGNAL",
		"RESTART", "RESULT", "RESULT_SET_LOCATOR", "RETURN", "RETURNING",
		"RETURNS", "REVOKE", "RID", "RIGHT", "ROLLBACK", "ROLLUP", "ROUTINE",
		"ROW", "ROW_NUMBER", "ROWNUMBER", "ROWS", "RRN", "RUN", "SAVEPOINT",
		"SBCS", "SCALAR", "SCHEMA", "SCRATCHPAD", "SCROLL", "SEARCH", "SECOND",
		"SECONDS", "SECQTY", "SECURED", "SELECT", "SENSITIVE", "SEQUENCE",
		"SESSION", "SESSION_USER", "SET", "SIGNAL", "SIMPLE", "SKIP", "SNAN",
		"SOME", "SOURCE", "SPECIFIC", "SQL", "SQLID", "SQLIND_DEFAULT",
		"SQLIND_UNASSIGNED", "STACKED", "START", "STARTING", "STATEMENT",
		"STATIC", "STOGROUP", "SUBSTRING", "SUMMARY", "SYNONYM", "SYSTEM_TIME",
		"SYSTEM_USER", "TABLE", "TABLESPACE", "TABLESPACES", "TAG", "THEN",
		"THREADSAFE", "TO", "TRANSACTION", "TRANSFER", "TRIGGER", "TRIM",
		"TRIM_ARRAY", "TRUE", "TRUNCATE", "TRY_CAST", "TYPE", "UNDO", "UNION",
		"UNIQUE", "UNIT", "UNKNOWN", "UNNEST", "UNTIL", "UPDATE", "UPDATING",
		"URI", "USAGE", "USE", "USER", "USERID", "USING", "VALUE", "VALUES",
		"VARIABLE", "VARIANT", "VCAT", "VERSION", "VERSIONING", "VIEW",
		"VOLATILE", "WAIT", "WHEN", "WHENEVER", "WHERE", "WHILE", "WITH",
		"WITHIN", "WITHOUT", "WRAPPED", "WRAPPER", "WRITE", "WRKSTNNAME",
		"XMLAGG", "XMLATTRIBUTES", "XMLCAST", "XMLCOMMENT", "XMLCONCAT",
		"XMLDOCUMENT", "XMLELEMENT", "XMLFOREST", "XMLGROUP", "XMLNAMESPACES",
		"XMLPARSE", "XMLPI", "XMLROW", "XMLSERIALIZE", "XMLTABLE", "XMLTEXT",
		"XMLVALIDATE", "XSLTRANSFORM", "XSROBJECT", "YEAR", "YEARS", "YES",
		"ZONE"
	],
	vs = ["ARRAY", "BIGINT", "BINARY", "BIT", "BLOB", "BOOLEAN", "CCSID",
		"CHAR", "CHARACTER", "CLOB", "DATA", "DATALINK", "DATE", "DBCLOB",
		"DECFLOAT", "DECIMAL", "DEC", "DOUBLE", "DOUBLE PRECISION", "FLOAT",
		"GRAPHIC", "INT", "INTEGER", "LONG", "NUMERIC", "REAL", "ROWID",
		"SMALLINT", "TIME", "TIMESTAMP", "VARBINARY", "VARCHAR", "VARGRAPHIC",
		"XML"
	],
	Fs = v(["SELECT [ALL | DISTINCT]"]),
	Ys = v(["WITH [RECURSIVE]", "INTO", "FROM", "WHERE", "GROUP BY", "HAVING",
		"PARTITION BY", "ORDER [SIBLINGS] BY [INPUT SEQUENCE]", "LIMIT",
		"OFFSET", "FETCH {FIRST | NEXT}", "FOR UPDATE [OF]",
		"FOR READ ONLY", "OPTIMIZE FOR", "INSERT INTO", "VALUES", "SET",
		"MERGE INTO", "WHEN [NOT] MATCHED [THEN]", "UPDATE SET", "DELETE",
		"INSERT", "FOR SYSTEM NAME"
	]),
	Rr = v(["CREATE [OR REPLACE] TABLE"]),
	kt = v(["CREATE [OR REPLACE] [RECURSIVE] VIEW", "UPDATE",
		"WHERE CURRENT OF", "WITH {NC | RR | RS | CS | UR}", "DELETE FROM",
		"DROP TABLE", "ALTER TABLE", "ADD [COLUMN]", "ALTER [COLUMN]",
		"DROP [COLUMN]", "SET DATA TYPE",
		"SET {GENERATED ALWAYS | GENERATED BY DEFAULT}", "SET NOT NULL",
		"SET {NOT HIDDEN | IMPLICITLY HIDDEN}", "SET FIELDPROC",
		"DROP {DEFAULT | NOT NULL | GENERATED | IDENTITY | ROW CHANGE TIMESTAMP | FIELDPROC}",
		"TRUNCATE [TABLE]", "SET [CURRENT] SCHEMA", "SET CURRENT_SCHEMA",
		"ALLOCATE CURSOR", "ALLOCATE [SQL] DESCRIPTOR [LOCAL | GLOBAL] SQL",
		"ALTER [SPECIFIC] {FUNCTION | PROCEDURE}",
		"ALTER {MASK | PERMISSION | SEQUENCE | TRIGGER}",
		"ASSOCIATE [RESULT SET] {LOCATOR | LOCATORS}",
		"BEGIN DECLARE SECTION", "CALL", "CLOSE",
		"COMMENT ON {ALIAS | COLUMN | CONSTRAINT | INDEX | MASK | PACKAGE | PARAMETER | PERMISSION | SEQUENCE | TABLE | TRIGGER | VARIABLE | XSROBJECT}",
		"COMMENT ON [SPECIFIC] {FUNCTION | PROCEDURE | ROUTINE}",
		"COMMENT ON PARAMETER SPECIFIC {FUNCTION | PROCEDURE | ROUTINE}",
		"COMMENT ON [TABLE FUNCTION] RETURN COLUMN",
		"COMMENT ON [TABLE FUNCTION] RETURN COLUMN SPECIFIC [PROCEDURE | ROUTINE]",
		"COMMIT [WORK] [HOLD]", "CONNECT [TO | RESET] USER",
		"CREATE [OR REPLACE] {ALIAS | FUNCTION | MASK | PERMISSION | PROCEDURE | SEQUENCE | TRIGGER | VARIABLE}",
		"CREATE [ENCODED VECTOR] INDEX",
		"CREATE UNIQUE [WHERE NOT NULL] INDEX", "CREATE SCHEMA",
		"CREATE TYPE", "DEALLOCATE [SQL] DESCRIPTOR [LOCAL | GLOBAL]",
		"DECLARE CURSOR", "DECLARE GLOBAL TEMPORARY TABLE", "DECLARE",
		"DESCRIBE CURSOR", "DESCRIBE INPUT", "DESCRIBE [OUTPUT]",
		"DESCRIBE {PROCEDURE | ROUTINE}", "DESCRIBE TABLE",
		"DISCONNECT ALL [SQL]", "DISCONNECT [CURRENT]",
		"DROP {ALIAS | INDEX | MASK | PACKAGE | PERMISSION | SCHEMA | SEQUENCE | TABLE | TYPE | VARIABLE | XSROBJECT} [IF EXISTS]",
		"DROP [SPECIFIC] {FUNCTION | PROCEDURE | ROUTINE} [IF EXISTS]",
		"END DECLARE SECTION", "EXECUTE [IMMEDIATE]", "FREE LOCATOR",
		"GET [SQL] DESCRIPTOR [LOCAL | GLOBAL]",
		"GET [CURRENT | STACKED] DIAGNOSTICS",
		"GRANT {ALL [PRIVILEGES] | ALTER | EXECUTE} ON {FUNCTION | PROCEDURE | ROUTINE | PACKAGE | SCHEMA | SEQUENCE | TABLE | TYPE | VARIABLE | XSROBJECT}",
		"HOLD LOCATOR", "INCLUDE",
		"LABEL ON {ALIAS | COLUMN | CONSTRAINT | INDEX | MASK | PACKAGE | PERMISSION | SEQUENCE | TABLE | TRIGGER | VARIABLE | XSROBJECT}",
		"LABEL ON [SPECIFIC] {FUNCTION | PROCEDURE | ROUTINE}",
		"LOCK TABLE", "OPEN", "PREPARE", "REFRESH TABLE", "RELEASE",
		"RELEASE [TO] SAVEPOINT", "RENAME [TABLE | INDEX] TO",
		"REVOKE {ALL [PRIVILEGES] | ALTER | EXECUTE} ON {FUNCTION | PROCEDURE | ROUTINE | PACKAGE | SCHEMA | SEQUENCE | TABLE | TYPE | VARIABLE | XSROBJECT}",
		"ROLLBACK [WORK] [HOLD | TO SAVEPOINT]", "SAVEPOINT",
		"SET CONNECTION",
		"SET CURRENT {DEBUG MODE | DECFLOAT ROUNDING MODE | DEGREE | IMPLICIT XMLPARSE OPTION | TEMPORAL SYSTEM_TIME}",
		"SET [SQL] DESCRIPTOR [LOCAL | GLOBAL]", "SET ENCRYPTION PASSWORD",
		"SET OPTION", "SET {[CURRENT [FUNCTION]] PATH | CURRENT_PATH}",
		"SET RESULT SETS [WITH RETURN [TO CALLER | TO CLIENT]]",
		"SET SESSION AUTHORIZATION", "SET SESSION_USER", "SET TRANSACTION",
		"SIGNAL SQLSTATE [VALUE]", "TAG", "TRANSFER OWNERSHIP OF",
		"WHENEVER {NOT FOUND | SQLERROR | SQLWARNING}"
	]),
	Vs = v(["UNION [ALL]", "EXCEPT [ALL]", "INTERSECT [ALL]"]),
	Ws = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"[LEFT | RIGHT] EXCEPTION JOIN", "{INNER | CROSS} JOIN"
	]),
	ws = v(["ON DELETE", "ON UPDATE", "SET NULL", "{ROWS | RANGE} BETWEEN"]),
	$s = {
		name: "db2i",
		tokenizerOptions: {
			reservedSelect: Fs,
			reservedClauses: [...Ys, ...Rr, ...kt],
			reservedSetOperations: Vs,
			reservedJoins: Ws,
			reservedPhrases: ws,
			reservedKeywords: Bs,
			reservedDataTypes: vs,
			reservedFunctionNames: ys,
			nestedBlockComments: !0,
			extraParens: ["[]"],
			stringTypes: [{
				quote: "''-qq",
				prefixes: ["G", "N"]
			}, {
				quote: "''-raw",
				prefixes: ["X", "BX", "GX", "UX"],
				requirePrefix: !0
			}],
			identTypes: ['""-qq'],
			identChars: {
				first: "@#$",
				rest: "@#$"
			},
			paramTypes: {
				positional: !0,
				named: [":"]
			},
			paramChars: {
				first: "@#$",
				rest: "@#$"
			},
			operators: ["**", "¬=", "¬>", "¬<", "!>", "!<", "||", "=>"]
		},
		formatOptions: {
			onelineClauses: [...Rr, ...kt],
			tabularOnelineClauses: kt
		}
	},
	xs = ["ABS", "ACOS", "ASIN", "ATAN", "BIN", "BROUND", "CBRT", "CEIL",
		"CEILING", "CONV", "COS", "DEGREES", "EXP", "FACTORIAL", "FLOOR",
		"GREATEST", "HEX", "LEAST", "LN", "LOG", "LOG10", "LOG2", "NEGATIVE",
		"PI", "PMOD", "POSITIVE", "POW", "POWER", "RADIANS", "RAND", "ROUND",
		"SHIFTLEFT", "SHIFTRIGHT", "SHIFTRIGHTUNSIGNED", "SIGN", "SIN", "SQRT",
		"TAN", "UNHEX", "WIDTH_BUCKET", "ARRAY_CONTAINS", "MAP_KEYS",
		"MAP_VALUES", "SIZE", "SORT_ARRAY", "BINARY", "CAST", "ADD_MONTHS",
		"DATE", "DATE_ADD", "DATE_FORMAT", "DATE_SUB", "DATEDIFF", "DAY",
		"DAYNAME", "DAYOFMONTH", "DAYOFYEAR", "EXTRACT", "FROM_UNIXTIME",
		"FROM_UTC_TIMESTAMP", "HOUR", "LAST_DAY", "MINUTE", "MONTH",
		"MONTHS_BETWEEN", "NEXT_DAY", "QUARTER", "SECOND", "TIMESTAMP",
		"TO_DATE", "TO_UTC_TIMESTAMP", "TRUNC", "UNIX_TIMESTAMP", "WEEKOFYEAR",
		"YEAR", "ASSERT_TRUE", "COALESCE", "IF", "ISNOTNULL", "ISNULL",
		"NULLIF", "NVL", "ASCII", "BASE64", "CHARACTER_LENGTH", "CHR", "CONCAT",
		"CONCAT_WS", "CONTEXT_NGRAMS", "DECODE", "ELT", "ENCODE", "FIELD",
		"FIND_IN_SET", "FORMAT_NUMBER", "GET_JSON_OBJECT", "IN_FILE", "INITCAP",
		"INSTR", "LCASE", "LENGTH", "LEVENSHTEIN", "LOCATE", "LOWER", "LPAD",
		"LTRIM", "NGRAMS", "OCTET_LENGTH", "PARSE_URL", "PRINTF", "QUOTE",
		"REGEXP_EXTRACT", "REGEXP_REPLACE", "REPEAT", "REVERSE", "RPAD",
		"RTRIM", "SENTENCES", "SOUNDEX", "SPACE", "SPLIT", "STR_TO_MAP",
		"SUBSTR", "SUBSTRING", "TRANSLATE", "TRIM", "UCASE", "UNBASE64",
		"UPPER", "MASK", "MASK_FIRST_N", "MASK_HASH", "MASK_LAST_N",
		"MASK_SHOW_FIRST_N", "MASK_SHOW_LAST_N", "AES_DECRYPT", "AES_ENCRYPT",
		"CRC32", "CURRENT_DATABASE", "CURRENT_USER", "HASH", "JAVA_METHOD",
		"LOGGED_IN_USER", "MD5", "REFLECT", "SHA", "SHA1", "SHA2",
		"SURROGATE_KEY", "VERSION", "AVG", "COLLECT_LIST", "COLLECT_SET",
		"CORR", "COUNT", "COVAR_POP", "COVAR_SAMP", "HISTOGRAM_NUMERIC", "MAX",
		"MIN", "NTILE", "PERCENTILE", "PERCENTILE_APPROX", "REGR_AVGX",
		"REGR_AVGY", "REGR_COUNT", "REGR_INTERCEPT", "REGR_R2", "REGR_SLOPE",
		"REGR_SXX", "REGR_SXY", "REGR_SYY", "STDDEV_POP", "STDDEV_SAMP", "SUM",
		"VAR_POP", "VAR_SAMP", "VARIANCE", "EXPLODE", "INLINE", "JSON_TUPLE",
		"PARSE_URL_TUPLE", "POSEXPLODE", "STACK", "LEAD", "LAG", "FIRST_VALUE",
		"LAST_VALUE", "RANK", "ROW_NUMBER", "DENSE_RANK", "CUME_DIST",
		"PERCENT_RANK", "NTILE"
	],
	Xs = ["ADD", "ADMIN", "AFTER", "ANALYZE", "ARCHIVE", "ASC", "BEFORE",
		"BUCKET", "BUCKETS", "CASCADE", "CHANGE", "CLUSTER", "CLUSTERED",
		"CLUSTERSTATUS", "COLLECTION", "COLUMNS", "COMMENT", "COMPACT",
		"COMPACTIONS", "COMPUTE", "CONCATENATE", "CONTINUE", "DATA",
		"DATABASES", "DATETIME", "DAY", "DBPROPERTIES", "DEFERRED", "DEFINED",
		"DELIMITED", "DEPENDENCY", "DESC", "DIRECTORIES", "DIRECTORY",
		"DISABLE", "DISTRIBUTE", "ELEM_TYPE", "ENABLE", "ESCAPED", "EXCLUSIVE",
		"EXPLAIN", "EXPORT", "FIELDS", "FILE", "FILEFORMAT", "FIRST", "FORMAT",
		"FORMATTED", "FUNCTIONS", "HOLD_DDLTIME", "HOUR", "IDXPROPERTIES",
		"IGNORE", "INDEX", "INDEXES", "INPATH", "INPUTDRIVER", "INPUTFORMAT",
		"ITEMS", "JAR", "KEYS", "KEY_TYPE", "LIMIT", "LINES", "LOAD",
		"LOCATION", "LOCK", "LOCKS", "LOGICAL", "LONG", "MAPJOIN",
		"MATERIALIZED", "METADATA", "MINUS", "MINUTE", "MONTH", "MSCK",
		"NOSCAN", "NO_DROP", "OFFLINE", "OPTION", "OUTPUTDRIVER",
		"OUTPUTFORMAT", "OVERWRITE", "OWNER", "PARTITIONED", "PARTITIONS",
		"PLUS", "PRETTY", "PRINCIPALS", "PROTECTION", "PURGE", "READ",
		"READONLY", "REBUILD", "RECORDREADER", "RECORDWRITER", "RELOAD",
		"RENAME", "REPAIR", "REPLACE", "REPLICATION", "RESTRICT", "REWRITE",
		"ROLE", "ROLES", "SCHEMA", "SCHEMAS", "SECOND", "SEMI", "SERDE",
		"SERDEPROPERTIES", "SERVER", "SETS", "SHARED", "SHOW", "SHOW_DATABASE",
		"SKEWED", "SORT", "SORTED", "SSL", "STATISTICS", "STORED",
		"STREAMTABLE", "STRING", "TABLES", "TBLPROPERTIES", "TEMPORARY",
		"TERMINATED", "TINYINT", "TOUCH", "TRANSACTIONS", "UNARCHIVE", "UNDO",
		"UNIONTYPE", "UNLOCK", "UNSET", "UNSIGNED", "URI", "USE", "UTC",
		"UTCTIMESTAMP", "VALUE_TYPE", "VIEW", "WHILE", "YEAR", "AUTOCOMMIT",
		"ISOLATION", "LEVEL", "OFFSET", "SNAPSHOT", "TRANSACTION", "WORK",
		"WRITE", "ABORT", "KEY", "LAST", "NORELY", "NOVALIDATE", "NULLS",
		"RELY", "VALIDATE", "DETAIL", "DOW", "EXPRESSION", "OPERATOR",
		"QUARTER", "SUMMARY", "VECTORIZATION", "WEEK", "YEARS", "MONTHS",
		"WEEKS", "DAYS", "HOURS", "MINUTES", "SECONDS", "TIMESTAMPTZ", "ZONE",
		"ALL", "ALTER", "AND", "AS", "AUTHORIZATION", "BETWEEN", "BOTH", "BY",
		"CASE", "CAST", "COLUMN", "CONF", "CREATE", "CROSS", "CUBE", "CURRENT",
		"CURRENT_DATE", "CURRENT_TIMESTAMP", "CURSOR", "DATABASE", "DELETE",
		"DESCRIBE", "DISTINCT", "DROP", "ELSE", "END", "EXCHANGE", "EXISTS",
		"EXTENDED", "EXTERNAL", "FALSE", "FETCH", "FOLLOWING", "FOR", "FROM",
		"FULL", "FUNCTION", "GRANT", "GROUP", "GROUPING", "HAVING", "IF",
		"IMPORT", "IN", "INNER", "INSERT", "INTERSECT", "INTO", "IS", "JOIN",
		"LATERAL", "LEFT", "LESS", "LIKE", "LOCAL", "MACRO", "MORE", "NONE",
		"NOT", "NULL", "OF", "ON", "OR", "ORDER", "OUT", "OUTER", "OVER",
		"PARTIALSCAN", "PARTITION", "PERCENT", "PRECEDING", "PRESERVE",
		"PROCEDURE", "RANGE", "READS", "REDUCE", "REVOKE", "RIGHT", "ROLLUP",
		"ROW", "ROWS", "SELECT", "SET", "TABLE", "TABLESAMPLE", "THEN", "TO",
		"TRANSFORM", "TRIGGER", "TRUE", "TRUNCATE", "UNBOUNDED", "UNION",
		"UNIQUEJOIN", "UPDATE", "USER", "USING", "UTC_TMESTAMP", "VALUES",
		"WHEN", "WHERE", "WINDOW", "WITH", "COMMIT", "ONLY", "REGEXP", "RLIKE",
		"ROLLBACK", "START", "CACHE", "CONSTRAINT", "FOREIGN", "PRIMARY",
		"REFERENCES", "DAYOFWEEK", "EXTRACT", "FLOOR", "VIEWS", "TIME", "SYNC",
		"TEXTFILE", "SEQUENCEFILE", "ORC", "CSV", "TSV", "PARQUET", "AVRO",
		"RCFILE", "JSONFILE", "INPUTFORMAT", "OUTPUTFORMAT"
	],
	ks = ["ARRAY", "BIGINT", "BINARY", "BOOLEAN", "CHAR", "DATE", "DECIMAL",
		"DOUBLE", "FLOAT", "INT", "INTEGER", "INTERVAL", "MAP", "NUMERIC",
		"PRECISION", "SMALLINT", "STRUCT", "TIMESTAMP", "VARCHAR"
	],
	Ks = v(["SELECT [ALL | DISTINCT]"]),
	Js = v(["WITH", "FROM", "WHERE", "GROUP BY", "HAVING", "WINDOW",
		"PARTITION BY", "ORDER BY", "SORT BY", "CLUSTER BY",
		"DISTRIBUTE BY", "LIMIT", "INSERT INTO [TABLE]", "VALUES", "SET",
		"MERGE INTO", "WHEN [NOT] MATCHED [THEN]", "UPDATE SET",
		"INSERT [VALUES]", "INSERT OVERWRITE [LOCAL] DIRECTORY",
		"LOAD DATA [LOCAL] INPATH", "[OVERWRITE] INTO TABLE"
	]),
	nr = v(["CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS]"]),
	Kt = v(["CREATE [MATERIALIZED] VIEW [IF NOT EXISTS]", "UPDATE",
		"DELETE FROM", "DROP TABLE [IF EXISTS]", "ALTER TABLE", "RENAME TO",
		"TRUNCATE [TABLE]", "ALTER", "CREATE", "USE", "DESCRIBE", "DROP",
		"FETCH", "SHOW", "STORED AS", "STORED BY", "ROW FORMAT"
	]),
	qs = v(["UNION [ALL | DISTINCT]"]),
	Qs = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "LEFT SEMI JOIN"
	]),
	Zs = v(["{ROWS | RANGE} BETWEEN"]),
	js = {
		name: "hive",
		tokenizerOptions: {
			reservedSelect: Ks,
			reservedClauses: [...Js, ...nr, ...Kt],
			reservedSetOperations: qs,
			reservedJoins: Qs,
			reservedPhrases: Zs,
			reservedKeywords: Xs,
			reservedDataTypes: ks,
			reservedFunctionNames: xs,
			extraParens: ["[]"],
			stringTypes: ['""-bs', "''-bs"],
			identTypes: ["``"],
			variableTypes: [{
				quote: "{}",
				prefixes: ["$"],
				requirePrefix: !0
			}],
			operators: ["%", "~", "^", "|", "&", "<=>", "==", "!", "||"]
		},
		formatOptions: {
			onelineClauses: [...nr, ...Kt],
			tabularOnelineClauses: Kt
		}
	};

function yt(E) {
	return E.map((e, T) => {
		const t = E[T + 1] || tt;
		if (FE.SET(e) && t.text === "(") return AE(EE({}, e), {
			type: "RESERVED_FUNCTION_NAME"
		});
		const r = E[T - 1] || tt;
		return FE.VALUES(e) && r.text === "=" ? AE(EE({}, e), {
			type: "RESERVED_FUNCTION_NAME"
		}) : e
	})
}
var zs = ["ACCESSIBLE", "ADD", "ALL", "ALTER", "ANALYZE", "AND", "AS", "ASC",
		"ASENSITIVE", "BEFORE", "BETWEEN", "BOTH", "BY", "CALL", "CASCADE",
		"CASE", "CHANGE", "CHECK", "COLLATE", "COLUMN", "CONDITION",
		"CONSTRAINT", "CONTINUE", "CONVERT", "CREATE", "CROSS", "CURRENT_DATE",
		"CURRENT_ROLE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER",
		"CURSOR", "DATABASE", "DATABASES", "DAY_HOUR", "DAY_MICROSECOND",
		"DAY_MINUTE", "DAY_SECOND", "DECLARE", "DEFAULT", "DELAYED", "DELETE",
		"DELETE_DOMAIN_ID", "DESC", "DESCRIBE", "DETERMINISTIC", "DISTINCT",
		"DISTINCTROW", "DIV", "DO_DOMAIN_IDS", "DROP", "DUAL", "EACH", "ELSE",
		"ELSEIF", "ENCLOSED", "ESCAPED", "EXCEPT", "EXISTS", "EXIT", "EXPLAIN",
		"FALSE", "FETCH", "FOR", "FORCE", "FOREIGN", "FROM", "FULLTEXT",
		"GENERAL", "GRANT", "GROUP", "HAVING", "HIGH_PRIORITY",
		"HOUR_MICROSECOND", "HOUR_MINUTE", "HOUR_SECOND", "IF", "IGNORE",
		"IGNORE_DOMAIN_IDS", "IGNORE_SERVER_IDS", "IN", "INDEX", "INFILE",
		"INNER", "INOUT", "INSENSITIVE", "INSERT", "INTERSECT", "INTERVAL",
		"INTO", "IS", "ITERATE", "JOIN", "KEY", "KEYS", "KILL", "LEADING",
		"LEAVE", "LEFT", "LIKE", "LIMIT", "LINEAR", "LINES", "LOAD",
		"LOCALTIME", "LOCALTIMESTAMP", "LOCK", "LOOP", "LOW_PRIORITY",
		"MASTER_HEARTBEAT_PERIOD", "MASTER_SSL_VERIFY_SERVER_CERT", "MATCH",
		"MAXVALUE", "MINUTE_MICROSECOND", "MINUTE_SECOND", "MOD", "MODIFIES",
		"NATURAL", "NOT", "NO_WRITE_TO_BINLOG", "NULL", "OFFSET", "ON",
		"OPTIMIZE", "OPTION", "OPTIONALLY", "OR", "ORDER", "OUT", "OUTER",
		"OUTFILE", "OVER", "PAGE_CHECKSUM", "PARSE_VCOL_EXPR", "PARTITION",
		"POSITION", "PRIMARY", "PROCEDURE", "PURGE", "RANGE", "READ", "READS",
		"READ_WRITE", "RECURSIVE", "REF_SYSTEM_ID", "REFERENCES", "REGEXP",
		"RELEASE", "RENAME", "REPEAT", "REPLACE", "REQUIRE", "RESIGNAL",
		"RESTRICT", "RETURN", "RETURNING", "REVOKE", "RIGHT", "RLIKE",
		"ROW_NUMBER", "ROWS", "SCHEMA", "SCHEMAS", "SECOND_MICROSECOND",
		"SELECT", "SENSITIVE", "SEPARATOR", "SET", "SHOW", "SIGNAL", "SLOW",
		"SPATIAL", "SPECIFIC", "SQL", "SQLEXCEPTION", "SQLSTATE", "SQLWARNING",
		"SQL_BIG_RESULT", "SQL_CALC_FOUND_ROWS", "SQL_SMALL_RESULT", "SSL",
		"STARTING", "STATS_AUTO_RECALC", "STATS_PERSISTENT",
		"STATS_SAMPLE_PAGES", "STRAIGHT_JOIN", "TABLE", "TERMINATED", "THEN",
		"TO", "TRAILING", "TRIGGER", "TRUE", "UNDO", "UNION", "UNIQUE",
		"UNLOCK", "UNSIGNED", "UPDATE", "USAGE", "USE", "USING", "UTC_DATE",
		"UTC_TIME", "UTC_TIMESTAMP", "VALUES", "WHEN", "WHERE", "WHILE",
		"WINDOW", "WITH", "WRITE", "XOR", "YEAR_MONTH", "ZEROFILL"
	],
	eS = ["BIGINT", "BINARY", "BIT", "BLOB", "CHAR BYTE", "CHAR", "CHARACTER",
		"DATETIME", "DEC", "DECIMAL", "DOUBLE PRECISION", "DOUBLE", "ENUM",
		"FIXED", "FLOAT", "FLOAT4", "FLOAT8", "INT", "INT1", "INT2", "INT3",
		"INT4", "INT8", "INTEGER", "LONG", "LONGBLOB", "LONGTEXT", "MEDIUMBLOB",
		"MEDIUMINT", "MEDIUMTEXT", "MIDDLEINT", "NATIONAL CHAR",
		"NATIONAL VARCHAR", "NUMERIC", "PRECISION", "REAL", "SMALLINT", "TEXT",
		"TIMESTAMP", "TINYBLOB", "TINYINT", "TINYTEXT", "VARBINARY", "VARCHAR",
		"VARCHARACTER", "VARYING", "YEAR"
	],
	ES = ["ADDDATE", "ADD_MONTHS", "BIT_AND", "BIT_OR", "BIT_XOR", "CAST",
		"COUNT", "CUME_DIST", "CURDATE", "CURTIME", "DATE_ADD", "DATE_SUB",
		"DATE_FORMAT", "DECODE", "DENSE_RANK", "EXTRACT", "FIRST_VALUE",
		"GROUP_CONCAT", "JSON_ARRAYAGG", "JSON_OBJECTAGG", "LAG", "LEAD", "MAX",
		"MEDIAN", "MID", "MIN", "NOW", "NTH_VALUE", "NTILE", "POSITION",
		"PERCENT_RANK", "PERCENTILE_CONT", "PERCENTILE_DISC", "RANK",
		"ROW_NUMBER", "SESSION_USER", "STD", "STDDEV", "STDDEV_POP",
		"STDDEV_SAMP", "SUBDATE", "SUBSTR", "SUBSTRING", "SUM", "SYSTEM_USER",
		"TRIM", "TRIM_ORACLE", "VARIANCE", "VAR_POP", "VAR_SAMP", "ABS", "ACOS",
		"ADDTIME", "AES_DECRYPT", "AES_ENCRYPT", "ASIN", "ATAN", "ATAN2",
		"BENCHMARK", "BIN", "BINLOG_GTID_POS", "BIT_COUNT", "BIT_LENGTH",
		"CEIL", "CEILING", "CHARACTER_LENGTH", "CHAR_LENGTH", "CHR",
		"COERCIBILITY", "COLUMN_CHECK", "COLUMN_EXISTS", "COLUMN_LIST",
		"COLUMN_JSON", "COMPRESS", "CONCAT", "CONCAT_OPERATOR_ORACLE",
		"CONCAT_WS", "CONNECTION_ID", "CONV", "CONVERT_TZ", "COS", "COT",
		"CRC32", "DATEDIFF", "DAYNAME", "DAYOFMONTH", "DAYOFWEEK", "DAYOFYEAR",
		"DEGREES", "DECODE_HISTOGRAM", "DECODE_ORACLE", "DES_DECRYPT",
		"DES_ENCRYPT", "ELT", "ENCODE", "ENCRYPT", "EXP", "EXPORT_SET",
		"EXTRACTVALUE", "FIELD", "FIND_IN_SET", "FLOOR", "FORMAT", "FOUND_ROWS",
		"FROM_BASE64", "FROM_DAYS", "FROM_UNIXTIME", "GET_LOCK", "GREATEST",
		"HEX", "IFNULL", "INSTR", "ISNULL", "IS_FREE_LOCK", "IS_USED_LOCK",
		"JSON_ARRAY", "JSON_ARRAY_APPEND", "JSON_ARRAY_INSERT", "JSON_COMPACT",
		"JSON_CONTAINS", "JSON_CONTAINS_PATH", "JSON_DEPTH", "JSON_DETAILED",
		"JSON_EXISTS", "JSON_EXTRACT", "JSON_INSERT", "JSON_KEYS",
		"JSON_LENGTH", "JSON_LOOSE", "JSON_MERGE", "JSON_MERGE_PATCH",
		"JSON_MERGE_PRESERVE", "JSON_QUERY", "JSON_QUOTE", "JSON_OBJECT",
		"JSON_REMOVE", "JSON_REPLACE", "JSON_SET", "JSON_SEARCH", "JSON_TYPE",
		"JSON_UNQUOTE", "JSON_VALID", "JSON_VALUE", "LAST_DAY",
		"LAST_INSERT_ID", "LCASE", "LEAST", "LENGTH", "LENGTHB", "LN",
		"LOAD_FILE", "LOCATE", "LOG", "LOG10", "LOG2", "LOWER", "LPAD",
		"LPAD_ORACLE", "LTRIM", "LTRIM_ORACLE", "MAKEDATE", "MAKETIME",
		"MAKE_SET", "MASTER_GTID_WAIT", "MASTER_POS_WAIT", "MD5", "MONTHNAME",
		"NAME_CONST", "NVL", "NVL2", "OCT", "OCTET_LENGTH", "ORD", "PERIOD_ADD",
		"PERIOD_DIFF", "PI", "POW", "POWER", "QUOTE", "REGEXP_INSTR",
		"REGEXP_REPLACE", "REGEXP_SUBSTR", "RADIANS", "RAND",
		"RELEASE_ALL_LOCKS", "RELEASE_LOCK", "REPLACE_ORACLE", "REVERSE",
		"ROUND", "RPAD", "RPAD_ORACLE", "RTRIM", "RTRIM_ORACLE", "SEC_TO_TIME",
		"SHA", "SHA1", "SHA2", "SIGN", "SIN", "SLEEP", "SOUNDEX", "SPACE",
		"SQRT", "STRCMP", "STR_TO_DATE", "SUBSTR_ORACLE", "SUBSTRING_INDEX",
		"SUBTIME", "SYS_GUID", "TAN", "TIMEDIFF", "TIME_FORMAT", "TIME_TO_SEC",
		"TO_BASE64", "TO_CHAR", "TO_DAYS", "TO_SECONDS", "UCASE", "UNCOMPRESS",
		"UNCOMPRESSED_LENGTH", "UNHEX", "UNIX_TIMESTAMP", "UPDATEXML", "UPPER",
		"UUID", "UUID_SHORT", "VERSION", "WEEKDAY", "WEEKOFYEAR",
		"WSREP_LAST_WRITTEN_GTID", "WSREP_LAST_SEEN_GTID",
		"WSREP_SYNC_WAIT_UPTO_GTID", "YEARWEEK", "COALESCE", "NULLIF"
	],
	tS = v(["SELECT [ALL | DISTINCT | DISTINCTROW]"]),
	TS = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY", "HAVING",
		"PARTITION BY", "ORDER BY", "LIMIT", "OFFSET",
		"FETCH {FIRST | NEXT}",
		"INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE] [INTO]",
		"REPLACE [LOW_PRIORITY | DELAYED] [INTO]", "VALUES",
		"ON DUPLICATE KEY UPDATE", "SET", "RETURNING"
	]),
	Ar = v(["CREATE [OR REPLACE] [TEMPORARY] TABLE [IF NOT EXISTS]"]),
	Jt = v([
		"CREATE [OR REPLACE] [SQL SECURITY DEFINER | SQL SECURITY INVOKER] VIEW [IF NOT EXISTS]",
		"UPDATE [LOW_PRIORITY] [IGNORE]",
		"DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM",
		"DROP [TEMPORARY] TABLE [IF EXISTS]",
		"ALTER [ONLINE] [IGNORE] TABLE [IF EXISTS]",
		"ADD [COLUMN] [IF NOT EXISTS]",
		"{CHANGE | MODIFY} [COLUMN] [IF EXISTS]",
		"DROP [COLUMN] [IF EXISTS]", "RENAME [TO]", "RENAME COLUMN",
		"ALTER [COLUMN]", "{SET | DROP} DEFAULT",
		"SET {VISIBLE | INVISIBLE}", "TRUNCATE [TABLE]", "ALTER DATABASE",
		"ALTER DATABASE COMMENT", "ALTER EVENT", "ALTER FUNCTION",
		"ALTER PROCEDURE", "ALTER SCHEMA", "ALTER SCHEMA COMMENT",
		"ALTER SEQUENCE", "ALTER SERVER", "ALTER USER", "ALTER VIEW",
		"ANALYZE", "ANALYZE TABLE", "BACKUP LOCK", "BACKUP STAGE",
		"BACKUP UNLOCK", "BEGIN", "BINLOG", "CACHE INDEX", "CALL",
		"CHANGE MASTER TO", "CHECK TABLE", "CHECK VIEW", "CHECKSUM TABLE",
		"COMMIT", "CREATE AGGREGATE FUNCTION", "CREATE DATABASE",
		"CREATE EVENT", "CREATE FUNCTION", "CREATE INDEX",
		"CREATE PROCEDURE", "CREATE ROLE", "CREATE SEQUENCE",
		"CREATE SERVER", "CREATE SPATIAL INDEX", "CREATE TRIGGER",
		"CREATE UNIQUE INDEX", "CREATE USER", "DEALLOCATE PREPARE",
		"DESCRIBE", "DROP DATABASE", "DROP EVENT", "DROP FUNCTION",
		"DROP INDEX", "DROP PREPARE", "DROP PROCEDURE", "DROP ROLE",
		"DROP SEQUENCE", "DROP SERVER", "DROP TRIGGER", "DROP USER",
		"DROP VIEW", "EXECUTE", "EXPLAIN", "FLUSH", "GET DIAGNOSTICS",
		"GET DIAGNOSTICS CONDITION", "GRANT", "HANDLER", "HELP",
		"INSTALL PLUGIN", "INSTALL SONAME", "KILL", "LOAD DATA INFILE",
		"LOAD INDEX INTO CACHE", "LOAD XML INFILE", "LOCK TABLE",
		"OPTIMIZE TABLE", "PREPARE", "PURGE BINARY LOGS",
		"PURGE MASTER LOGS", "RELEASE SAVEPOINT", "RENAME TABLE",
		"RENAME USER", "REPAIR TABLE", "REPAIR VIEW", "RESET MASTER",
		"RESET QUERY CACHE", "RESET REPLICA", "RESET SLAVE", "RESIGNAL",
		"REVOKE", "ROLLBACK", "SAVEPOINT", "SET CHARACTER SET",
		"SET DEFAULT ROLE", "SET GLOBAL TRANSACTION", "SET NAMES",
		"SET PASSWORD", "SET ROLE", "SET STATEMENT", "SET TRANSACTION",
		"SHOW", "SHOW ALL REPLICAS STATUS", "SHOW ALL SLAVES STATUS",
		"SHOW AUTHORS", "SHOW BINARY LOGS", "SHOW BINLOG EVENTS",
		"SHOW BINLOG STATUS", "SHOW CHARACTER SET",
		"SHOW CLIENT_STATISTICS", "SHOW COLLATION", "SHOW COLUMNS",
		"SHOW CONTRIBUTORS", "SHOW CREATE DATABASE", "SHOW CREATE EVENT",
		"SHOW CREATE FUNCTION", "SHOW CREATE PACKAGE",
		"SHOW CREATE PACKAGE BODY", "SHOW CREATE PROCEDURE",
		"SHOW CREATE SEQUENCE", "SHOW CREATE TABLE", "SHOW CREATE TRIGGER",
		"SHOW CREATE USER", "SHOW CREATE VIEW", "SHOW DATABASES",
		"SHOW ENGINE", "SHOW ENGINE INNODB STATUS", "SHOW ENGINES",
		"SHOW ERRORS", "SHOW EVENTS", "SHOW EXPLAIN", "SHOW FUNCTION CODE",
		"SHOW FUNCTION STATUS", "SHOW GRANTS", "SHOW INDEX", "SHOW INDEXES",
		"SHOW INDEX_STATISTICS", "SHOW KEYS", "SHOW LOCALES",
		"SHOW MASTER LOGS", "SHOW MASTER STATUS", "SHOW OPEN TABLES",
		"SHOW PACKAGE BODY CODE", "SHOW PACKAGE BODY STATUS",
		"SHOW PACKAGE STATUS", "SHOW PLUGINS", "SHOW PLUGINS SONAME",
		"SHOW PRIVILEGES", "SHOW PROCEDURE CODE", "SHOW PROCEDURE STATUS",
		"SHOW PROCESSLIST", "SHOW PROFILE", "SHOW PROFILES",
		"SHOW QUERY_RESPONSE_TIME", "SHOW RELAYLOG EVENTS", "SHOW REPLICA",
		"SHOW REPLICA HOSTS", "SHOW REPLICA STATUS", "SHOW SCHEMAS",
		"SHOW SLAVE", "SHOW SLAVE HOSTS", "SHOW SLAVE STATUS",
		"SHOW STATUS", "SHOW STORAGE ENGINES", "SHOW TABLE STATUS",
		"SHOW TABLES", "SHOW TRIGGERS", "SHOW USER_STATISTICS",
		"SHOW VARIABLES", "SHOW WARNINGS", "SHOW WSREP_MEMBERSHIP",
		"SHOW WSREP_STATUS", "SHUTDOWN", "SIGNAL", "START ALL REPLICAS",
		"START ALL SLAVES", "START REPLICA", "START SLAVE",
		"START TRANSACTION", "STOP ALL REPLICAS", "STOP ALL SLAVES",
		"STOP REPLICA", "STOP SLAVE", "UNINSTALL PLUGIN",
		"UNINSTALL SONAME", "UNLOCK TABLE", "USE", "XA BEGIN", "XA COMMIT",
		"XA END", "XA PREPARE", "XA RECOVER", "XA ROLLBACK", "XA START"
	]),
	rS = v(["UNION [ALL | DISTINCT]", "EXCEPT [ALL | DISTINCT]",
		"INTERSECT [ALL | DISTINCT]", "MINUS [ALL | DISTINCT]"
	]),
	RS = v(["JOIN", "{LEFT | RIGHT} [OUTER] JOIN", "{INNER | CROSS} JOIN",
		"NATURAL JOIN", "NATURAL {LEFT | RIGHT} [OUTER] JOIN",
		"STRAIGHT_JOIN"
	]),
	nS = v(["ON {UPDATE | DELETE} [SET NULL | SET DEFAULT]", "CHARACTER SET",
		"{ROWS | RANGE} BETWEEN", "IDENTIFIED BY"
	]),
	AS = {
		name: "mariadb",
		tokenizerOptions: {
			reservedSelect: tS,
			reservedClauses: [...TS, ...Ar, ...Jt],
			reservedSetOperations: rS,
			reservedJoins: RS,
			reservedPhrases: nS,
			supportsXor: !0,
			reservedKeywords: zs,
			reservedDataTypes: eS,
			reservedFunctionNames: ES,
			stringTypes: ['""-qq-bs', "''-qq-bs", {
				quote: "''-raw",
				prefixes: ["B", "X"],
				requirePrefix: !0
			}],
			identTypes: ["``"],
			identChars: {
				first: "$",
				rest: "$",
				allowFirstCharNumber: !0
			},
			variableTypes: [{
				regex: "@@?[A-Za-z0-9_.$]+"
			}, {
				quote: '""-qq-bs',
				prefixes: ["@"],
				requirePrefix: !0
			}, {
				quote: "''-qq-bs",
				prefixes: ["@"],
				requirePrefix: !0
			}, {
				quote: "``",
				prefixes: ["@"],
				requirePrefix: !0
			}],
			paramTypes: {
				positional: !0
			},
			lineCommentTypes: ["--", "#"],
			operators: ["%", ":=", "&", "|", "^", "~", "<<", ">>", "<=>", "&&",
				"||", "!", "*.*"
			],
			postProcess: yt
		},
		formatOptions: {
			onelineClauses: [...Ar, ...Jt],
			tabularOnelineClauses: Jt
		}
	},
	sS = ["ACCESSIBLE", "ADD", "ALL", "ALTER", "ANALYZE", "AND", "AS", "ASC",
		"ASENSITIVE", "BEFORE", "BETWEEN", "BOTH", "BY", "CALL", "CASCADE",
		"CASE", "CHANGE", "CHECK", "COLLATE", "COLUMN", "CONDITION",
		"CONSTRAINT", "CONTINUE", "CONVERT", "CREATE", "CROSS", "CUBE",
		"CUME_DIST", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP",
		"CURRENT_USER", "CURSOR", "DATABASE", "DATABASES", "DAY_HOUR",
		"DAY_MICROSECOND", "DAY_MINUTE", "DAY_SECOND", "DECLARE", "DEFAULT",
		"DELAYED", "DELETE", "DENSE_RANK", "DESC", "DESCRIBE", "DETERMINISTIC",
		"DISTINCT", "DISTINCTROW", "DIV", "DROP", "DUAL", "EACH", "ELSE",
		"ELSEIF", "EMPTY", "ENCLOSED", "ESCAPED", "EXCEPT", "EXISTS", "EXIT",
		"EXPLAIN", "FALSE", "FETCH", "FIRST_VALUE", "FOR", "FORCE", "FOREIGN",
		"FROM", "FULLTEXT", "FUNCTION", "GENERATED", "GET", "GRANT", "GROUP",
		"GROUPING", "GROUPS", "HAVING", "HIGH_PRIORITY", "HOUR_MICROSECOND",
		"HOUR_MINUTE", "HOUR_SECOND", "IF", "IGNORE", "IN", "INDEX", "INFILE",
		"INNER", "INOUT", "INSENSITIVE", "INSERT", "IN", "INTERSECT",
		"INTERVAL", "INTO", "IO_AFTER_GTIDS", "IO_BEFORE_GTIDS", "IS",
		"ITERATE", "JOIN", "JSON_TABLE", "KEY", "KEYS", "KILL", "LAG",
		"LAST_VALUE", "LATERAL", "LEAD", "LEADING", "LEAVE", "LEFT", "LIKE",
		"LIMIT", "LINEAR", "LINES", "LOAD", "LOCALTIME", "LOCALTIMESTAMP",
		"LOCK", "LONG", "LOOP", "LOW_PRIORITY", "MASTER_BIND",
		"MASTER_SSL_VERIFY_SERVER_CERT", "MATCH", "MAXVALUE",
		"MINUTE_MICROSECOND", "MINUTE_SECOND", "MOD", "MODIFIES", "NATURAL",
		"NOT", "NO_WRITE_TO_BINLOG", "NTH_VALUE", "NTILE", "NULL", "OF", "ON",
		"OPTIMIZE", "OPTIMIZER_COSTS", "OPTION", "OPTIONALLY", "OR", "ORDER",
		"OUT", "OUTER", "OUTFILE", "OVER", "PARTITION", "PERCENT_RANK",
		"PRIMARY", "PROCEDURE", "PURGE", "RANGE", "RANK", "READ", "READS",
		"READ_WRITE", "RECURSIVE", "REFERENCES", "REGEXP", "RELEASE", "RENAME",
		"REPEAT", "REPLACE", "REQUIRE", "RESIGNAL", "RESTRICT", "RETURN",
		"REVOKE", "RIGHT", "RLIKE", "ROW", "ROWS", "ROW_NUMBER", "SCHEMA",
		"SCHEMAS", "SECOND_MICROSECOND", "SELECT", "SENSITIVE", "SEPARATOR",
		"SET", "SHOW", "SIGNAL", "SPATIAL", "SPECIFIC", "SQL", "SQLEXCEPTION",
		"SQLSTATE", "SQLWARNING", "SQL_BIG_RESULT", "SQL_CALC_FOUND_ROWS",
		"SQL_SMALL_RESULT", "SSL", "STARTING", "STORED", "STRAIGHT_JOIN",
		"SYSTEM", "TABLE", "TERMINATED", "THEN", "TO", "TRAILING", "TRIGGER",
		"TRUE", "UNDO", "UNION", "UNIQUE", "UNLOCK", "UNSIGNED", "UPDATE",
		"USAGE", "USE", "USING", "UTC_DATE", "UTC_TIME", "UTC_TIMESTAMP",
		"VALUES", "VIRTUAL", "WHEN", "WHERE", "WHILE", "WINDOW", "WITH",
		"WRITE", "XOR", "YEAR_MONTH", "ZEROFILL"
	],
	SS = ["BIGINT", "BINARY", "BIT", "BLOB", "BOOL", "BOOLEAN", "CHAR",
		"CHARACTER", "DATE", "DATETIME", "DEC", "DECIMAL", "DOUBLE PRECISION",
		"DOUBLE", "ENUM", "FIXED", "FLOAT", "FLOAT4", "FLOAT8", "INT", "INT1",
		"INT2", "INT3", "INT4", "INT8", "INTEGER", "LONGBLOB", "LONGTEXT",
		"MEDIUMBLOB", "MEDIUMINT", "MEDIUMTEXT", "MIDDLEINT", "NATIONAL CHAR",
		"NATIONAL VARCHAR", "NUMERIC", "PRECISION", "REAL", "SMALLINT", "TEXT",
		"TIME", "TIMESTAMP", "TINYBLOB", "TINYINT", "TINYTEXT", "VARBINARY",
		"VARCHAR", "VARCHARACTER", "VARYING", "YEAR"
	],
	oS = ["ABS", "ACOS", "ADDDATE", "ADDTIME", "AES_DECRYPT", "AES_ENCRYPT",
		"ANY_VALUE", "ASCII", "ASIN", "ATAN", "ATAN2", "AVG", "BENCHMARK",
		"BIN", "BIN_TO_UUID", "BINARY", "BIT_AND", "BIT_COUNT", "BIT_LENGTH",
		"BIT_OR", "BIT_XOR", "CAN_ACCESS_COLUMN", "CAN_ACCESS_DATABASE",
		"CAN_ACCESS_TABLE", "CAN_ACCESS_USER", "CAN_ACCESS_VIEW", "CAST",
		"CEIL", "CEILING", "CHAR", "CHAR_LENGTH", "CHARACTER_LENGTH", "CHARSET",
		"COALESCE", "COERCIBILITY", "COLLATION", "COMPRESS", "CONCAT",
		"CONCAT_WS", "CONNECTION_ID", "CONV", "CONVERT", "CONVERT_TZ", "COS",
		"COT", "COUNT", "CRC32", "CUME_DIST", "CURDATE", "CURRENT_DATE",
		"CURRENT_ROLE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER",
		"CURTIME", "DATABASE", "DATE", "DATE_ADD", "DATE_FORMAT", "DATE_SUB",
		"DATEDIFF", "DAY", "DAYNAME", "DAYOFMONTH", "DAYOFWEEK", "DAYOFYEAR",
		"DEFAULT", "DEGREES", "DENSE_RANK", "DIV", "ELT", "EXP", "EXPORT_SET",
		"EXTRACT", "EXTRACTVALUE", "FIELD", "FIND_IN_SET", "FIRST_VALUE",
		"FLOOR", "FORMAT", "FORMAT_BYTES", "FORMAT_PICO_TIME", "FOUND_ROWS",
		"FROM_BASE64", "FROM_DAYS", "FROM_UNIXTIME", "GEOMCOLLECTION",
		"GEOMETRYCOLLECTION", "GET_DD_COLUMN_PRIVILEGES",
		"GET_DD_CREATE_OPTIONS", "GET_DD_INDEX_SUB_PART_LENGTH", "GET_FORMAT",
		"GET_LOCK", "GREATEST", "GROUP_CONCAT", "GROUPING", "GTID_SUBSET",
		"GTID_SUBTRACT", "HEX", "HOUR", "ICU_VERSION", "IF", "IFNULL",
		"INET_ATON", "INET_NTOA", "INET6_ATON", "INET6_NTOA", "INSERT", "INSTR",
		"INTERNAL_AUTO_INCREMENT", "INTERNAL_AVG_ROW_LENGTH",
		"INTERNAL_CHECK_TIME", "INTERNAL_CHECKSUM", "INTERNAL_DATA_FREE",
		"INTERNAL_DATA_LENGTH", "INTERNAL_DD_CHAR_LENGTH",
		"INTERNAL_GET_COMMENT_OR_ERROR", "INTERNAL_GET_ENABLED_ROLE_JSON",
		"INTERNAL_GET_HOSTNAME", "INTERNAL_GET_USERNAME",
		"INTERNAL_GET_VIEW_WARNING_OR_ERROR",
		"INTERNAL_INDEX_COLUMN_CARDINALITY", "INTERNAL_INDEX_LENGTH",
		"INTERNAL_IS_ENABLED_ROLE", "INTERNAL_IS_MANDATORY_ROLE",
		"INTERNAL_KEYS_DISABLED", "INTERNAL_MAX_DATA_LENGTH",
		"INTERNAL_TABLE_ROWS", "INTERNAL_UPDATE_TIME", "INTERVAL", "IS",
		"IS_FREE_LOCK", "IS_IPV4", "IS_IPV4_COMPAT", "IS_IPV4_MAPPED",
		"IS_IPV6", "IS NOT", "IS NOT NULL", "IS NULL", "IS_USED_LOCK",
		"IS_UUID", "ISNULL", "JSON_ARRAY", "JSON_ARRAY_APPEND",
		"JSON_ARRAY_INSERT", "JSON_ARRAYAGG", "JSON_CONTAINS",
		"JSON_CONTAINS_PATH", "JSON_DEPTH", "JSON_EXTRACT", "JSON_INSERT",
		"JSON_KEYS", "JSON_LENGTH", "JSON_MERGE", "JSON_MERGE_PATCH",
		"JSON_MERGE_PRESERVE", "JSON_OBJECT", "JSON_OBJECTAGG", "JSON_OVERLAPS",
		"JSON_PRETTY", "JSON_QUOTE", "JSON_REMOVE", "JSON_REPLACE",
		"JSON_SCHEMA_VALID", "JSON_SCHEMA_VALIDATION_REPORT", "JSON_SEARCH",
		"JSON_SET", "JSON_STORAGE_FREE", "JSON_STORAGE_SIZE", "JSON_TABLE",
		"JSON_TYPE", "JSON_UNQUOTE", "JSON_VALID", "JSON_VALUE", "LAG",
		"LAST_DAY", "LAST_INSERT_ID", "LAST_VALUE", "LCASE", "LEAD", "LEAST",
		"LEFT", "LENGTH", "LIKE", "LINESTRING", "LN", "LOAD_FILE", "LOCALTIME",
		"LOCALTIMESTAMP", "LOCATE", "LOG", "LOG10", "LOG2", "LOWER", "LPAD",
		"LTRIM", "MAKE_SET", "MAKEDATE", "MAKETIME", "MASTER_POS_WAIT", "MATCH",
		"MAX", "MBRCONTAINS", "MBRCOVEREDBY", "MBRCOVERS", "MBRDISJOINT",
		"MBREQUALS", "MBRINTERSECTS", "MBROVERLAPS", "MBRTOUCHES", "MBRWITHIN",
		"MD5", "MEMBER OF", "MICROSECOND", "MID", "MIN", "MINUTE", "MOD",
		"MONTH", "MONTHNAME", "MULTILINESTRING", "MULTIPOINT", "MULTIPOLYGON",
		"NAME_CONST", "NOT", "NOT IN", "NOT LIKE", "NOT REGEXP", "NOW",
		"NTH_VALUE", "NTILE", "NULLIF", "OCT", "OCTET_LENGTH", "ORD",
		"PERCENT_RANK", "PERIOD_ADD", "PERIOD_DIFF", "PI", "POINT", "POLYGON",
		"POSITION", "POW", "POWER", "PS_CURRENT_THREAD_ID", "PS_THREAD_ID",
		"QUARTER", "QUOTE", "RADIANS", "RAND", "RANDOM_BYTES", "RANK", "REGEXP",
		"REGEXP_INSTR", "REGEXP_LIKE", "REGEXP_REPLACE", "REGEXP_SUBSTR",
		"RELEASE_ALL_LOCKS", "RELEASE_LOCK", "REPEAT", "REPLACE", "REVERSE",
		"RIGHT", "RLIKE", "ROLES_GRAPHML", "ROUND", "ROW_COUNT", "ROW_NUMBER",
		"RPAD", "RTRIM", "SCHEMA", "SEC_TO_TIME", "SECOND", "SESSION_USER",
		"SHA1", "SHA2", "SIGN", "SIN", "SLEEP", "SOUNDEX", "SOUNDS LIKE",
		"SOURCE_POS_WAIT", "SPACE", "SQRT", "ST_AREA", "ST_ASBINARY",
		"ST_ASGEOJSON", "ST_ASTEXT", "ST_BUFFER", "ST_BUFFER_STRATEGY",
		"ST_CENTROID", "ST_COLLECT", "ST_CONTAINS", "ST_CONVEXHULL",
		"ST_CROSSES", "ST_DIFFERENCE", "ST_DIMENSION", "ST_DISJOINT",
		"ST_DISTANCE", "ST_DISTANCE_SPHERE", "ST_ENDPOINT", "ST_ENVELOPE",
		"ST_EQUALS", "ST_EXTERIORRING", "ST_FRECHETDISTANCE", "ST_GEOHASH",
		"ST_GEOMCOLLFROMTEXT", "ST_GEOMCOLLFROMWKB", "ST_GEOMETRYN",
		"ST_GEOMETRYTYPE", "ST_GEOMFROMGEOJSON", "ST_GEOMFROMTEXT",
		"ST_GEOMFROMWKB", "ST_HAUSDORFFDISTANCE", "ST_INTERIORRINGN",
		"ST_INTERSECTION", "ST_INTERSECTS", "ST_ISCLOSED", "ST_ISEMPTY",
		"ST_ISSIMPLE", "ST_ISVALID", "ST_LATFROMGEOHASH", "ST_LATITUDE",
		"ST_LENGTH", "ST_LINEFROMTEXT", "ST_LINEFROMWKB",
		"ST_LINEINTERPOLATEPOINT", "ST_LINEINTERPOLATEPOINTS",
		"ST_LONGFROMGEOHASH", "ST_LONGITUDE", "ST_MAKEENVELOPE",
		"ST_MLINEFROMTEXT", "ST_MLINEFROMWKB", "ST_MPOINTFROMTEXT",
		"ST_MPOINTFROMWKB", "ST_MPOLYFROMTEXT", "ST_MPOLYFROMWKB",
		"ST_NUMGEOMETRIES", "ST_NUMINTERIORRING", "ST_NUMPOINTS", "ST_OVERLAPS",
		"ST_POINTATDISTANCE", "ST_POINTFROMGEOHASH", "ST_POINTFROMTEXT",
		"ST_POINTFROMWKB", "ST_POINTN", "ST_POLYFROMTEXT", "ST_POLYFROMWKB",
		"ST_SIMPLIFY", "ST_SRID", "ST_STARTPOINT", "ST_SWAPXY",
		"ST_SYMDIFFERENCE", "ST_TOUCHES", "ST_TRANSFORM", "ST_UNION",
		"ST_VALIDATE", "ST_WITHIN", "ST_X", "ST_Y", "STATEMENT_DIGEST",
		"STATEMENT_DIGEST_TEXT", "STD", "STDDEV", "STDDEV_POP", "STDDEV_SAMP",
		"STR_TO_DATE", "STRCMP", "SUBDATE", "SUBSTR", "SUBSTRING",
		"SUBSTRING_INDEX", "SUBTIME", "SUM", "SYSDATE", "SYSTEM_USER", "TAN",
		"TIME", "TIME_FORMAT", "TIME_TO_SEC", "TIMEDIFF", "TIMESTAMP",
		"TIMESTAMPADD", "TIMESTAMPDIFF", "TO_BASE64", "TO_DAYS", "TO_SECONDS",
		"TRIM", "TRUNCATE", "UCASE", "UNCOMPRESS", "UNCOMPRESSED_LENGTH",
		"UNHEX", "UNIX_TIMESTAMP", "UPDATEXML", "UPPER", "UTC_DATE", "UTC_TIME",
		"UTC_TIMESTAMP", "UUID", "UUID_SHORT", "UUID_TO_BIN",
		"VALIDATE_PASSWORD_STRENGTH", "VALUES", "VAR_POP", "VAR_SAMP",
		"VARIANCE", "VERSION", "WAIT_FOR_EXECUTED_GTID_SET",
		"WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS", "WEEK", "WEEKDAY", "WEEKOFYEAR",
		"WEIGHT_STRING", "YEAR", "YEARWEEK"
	],
	OS = v(["SELECT [ALL | DISTINCT | DISTINCTROW]"]),
	iS = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY", "HAVING", "WINDOW",
		"PARTITION BY", "ORDER BY", "LIMIT", "OFFSET",
		"INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE] [INTO]",
		"REPLACE [LOW_PRIORITY | DELAYED] [INTO]", "VALUES",
		"ON DUPLICATE KEY UPDATE", "SET"
	]),
	sr = v(["CREATE [TEMPORARY] TABLE [IF NOT EXISTS]"]),
	qt = v([
		"CREATE [OR REPLACE] [SQL SECURITY DEFINER | SQL SECURITY INVOKER] VIEW [IF NOT EXISTS]",
		"UPDATE [LOW_PRIORITY] [IGNORE]",
		"DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM",
		"DROP [TEMPORARY] TABLE [IF EXISTS]", "ALTER TABLE", "ADD [COLUMN]",
		"{CHANGE | MODIFY} [COLUMN]", "DROP [COLUMN]", "RENAME [TO | AS]",
		"RENAME COLUMN", "ALTER [COLUMN]", "{SET | DROP} DEFAULT",
		"TRUNCATE [TABLE]", "ALTER DATABASE", "ALTER EVENT",
		"ALTER FUNCTION", "ALTER INSTANCE", "ALTER LOGFILE GROUP",
		"ALTER PROCEDURE", "ALTER RESOURCE GROUP", "ALTER SERVER",
		"ALTER TABLESPACE", "ALTER USER", "ALTER VIEW", "ANALYZE TABLE",
		"BINLOG", "CACHE INDEX", "CALL", "CHANGE MASTER TO",
		"CHANGE REPLICATION FILTER", "CHANGE REPLICATION SOURCE TO",
		"CHECK TABLE", "CHECKSUM TABLE", "CLONE", "COMMIT",
		"CREATE DATABASE", "CREATE EVENT", "CREATE FUNCTION",
		"CREATE FUNCTION", "CREATE INDEX", "CREATE LOGFILE GROUP",
		"CREATE PROCEDURE", "CREATE RESOURCE GROUP", "CREATE ROLE",
		"CREATE SERVER", "CREATE SPATIAL REFERENCE SYSTEM",
		"CREATE TABLESPACE", "CREATE TRIGGER", "CREATE USER",
		"DEALLOCATE PREPARE", "DESCRIBE", "DROP DATABASE", "DROP EVENT",
		"DROP FUNCTION", "DROP FUNCTION", "DROP INDEX",
		"DROP LOGFILE GROUP", "DROP PROCEDURE", "DROP RESOURCE GROUP",
		"DROP ROLE", "DROP SERVER", "DROP SPATIAL REFERENCE SYSTEM",
		"DROP TABLESPACE", "DROP TRIGGER", "DROP USER", "DROP VIEW",
		"EXECUTE", "EXPLAIN", "FLUSH", "GRANT", "HANDLER", "HELP",
		"IMPORT TABLE", "INSTALL COMPONENT", "INSTALL PLUGIN", "KILL",
		"LOAD DATA", "LOAD INDEX INTO CACHE", "LOAD XML",
		"LOCK INSTANCE FOR BACKUP", "LOCK TABLES", "MASTER_POS_WAIT",
		"OPTIMIZE TABLE", "PREPARE", "PURGE BINARY LOGS",
		"RELEASE SAVEPOINT", "RENAME TABLE", "RENAME USER", "REPAIR TABLE",
		"RESET", "RESET MASTER", "RESET PERSIST", "RESET REPLICA",
		"RESET SLAVE", "RESTART", "REVOKE", "ROLLBACK",
		"ROLLBACK TO SAVEPOINT", "SAVEPOINT", "SET CHARACTER SET",
		"SET DEFAULT ROLE", "SET NAMES", "SET PASSWORD",
		"SET RESOURCE GROUP", "SET ROLE", "SET TRANSACTION", "SHOW",
		"SHOW BINARY LOGS", "SHOW BINLOG EVENTS", "SHOW CHARACTER SET",
		"SHOW COLLATION", "SHOW COLUMNS", "SHOW CREATE DATABASE",
		"SHOW CREATE EVENT", "SHOW CREATE FUNCTION",
		"SHOW CREATE PROCEDURE", "SHOW CREATE TABLE", "SHOW CREATE TRIGGER",
		"SHOW CREATE USER", "SHOW CREATE VIEW", "SHOW DATABASES",
		"SHOW ENGINE", "SHOW ENGINES", "SHOW ERRORS", "SHOW EVENTS",
		"SHOW FUNCTION CODE", "SHOW FUNCTION STATUS", "SHOW GRANTS",
		"SHOW INDEX", "SHOW MASTER STATUS", "SHOW OPEN TABLES",
		"SHOW PLUGINS", "SHOW PRIVILEGES", "SHOW PROCEDURE CODE",
		"SHOW PROCEDURE STATUS", "SHOW PROCESSLIST", "SHOW PROFILE",
		"SHOW PROFILES", "SHOW RELAYLOG EVENTS", "SHOW REPLICA STATUS",
		"SHOW REPLICAS", "SHOW SLAVE", "SHOW SLAVE HOSTS", "SHOW STATUS",
		"SHOW TABLE STATUS", "SHOW TABLES", "SHOW TRIGGERS",
		"SHOW VARIABLES", "SHOW WARNINGS", "SHUTDOWN", "SOURCE_POS_WAIT",
		"START GROUP_REPLICATION", "START REPLICA", "START SLAVE",
		"START TRANSACTION", "STOP GROUP_REPLICATION", "STOP REPLICA",
		"STOP SLAVE", "TABLE", "UNINSTALL COMPONENT", "UNINSTALL PLUGIN",
		"UNLOCK INSTANCE", "UNLOCK TABLES", "USE", "XA", "ITERATE", "LEAVE",
		"LOOP", "REPEAT", "RETURN", "WHILE"
	]),
	aS = v(["UNION [ALL | DISTINCT]"]),
	IS = v(["JOIN", "{LEFT | RIGHT} [OUTER] JOIN", "{INNER | CROSS} JOIN",
		"NATURAL [INNER] JOIN", "NATURAL {LEFT | RIGHT} [OUTER] JOIN",
		"STRAIGHT_JOIN"
	]),
	NS = v(["ON {UPDATE | DELETE} [SET NULL]", "CHARACTER SET",
		"{ROWS | RANGE} BETWEEN", "IDENTIFIED BY"
	]),
	lS = {
		name: "mysql",
		tokenizerOptions: {
			reservedSelect: OS,
			reservedClauses: [...iS, ...sr, ...qt],
			reservedSetOperations: aS,
			reservedJoins: IS,
			reservedPhrases: NS,
			supportsXor: !0,
			reservedKeywords: sS,
			reservedDataTypes: SS,
			reservedFunctionNames: oS,
			stringTypes: ['""-qq-bs', {
				quote: "''-qq-bs",
				prefixes: ["N"]
			}, {
				quote: "''-raw",
				prefixes: ["B", "X"],
				requirePrefix: !0
			}],
			identTypes: ["``"],
			identChars: {
				first: "$",
				rest: "$",
				allowFirstCharNumber: !0
			},
			variableTypes: [{
				regex: "@@?[A-Za-z0-9_.$]+"
			}, {
				quote: '""-qq-bs',
				prefixes: ["@"],
				requirePrefix: !0
			}, {
				quote: "''-qq-bs",
				prefixes: ["@"],
				requirePrefix: !0
			}, {
				quote: "``",
				prefixes: ["@"],
				requirePrefix: !0
			}],
			paramTypes: {
				positional: !0
			},
			lineCommentTypes: ["--", "#"],
			operators: ["%", ":=", "&", "|", "^", "~", "<<", ">>", "<=>", "->",
				"->>", "&&", "||", "!", "*.*"
			],
			postProcess: yt
		},
		formatOptions: {
			onelineClauses: [...sr, ...qt],
			tabularOnelineClauses: qt
		}
	},
	_S = ["ADD", "ALL", "ALTER", "ANALYZE", "AND", "ARRAY", "AS", "ASC",
		"BETWEEN", "BOTH", "BY", "CALL", "CASCADE", "CASE", "CHANGE", "CHECK",
		"COLLATE", "COLUMN", "CONSTRAINT", "CONTINUE", "CONVERT", "CREATE",
		"CROSS", "CURRENT_DATE", "CURRENT_ROLE", "CURRENT_TIME",
		"CURRENT_TIMESTAMP", "CURRENT_USER", "CURSOR", "DATABASE", "DATABASES",
		"DAY_HOUR", "DAY_MICROSECOND", "DAY_MINUTE", "DAY_SECOND", "DEFAULT",
		"DELAYED", "DELETE", "DESC", "DESCRIBE", "DISTINCT", "DISTINCTROW",
		"DIV", "DOUBLE", "DROP", "DUAL", "ELSE", "ELSEIF", "ENCLOSED",
		"ESCAPED", "EXCEPT", "EXISTS", "EXIT", "EXPLAIN", "FALSE", "FETCH",
		"FOR", "FORCE", "FOREIGN", "FROM", "FULLTEXT", "GENERATED", "GRANT",
		"GROUP", "GROUPS", "HAVING", "HIGH_PRIORITY", "HOUR_MICROSECOND",
		"HOUR_MINUTE", "HOUR_SECOND", "IF", "IGNORE", "ILIKE", "IN", "INDEX",
		"INFILE", "INNER", "INOUT", "INSERT", "INTERSECT", "INTERVAL", "INTO",
		"IS", "ITERATE", "JOIN", "KEY", "KEYS", "KILL", "LEADING", "LEAVE",
		"LEFT", "LIKE", "LIMIT", "LINEAR", "LINES", "LOAD", "LOCALTIME",
		"LOCALTIMESTAMP", "LOCK", "LONG", "LOW_PRIORITY", "MATCH", "MAXVALUE",
		"MINUTE_MICROSECOND", "MINUTE_SECOND", "MOD", "NATURAL", "NOT",
		"NO_WRITE_TO_BINLOG", "NULL", "OF", "ON", "OPTIMIZE", "OPTION",
		"OPTIONALLY", "OR", "ORDER", "OUT", "OUTER", "OUTFILE", "OVER",
		"PARTITION", "PRIMARY", "PROCEDURE", "RANGE", "READ", "RECURSIVE",
		"REFERENCES", "REGEXP", "RELEASE", "RENAME", "REPEAT", "REPLACE",
		"REQUIRE", "RESTRICT", "REVOKE", "RIGHT", "RLIKE", "ROW", "ROWS",
		"SECOND_MICROSECOND", "SELECT", "SET", "SHOW", "SPATIAL", "SQL",
		"SQLEXCEPTION", "SQLSTATE", "SQLWARNING", "SQL_BIG_RESULT",
		"SQL_CALC_FOUND_ROWS", "SQL_SMALL_RESULT", "SSL", "STARTING",
		"STATS_EXTENDED", "STORED", "STRAIGHT_JOIN", "TABLE", "TABLESAMPLE",
		"TERMINATED", "THEN", "TO", "TRAILING", "TRIGGER", "TRUE",
		"TiDB_CURRENT_TSO", "UNION", "UNIQUE", "UNLOCK", "UNSIGNED", "UNTIL",
		"UPDATE", "USAGE", "USE", "USING", "UTC_DATE", "UTC_TIME",
		"UTC_TIMESTAMP", "VALUES", "VIRTUAL", "WHEN", "WHERE", "WHILE",
		"WINDOW", "WITH", "WRITE", "XOR", "YEAR_MONTH", "ZEROFILL"
	],
	LS = ["BIGINT", "BINARY", "BIT", "BLOB", "BOOL", "BOOLEAN", "CHAR",
		"CHARACTER", "DATE", "DATETIME", "DEC", "DECIMAL", "DOUBLE PRECISION",
		"DOUBLE", "ENUM", "FIXED", "INT", "INT1", "INT2", "INT3", "INT4",
		"INT8", "INTEGER", "LONGBLOB", "LONGTEXT", "MEDIUMBLOB", "MEDIUMINT",
		"MIDDLEINT", "NATIONAL CHAR", "NATIONAL VARCHAR", "NUMERIC",
		"PRECISION", "SMALLINT", "TEXT", "TIME", "TIMESTAMP", "TINYBLOB",
		"TINYINT", "TINYTEXT", "VARBINARY", "VARCHAR", "VARCHARACTER",
		"VARYING", "YEAR"
	],
	CS = ["ABS", "ACOS", "ADDDATE", "ADDTIME", "AES_DECRYPT", "AES_ENCRYPT",
		"ANY_VALUE", "ASCII", "ASIN", "ATAN", "ATAN2", "AVG", "BENCHMARK",
		"BIN", "BIN_TO_UUID", "BIT_AND", "BIT_COUNT", "BIT_LENGTH", "BIT_OR",
		"BIT_XOR", "BITAND", "BITNEG", "BITOR", "BITXOR", "CASE", "CAST",
		"CEIL", "CEILING", "CHAR_FUNC", "CHAR_LENGTH", "CHARACTER_LENGTH",
		"CHARSET", "COALESCE", "COERCIBILITY", "COLLATION", "COMPRESS",
		"CONCAT", "CONCAT_WS", "CONNECTION_ID", "CONV", "CONVERT", "CONVERT_TZ",
		"COS", "COT", "COUNT", "CRC32", "CUME_DIST", "CURDATE", "CURRENT_DATE",
		"CURRENT_RESOURCE_GROUP", "CURRENT_ROLE", "CURRENT_TIME",
		"CURRENT_TIMESTAMP", "CURRENT_USER", "CURTIME", "DATABASE", "DATE",
		"DATE_ADD", "DATE_FORMAT", "DATE_SUB", "DATEDIFF", "DAY", "DAYNAME",
		"DAYOFMONTH", "DAYOFWEEK", "DAYOFYEAR", "DECODE", "DEFAULT_FUNC",
		"DEGREES", "DENSE_RANK", "DES_DECRYPT", "DES_ENCRYPT", "DIV", "ELT",
		"ENCODE", "ENCRYPT", "EQ", "EXP", "EXPORT_SET", "EXTRACT", "FIELD",
		"FIND_IN_SET", "FIRST_VALUE", "FLOOR", "FORMAT", "FORMAT_BYTES",
		"FORMAT_NANO_TIME", "FOUND_ROWS", "FROM_BASE64", "FROM_DAYS",
		"FROM_UNIXTIME", "GE", "GET_FORMAT", "GET_LOCK", "GETPARAM", "GREATEST",
		"GROUP_CONCAT", "GROUPING", "GT", "HEX", "HOUR", "IF", "IFNULL",
		"ILIKE", "INET6_ATON", "INET6_NTOA", "INET_ATON", "INET_NTOA",
		"INSERT_FUNC", "INSTR", "INTDIV", "INTERVAL", "IS_FREE_LOCK", "IS_IPV4",
		"IS_IPV4_COMPAT", "IS_IPV4_MAPPED", "IS_IPV6", "IS_USED_LOCK",
		"IS_UUID", "ISFALSE", "ISNULL", "ISTRUE", "JSON_ARRAY", "JSON_ARRAYAGG",
		"JSON_ARRAY_APPEND", "JSON_ARRAY_INSERT", "JSON_CONTAINS",
		"JSON_CONTAINS_PATH", "JSON_DEPTH", "JSON_EXTRACT", "JSON_INSERT",
		"JSON_KEYS", "JSON_LENGTH", "JSON_MEMBEROF", "JSON_MERGE",
		"JSON_MERGE_PATCH", "JSON_MERGE_PRESERVE", "JSON_OBJECT",
		"JSON_OBJECTAGG", "JSON_OVERLAPS", "JSON_PRETTY", "JSON_QUOTE",
		"JSON_REMOVE", "JSON_REPLACE", "JSON_SEARCH", "JSON_SET",
		"JSON_STORAGE_FREE", "JSON_STORAGE_SIZE", "JSON_TYPE", "JSON_UNQUOTE",
		"JSON_VALID", "LAG", "LAST_DAY", "LAST_INSERT_ID", "LAST_VALUE",
		"LASTVAL", "LCASE", "LE", "LEAD", "LEAST", "LEFT", "LEFTSHIFT",
		"LENGTH", "LIKE", "LN", "LOAD_FILE", "LOCALTIME", "LOCALTIMESTAMP",
		"LOCATE", "LOG", "LOG10", "LOG2", "LOWER", "LPAD", "LT", "LTRIM",
		"MAKE_SET", "MAKEDATE", "MAKETIME", "MASTER_POS_WAIT", "MAX", "MD5",
		"MICROSECOND", "MID", "MIN", "MINUS", "MINUTE", "MOD", "MONTH",
		"MONTHNAME", "MUL", "NAME_CONST", "NE", "NEXTVAL", "NOT", "NOW",
		"NTH_VALUE", "NTILE", "NULLEQ", "OCT", "OCTET_LENGTH", "OLD_PASSWORD",
		"ORD", "PASSWORD_FUNC", "PERCENT_RANK", "PERIOD_ADD", "PERIOD_DIFF",
		"PI", "PLUS", "POSITION", "POW", "POWER", "QUARTER", "QUOTE", "RADIANS",
		"RAND", "RANDOM_BYTES", "RANK", "REGEXP", "REGEXP_INSTR", "REGEXP_LIKE",
		"REGEXP_REPLACE", "REGEXP_SUBSTR", "RELEASE_ALL_LOCKS", "RELEASE_LOCK",
		"REPEAT", "REPLACE", "REVERSE", "RIGHT", "RIGHTSHIFT", "ROUND",
		"ROW_COUNT", "ROW_NUMBER", "RPAD", "RTRIM", "SCHEMA", "SEC_TO_TIME",
		"SECOND", "SESSION_USER", "SETVAL", "SETVAR", "SHA", "SHA1", "SHA2",
		"SIGN", "SIN", "SLEEP", "SM3", "SPACE", "SQRT", "STD", "STDDEV",
		"STDDEV_POP", "STDDEV_SAMP", "STR_TO_DATE", "STRCMP", "SUBDATE",
		"SUBSTR", "SUBSTRING", "SUBSTRING_INDEX", "SUBTIME", "SUM", "SYSDATE",
		"SYSTEM_USER", "TAN", "TIDB_BOUNDED_STALENESS", "TIDB_CURRENT_TSO",
		"TIDB_DECODE_BINARY_PLAN", "TIDB_DECODE_KEY", "TIDB_DECODE_PLAN",
		"TIDB_DECODE_SQL_DIGESTS", "TIDB_ENCODE_SQL_DIGEST",
		"TIDB_IS_DDL_OWNER", "TIDB_PARSE_TSO", "TIDB_PARSE_TSO_LOGICAL",
		"TIDB_ROW_CHECKSUM", "TIDB_SHARD", "TIDB_VERSION", "TIME",
		"TIME_FORMAT", "TIME_TO_SEC", "TIMEDIFF", "TIMESTAMP", "TIMESTAMPADD",
		"TIMESTAMPDIFF", "TO_BASE64", "TO_DAYS", "TO_SECONDS", "TRANSLATE",
		"TRIM", "TRUNCATE", "UCASE", "UNARYMINUS", "UNCOMPRESS",
		"UNCOMPRESSED_LENGTH", "UNHEX", "UNIX_TIMESTAMP", "UPPER", "UTC_DATE",
		"UTC_TIME", "UTC_TIMESTAMP", "UUID", "UUID_SHORT", "UUID_TO_BIN",
		"VALIDATE_PASSWORD_STRENGTH", "VAR_POP", "VAR_SAMP", "VARIANCE",
		"VERSION", "VITESS_HASH", "WEEK", "WEEKDAY", "WEEKOFYEAR",
		"WEIGHT_STRING", "YEAR", "YEARWEEK"
	],
	uS = v(["SELECT [ALL | DISTINCT | DISTINCTROW]"]),
	cS = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY", "HAVING", "WINDOW",
		"PARTITION BY", "ORDER BY", "LIMIT", "OFFSET",
		"INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE] [INTO]",
		"REPLACE [LOW_PRIORITY | DELAYED] [INTO]", "VALUES",
		"ON DUPLICATE KEY UPDATE", "SET"
	]),
	Sr = v(["CREATE [TEMPORARY] TABLE [IF NOT EXISTS]"]),
	Qt = v([
		"CREATE [OR REPLACE] [SQL SECURITY DEFINER | SQL SECURITY INVOKER] VIEW [IF NOT EXISTS]",
		"UPDATE [LOW_PRIORITY] [IGNORE]",
		"DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM",
		"DROP [TEMPORARY] TABLE [IF EXISTS]", "ALTER TABLE", "ADD [COLUMN]",
		"{CHANGE | MODIFY} [COLUMN]", "DROP [COLUMN]", "RENAME [TO | AS]",
		"RENAME COLUMN", "ALTER [COLUMN]", "{SET | DROP} DEFAULT",
		"TRUNCATE [TABLE]", "ALTER DATABASE", "ALTER INSTANCE",
		"ALTER RESOURCE GROUP", "ALTER SEQUENCE", "ALTER USER",
		"ALTER VIEW", "ANALYZE TABLE", "CHECK TABLE", "CHECKSUM TABLE",
		"COMMIT", "CREATE DATABASE", "CREATE INDEX",
		"CREATE RESOURCE GROUP", "CREATE ROLE", "CREATE SEQUENCE",
		"CREATE USER", "DEALLOCATE PREPARE", "DESCRIBE", "DROP DATABASE",
		"DROP INDEX", "DROP RESOURCE GROUP", "DROP ROLE", "DROP TABLESPACE",
		"DROP USER", "DROP VIEW", "EXPLAIN", "FLUSH", "GRANT",
		"IMPORT TABLE", "INSTALL COMPONENT", "INSTALL PLUGIN", "KILL",
		"LOAD DATA", "LOCK INSTANCE FOR BACKUP", "LOCK TABLES",
		"OPTIMIZE TABLE", "PREPARE", "RELEASE SAVEPOINT", "RENAME TABLE",
		"RENAME USER", "REPAIR TABLE", "RESET", "REVOKE", "ROLLBACK",
		"ROLLBACK TO SAVEPOINT", "SAVEPOINT", "SET CHARACTER SET",
		"SET DEFAULT ROLE", "SET NAMES", "SET PASSWORD",
		"SET RESOURCE GROUP", "SET ROLE", "SET TRANSACTION", "SHOW",
		"SHOW BINARY LOGS", "SHOW BINLOG EVENTS", "SHOW CHARACTER SET",
		"SHOW COLLATION", "SHOW COLUMNS", "SHOW CREATE DATABASE",
		"SHOW CREATE TABLE", "SHOW CREATE USER", "SHOW CREATE VIEW",
		"SHOW DATABASES", "SHOW ENGINE", "SHOW ENGINES", "SHOW ERRORS",
		"SHOW EVENTS", "SHOW GRANTS", "SHOW INDEX", "SHOW MASTER STATUS",
		"SHOW OPEN TABLES", "SHOW PLUGINS", "SHOW PRIVILEGES",
		"SHOW PROCESSLIST", "SHOW PROFILE", "SHOW PROFILES", "SHOW STATUS",
		"SHOW TABLE STATUS", "SHOW TABLES", "SHOW TRIGGERS",
		"SHOW VARIABLES", "SHOW WARNINGS", "TABLE", "UNINSTALL COMPONENT",
		"UNINSTALL PLUGIN", "UNLOCK INSTANCE", "UNLOCK TABLES", "USE"
	]),
	fS = v(["UNION [ALL | DISTINCT]"]),
	PS = v(["JOIN", "{LEFT | RIGHT} [OUTER] JOIN", "{INNER | CROSS} JOIN",
		"NATURAL [INNER] JOIN", "NATURAL {LEFT | RIGHT} [OUTER] JOIN",
		"STRAIGHT_JOIN"
	]),
	DS = v(["ON {UPDATE | DELETE} [SET NULL]", "CHARACTER SET",
		"{ROWS | RANGE} BETWEEN", "IDENTIFIED BY"
	]),
	dS = {
		name: "tidb",
		tokenizerOptions: {
			reservedSelect: uS,
			reservedClauses: [...cS, ...Sr, ...Qt],
			reservedSetOperations: fS,
			reservedJoins: PS,
			reservedPhrases: DS,
			supportsXor: !0,
			reservedKeywords: _S,
			reservedDataTypes: LS,
			reservedFunctionNames: CS,
			stringTypes: ['""-qq-bs', {
				quote: "''-qq-bs",
				prefixes: ["N"]
			}, {
				quote: "''-raw",
				prefixes: ["B", "X"],
				requirePrefix: !0
			}],
			identTypes: ["``"],
			identChars: {
				first: "$",
				rest: "$",
				allowFirstCharNumber: !0
			},
			variableTypes: [{
				regex: "@@?[A-Za-z0-9_.$]+"
			}, {
				quote: '""-qq-bs',
				prefixes: ["@"],
				requirePrefix: !0
			}, {
				quote: "''-qq-bs",
				prefixes: ["@"],
				requirePrefix: !0
			}, {
				quote: "``",
				prefixes: ["@"],
				requirePrefix: !0
			}],
			paramTypes: {
				positional: !0
			},
			lineCommentTypes: ["--", "#"],
			operators: ["%", ":=", "&", "|", "^", "~", "<<", ">>", "<=>", "->",
				"->>", "&&", "||", "!", "*.*"
			],
			postProcess: yt
		},
		formatOptions: {
			onelineClauses: [...Sr, ...Qt],
			tabularOnelineClauses: Qt
		}
	},
	pS = ["ABORT", "ABS", "ACOS", "ADVISOR", "ARRAY_AGG", "ARRAY_AGG",
		"ARRAY_APPEND", "ARRAY_AVG", "ARRAY_BINARY_SEARCH", "ARRAY_CONCAT",
		"ARRAY_CONTAINS", "ARRAY_COUNT", "ARRAY_DISTINCT", "ARRAY_EXCEPT",
		"ARRAY_FLATTEN", "ARRAY_IFNULL", "ARRAY_INSERT", "ARRAY_INTERSECT",
		"ARRAY_LENGTH", "ARRAY_MAX", "ARRAY_MIN", "ARRAY_MOVE",
		"ARRAY_POSITION", "ARRAY_PREPEND", "ARRAY_PUT", "ARRAY_RANGE",
		"ARRAY_REMOVE", "ARRAY_REPEAT", "ARRAY_REPLACE", "ARRAY_REVERSE",
		"ARRAY_SORT", "ARRAY_STAR", "ARRAY_SUM", "ARRAY_SYMDIFF",
		"ARRAY_SYMDIFF1", "ARRAY_SYMDIFFN", "ARRAY_UNION", "ASIN", "ATAN",
		"ATAN2", "AVG", "BASE64", "BASE64_DECODE", "BASE64_ENCODE", "BITAND ",
		"BITCLEAR ", "BITNOT ", "BITOR ", "BITSET ", "BITSHIFT ", "BITTEST ",
		"BITXOR ", "CEIL", "CLOCK_LOCAL", "CLOCK_MILLIS", "CLOCK_STR",
		"CLOCK_TZ", "CLOCK_UTC", "COALESCE", "CONCAT", "CONCAT2", "CONTAINS",
		"CONTAINS_TOKEN", "CONTAINS_TOKEN_LIKE", "CONTAINS_TOKEN_REGEXP", "COS",
		"COUNT", "COUNT", "COUNTN", "CUME_DIST", "CURL", "DATE_ADD_MILLIS",
		"DATE_ADD_STR", "DATE_DIFF_MILLIS", "DATE_DIFF_STR", "DATE_FORMAT_STR",
		"DATE_PART_MILLIS", "DATE_PART_STR", "DATE_RANGE_MILLIS",
		"DATE_RANGE_STR", "DATE_TRUNC_MILLIS", "DATE_TRUNC_STR", "DECODE",
		"DECODE_JSON", "DEGREES", "DENSE_RANK", "DURATION_TO_STR",
		"ENCODED_SIZE", "ENCODE_JSON", "EXP", "FIRST_VALUE", "FLOOR",
		"GREATEST", "HAS_TOKEN", "IFINF", "IFMISSING", "IFMISSINGORNULL",
		"IFNAN", "IFNANORINF", "IFNULL", "INITCAP", "ISARRAY", "ISATOM",
		"ISBITSET", "ISBOOLEAN", "ISNUMBER", "ISOBJECT", "ISSTRING", "LAG",
		"LAST_VALUE", "LEAD", "LEAST", "LENGTH", "LN", "LOG", "LOWER", "LTRIM",
		"MAX", "MEAN", "MEDIAN", "META", "MILLIS", "MILLIS_TO_LOCAL",
		"MILLIS_TO_STR", "MILLIS_TO_TZ", "MILLIS_TO_UTC", "MILLIS_TO_ZONE_NAME",
		"MIN", "MISSINGIF", "NANIF", "NEGINFIF", "NOW_LOCAL", "NOW_MILLIS",
		"NOW_STR", "NOW_TZ", "NOW_UTC", "NTH_VALUE", "NTILE", "NULLIF", "NVL",
		"NVL2", "OBJECT_ADD", "OBJECT_CONCAT", "OBJECT_INNER_PAIRS",
		"OBJECT_INNER_VALUES", "OBJECT_LENGTH", "OBJECT_NAMES", "OBJECT_PAIRS",
		"OBJECT_PUT", "OBJECT_REMOVE", "OBJECT_RENAME", "OBJECT_REPLACE",
		"OBJECT_UNWRAP", "OBJECT_VALUES", "PAIRS", "PERCENT_RANK", "PI",
		"POLY_LENGTH", "POSINFIF", "POSITION", "POWER", "RADIANS", "RANDOM",
		"RANK", "RATIO_TO_REPORT", "REGEXP_CONTAINS", "REGEXP_LIKE",
		"REGEXP_MATCHES", "REGEXP_POSITION", "REGEXP_REPLACE", "REGEXP_SPLIT",
		"REGEX_CONTAINS", "REGEX_LIKE", "REGEX_MATCHES", "REGEX_POSITION",
		"REGEX_REPLACE", "REGEX_SPLIT", "REPEAT", "REPLACE", "REVERSE", "ROUND",
		"ROW_NUMBER", "RTRIM", "SEARCH", "SEARCH_META", "SEARCH_SCORE", "SIGN",
		"SIN", "SPLIT", "SQRT", "STDDEV", "STDDEV_POP", "STDDEV_SAMP",
		"STR_TO_DURATION", "STR_TO_MILLIS", "STR_TO_TZ", "STR_TO_UTC",
		"STR_TO_ZONE_NAME", "SUBSTR", "SUFFIXES", "SUM", "TAN", "TITLE",
		"TOARRAY", "TOATOM", "TOBOOLEAN", "TOKENS", "TOKENS", "TONUMBER",
		"TOOBJECT", "TOSTRING", "TRIM", "TRUNC", "UPPER", "UUID", "VARIANCE",
		"VARIANCE_POP", "VARIANCE_SAMP", "VAR_POP", "VAR_SAMP",
		"WEEKDAY_MILLIS", "WEEKDAY_STR", "CAST"
	],
	MS = ["ADVISE", "ALL", "ALTER", "ANALYZE", "AND", "ANY", "ARRAY", "AS",
		"ASC", "AT", "BEGIN", "BETWEEN", "BINARY", "BOOLEAN", "BREAK", "BUCKET",
		"BUILD", "BY", "CALL", "CASE", "CAST", "CLUSTER", "COLLATE",
		"COLLECTION", "COMMIT", "COMMITTED", "CONNECT", "CONTINUE",
		"CORRELATED", "COVER", "CREATE", "CURRENT", "DATABASE", "DATASET",
		"DATASTORE", "DECLARE", "DECREMENT", "DELETE", "DERIVED", "DESC",
		"DESCRIBE", "DISTINCT", "DO", "DROP", "EACH", "ELEMENT", "ELSE", "END",
		"EVERY", "EXCEPT", "EXCLUDE", "EXECUTE", "EXISTS", "EXPLAIN", "FALSE",
		"FETCH", "FILTER", "FIRST", "FLATTEN", "FLUSH", "FOLLOWING", "FOR",
		"FORCE", "FROM", "FTS", "FUNCTION", "GOLANG", "GRANT", "GROUP",
		"GROUPS", "GSI", "HASH", "HAVING", "IF", "IGNORE", "ILIKE", "IN",
		"INCLUDE", "INCREMENT", "INDEX", "INFER", "INLINE", "INNER", "INSERT",
		"INTERSECT", "INTO", "IS", "ISOLATION", "JAVASCRIPT", "JOIN", "KEY",
		"KEYS", "KEYSPACE", "KNOWN", "LANGUAGE", "LAST", "LEFT", "LET",
		"LETTING", "LEVEL", "LIKE", "LIMIT", "LSM", "MAP", "MAPPING", "MATCHED",
		"MATERIALIZED", "MERGE", "MINUS", "MISSING", "NAMESPACE", "NEST", "NL",
		"NO", "NOT", "NTH_VALUE", "NULL", "NULLS", "NUMBER", "OBJECT", "OFFSET",
		"ON", "OPTION", "OPTIONS", "OR", "ORDER", "OTHERS", "OUTER", "OVER",
		"PARSE", "PARTITION", "PASSWORD", "PATH", "POOL", "PRECEDING",
		"PREPARE", "PRIMARY", "PRIVATE", "PRIVILEGE", "PROBE", "PROCEDURE",
		"PUBLIC", "RANGE", "RAW", "REALM", "REDUCE", "RENAME", "RESPECT",
		"RETURN", "RETURNING", "REVOKE", "RIGHT", "ROLE", "ROLLBACK", "ROW",
		"ROWS", "SATISFIES", "SAVEPOINT", "SCHEMA", "SCOPE", "SELECT", "SELF",
		"SEMI", "SET", "SHOW", "SOME", "START", "STATISTICS", "STRING",
		"SYSTEM", "THEN", "TIES", "TO", "TRAN", "TRANSACTION", "TRIGGER",
		"TRUE", "TRUNCATE", "UNBOUNDED", "UNDER", "UNION", "UNIQUE", "UNKNOWN",
		"UNNEST", "UNSET", "UPDATE", "UPSERT", "USE", "USER", "USING",
		"VALIDATE", "VALUE", "VALUED", "VALUES", "VIA", "VIEW", "WHEN", "WHERE",
		"WHILE", "WINDOW", "WITH", "WITHIN", "WORK", "XOR"
	],
	US = [],
	mS = v(["SELECT [ALL | DISTINCT]"]),
	hS = v(["WITH", "FROM", "WHERE", "GROUP BY", "HAVING", "WINDOW",
		"PARTITION BY", "ORDER BY", "LIMIT", "OFFSET", "INSERT INTO",
		"VALUES", "SET", "MERGE INTO", "WHEN [NOT] MATCHED THEN",
		"UPDATE SET", "INSERT", "NEST", "UNNEST", "RETURNING"
	]),
	or = v(["UPDATE", "DELETE FROM", "SET SCHEMA", "ADVISE", "ALTER INDEX",
		"BEGIN TRANSACTION", "BUILD INDEX", "COMMIT TRANSACTION",
		"CREATE COLLECTION", "CREATE FUNCTION", "CREATE INDEX",
		"CREATE PRIMARY INDEX", "CREATE SCOPE", "DROP COLLECTION",
		"DROP FUNCTION", "DROP INDEX", "DROP PRIMARY INDEX", "DROP SCOPE",
		"EXECUTE", "EXECUTE FUNCTION", "EXPLAIN", "GRANT", "INFER",
		"PREPARE", "REVOKE", "ROLLBACK TRANSACTION", "SAVEPOINT",
		"SET TRANSACTION", "UPDATE STATISTICS", "UPSERT", "LET",
		"SET CURRENT SCHEMA", "SHOW", "USE [PRIMARY] KEYS"
	]),
	GS = v(["UNION [ALL]", "EXCEPT [ALL]", "INTERSECT [ALL]"]),
	gS = v(["JOIN", "{LEFT | RIGHT} [OUTER] JOIN", "INNER JOIN"]),
	HS = v(["{ROWS | RANGE | GROUPS} BETWEEN"]),
	bS = {
		name: "n1ql",
		tokenizerOptions: {
			reservedSelect: mS,
			reservedClauses: [...hS, ...or],
			reservedSetOperations: GS,
			reservedJoins: gS,
			reservedPhrases: HS,
			supportsXor: !0,
			reservedKeywords: MS,
			reservedDataTypes: US,
			reservedFunctionNames: pS,
			stringTypes: ['""-bs', "''-bs"],
			identTypes: ["``"],
			extraParens: ["[]", "{}"],
			paramTypes: {
				positional: !0,
				numbered: ["$"],
				named: ["$"]
			},
			lineCommentTypes: ["#", "--"],
			operators: ["%", "==", ":", "||"]
		},
		formatOptions: {
			onelineClauses: or
		}
	},
	yS = ["ADD", "AGENT", "AGGREGATE", "ALL", "ALTER", "AND", "ANY", "ARROW",
		"AS", "ASC", "AT", "ATTRIBUTE", "AUTHID", "AVG", "BEGIN", "BETWEEN",
		"BLOCK", "BODY", "BOTH", "BOUND", "BULK", "BY", "BYTE", "CALL",
		"CALLING", "CASCADE", "CASE", "CHARSET", "CHARSETFORM", "CHARSETID",
		"CHECK", "CLOSE", "CLUSTER", "CLUSTERS", "COLAUTH", "COLLECT",
		"COLUMNS", "COMMENT", "COMMIT", "COMMITTED", "COMPILED", "COMPRESS",
		"CONNECT", "CONSTANT", "CONSTRUCTOR", "CONTEXT", "CONVERT", "COUNT",
		"CRASH", "CREATE", "CURRENT", "CURSOR", "CUSTOMDATUM", "DANGLING",
		"DATA", "DAY", "DECLARE", "DEFAULT", "DEFINE", "DELETE", "DESC",
		"DETERMINISTIC", "DISTINCT", "DROP", "DURATION", "ELEMENT", "ELSE",
		"ELSIF", "EMPTY", "END", "ESCAPE", "EXCEPT", "EXCEPTION", "EXCEPTIONS",
		"EXCLUSIVE", "EXECUTE", "EXISTS", "EXIT", "EXTERNAL", "FETCH", "FINAL",
		"FIXED", "FOR", "FORALL", "FORCE", "FORM", "FROM", "FUNCTION",
		"GENERAL", "GOTO", "GRANT", "GROUP", "HASH", "HAVING", "HEAP", "HIDDEN",
		"HOUR", "IDENTIFIED", "IF", "IMMEDIATE", "IN", "INCLUDING", "INDEX",
		"INDEXES", "INDICATOR", "INDICES", "INFINITE", "INSERT", "INSTANTIABLE",
		"INTERFACE", "INTERSECT", "INTERVAL", "INTO", "INVALIDATE", "IS",
		"ISOLATION", "JAVA", "LANGUAGE", "LARGE", "LEADING", "LENGTH", "LEVEL",
		"LIBRARY", "LIKE", "LIKE2", "LIKE4", "LIKEC", "LIMIT", "LIMITED",
		"LOCAL", "LOCK", "LOOP", "MAP", "MAX", "MAXLEN", "MEMBER", "MERGE",
		"MIN", "MINUS", "MINUTE", "MOD", "MODE", "MODIFY", "MONTH", "MULTISET",
		"NAME", "NAN", "NATIONAL", "NATIVE", "NEW", "NOCOMPRESS", "NOCOPY",
		"NOT", "NOWAIT", "NULL", "OBJECT", "OCICOLL", "OCIDATE", "OCIDATETIME",
		"OCIDURATION", "OCIINTERVAL", "OCILOBLOCATOR", "OCINUMBER", "OCIRAW",
		"OCIREF", "OCIREFCURSOR", "OCIROWID", "OCISTRING", "OCITYPE", "OF",
		"ON", "ONLY", "OPAQUE", "OPEN", "OPERATOR", "OPTION", "OR", "ORACLE",
		"ORADATA", "ORDER", "OVERLAPS", "ORGANIZATION", "ORLANY", "ORLVARY",
		"OTHERS", "OUT", "OVERRIDING", "PACKAGE", "PARALLEL_ENABLE",
		"PARAMETER", "PARAMETERS", "PARTITION", "PASCAL", "PIPE", "PIPELINED",
		"PRAGMA", "PRIOR", "PRIVATE", "PROCEDURE", "PUBLIC", "RAISE", "RANGE",
		"READ", "RECORD", "REF", "REFERENCE", "REM", "REMAINDER", "RENAME",
		"RESOURCE", "RESULT", "RETURN", "RETURNING", "REVERSE", "REVOKE",
		"ROLLBACK", "ROW", "SAMPLE", "SAVE", "SAVEPOINT", "SB1", "SB2", "SB4",
		"SECOND", "SEGMENT", "SELECT", "SELF", "SEPARATE", "SEQUENCE",
		"SERIALIZABLE", "SET", "SHARE", "SHORT", "SIZE", "SIZE_T", "SOME",
		"SPARSE", "SQL", "SQLCODE", "SQLDATA", "SQLNAME", "SQLSTATE",
		"STANDARD", "START", "STATIC", "STDDEV", "STORED", "STRING", "STRUCT",
		"STYLE", "SUBMULTISET", "SUBPARTITION", "SUBSTITUTABLE", "SUBTYPE",
		"SUM", "SYNONYM", "TABAUTH", "TABLE", "TDO", "THE", "THEN", "TIME",
		"TIMEZONE_ABBR", "TIMEZONE_HOUR", "TIMEZONE_MINUTE", "TIMEZONE_REGION",
		"TO", "TRAILING", "TRANSAC", "TRANSACTIONAL", "TRUSTED", "TYPE", "UB1",
		"UB2", "UB4", "UNDER", "UNION", "UNIQUE", "UNSIGNED", "UNTRUSTED",
		"UPDATE", "USE", "USING", "VALIST", "VALUE", "VALUES", "VARIABLE",
		"VARIANCE", "VARRAY", "VIEW", "VIEWS", "VOID", "WHEN", "WHERE", "WHILE",
		"WITH", "WORK", "WRAPPED", "WRITE", "YEAR", "ZONE"
	],
	BS = ["ARRAY", "BFILE_BASE", "BINARY", "BLOB_BASE", "CHAR VARYING",
		"CHAR_BASE", "CHAR", "CHARACTER VARYING", "CHARACTER", "CLOB_BASE",
		"DATE_BASE", "DATE", "DECIMAL", "DOUBLE", "FLOAT", "INT",
		"INTERVAL DAY", "INTERVAL YEAR", "LONG", "NATIONAL CHAR VARYING",
		"NATIONAL CHAR", "NATIONAL CHARACTER VARYING", "NATIONAL CHARACTER",
		"NCHAR VARYING", "NCHAR", "NCHAR", "NUMBER_BASE", "NUMBER", "NUMBERIC",
		"NVARCHAR", "PRECISION", "RAW", "TIMESTAMP", "UROWID", "VARCHAR",
		"VARCHAR2"
	],
	vS = ["ABS", "ACOS", "ASIN", "ATAN", "ATAN2", "BITAND", "CEIL", "COS",
		"COSH", "EXP", "FLOOR", "LN", "LOG", "MOD", "NANVL", "POWER",
		"REMAINDER", "ROUND", "SIGN", "SIN", "SINH", "SQRT", "TAN", "TANH",
		"TRUNC", "WIDTH_BUCKET", "CHR", "CONCAT", "INITCAP", "LOWER", "LPAD",
		"LTRIM", "NLS_INITCAP", "NLS_LOWER", "NLSSORT", "NLS_UPPER",
		"REGEXP_REPLACE", "REGEXP_SUBSTR", "REPLACE", "RPAD", "RTRIM",
		"SOUNDEX", "SUBSTR", "TRANSLATE", "TREAT", "TRIM", "UPPER",
		"NLS_CHARSET_DECL_LEN", "NLS_CHARSET_ID", "NLS_CHARSET_NAME", "ASCII",
		"INSTR", "LENGTH", "REGEXP_INSTR", "ADD_MONTHS", "CURRENT_DATE",
		"CURRENT_TIMESTAMP", "DBTIMEZONE", "EXTRACT", "FROM_TZ", "LAST_DAY",
		"LOCALTIMESTAMP", "MONTHS_BETWEEN", "NEW_TIME", "NEXT_DAY",
		"NUMTODSINTERVAL", "NUMTOYMINTERVAL", "ROUND", "SESSIONTIMEZONE",
		"SYS_EXTRACT_UTC", "SYSDATE", "SYSTIMESTAMP", "TO_CHAR", "TO_TIMESTAMP",
		"TO_TIMESTAMP_TZ", "TO_DSINTERVAL", "TO_YMINTERVAL", "TRUNC",
		"TZ_OFFSET", "GREATEST", "LEAST", "ASCIISTR", "BIN_TO_NUM", "CAST",
		"CHARTOROWID", "COMPOSE", "CONVERT", "DECOMPOSE", "HEXTORAW",
		"NUMTODSINTERVAL", "NUMTOYMINTERVAL", "RAWTOHEX", "RAWTONHEX",
		"ROWIDTOCHAR", "ROWIDTONCHAR", "SCN_TO_TIMESTAMP", "TIMESTAMP_TO_SCN",
		"TO_BINARY_DOUBLE", "TO_BINARY_FLOAT", "TO_CHAR", "TO_CLOB", "TO_DATE",
		"TO_DSINTERVAL", "TO_LOB", "TO_MULTI_BYTE", "TO_NCHAR", "TO_NCLOB",
		"TO_NUMBER", "TO_DSINTERVAL", "TO_SINGLE_BYTE", "TO_TIMESTAMP",
		"TO_TIMESTAMP_TZ", "TO_YMINTERVAL", "TO_YMINTERVAL", "TRANSLATE",
		"UNISTR", "BFILENAME", "EMPTY_BLOB,", "EMPTY_CLOB", "CARDINALITY",
		"COLLECT", "POWERMULTISET", "POWERMULTISET_BY_CARDINALITY", "SET",
		"SYS_CONNECT_BY_PATH", "CLUSTER_ID", "CLUSTER_PROBABILITY",
		"CLUSTER_SET", "FEATURE_ID", "FEATURE_SET", "FEATURE_VALUE",
		"PREDICTION", "PREDICTION_COST", "PREDICTION_DETAILS",
		"PREDICTION_PROBABILITY", "PREDICTION_SET", "APPENDCHILDXML",
		"DELETEXML", "DEPTH", "EXTRACT", "EXISTSNODE", "EXTRACTVALUE",
		"INSERTCHILDXML", "INSERTXMLBEFORE", "PATH", "SYS_DBURIGEN",
		"SYS_XMLAGG", "SYS_XMLGEN", "UPDATEXML", "XMLAGG", "XMLCDATA",
		"XMLCOLATTVAL", "XMLCOMMENT", "XMLCONCAT", "XMLFOREST", "XMLPARSE",
		"XMLPI", "XMLQUERY", "XMLROOT", "XMLSEQUENCE", "XMLSERIALIZE",
		"XMLTABLE", "XMLTRANSFORM", "DECODE", "DUMP", "ORA_HASH", "VSIZE",
		"COALESCE", "LNNVL", "NULLIF", "NVL", "NVL2", "SYS_CONTEXT", "SYS_GUID",
		"SYS_TYPEID", "UID", "USER", "USERENV", "AVG", "COLLECT", "CORR",
		"CORR_S", "CORR_K", "COUNT", "COVAR_POP", "COVAR_SAMP", "CUME_DIST",
		"DENSE_RANK", "FIRST", "GROUP_ID", "GROUPING", "GROUPING_ID", "LAST",
		"MAX", "MEDIAN", "MIN", "PERCENTILE_CONT", "PERCENTILE_DISC",
		"PERCENT_RANK", "RANK", "REGR_SLOPE", "REGR_INTERCEPT", "REGR_COUNT",
		"REGR_R2", "REGR_AVGX", "REGR_AVGY", "REGR_SXX", "REGR_SYY", "REGR_SXY",
		"STATS_BINOMIAL_TEST", "STATS_CROSSTAB", "STATS_F_TEST",
		"STATS_KS_TEST", "STATS_MODE", "STATS_MW_TEST", "STATS_ONE_WAY_ANOVA",
		"STATS_T_TEST_ONE", "STATS_T_TEST_PAIRED", "STATS_T_TEST_INDEP",
		"STATS_T_TEST_INDEPU", "STATS_WSR_TEST", "STDDEV", "STDDEV_POP",
		"STDDEV_SAMP", "SUM", "VAR_POP", "VAR_SAMP", "VARIANCE", "FIRST_VALUE",
		"LAG", "LAST_VALUE", "LEAD", "NTILE", "RATIO_TO_REPORT", "ROW_NUMBER",
		"DEREF", "MAKE_REF", "REF", "REFTOHEX", "VALUE", "CV",
		"ITERATION_NUMBER", "PRESENTNNV", "PRESENTV", "PREVIOUS"
	],
	FS = v(["SELECT [ALL | DISTINCT | UNIQUE]"]),
	YS = v(["WITH", "FROM", "WHERE", "GROUP BY", "HAVING", "PARTITION BY",
		"ORDER [SIBLINGS] BY", "OFFSET", "FETCH {FIRST | NEXT}",
		"FOR UPDATE [OF]", "INSERT [INTO | ALL INTO]", "VALUES", "SET",
		"MERGE [INTO]", "WHEN [NOT] MATCHED [THEN]", "UPDATE SET",
		"RETURNING"
	]),
	Or = v([
		"CREATE [GLOBAL TEMPORARY | PRIVATE TEMPORARY | SHARDED | DUPLICATED | IMMUTABLE BLOCKCHAIN | BLOCKCHAIN | IMMUTABLE] TABLE"
	]),
	Zt = v([
		"CREATE [OR REPLACE] [NO FORCE | FORCE] [EDITIONING | EDITIONABLE | EDITIONABLE EDITIONING | NONEDITIONABLE] VIEW",
		"CREATE MATERIALIZED VIEW", "UPDATE [ONLY]", "DELETE FROM [ONLY]",
		"DROP TABLE", "ALTER TABLE", "ADD",
		"DROP {COLUMN | UNUSED COLUMNS | COLUMNS CONTINUE}", "MODIFY",
		"RENAME TO", "RENAME COLUMN", "TRUNCATE TABLE", "SET SCHEMA",
		"BEGIN", "CONNECT BY", "DECLARE", "EXCEPT", "EXCEPTION", "LOOP",
		"START WITH"
	]),
	VS = v(["UNION [ALL]", "EXCEPT", "INTERSECT"]),
	WS = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "NATURAL [INNER] JOIN",
		"NATURAL {LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{CROSS | OUTER} APPLY"
	]),
	wS = v(["ON {UPDATE | DELETE} [SET NULL]", "ON COMMIT",
		"{ROWS | RANGE} BETWEEN"
	]),
	$S = {
		name: "plsql",
		tokenizerOptions: {
			reservedSelect: FS,
			reservedClauses: [...YS, ...Or, ...Zt],
			reservedSetOperations: VS,
			reservedJoins: WS,
			reservedPhrases: wS,
			supportsXor: !0,
			reservedKeywords: yS,
			reservedDataTypes: BS,
			reservedFunctionNames: vS,
			stringTypes: [{
				quote: "''-qq",
				prefixes: ["N"]
			}, {
				quote: "q''",
				prefixes: ["N"]
			}],
			identTypes: ['""-qq'],
			identChars: {
				rest: "$#"
			},
			variableTypes: [{
				regex: "&{1,2}[A-Za-z][A-Za-z0-9_$#]*"
			}],
			paramTypes: {
				numbered: [":"],
				named: [":"]
			},
			paramChars: {},
			operators: ["**", ":=", "%", "~=", "^=", ">>", "<<", "=>", "@",
				"||"
			],
			postProcess: xS
		},
		formatOptions: {
			alwaysDenseOperators: ["@"],
			onelineClauses: [...Or, ...Zt],
			tabularOnelineClauses: Zt
		}
	};

function xS(E) {
	let e = tt;
	return E.map(T => FE.SET(T) && FE.BY(e) ? AE(EE({}, T), {
		type: "RESERVED_KEYWORD"
	}) : (wR(T.type) && (e = T), T))
}
var XS = ["ABS", "ACOS", "ACOSD", "ACOSH", "ASIN", "ASIND", "ASINH", "ATAN",
		"ATAN2", "ATAN2D", "ATAND", "ATANH", "CBRT", "CEIL", "CEILING", "COS",
		"COSD", "COSH", "COT", "COTD", "DEGREES", "DIV", "EXP", "FACTORIAL",
		"FLOOR", "GCD", "LCM", "LN", "LOG", "LOG10", "MIN_SCALE", "MOD", "PI",
		"POWER", "RADIANS", "RANDOM", "ROUND", "SCALE", "SETSEED", "SIGN",
		"SIN", "SIND", "SINH", "SQRT", "TAN", "TAND", "TANH", "TRIM_SCALE",
		"TRUNC", "WIDTH_BUCKET", "ABS", "ASCII", "BIT_LENGTH", "BTRIM",
		"CHARACTER_LENGTH", "CHAR_LENGTH", "CHR", "CONCAT", "CONCAT_WS",
		"FORMAT", "INITCAP", "LEFT", "LENGTH", "LOWER", "LPAD", "LTRIM", "MD5",
		"NORMALIZE", "OCTET_LENGTH", "OVERLAY", "PARSE_IDENT",
		"PG_CLIENT_ENCODING", "POSITION", "QUOTE_IDENT", "QUOTE_LITERAL",
		"QUOTE_NULLABLE", "REGEXP_MATCH", "REGEXP_MATCHES", "REGEXP_REPLACE",
		"REGEXP_SPLIT_TO_ARRAY", "REGEXP_SPLIT_TO_TABLE", "REPEAT", "REPLACE",
		"REVERSE", "RIGHT", "RPAD", "RTRIM", "SPLIT_PART", "SPRINTF",
		"STARTS_WITH", "STRING_AGG", "STRING_TO_ARRAY", "STRING_TO_TABLE",
		"STRPOS", "SUBSTR", "SUBSTRING", "TO_ASCII", "TO_HEX", "TRANSLATE",
		"TRIM", "UNISTR", "UPPER", "BIT_COUNT", "BIT_LENGTH", "BTRIM",
		"CONVERT", "CONVERT_FROM", "CONVERT_TO", "DECODE", "ENCODE", "GET_BIT",
		"GET_BYTE", "LENGTH", "LTRIM", "MD5", "OCTET_LENGTH", "OVERLAY",
		"POSITION", "RTRIM", "SET_BIT", "SET_BYTE", "SHA224", "SHA256",
		"SHA384", "SHA512", "STRING_AGG", "SUBSTR", "SUBSTRING", "TRIM",
		"BIT_COUNT", "BIT_LENGTH", "GET_BIT", "LENGTH", "OCTET_LENGTH",
		"OVERLAY", "POSITION", "SET_BIT", "SUBSTRING", "REGEXP_MATCH",
		"REGEXP_MATCHES", "REGEXP_REPLACE", "REGEXP_SPLIT_TO_ARRAY",
		"REGEXP_SPLIT_TO_TABLE", "TO_CHAR", "TO_DATE", "TO_NUMBER",
		"TO_TIMESTAMP", "CLOCK_TIMESTAMP", "CURRENT_DATE", "CURRENT_TIME",
		"CURRENT_TIMESTAMP", "DATE_BIN", "DATE_PART", "DATE_TRUNC", "EXTRACT",
		"ISFINITE", "JUSTIFY_DAYS", "JUSTIFY_HOURS", "JUSTIFY_INTERVAL",
		"LOCALTIME", "LOCALTIMESTAMP", "MAKE_DATE", "MAKE_INTERVAL",
		"MAKE_TIME", "MAKE_TIMESTAMP", "MAKE_TIMESTAMPTZ", "NOW", "PG_SLEEP",
		"PG_SLEEP_FOR", "PG_SLEEP_UNTIL", "STATEMENT_TIMESTAMP", "TIMEOFDAY",
		"TO_TIMESTAMP", "TRANSACTION_TIMESTAMP", "ENUM_FIRST", "ENUM_LAST",
		"ENUM_RANGE", "AREA", "BOUND_BOX", "BOX", "CENTER", "CIRCLE",
		"DIAGONAL", "DIAMETER", "HEIGHT", "ISCLOSED", "ISOPEN", "LENGTH",
		"LINE", "LSEG", "NPOINTS", "PATH", "PCLOSE", "POINT", "POLYGON",
		"POPEN", "RADIUS", "SLOPE", "WIDTH", "ABBREV", "BROADCAST", "FAMILY",
		"HOST", "HOSTMASK", "INET_MERGE", "INET_SAME_FAMILY",
		"MACADDR8_SET7BIT", "MASKLEN", "NETMASK", "NETWORK", "SET_MASKLEN",
		"TRUNC", "ARRAY_TO_TSVECTOR", "GET_CURRENT_TS_CONFIG",
		"JSONB_TO_TSVECTOR", "JSON_TO_TSVECTOR", "LENGTH", "NUMNODE",
		"PHRASETO_TSQUERY", "PLAINTO_TSQUERY", "QUERYTREE", "SETWEIGHT",
		"STRIP", "TO_TSQUERY", "TO_TSVECTOR", "TSQUERY_PHRASE",
		"TSVECTOR_TO_ARRAY", "TS_DEBUG", "TS_DELETE", "TS_FILTER",
		"TS_HEADLINE", "TS_LEXIZE", "TS_PARSE", "TS_RANK", "TS_RANK_CD",
		"TS_REWRITE", "TS_STAT", "TS_TOKEN_TYPE", "WEBSEARCH_TO_TSQUERY",
		"UUID", "CURSOR_TO_XML", "CURSOR_TO_XMLSCHEMA", "DATABASE_TO_XML",
		"DATABASE_TO_XMLSCHEMA", "DATABASE_TO_XML_AND_XMLSCHEMA", "NEXTVAL",
		"QUERY_TO_XML", "QUERY_TO_XMLSCHEMA", "QUERY_TO_XML_AND_XMLSCHEMA",
		"SCHEMA_TO_XML", "SCHEMA_TO_XMLSCHEMA", "SCHEMA_TO_XML_AND_XMLSCHEMA",
		"STRING", "TABLE_TO_XML", "TABLE_TO_XMLSCHEMA",
		"TABLE_TO_XML_AND_XMLSCHEMA", "XMLAGG", "XMLCOMMENT", "XMLCONCAT",
		"XMLELEMENT", "XMLEXISTS", "XMLFOREST", "XMLPARSE", "XMLPI", "XMLROOT",
		"XMLSERIALIZE", "XMLTABLE", "XML_IS_WELL_FORMED",
		"XML_IS_WELL_FORMED_CONTENT", "XML_IS_WELL_FORMED_DOCUMENT", "XPATH",
		"XPATH_EXISTS", "ARRAY_TO_JSON", "JSONB_AGG", "JSONB_ARRAY_ELEMENTS",
		"JSONB_ARRAY_ELEMENTS_TEXT", "JSONB_ARRAY_LENGTH", "JSONB_BUILD_ARRAY",
		"JSONB_BUILD_OBJECT", "JSONB_EACH", "JSONB_EACH_TEXT",
		"JSONB_EXTRACT_PATH", "JSONB_EXTRACT_PATH_TEXT", "JSONB_INSERT",
		"JSONB_OBJECT", "JSONB_OBJECT_AGG", "JSONB_OBJECT_KEYS",
		"JSONB_PATH_EXISTS", "JSONB_PATH_EXISTS_TZ", "JSONB_PATH_MATCH",
		"JSONB_PATH_MATCH_TZ", "JSONB_PATH_QUERY", "JSONB_PATH_QUERY_ARRAY",
		"JSONB_PATH_QUERY_ARRAY_TZ", "JSONB_PATH_QUERY_FIRST",
		"JSONB_PATH_QUERY_FIRST_TZ", "JSONB_PATH_QUERY_TZ",
		"JSONB_POPULATE_RECORD", "JSONB_POPULATE_RECORDSET", "JSONB_PRETTY",
		"JSONB_SET", "JSONB_SET_LAX", "JSONB_STRIP_NULLS", "JSONB_TO_RECORD",
		"JSONB_TO_RECORDSET", "JSONB_TYPEOF", "JSON_AGG", "JSON_ARRAY_ELEMENTS",
		"JSON_ARRAY_ELEMENTS_TEXT", "JSON_ARRAY_LENGTH", "JSON_BUILD_ARRAY",
		"JSON_BUILD_OBJECT", "JSON_EACH", "JSON_EACH_TEXT", "JSON_EXTRACT_PATH",
		"JSON_EXTRACT_PATH_TEXT", "JSON_OBJECT", "JSON_OBJECT_AGG",
		"JSON_OBJECT_KEYS", "JSON_POPULATE_RECORD", "JSON_POPULATE_RECORDSET",
		"JSON_STRIP_NULLS", "JSON_TO_RECORD", "JSON_TO_RECORDSET",
		"JSON_TYPEOF", "ROW_TO_JSON", "TO_JSON", "TO_JSONB", "TO_TIMESTAMP",
		"CURRVAL", "LASTVAL", "NEXTVAL", "SETVAL", "COALESCE", "GREATEST",
		"LEAST", "NULLIF", "ARRAY_AGG", "ARRAY_APPEND", "ARRAY_CAT",
		"ARRAY_DIMS", "ARRAY_FILL", "ARRAY_LENGTH", "ARRAY_LOWER",
		"ARRAY_NDIMS", "ARRAY_POSITION", "ARRAY_POSITIONS", "ARRAY_PREPEND",
		"ARRAY_REMOVE", "ARRAY_REPLACE", "ARRAY_TO_STRING", "ARRAY_UPPER",
		"CARDINALITY", "STRING_TO_ARRAY", "TRIM_ARRAY", "UNNEST", "ISEMPTY",
		"LOWER", "LOWER_INC", "LOWER_INF", "MULTIRANGE", "RANGE_MERGE", "UPPER",
		"UPPER_INC", "UPPER_INF", "ARRAY_AGG", "AVG", "BIT_AND", "BIT_OR",
		"BIT_XOR", "BOOL_AND", "BOOL_OR", "COALESCE", "CORR", "COUNT",
		"COVAR_POP", "COVAR_SAMP", "CUME_DIST", "DENSE_RANK", "EVERY",
		"GROUPING", "JSONB_AGG", "JSONB_OBJECT_AGG", "JSON_AGG",
		"JSON_OBJECT_AGG", "MAX", "MIN", "MODE", "PERCENTILE_CONT",
		"PERCENTILE_DISC", "PERCENT_RANK", "RANGE_AGG", "RANGE_INTERSECT_AGG",
		"RANK", "REGR_AVGX", "REGR_AVGY", "REGR_COUNT", "REGR_INTERCEPT",
		"REGR_R2", "REGR_SLOPE", "REGR_SXX", "REGR_SXY", "REGR_SYY", "STDDEV",
		"STDDEV_POP", "STDDEV_SAMP", "STRING_AGG", "SUM", "TO_JSON", "TO_JSONB",
		"VARIANCE", "VAR_POP", "VAR_SAMP", "XMLAGG", "CUME_DIST", "DENSE_RANK",
		"FIRST_VALUE", "LAG", "LAST_VALUE", "LEAD", "NTH_VALUE", "NTILE",
		"PERCENT_RANK", "RANK", "ROW_NUMBER", "GENERATE_SERIES",
		"GENERATE_SUBSCRIPTS", "ACLDEFAULT", "ACLEXPLODE", "COL_DESCRIPTION",
		"CURRENT_CATALOG", "CURRENT_DATABASE", "CURRENT_QUERY", "CURRENT_ROLE",
		"CURRENT_SCHEMA", "CURRENT_SCHEMAS", "CURRENT_USER", "FORMAT_TYPE",
		"HAS_ANY_COLUMN_PRIVILEGE", "HAS_COLUMN_PRIVILEGE",
		"HAS_DATABASE_PRIVILEGE", "HAS_FOREIGN_DATA_WRAPPER_PRIVILEGE",
		"HAS_FUNCTION_PRIVILEGE", "HAS_LANGUAGE_PRIVILEGE",
		"HAS_SCHEMA_PRIVILEGE", "HAS_SEQUENCE_PRIVILEGE",
		"HAS_SERVER_PRIVILEGE", "HAS_TABLESPACE_PRIVILEGE",
		"HAS_TABLE_PRIVILEGE", "HAS_TYPE_PRIVILEGE", "INET_CLIENT_ADDR",
		"INET_CLIENT_PORT", "INET_SERVER_ADDR", "INET_SERVER_PORT",
		"MAKEACLITEM", "OBJ_DESCRIPTION", "PG_BACKEND_PID", "PG_BLOCKING_PIDS",
		"PG_COLLATION_IS_VISIBLE", "PG_CONF_LOAD_TIME", "PG_CONTROL_CHECKPOINT",
		"PG_CONTROL_INIT", "PG_CONTROL_SYSTEM", "PG_CONVERSION_IS_VISIBLE",
		"PG_CURRENT_LOGFILE", "PG_CURRENT_SNAPSHOT", "PG_CURRENT_XACT_ID",
		"PG_CURRENT_XACT_ID_IF_ASSIGNED", "PG_DESCRIBE_OBJECT",
		"PG_FUNCTION_IS_VISIBLE", "PG_GET_CATALOG_FOREIGN_KEYS",
		"PG_GET_CONSTRAINTDEF", "PG_GET_EXPR", "PG_GET_FUNCTIONDEF",
		"PG_GET_FUNCTION_ARGUMENTS", "PG_GET_FUNCTION_IDENTITY_ARGUMENTS",
		"PG_GET_FUNCTION_RESULT", "PG_GET_INDEXDEF", "PG_GET_KEYWORDS",
		"PG_GET_OBJECT_ADDRESS", "PG_GET_OWNED_SEQUENCE", "PG_GET_RULEDEF",
		"PG_GET_SERIAL_SEQUENCE", "PG_GET_STATISTICSOBJDEF",
		"PG_GET_TRIGGERDEF", "PG_GET_USERBYID", "PG_GET_VIEWDEF", "PG_HAS_ROLE",
		"PG_IDENTIFY_OBJECT", "PG_IDENTIFY_OBJECT_AS_ADDRESS",
		"PG_INDEXAM_HAS_PROPERTY", "PG_INDEX_COLUMN_HAS_PROPERTY",
		"PG_INDEX_HAS_PROPERTY", "PG_IS_OTHER_TEMP_SCHEMA", "PG_JIT_AVAILABLE",
		"PG_LAST_COMMITTED_XACT", "PG_LISTENING_CHANNELS", "PG_MY_TEMP_SCHEMA",
		"PG_NOTIFICATION_QUEUE_USAGE", "PG_OPCLASS_IS_VISIBLE",
		"PG_OPERATOR_IS_VISIBLE", "PG_OPFAMILY_IS_VISIBLE",
		"PG_OPTIONS_TO_TABLE", "PG_POSTMASTER_START_TIME",
		"PG_SAFE_SNAPSHOT_BLOCKING_PIDS", "PG_SNAPSHOT_XIP", "PG_SNAPSHOT_XMAX",
		"PG_SNAPSHOT_XMIN", "PG_STATISTICS_OBJ_IS_VISIBLE",
		"PG_TABLESPACE_DATABASES", "PG_TABLESPACE_LOCATION",
		"PG_TABLE_IS_VISIBLE", "PG_TRIGGER_DEPTH", "PG_TS_CONFIG_IS_VISIBLE",
		"PG_TS_DICT_IS_VISIBLE", "PG_TS_PARSER_IS_VISIBLE",
		"PG_TS_TEMPLATE_IS_VISIBLE", "PG_TYPEOF", "PG_TYPE_IS_VISIBLE",
		"PG_VISIBLE_IN_SNAPSHOT", "PG_XACT_COMMIT_TIMESTAMP",
		"PG_XACT_COMMIT_TIMESTAMP_ORIGIN", "PG_XACT_STATUS", "PQSERVERVERSION",
		"ROW_SECURITY_ACTIVE", "SESSION_USER", "SHOBJ_DESCRIPTION",
		"TO_REGCLASS", "TO_REGCOLLATION", "TO_REGNAMESPACE", "TO_REGOPER",
		"TO_REGOPERATOR", "TO_REGPROC", "TO_REGPROCEDURE", "TO_REGROLE",
		"TO_REGTYPE", "TXID_CURRENT", "TXID_CURRENT_IF_ASSIGNED",
		"TXID_CURRENT_SNAPSHOT", "TXID_SNAPSHOT_XIP", "TXID_SNAPSHOT_XMAX",
		"TXID_SNAPSHOT_XMIN", "TXID_STATUS", "TXID_VISIBLE_IN_SNAPSHOT", "USER",
		"VERSION", "BRIN_DESUMMARIZE_RANGE", "BRIN_SUMMARIZE_NEW_VALUES",
		"BRIN_SUMMARIZE_RANGE", "CONVERT_FROM", "CURRENT_SETTING",
		"GIN_CLEAN_PENDING_LIST", "PG_ADVISORY_LOCK", "PG_ADVISORY_LOCK_SHARED",
		"PG_ADVISORY_UNLOCK", "PG_ADVISORY_UNLOCK_ALL",
		"PG_ADVISORY_UNLOCK_SHARED", "PG_ADVISORY_XACT_LOCK",
		"PG_ADVISORY_XACT_LOCK_SHARED", "PG_BACKUP_START_TIME",
		"PG_CANCEL_BACKEND", "PG_COLLATION_ACTUAL_VERSION",
		"PG_COLUMN_COMPRESSION", "PG_COLUMN_SIZE",
		"PG_COPY_LOGICAL_REPLICATION_SLOT", "PG_COPY_PHYSICAL_REPLICATION_SLOT",
		"PG_CREATE_LOGICAL_REPLICATION_SLOT",
		"PG_CREATE_PHYSICAL_REPLICATION_SLOT", "PG_CREATE_RESTORE_POINT",
		"PG_CURRENT_WAL_FLUSH_LSN", "PG_CURRENT_WAL_INSERT_LSN",
		"PG_CURRENT_WAL_LSN", "PG_DATABASE_SIZE", "PG_DROP_REPLICATION_SLOT",
		"PG_EXPORT_SNAPSHOT", "PG_FILENODE_RELATION",
		"PG_GET_WAL_REPLAY_PAUSE_STATE", "PG_IMPORT_SYSTEM_COLLATIONS",
		"PG_INDEXES_SIZE", "PG_IS_IN_BACKUP", "PG_IS_IN_RECOVERY",
		"PG_IS_WAL_REPLAY_PAUSED", "PG_LAST_WAL_RECEIVE_LSN",
		"PG_LAST_WAL_REPLAY_LSN", "PG_LAST_XACT_REPLAY_TIMESTAMP",
		"PG_LOGICAL_EMIT_MESSAGE", "PG_LOGICAL_SLOT_GET_BINARY_CHANGES",
		"PG_LOGICAL_SLOT_GET_CHANGES", "PG_LOGICAL_SLOT_PEEK_BINARY_CHANGES",
		"PG_LOGICAL_SLOT_PEEK_CHANGES", "PG_LOG_BACKEND_MEMORY_CONTEXTS",
		"PG_LS_ARCHIVE_STATUSDIR", "PG_LS_DIR", "PG_LS_LOGDIR", "PG_LS_TMPDIR",
		"PG_LS_WALDIR", "PG_PARTITION_ANCESTORS", "PG_PARTITION_ROOT",
		"PG_PARTITION_TREE", "PG_PROMOTE", "PG_READ_BINARY_FILE",
		"PG_READ_FILE", "PG_RELATION_FILENODE", "PG_RELATION_FILEPATH",
		"PG_RELATION_SIZE", "PG_RELOAD_CONF", "PG_REPLICATION_ORIGIN_ADVANCE",
		"PG_REPLICATION_ORIGIN_CREATE", "PG_REPLICATION_ORIGIN_DROP",
		"PG_REPLICATION_ORIGIN_OID", "PG_REPLICATION_ORIGIN_PROGRESS",
		"PG_REPLICATION_ORIGIN_SESSION_IS_SETUP",
		"PG_REPLICATION_ORIGIN_SESSION_PROGRESS",
		"PG_REPLICATION_ORIGIN_SESSION_RESET",
		"PG_REPLICATION_ORIGIN_SESSION_SETUP",
		"PG_REPLICATION_ORIGIN_XACT_RESET", "PG_REPLICATION_ORIGIN_XACT_SETUP",
		"PG_REPLICATION_SLOT_ADVANCE", "PG_ROTATE_LOGFILE", "PG_SIZE_BYTES",
		"PG_SIZE_PRETTY", "PG_START_BACKUP", "PG_STAT_FILE", "PG_STOP_BACKUP",
		"PG_SWITCH_WAL", "PG_TABLESPACE_SIZE", "PG_TABLE_SIZE",
		"PG_TERMINATE_BACKEND", "PG_TOTAL_RELATION_SIZE",
		"PG_TRY_ADVISORY_LOCK", "PG_TRY_ADVISORY_LOCK_SHARED",
		"PG_TRY_ADVISORY_XACT_LOCK", "PG_TRY_ADVISORY_XACT_LOCK_SHARED",
		"PG_WALFILE_NAME", "PG_WALFILE_NAME_OFFSET", "PG_WAL_LSN_DIFF",
		"PG_WAL_REPLAY_PAUSE", "PG_WAL_REPLAY_RESUME", "SET_CONFIG",
		"SUPPRESS_REDUNDANT_UPDATES_TRIGGER", "TSVECTOR_UPDATE_TRIGGER",
		"TSVECTOR_UPDATE_TRIGGER_COLUMN", "PG_EVENT_TRIGGER_DDL_COMMANDS",
		"PG_EVENT_TRIGGER_DROPPED_OBJECTS",
		"PG_EVENT_TRIGGER_TABLE_REWRITE_OID",
		"PG_EVENT_TRIGGER_TABLE_REWRITE_REASON", "PG_GET_OBJECT_ADDRESS",
		"PG_MCV_LIST_ITEMS", "CAST"
	],
	kS = ["ALL", "ANALYSE", "ANALYZE", "AND", "ANY", "AS", "ASC", "ASYMMETRIC",
		"AUTHORIZATION", "BETWEEN", "BINARY", "BOTH", "CASE", "CAST", "CHECK",
		"COLLATE", "COLLATION", "COLUMN", "CONCURRENTLY", "CONSTRAINT",
		"CREATE", "CROSS", "CURRENT_CATALOG", "CURRENT_DATE", "CURRENT_ROLE",
		"CURRENT_SCHEMA", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER",
		"DAY", "DEFAULT", "DEFERRABLE", "DESC", "DISTINCT", "DO", "ELSE", "END",
		"EXCEPT", "EXISTS", "FALSE", "FETCH", "FILTER", "FOR", "FOREIGN",
		"FREEZE", "FROM", "FULL", "GRANT", "GROUP", "HAVING", "HOUR", "ILIKE",
		"IN", "INITIALLY", "INNER", "INOUT", "INTERSECT", "INTO", "IS",
		"ISNULL", "JOIN", "LATERAL", "LEADING", "LEFT", "LIKE", "LIMIT",
		"LOCALTIME", "LOCALTIMESTAMP", "MINUTE", "MONTH", "NATURAL", "NOT",
		"NOTNULL", "NULL", "NULLIF", "OFFSET", "ON", "ONLY", "OR", "ORDER",
		"OUT", "OUTER", "OVER", "OVERLAPS", "PLACING", "PRIMARY", "REFERENCES",
		"RETURNING", "RIGHT", "ROW", "SECOND", "SELECT", "SESSION_USER",
		"SIMILAR", "SOME", "SYMMETRIC", "TABLE", "TABLESAMPLE", "THEN", "TO",
		"TRAILING", "TRUE", "UNION", "UNIQUE", "USER", "USING", "VALUES",
		"VARIADIC", "VERBOSE", "WHEN", "WHERE", "WINDOW", "WITH", "WITHIN",
		"WITHOUT", "YEAR"
	],
	KS = ["ARRAY", "BIGINT", "BIT", "BIT VARYING", "BOOL", "BOOLEAN", "CHAR",
		"CHARACTER", "CHARACTER VARYING", "DECIMAL", "DEC", "DOUBLE", "ENUM",
		"FLOAT", "INT", "INTEGER", "INTERVAL", "NCHAR", "NUMERIC", "PRECISION",
		"REAL", "SMALLINT", "TEXT", "TIME", "TIMESTAMP", "TIMESTAMPTZ",
		"VARCHAR", "XML", "ZONE"
	],
	JS = v(["SELECT [ALL | DISTINCT]"]),
	qS = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY [ALL | DISTINCT]",
		"HAVING", "WINDOW", "PARTITION BY", "ORDER BY", "LIMIT", "OFFSET",
		"FETCH {FIRST | NEXT}",
		"FOR {UPDATE | NO KEY UPDATE | SHARE | KEY SHARE} [OF]",
		"INSERT INTO", "VALUES", "DEFAULT VALUES", "SET", "RETURNING"
	]),
	ir = v([
		"CREATE [GLOBAL | LOCAL] [TEMPORARY | TEMP | UNLOGGED] TABLE [IF NOT EXISTS]"
	]),
	jt = v(["CREATE [OR REPLACE] [TEMP | TEMPORARY] [RECURSIVE] VIEW",
		"CREATE [MATERIALIZED] VIEW [IF NOT EXISTS]", "UPDATE [ONLY]",
		"WHERE CURRENT OF", "ON CONFLICT", "DELETE FROM [ONLY]",
		"DROP TABLE [IF EXISTS]", "ALTER TABLE [IF EXISTS] [ONLY]",
		"ALTER TABLE ALL IN TABLESPACE", "RENAME [COLUMN]", "RENAME TO",
		"ADD [COLUMN] [IF NOT EXISTS]", "DROP [COLUMN] [IF EXISTS]",
		"ALTER [COLUMN]", "SET DATA TYPE", "{SET | DROP} DEFAULT",
		"{SET | DROP} NOT NULL", "TRUNCATE [TABLE] [ONLY]", "SET SCHEMA",
		"AFTER", "ABORT", "ALTER AGGREGATE", "ALTER COLLATION",
		"ALTER CONVERSION", "ALTER DATABASE", "ALTER DEFAULT PRIVILEGES",
		"ALTER DOMAIN", "ALTER EVENT TRIGGER", "ALTER EXTENSION",
		"ALTER FOREIGN DATA WRAPPER", "ALTER FOREIGN TABLE",
		"ALTER FUNCTION", "ALTER GROUP", "ALTER INDEX", "ALTER LANGUAGE",
		"ALTER LARGE OBJECT", "ALTER MATERIALIZED VIEW", "ALTER OPERATOR",
		"ALTER OPERATOR CLASS", "ALTER OPERATOR FAMILY", "ALTER POLICY",
		"ALTER PROCEDURE", "ALTER PUBLICATION", "ALTER ROLE",
		"ALTER ROUTINE", "ALTER RULE", "ALTER SCHEMA", "ALTER SEQUENCE",
		"ALTER SERVER", "ALTER STATISTICS", "ALTER SUBSCRIPTION",
		"ALTER SYSTEM", "ALTER TABLESPACE",
		"ALTER TEXT SEARCH CONFIGURATION", "ALTER TEXT SEARCH DICTIONARY",
		"ALTER TEXT SEARCH PARSER", "ALTER TEXT SEARCH TEMPLATE",
		"ALTER TRIGGER", "ALTER TYPE", "ALTER USER", "ALTER USER MAPPING",
		"ALTER VIEW", "ANALYZE", "BEGIN", "CALL", "CHECKPOINT", "CLOSE",
		"CLUSTER", "COMMIT", "COMMIT PREPARED", "COPY",
		"CREATE ACCESS METHOD", "CREATE AGGREGATE", "CREATE CAST",
		"CREATE COLLATION", "CREATE CONVERSION", "CREATE DATABASE",
		"CREATE DOMAIN", "CREATE EVENT TRIGGER", "CREATE EXTENSION",
		"CREATE FOREIGN DATA WRAPPER", "CREATE FOREIGN TABLE",
		"CREATE FUNCTION", "CREATE GROUP", "CREATE INDEX",
		"CREATE LANGUAGE", "CREATE OPERATOR", "CREATE OPERATOR CLASS",
		"CREATE OPERATOR FAMILY", "CREATE POLICY", "CREATE PROCEDURE",
		"CREATE PUBLICATION", "CREATE ROLE", "CREATE RULE", "CREATE SCHEMA",
		"CREATE SEQUENCE", "CREATE SERVER", "CREATE STATISTICS",
		"CREATE SUBSCRIPTION", "CREATE TABLESPACE",
		"CREATE TEXT SEARCH CONFIGURATION", "CREATE TEXT SEARCH DICTIONARY",
		"CREATE TEXT SEARCH PARSER", "CREATE TEXT SEARCH TEMPLATE",
		"CREATE TRANSFORM", "CREATE TRIGGER", "CREATE TYPE", "CREATE USER",
		"CREATE USER MAPPING", "DEALLOCATE", "DECLARE", "DISCARD",
		"DROP ACCESS METHOD", "DROP AGGREGATE", "DROP CAST",
		"DROP COLLATION", "DROP CONVERSION", "DROP DATABASE", "DROP DOMAIN",
		"DROP EVENT TRIGGER", "DROP EXTENSION", "DROP FOREIGN DATA WRAPPER",
		"DROP FOREIGN TABLE", "DROP FUNCTION", "DROP GROUP", "DROP INDEX",
		"DROP LANGUAGE", "DROP MATERIALIZED VIEW", "DROP OPERATOR",
		"DROP OPERATOR CLASS", "DROP OPERATOR FAMILY", "DROP OWNED",
		"DROP POLICY", "DROP PROCEDURE", "DROP PUBLICATION", "DROP ROLE",
		"DROP ROUTINE", "DROP RULE", "DROP SCHEMA", "DROP SEQUENCE",
		"DROP SERVER", "DROP STATISTICS", "DROP SUBSCRIPTION",
		"DROP TABLESPACE", "DROP TEXT SEARCH CONFIGURATION",
		"DROP TEXT SEARCH DICTIONARY", "DROP TEXT SEARCH PARSER",
		"DROP TEXT SEARCH TEMPLATE", "DROP TRANSFORM", "DROP TRIGGER",
		"DROP TYPE", "DROP USER", "DROP USER MAPPING", "DROP VIEW",
		"EXECUTE", "EXPLAIN", "FETCH", "GRANT", "IMPORT FOREIGN SCHEMA",
		"LISTEN", "LOAD", "LOCK", "MOVE", "NOTIFY", "PREPARE",
		"PREPARE TRANSACTION", "REASSIGN OWNED",
		"REFRESH MATERIALIZED VIEW", "REINDEX", "RELEASE SAVEPOINT",
		"RESET", "REVOKE", "ROLLBACK", "ROLLBACK PREPARED",
		"ROLLBACK TO SAVEPOINT", "SAVEPOINT", "SECURITY LABEL",
		"SELECT INTO", "SET CONSTRAINTS", "SET ROLE",
		"SET SESSION AUTHORIZATION", "SET TRANSACTION", "SHOW",
		"START TRANSACTION", "UNLISTEN", "VACUUM"
	]),
	QS = v(["UNION [ALL | DISTINCT]", "EXCEPT [ALL | DISTINCT]",
		"INTERSECT [ALL | DISTINCT]"
	]),
	ZS = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "NATURAL [INNER] JOIN",
		"NATURAL {LEFT | RIGHT | FULL} [OUTER] JOIN"
	]),
	jS = v(["PRIMARY KEY", "GENERATED {ALWAYS | BY DEFAULT} AS IDENTITY",
		"ON {UPDATE | DELETE} [SET NULL | SET DEFAULT]",
		"{ROWS | RANGE | GROUPS} BETWEEN",
		"[TIMESTAMP | TIME] {WITH | WITHOUT} TIME ZONE",
		"IS [NOT] DISTINCT FROM"
	]),
	zS = {
		name: "postgresql",
		tokenizerOptions: {
			reservedSelect: JS,
			reservedClauses: [...qS, ...ir, ...jt],
			reservedSetOperations: QS,
			reservedJoins: ZS,
			reservedPhrases: jS,
			reservedKeywords: kS,
			reservedDataTypes: KS,
			reservedFunctionNames: XS,
			nestedBlockComments: !0,
			extraParens: ["[]"],
			stringTypes: ["$$", {
				quote: "''-qq",
				prefixes: ["U&"]
			}, {
				quote: "''-qq-bs",
				prefixes: ["E"],
				requirePrefix: !0
			}, {
				quote: "''-raw",
				prefixes: ["B", "X"],
				requirePrefix: !0
			}],
			identTypes: [{
				quote: '""-qq',
				prefixes: ["U&"]
			}],
			identChars: {
				rest: "$"
			},
			paramTypes: {
				numbered: ["$"]
			},
			operators: ["%", "^", "|/", "||/", "@", ":=", "&", "|", "#", "~",
				"<<", ">>", "~>~", "~<~", "~>=~", "~<=~", "@-@", "@@", "##",
				"<->", "&&", "&<", "&>", "<<|", "&<|", "|>>", "|&>", "<^",
				"^>", "?#", "?-", "?|", "?-|", "?||", "@>", "<@", "~=", "?",
				"@?", "?&", "->", "->>", "#>", "#>>", "#-", "=>", ">>=",
				"<<=", "~~", "~~*", "!~~", "!~~*", "~", "~*", "!~", "!~*",
				"-|-", "||", "@@@", "!!", "^@", "<%", "%>", "<<%", "%>>",
				"<<->", "<->>", "<<<->", "<->>>", "::", ":"
			]
		},
		formatOptions: {
			alwaysDenseOperators: ["::", ":"],
			onelineClauses: [...ir, ...jt],
			tabularOnelineClauses: jt
		}
	},
	eo = ["ANY_VALUE", "APPROXIMATE PERCENTILE_DISC", "AVG", "COUNT", "LISTAGG",
		"MAX", "MEDIAN", "MIN", "PERCENTILE_CONT", "STDDEV_SAMP", "STDDEV_POP",
		"SUM", "VAR_SAMP", "VAR_POP", "array", "array_concat", "array_flatten",
		"get_array_length", "split_to_array", "subarray", "BIT_AND", "BIT_OR",
		"BOOL_AND", "BOOL_OR", "COALESCE", "DECODE", "GREATEST", "LEAST", "NVL",
		"NVL2", "NULLIF", "ADD_MONTHS", "AT TIME ZONE", "CONVERT_TIMEZONE",
		"CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "DATE_CMP",
		"DATE_CMP_TIMESTAMP", "DATE_CMP_TIMESTAMPTZ", "DATE_PART_YEAR",
		"DATEADD", "DATEDIFF", "DATE_PART", "DATE_TRUNC", "EXTRACT", "GETDATE",
		"INTERVAL_CMP", "LAST_DAY", "MONTHS_BETWEEN", "NEXT_DAY", "SYSDATE",
		"TIMEOFDAY", "TIMESTAMP_CMP", "TIMESTAMP_CMP_DATE",
		"TIMESTAMP_CMP_TIMESTAMPTZ", "TIMESTAMPTZ_CMP", "TIMESTAMPTZ_CMP_DATE",
		"TIMESTAMPTZ_CMP_TIMESTAMP", "TIMEZONE", "TO_TIMESTAMP", "TRUNC",
		"AddBBox", "DropBBox", "GeometryType", "ST_AddPoint", "ST_Angle",
		"ST_Area", "ST_AsBinary", "ST_AsEWKB", "ST_AsEWKT", "ST_AsGeoJSON",
		"ST_AsText", "ST_Azimuth", "ST_Boundary", "ST_Collect", "ST_Contains",
		"ST_ContainsProperly", "ST_ConvexHull", "ST_CoveredBy", "ST_Covers",
		"ST_Crosses", "ST_Dimension", "ST_Disjoint", "ST_Distance",
		"ST_DistanceSphere", "ST_DWithin", "ST_EndPoint", "ST_Envelope",
		"ST_Equals", "ST_ExteriorRing", "ST_Force2D", "ST_Force3D",
		"ST_Force3DM", "ST_Force3DZ", "ST_Force4D", "ST_GeometryN",
		"ST_GeometryType", "ST_GeomFromEWKB", "ST_GeomFromEWKT",
		"ST_GeomFromText", "ST_GeomFromWKB", "ST_InteriorRingN",
		"ST_Intersects", "ST_IsPolygonCCW", "ST_IsPolygonCW", "ST_IsClosed",
		"ST_IsCollection", "ST_IsEmpty", "ST_IsSimple", "ST_IsValid",
		"ST_Length", "ST_LengthSphere", "ST_Length2D", "ST_LineFromMultiPoint",
		"ST_LineInterpolatePoint", "ST_M", "ST_MakeEnvelope", "ST_MakeLine",
		"ST_MakePoint", "ST_MakePolygon", "ST_MemSize", "ST_MMax", "ST_MMin",
		"ST_Multi", "ST_NDims", "ST_NPoints", "ST_NRings", "ST_NumGeometries",
		"ST_NumInteriorRings", "ST_NumPoints", "ST_Perimeter", "ST_Perimeter2D",
		"ST_Point", "ST_PointN", "ST_Points", "ST_Polygon", "ST_RemovePoint",
		"ST_Reverse", "ST_SetPoint", "ST_SetSRID", "ST_Simplify", "ST_SRID",
		"ST_StartPoint", "ST_Touches", "ST_Within", "ST_X", "ST_XMax",
		"ST_XMin", "ST_Y", "ST_YMax", "ST_YMin", "ST_Z", "ST_ZMax", "ST_ZMin",
		"SupportsBBox", "CHECKSUM", "FUNC_SHA1", "FNV_HASH", "MD5", "SHA",
		"SHA1", "SHA2", "HLL", "HLL_CREATE_SKETCH", "HLL_CARDINALITY",
		"HLL_COMBINE", "IS_VALID_JSON", "IS_VALID_JSON_ARRAY",
		"JSON_ARRAY_LENGTH", "JSON_EXTRACT_ARRAY_ELEMENT_TEXT",
		"JSON_EXTRACT_PATH_TEXT", "JSON_PARSE", "JSON_SERIALIZE", "ABS", "ACOS",
		"ASIN", "ATAN", "ATAN2", "CBRT", "CEILING", "CEIL", "COS", "COT",
		"DEGREES", "DEXP", "DLOG1", "DLOG10", "EXP", "FLOOR", "LN", "LOG",
		"MOD", "PI", "POWER", "RADIANS", "RANDOM", "ROUND", "SIN", "SIGN",
		"SQRT", "TAN", "TO_HEX", "TRUNC", "EXPLAIN_MODEL", "ASCII", "BPCHARCMP",
		"BTRIM", "BTTEXT_PATTERN_CMP", "CHAR_LENGTH", "CHARACTER_LENGTH",
		"CHARINDEX", "CHR", "COLLATE", "CONCAT", "CRC32", "DIFFERENCE",
		"INITCAP", "LEFT", "RIGHT", "LEN", "LENGTH", "LOWER", "LPAD", "RPAD",
		"LTRIM", "OCTETINDEX", "OCTET_LENGTH", "POSITION", "QUOTE_IDENT",
		"QUOTE_LITERAL", "REGEXP_COUNT", "REGEXP_INSTR", "REGEXP_REPLACE",
		"REGEXP_SUBSTR", "REPEAT", "REPLACE", "REPLICATE", "REVERSE", "RTRIM",
		"SOUNDEX", "SPLIT_PART", "STRPOS", "STRTOL", "SUBSTRING", "TEXTLEN",
		"TRANSLATE", "TRIM", "UPPER", "decimal_precision", "decimal_scale",
		"is_array", "is_bigint", "is_boolean", "is_char", "is_decimal",
		"is_float", "is_integer", "is_object", "is_scalar", "is_smallint",
		"is_varchar", "json_typeof", "AVG", "COUNT", "CUME_DIST", "DENSE_RANK",
		"FIRST_VALUE", "LAST_VALUE", "LAG", "LEAD", "LISTAGG", "MAX", "MEDIAN",
		"MIN", "NTH_VALUE", "NTILE", "PERCENT_RANK", "PERCENTILE_CONT",
		"PERCENTILE_DISC", "RANK", "RATIO_TO_REPORT", "ROW_NUMBER",
		"STDDEV_SAMP", "STDDEV_POP", "SUM", "VAR_SAMP", "VAR_POP", "CAST",
		"CONVERT", "TO_CHAR", "TO_DATE", "TO_NUMBER", "TEXT_TO_INT_ALT",
		"TEXT_TO_NUMERIC_ALT", "CHANGE_QUERY_PRIORITY",
		"CHANGE_SESSION_PRIORITY", "CHANGE_USER_PRIORITY", "CURRENT_SETTING",
		"PG_CANCEL_BACKEND", "PG_TERMINATE_BACKEND", "REBOOT_CLUSTER",
		"SET_CONFIG", "CURRENT_AWS_ACCOUNT", "CURRENT_DATABASE",
		"CURRENT_NAMESPACE", "CURRENT_SCHEMA", "CURRENT_SCHEMAS",
		"CURRENT_USER", "CURRENT_USER_ID", "HAS_ASSUMEROLE_PRIVILEGE",
		"HAS_DATABASE_PRIVILEGE", "HAS_SCHEMA_PRIVILEGE", "HAS_TABLE_PRIVILEGE",
		"PG_BACKEND_PID", "PG_GET_COLS", "PG_GET_GRANTEE_BY_IAM_ROLE",
		"PG_GET_IAM_ROLE_BY_USER", "PG_GET_LATE_BINDING_VIEW_COLS",
		"PG_LAST_COPY_COUNT", "PG_LAST_COPY_ID", "PG_LAST_UNLOAD_ID",
		"PG_LAST_QUERY_ID", "PG_LAST_UNLOAD_COUNT", "SESSION_USER", "SLICE_NUM",
		"USER", "VERSION"
	],
	Eo = ["AES128", "AES256", "ALL", "ALLOWOVERWRITE", "ANY", "AS", "ASC",
		"AUTHORIZATION", "BACKUP", "BETWEEN", "BINARY", "BOTH", "CHECK",
		"COLUMN", "CONSTRAINT", "CREATE", "CROSS", "DEFAULT", "DEFERRABLE",
		"DEFLATE", "DEFRAG", "DESC", "DISABLE", "DISTINCT", "DO", "ENABLE",
		"ENCODE", "ENCRYPT", "ENCRYPTION", "EXPLICIT", "FALSE", "FOR",
		"FOREIGN", "FREEZE", "FROM", "FULL", "GLOBALDICT256", "GLOBALDICT64K",
		"GROUP", "IDENTITY", "IGNORE", "ILIKE", "IN", "INITIALLY", "INNER",
		"INTO", "IS", "ISNULL", "LANGUAGE", "LEADING", "LIKE", "LIMIT",
		"LOCALTIME", "LOCALTIMESTAMP", "LUN", "LUNS", "MINUS", "NATURAL", "NEW",
		"NOT", "NOTNULL", "NULL", "NULLS", "OFF", "OFFLINE", "OFFSET", "OID",
		"OLD", "ON", "ONLY", "OPEN", "ORDER", "OUTER", "OVERLAPS", "PARALLEL",
		"PARTITION", "PERCENT", "PERMISSIONS", "PLACING", "PRIMARY", "RECOVER",
		"REFERENCES", "REJECTLOG", "RESORT", "RESPECT", "RESTORE", "SIMILAR",
		"SNAPSHOT", "SOME", "SYSTEM", "TABLE", "TAG", "TDES", "THEN",
		"TIMESTAMP", "TO", "TOP", "TRAILING", "TRUE", "UNIQUE", "USING",
		"VERBOSE", "WALLET", "WITHOUT", "ACCEPTANYDATE", "ACCEPTINVCHARS",
		"BLANKSASNULL", "DATEFORMAT", "EMPTYASNULL", "ENCODING", "ESCAPE",
		"EXPLICIT_IDS", "FILLRECORD", "IGNOREBLANKLINES", "IGNOREHEADER",
		"REMOVEQUOTES", "ROUNDEC", "TIMEFORMAT", "TRIMBLANKS",
		"TRUNCATECOLUMNS", "COMPROWS", "COMPUPDATE", "MAXERROR", "NOLOAD",
		"STATUPDATE", "FORMAT", "CSV", "DELIMITER", "FIXEDWIDTH", "SHAPEFILE",
		"AVRO", "JSON", "PARQUET", "ORC", "ACCESS_KEY_ID", "CREDENTIALS",
		"ENCRYPTED", "IAM_ROLE", "MASTER_SYMMETRIC_KEY", "SECRET_ACCESS_KEY",
		"SESSION_TOKEN", "BZIP2", "GZIP", "LZOP", "ZSTD", "MANIFEST",
		"READRATIO", "REGION", "SSH", "RAW", "AZ64", "BYTEDICT", "DELTA",
		"DELTA32K", "LZO", "MOSTLY8", "MOSTLY16", "MOSTLY32", "RUNLENGTH",
		"TEXT255", "TEXT32K", "CATALOG_ROLE", "SECRET_ARN", "EXTERNAL", "AUTO",
		"EVEN", "KEY", "PREDICATE", "COMPRESSION"
	],
	to = ["ARRAY", "BIGINT", "BPCHAR", "CHAR", "CHARACTER VARYING", "CHARACTER",
		"DECIMAL", "INT", "INT2", "INT4", "INT8", "INTEGER", "NCHAR", "NUMERIC",
		"NVARCHAR", "SMALLINT", "TEXT", "VARBYTE", "VARCHAR"
	],
	To = v(["SELECT [ALL | DISTINCT]"]),
	ro = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY", "HAVING",
		"PARTITION BY", "ORDER BY", "LIMIT", "OFFSET", "INSERT INTO",
		"VALUES", "SET"
	]),
	ar = v([
		"CREATE [TEMPORARY | TEMP | LOCAL TEMPORARY | LOCAL TEMP] TABLE [IF NOT EXISTS]"
	]),
	zt = v(["CREATE [OR REPLACE | MATERIALIZED] VIEW", "UPDATE",
		"DELETE [FROM]", "DROP TABLE [IF EXISTS]", "ALTER TABLE",
		"ALTER TABLE APPEND", "ADD [COLUMN]", "DROP [COLUMN]", "RENAME TO",
		"RENAME COLUMN", "ALTER COLUMN", "TYPE", "ENCODE",
		"TRUNCATE [TABLE]", "ABORT", "ALTER DATABASE", "ALTER DATASHARE",
		"ALTER DEFAULT PRIVILEGES", "ALTER GROUP",
		"ALTER MATERIALIZED VIEW", "ALTER PROCEDURE", "ALTER SCHEMA",
		"ALTER USER", "ANALYSE", "ANALYZE", "ANALYSE COMPRESSION",
		"ANALYZE COMPRESSION", "BEGIN", "CALL", "CANCEL", "CLOSE", "COMMIT",
		"COPY", "CREATE DATABASE", "CREATE DATASHARE",
		"CREATE EXTERNAL FUNCTION", "CREATE EXTERNAL SCHEMA",
		"CREATE EXTERNAL TABLE", "CREATE FUNCTION", "CREATE GROUP",
		"CREATE LIBRARY", "CREATE MODEL", "CREATE PROCEDURE",
		"CREATE SCHEMA", "CREATE USER", "DEALLOCATE", "DECLARE",
		"DESC DATASHARE", "DROP DATABASE", "DROP DATASHARE",
		"DROP FUNCTION", "DROP GROUP", "DROP LIBRARY", "DROP MODEL",
		"DROP MATERIALIZED VIEW", "DROP PROCEDURE", "DROP SCHEMA",
		"DROP USER", "DROP VIEW", "DROP", "EXECUTE", "EXPLAIN", "FETCH",
		"GRANT", "LOCK", "PREPARE", "REFRESH MATERIALIZED VIEW", "RESET",
		"REVOKE", "ROLLBACK", "SELECT INTO", "SET SESSION AUTHORIZATION",
		"SET SESSION CHARACTERISTICS", "SHOW", "SHOW EXTERNAL TABLE",
		"SHOW MODEL", "SHOW DATASHARES", "SHOW PROCEDURE", "SHOW TABLE",
		"SHOW VIEW", "START TRANSACTION", "UNLOAD", "VACUUM"
	]),
	Ro = v(["UNION [ALL]", "EXCEPT", "INTERSECT", "MINUS"]),
	no = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "NATURAL [INNER] JOIN",
		"NATURAL {LEFT | RIGHT | FULL} [OUTER] JOIN"
	]),
	Ao = v(["NULL AS", "DATA CATALOG", "HIVE METASTORE",
		"{ROWS | RANGE} BETWEEN"
	]),
	so = {
		name: "redshift",
		tokenizerOptions: {
			reservedSelect: To,
			reservedClauses: [...ro, ...ar, ...zt],
			reservedSetOperations: Ro,
			reservedJoins: no,
			reservedPhrases: Ao,
			reservedKeywords: Eo,
			reservedDataTypes: to,
			reservedFunctionNames: eo,
			stringTypes: ["''-qq"],
			identTypes: ['""-qq'],
			identChars: {
				first: "#"
			},
			paramTypes: {
				numbered: ["$"]
			},
			operators: ["^", "%", "@", "|/", "||/", "&", "|", "~", "<<", ">>",
				"||", "::"
			]
		},
		formatOptions: {
			alwaysDenseOperators: ["::"],
			onelineClauses: [...ar, ...zt],
			tabularOnelineClauses: zt
		}
	},
	So = ["ADD", "AFTER", "ALL", "ALTER", "ANALYZE", "AND", "ANTI", "ANY",
		"ARCHIVE", "AS", "ASC", "AT", "AUTHORIZATION", "BETWEEN", "BOTH",
		"BUCKET", "BUCKETS", "BY", "CACHE", "CASCADE", "CAST", "CHANGE",
		"CHECK", "CLEAR", "CLUSTER", "CLUSTERED", "CODEGEN", "COLLATE",
		"COLLECTION", "COLUMN", "COLUMNS", "COMMENT", "COMMIT", "COMPACT",
		"COMPACTIONS", "COMPUTE", "CONCATENATE", "CONSTRAINT", "COST", "CREATE",
		"CROSS", "CUBE", "CURRENT", "CURRENT_DATE", "CURRENT_TIME",
		"CURRENT_TIMESTAMP", "CURRENT_USER", "DATA", "DATABASE", "DATABASES",
		"DAY", "DBPROPERTIES", "DEFINED", "DELETE", "DELIMITED", "DESC",
		"DESCRIBE", "DFS", "DIRECTORIES", "DIRECTORY", "DISTINCT", "DISTRIBUTE",
		"DIV", "DROP", "ESCAPE", "ESCAPED", "EXCEPT", "EXCHANGE", "EXISTS",
		"EXPORT", "EXTENDED", "EXTERNAL", "EXTRACT", "FALSE", "FETCH", "FIELDS",
		"FILTER", "FILEFORMAT", "FIRST", "FIRST_VALUE", "FOLLOWING", "FOR",
		"FOREIGN", "FORMAT", "FORMATTED", "FULL", "FUNCTION", "FUNCTIONS",
		"GLOBAL", "GRANT", "GROUP", "GROUPING", "HOUR", "IF", "IGNORE",
		"IMPORT", "IN", "INDEX", "INDEXES", "INNER", "INPATH", "INPUTFORMAT",
		"INTERSECT", "INTO", "IS", "ITEMS", "KEYS", "LAST", "LAST_VALUE",
		"LATERAL", "LAZY", "LEADING", "LEFT", "LIKE", "LINES", "LIST", "LOCAL",
		"LOCATION", "LOCK", "LOCKS", "LOGICAL", "MACRO", "MATCHED", "MERGE",
		"MINUTE", "MONTH", "MSCK", "NAMESPACE", "NAMESPACES", "NATURAL", "NO",
		"NOT", "NULL", "NULLS", "OF", "ONLY", "OPTION", "OPTIONS", "OR",
		"ORDER", "OUT", "OUTER", "OUTPUTFORMAT", "OVER", "OVERLAPS", "OVERLAY",
		"OVERWRITE", "OWNER", "PARTITION", "PARTITIONED", "PARTITIONS",
		"PERCENT", "PLACING", "POSITION", "PRECEDING", "PRIMARY", "PRINCIPALS",
		"PROPERTIES", "PURGE", "QUERY", "RANGE", "RECORDREADER", "RECORDWRITER",
		"RECOVER", "REDUCE", "REFERENCES", "RENAME", "REPAIR", "REPLACE",
		"RESPECT", "RESTRICT", "REVOKE", "RIGHT", "RLIKE", "ROLE", "ROLES",
		"ROLLBACK", "ROLLUP", "ROW", "ROWS", "SCHEMA", "SECOND", "SELECT",
		"SEMI", "SEPARATED", "SERDE", "SERDEPROPERTIES", "SESSION_USER", "SETS",
		"SHOW", "SKEWED", "SOME", "SORT", "SORTED", "START", "STATISTICS",
		"STORED", "STRATIFY", "SUBSTR", "SUBSTRING", "TABLE", "TABLES",
		"TBLPROPERTIES", "TEMPORARY", "TERMINATED", "THEN", "TO", "TOUCH",
		"TRAILING", "TRANSACTION", "TRANSACTIONS", "TRIM", "TRUE", "TRUNCATE",
		"UNARCHIVE", "UNBOUNDED", "UNCACHE", "UNIQUE", "UNKNOWN", "UNLOCK",
		"UNSET", "USE", "USER", "USING", "VIEW", "WINDOW", "YEAR", "ANALYSE",
		"ARRAY_ZIP", "COALESCE", "CONTAINS", "CONVERT", "DAYS", "DAY_HOUR",
		"DAY_MINUTE", "DAY_SECOND", "DECODE", "DEFAULT", "DISTINCTROW",
		"ENCODE", "EXPLODE", "EXPLODE_OUTER", "FIXED", "GREATEST",
		"GROUP_CONCAT", "HOURS", "HOUR_MINUTE", "HOUR_SECOND", "IFNULL",
		"LEAST", "LEVEL", "MINUTE_SECOND", "NULLIF", "OFFSET", "ON", "OPTIMIZE",
		"REGEXP", "SEPARATOR", "SIZE", "TYPE", "TYPES", "UNSIGNED", "VARIABLES",
		"YEAR_MONTH"
	],
	oo = ["ARRAY", "BIGINT", "BINARY", "BOOLEAN", "BYTE", "CHAR", "DATE", "DEC",
		"DECIMAL", "DOUBLE", "FLOAT", "INT", "INTEGER", "INTERVAL", "LONG",
		"MAP", "NUMERIC", "REAL", "SHORT", "SMALLINT", "STRING", "STRUCT",
		"TIMESTAMP_LTZ", "TIMESTAMP_NTZ", "TIMESTAMP", "TINYINT", "VARCHAR"
	],
	Oo = ["APPROX_COUNT_DISTINCT", "APPROX_PERCENTILE", "AVG", "BIT_AND",
		"BIT_OR", "BIT_XOR", "BOOL_AND", "BOOL_OR", "COLLECT_LIST",
		"COLLECT_SET", "CORR", "COUNT", "COUNT", "COUNT", "COUNT_IF",
		"COUNT_MIN_SKETCH", "COVAR_POP", "COVAR_SAMP", "EVERY", "FIRST",
		"FIRST_VALUE", "GROUPING", "GROUPING_ID", "KURTOSIS", "LAST",
		"LAST_VALUE", "MAX", "MAX_BY", "MEAN", "MIN", "MIN_BY", "PERCENTILE",
		"PERCENTILE", "PERCENTILE_APPROX", "SKEWNESS", "STD", "STDDEV",
		"STDDEV_POP", "STDDEV_SAMP", "SUM", "VAR_POP", "VAR_SAMP", "VARIANCE",
		"CUME_DIST", "DENSE_RANK", "LAG", "LEAD", "NTH_VALUE", "NTILE",
		"PERCENT_RANK", "RANK", "ROW_NUMBER", "ARRAY", "ARRAY_CONTAINS",
		"ARRAY_DISTINCT", "ARRAY_EXCEPT", "ARRAY_INTERSECT", "ARRAY_JOIN",
		"ARRAY_MAX", "ARRAY_MIN", "ARRAY_POSITION", "ARRAY_REMOVE",
		"ARRAY_REPEAT", "ARRAY_UNION", "ARRAYS_OVERLAP", "ARRAYS_ZIP",
		"FLATTEN", "SEQUENCE", "SHUFFLE", "SLICE", "SORT_ARRAY", "ELEMENT_AT",
		"ELEMENT_AT", "MAP_CONCAT", "MAP_ENTRIES", "MAP_FROM_ARRAYS",
		"MAP_FROM_ENTRIES", "MAP_KEYS", "MAP_VALUES", "STR_TO_MAP",
		"ADD_MONTHS", "CURRENT_DATE", "CURRENT_DATE", "CURRENT_TIMESTAMP",
		"CURRENT_TIMESTAMP", "CURRENT_TIMEZONE", "DATE_ADD", "DATE_FORMAT",
		"DATE_FROM_UNIX_DATE", "DATE_PART", "DATE_SUB", "DATE_TRUNC",
		"DATEDIFF", "DAY", "DAYOFMONTH", "DAYOFWEEK", "DAYOFYEAR", "EXTRACT",
		"FROM_UNIXTIME", "FROM_UTC_TIMESTAMP", "HOUR", "LAST_DAY", "MAKE_DATE",
		"MAKE_DT_INTERVAL", "MAKE_INTERVAL", "MAKE_TIMESTAMP",
		"MAKE_YM_INTERVAL", "MINUTE", "MONTH", "MONTHS_BETWEEN", "NEXT_DAY",
		"NOW", "QUARTER", "SECOND", "SESSION_WINDOW", "TIMESTAMP_MICROS",
		"TIMESTAMP_MILLIS", "TIMESTAMP_SECONDS", "TO_DATE", "TO_TIMESTAMP",
		"TO_UNIX_TIMESTAMP", "TO_UTC_TIMESTAMP", "TRUNC", "UNIX_DATE",
		"UNIX_MICROS", "UNIX_MILLIS", "UNIX_SECONDS", "UNIX_TIMESTAMP",
		"WEEKDAY", "WEEKOFYEAR", "WINDOW", "YEAR", "FROM_JSON",
		"GET_JSON_OBJECT", "JSON_ARRAY_LENGTH", "JSON_OBJECT_KEYS",
		"JSON_TUPLE", "SCHEMA_OF_JSON", "TO_JSON", "ABS", "ACOS", "ACOSH",
		"AGGREGATE", "ARRAY_SORT", "ASCII", "ASIN", "ASINH", "ASSERT_TRUE",
		"ATAN", "ATAN2", "ATANH", "BASE64", "BIN", "BIT_COUNT", "BIT_GET",
		"BIT_LENGTH", "BROUND", "BTRIM", "CARDINALITY", "CBRT", "CEIL",
		"CEILING", "CHAR_LENGTH", "CHARACTER_LENGTH", "CHR", "CONCAT",
		"CONCAT_WS", "CONV", "COS", "COSH", "COT", "CRC32", "CURRENT_CATALOG",
		"CURRENT_DATABASE", "CURRENT_USER", "DEGREES", "ELT", "EXP", "EXPM1",
		"FACTORIAL", "FIND_IN_SET", "FLOOR", "FORALL", "FORMAT_NUMBER",
		"FORMAT_STRING", "FROM_CSV", "GETBIT", "HASH", "HEX", "HYPOT",
		"INITCAP", "INLINE", "INLINE_OUTER", "INPUT_FILE_BLOCK_LENGTH",
		"INPUT_FILE_BLOCK_START", "INPUT_FILE_NAME", "INSTR", "ISNAN",
		"ISNOTNULL", "ISNULL", "JAVA_METHOD", "LCASE", "LEFT", "LENGTH",
		"LEVENSHTEIN", "LN", "LOCATE", "LOG", "LOG10", "LOG1P", "LOG2", "LOWER",
		"LPAD", "LTRIM", "MAP_FILTER", "MAP_ZIP_WITH", "MD5", "MOD",
		"MONOTONICALLY_INCREASING_ID", "NAMED_STRUCT", "NANVL", "NEGATIVE",
		"NVL", "NVL2", "OCTET_LENGTH", "OVERLAY", "PARSE_URL", "PI", "PMOD",
		"POSEXPLODE", "POSEXPLODE_OUTER", "POSITION", "POSITIVE", "POW",
		"POWER", "PRINTF", "RADIANS", "RAISE_ERROR", "RAND", "RANDN", "RANDOM",
		"REFLECT", "REGEXP_EXTRACT", "REGEXP_EXTRACT_ALL", "REGEXP_LIKE",
		"REGEXP_REPLACE", "REPEAT", "REPLACE", "REVERSE", "RIGHT", "RINT",
		"ROUND", "RPAD", "RTRIM", "SCHEMA_OF_CSV", "SENTENCES", "SHA", "SHA1",
		"SHA2", "SHIFTLEFT", "SHIFTRIGHT", "SHIFTRIGHTUNSIGNED", "SIGN",
		"SIGNUM", "SIN", "SINH", "SOUNDEX", "SPACE", "SPARK_PARTITION_ID",
		"SPLIT", "SQRT", "STACK", "SUBSTR", "SUBSTRING", "SUBSTRING_INDEX",
		"TAN", "TANH", "TO_CSV", "TRANSFORM_KEYS", "TRANSFORM_VALUES",
		"TRANSLATE", "TRIM", "TRY_ADD", "TRY_DIVIDE", "TYPEOF", "UCASE",
		"UNBASE64", "UNHEX", "UPPER", "UUID", "VERSION", "WIDTH_BUCKET",
		"XPATH", "XPATH_BOOLEAN", "XPATH_DOUBLE", "XPATH_FLOAT", "XPATH_INT",
		"XPATH_LONG", "XPATH_NUMBER", "XPATH_SHORT", "XPATH_STRING", "XXHASH64",
		"ZIP_WITH", "CAST", "COALESCE", "NULLIF"
	],
	io = v(["SELECT [ALL | DISTINCT]"]),
	ao = v(["WITH", "FROM", "WHERE", "GROUP BY", "HAVING", "WINDOW",
		"PARTITION BY", "ORDER BY", "SORT BY", "CLUSTER BY",
		"DISTRIBUTE BY", "LIMIT", "INSERT [INTO | OVERWRITE] [TABLE]",
		"VALUES", "INSERT OVERWRITE [LOCAL] DIRECTORY",
		"LOAD DATA [LOCAL] INPATH", "[OVERWRITE] INTO TABLE"
	]),
	Ir = v(["CREATE [EXTERNAL] TABLE [IF NOT EXISTS]"]),
	eT = v([
		"CREATE [OR REPLACE] [GLOBAL TEMPORARY | TEMPORARY] VIEW [IF NOT EXISTS]",
		"DROP TABLE [IF EXISTS]", "ALTER TABLE", "ADD COLUMNS",
		"DROP {COLUMN | COLUMNS}", "RENAME TO", "RENAME COLUMN",
		"ALTER COLUMN", "TRUNCATE TABLE", "LATERAL VIEW", "ALTER DATABASE",
		"ALTER VIEW", "CREATE DATABASE", "CREATE FUNCTION", "DROP DATABASE",
		"DROP FUNCTION", "DROP VIEW", "REPAIR TABLE", "USE DATABASE",
		"TABLESAMPLE", "PIVOT", "TRANSFORM", "EXPLAIN", "ADD FILE",
		"ADD JAR", "ANALYZE TABLE", "CACHE TABLE", "CLEAR CACHE",
		"DESCRIBE DATABASE", "DESCRIBE FUNCTION", "DESCRIBE QUERY",
		"DESCRIBE TABLE", "LIST FILE", "LIST JAR", "REFRESH",
		"REFRESH TABLE", "REFRESH FUNCTION", "RESET", "SHOW COLUMNS",
		"SHOW CREATE TABLE", "SHOW DATABASES", "SHOW FUNCTIONS",
		"SHOW PARTITIONS", "SHOW TABLE EXTENDED", "SHOW TABLES",
		"SHOW TBLPROPERTIES", "SHOW VIEWS", "UNCACHE TABLE"
	]),
	Io = v(["UNION [ALL | DISTINCT]", "EXCEPT [ALL | DISTINCT]",
		"INTERSECT [ALL | DISTINCT]"
	]),
	No = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "NATURAL [INNER] JOIN",
		"NATURAL {LEFT | RIGHT | FULL} [OUTER] JOIN",
		"[LEFT] {ANTI | SEMI} JOIN", "NATURAL [LEFT] {ANTI | SEMI} JOIN"
	]),
	lo = v(["ON DELETE", "ON UPDATE", "CURRENT ROW", "{ROWS | RANGE} BETWEEN"]),
	_o = {
		name: "spark",
		tokenizerOptions: {
			reservedSelect: io,
			reservedClauses: [...ao, ...Ir, ...eT],
			reservedSetOperations: Io,
			reservedJoins: No,
			reservedPhrases: lo,
			supportsXor: !0,
			reservedKeywords: So,
			reservedDataTypes: oo,
			reservedFunctionNames: Oo,
			extraParens: ["[]"],
			stringTypes: ["''-bs", '""-bs', {
				quote: "''-raw",
				prefixes: ["R", "X"],
				requirePrefix: !0
			}, {
				quote: '""-raw',
				prefixes: ["R", "X"],
				requirePrefix: !0
			}],
			identTypes: ["``"],
			variableTypes: [{
				quote: "{}",
				prefixes: ["$"],
				requirePrefix: !0
			}],
			operators: ["%", "~", "^", "|", "&", "<=>", "==", "!", "||", "->"],
			postProcess: Lo
		},
		formatOptions: {
			onelineClauses: [...Ir, ...eT],
			tabularOnelineClauses: eT
		}
	};

function Lo(E) {
	return E.map((e, T) => {
		const t = E[T - 1] || tt,
			r = E[T + 1] || tt;
		return FE.WINDOW(e) && r.type === "OPEN_PAREN" ? AE(EE({}, e), {
				type: "RESERVED_FUNCTION_NAME"
			}) : e.text === "ITEMS" && e.type === "RESERVED_KEYWORD" &&
			!(t.text === "COLLECTION" && r.text === "TERMINATED") ? AE(
				EE({}, e), {
					type: "IDENTIFIER",
					text: e.raw
				}) : e
	})
}
var Co = ["ABS", "CHANGES", "CHAR", "COALESCE", "FORMAT", "GLOB", "HEX",
		"IFNULL", "IIF", "INSTR", "LAST_INSERT_ROWID", "LENGTH", "LIKE",
		"LIKELIHOOD", "LIKELY", "LOAD_EXTENSION", "LOWER", "LTRIM", "NULLIF",
		"PRINTF", "QUOTE", "RANDOM", "RANDOMBLOB", "REPLACE", "ROUND", "RTRIM",
		"SIGN", "SOUNDEX", "SQLITE_COMPILEOPTION_GET",
		"SQLITE_COMPILEOPTION_USED", "SQLITE_OFFSET", "SQLITE_SOURCE_ID",
		"SQLITE_VERSION", "SUBSTR", "SUBSTRING", "TOTAL_CHANGES", "TRIM",
		"TYPEOF", "UNICODE", "UNLIKELY", "UPPER", "ZEROBLOB", "AVG", "COUNT",
		"GROUP_CONCAT", "MAX", "MIN", "SUM", "TOTAL", "DATE", "TIME",
		"DATETIME", "JULIANDAY", "UNIXEPOCH", "STRFTIME", "row_number", "rank",
		"dense_rank", "percent_rank", "cume_dist", "ntile", "lag", "lead",
		"first_value", "last_value", "nth_value", "ACOS", "ACOSH", "ASIN",
		"ASINH", "ATAN", "ATAN2", "ATANH", "CEIL", "CEILING", "COS", "COSH",
		"DEGREES", "EXP", "FLOOR", "LN", "LOG", "LOG", "LOG10", "LOG2", "MOD",
		"PI", "POW", "POWER", "RADIANS", "SIN", "SINH", "SQRT", "TAN", "TANH",
		"TRUNC", "JSON", "JSON_ARRAY", "JSON_ARRAY_LENGTH", "JSON_ARRAY_LENGTH",
		"JSON_EXTRACT", "JSON_INSERT", "JSON_OBJECT", "JSON_PATCH",
		"JSON_REMOVE", "JSON_REPLACE", "JSON_SET", "JSON_TYPE", "JSON_TYPE",
		"JSON_VALID", "JSON_QUOTE", "JSON_GROUP_ARRAY", "JSON_GROUP_OBJECT",
		"JSON_EACH", "JSON_TREE", "CAST"
	],
	uo = ["ABORT", "ACTION", "ADD", "AFTER", "ALL", "ALTER", "AND", "ARE",
		"ALWAYS", "ANALYZE", "AS", "ASC", "ATTACH", "AUTOINCREMENT", "BEFORE",
		"BEGIN", "BETWEEN", "BY", "CASCADE", "CASE", "CAST", "CHECK", "COLLATE",
		"COLUMN", "COMMIT", "CONFLICT", "CONSTRAINT", "CREATE", "CROSS",
		"CURRENT", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP",
		"DATABASE", "DEFAULT", "DEFERRABLE", "DEFERRED", "DELETE", "DESC",
		"DETACH", "DISTINCT", "DO", "DROP", "EACH", "ELSE", "END", "ESCAPE",
		"EXCEPT", "EXCLUDE", "EXCLUSIVE", "EXISTS", "EXPLAIN", "FAIL", "FILTER",
		"FIRST", "FOLLOWING", "FOR", "FOREIGN", "FROM", "FULL", "GENERATED",
		"GLOB", "GROUP", "GROUPS", "HAVING", "IF", "IGNORE", "IMMEDIATE", "IN",
		"INDEX", "INDEXED", "INITIALLY", "INNER", "INSERT", "INSTEAD",
		"INTERSECT", "INTO", "IS", "ISNULL", "JOIN", "KEY", "LAST", "LEFT",
		"LIKE", "LIMIT", "MATCH", "MATERIALIZED", "NATURAL", "NO", "NOT",
		"NOTHING", "NOTNULL", "NULL", "NULLS", "OF", "OFFSET", "ON", "ONLY",
		"OPEN", "OR", "ORDER", "OTHERS", "OUTER", "OVER", "PARTITION", "PLAN",
		"PRAGMA", "PRECEDING", "PRIMARY", "QUERY", "RAISE", "RANGE",
		"RECURSIVE", "REFERENCES", "REGEXP", "REINDEX", "RELEASE", "RENAME",
		"REPLACE", "RESTRICT", "RETURNING", "RIGHT", "ROLLBACK", "ROW", "ROWS",
		"SAVEPOINT", "SELECT", "SET", "TABLE", "TEMP", "TEMPORARY", "THEN",
		"TIES", "TO", "TRANSACTION", "TRIGGER", "UNBOUNDED", "UNION", "UNIQUE",
		"UPDATE", "USING", "VACUUM", "VALUES", "VIEW", "VIRTUAL", "WHEN",
		"WHERE", "WINDOW", "WITH", "WITHOUT"
	],
	co = ["ANY", "ARRAY", "BLOB", "CHARACTER", "DECIMAL", "INT", "INTEGER",
		"NATIVE CHARACTER", "NCHAR", "NUMERIC", "NVARCHAR", "REAL", "TEXT",
		"VARCHAR", "VARYING CHARACTER"
	],
	fo = v(["SELECT [ALL | DISTINCT]"]),
	Po = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY", "HAVING", "WINDOW",
		"PARTITION BY", "ORDER BY", "LIMIT", "OFFSET",
		"INSERT [OR ABORT | OR FAIL | OR IGNORE | OR REPLACE | OR ROLLBACK] INTO",
		"REPLACE INTO", "VALUES", "SET"
	]),
	Nr = v(["CREATE [TEMPORARY | TEMP] TABLE [IF NOT EXISTS]"]),
	ET = v(["CREATE [TEMPORARY | TEMP] VIEW [IF NOT EXISTS]",
		"UPDATE [OR ABORT | OR FAIL | OR IGNORE | OR REPLACE | OR ROLLBACK]",
		"ON CONFLICT", "DELETE FROM", "DROP TABLE [IF EXISTS]",
		"ALTER TABLE", "ADD [COLUMN]", "DROP [COLUMN]", "RENAME [COLUMN]",
		"RENAME TO", "SET SCHEMA"
	]),
	Do = v(["UNION [ALL]", "EXCEPT", "INTERSECT"]),
	po = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "NATURAL [INNER] JOIN",
		"NATURAL {LEFT | RIGHT | FULL} [OUTER] JOIN"
	]),
	Mo = v(["ON {UPDATE | DELETE} [SET NULL | SET DEFAULT]",
		"{ROWS | RANGE | GROUPS} BETWEEN"
	]),
	Uo = {
		name: "sqlite",
		tokenizerOptions: {
			reservedSelect: fo,
			reservedClauses: [...Po, ...Nr, ...ET],
			reservedSetOperations: Do,
			reservedJoins: po,
			reservedPhrases: Mo,
			reservedKeywords: uo,
			reservedDataTypes: co,
			reservedFunctionNames: Co,
			stringTypes: ["''-qq", {
				quote: "''-raw",
				prefixes: ["X"],
				requirePrefix: !0
			}],
			identTypes: ['""-qq', "``", "[]"],
			paramTypes: {
				positional: !0,
				numbered: ["?"],
				named: [":", "@", "$"]
			},
			operators: ["%", "~", "&", "|", "<<", ">>", "==", "->", "->>", "||"]
		},
		formatOptions: {
			onelineClauses: [...Nr, ...ET],
			tabularOnelineClauses: ET
		}
	},
	mo = ["GROUPING", "RANK", "DENSE_RANK", "PERCENT_RANK", "CUME_DIST",
		"ROW_NUMBER", "POSITION", "OCCURRENCES_REGEX", "POSITION_REGEX",
		"EXTRACT", "CHAR_LENGTH", "CHARACTER_LENGTH", "OCTET_LENGTH",
		"CARDINALITY", "ABS", "MOD", "LN", "EXP", "POWER", "SQRT", "FLOOR",
		"CEIL", "CEILING", "WIDTH_BUCKET", "SUBSTRING", "SUBSTRING_REGEX",
		"UPPER", "LOWER", "CONVERT", "TRANSLATE", "TRANSLATE_REGEX", "TRIM",
		"OVERLAY", "NORMALIZE", "SPECIFICTYPE", "CURRENT_DATE", "CURRENT_TIME",
		"LOCALTIME", "CURRENT_TIMESTAMP", "LOCALTIMESTAMP", "COUNT", "AVG",
		"MAX", "MIN", "SUM", "STDDEV_POP", "STDDEV_SAMP", "VAR_SAMP", "VAR_POP",
		"COLLECT", "FUSION", "INTERSECTION", "COVAR_POP", "COVAR_SAMP", "CORR",
		"REGR_SLOPE", "REGR_INTERCEPT", "REGR_COUNT", "REGR_R2", "REGR_AVGX",
		"REGR_AVGY", "REGR_SXX", "REGR_SYY", "REGR_SXY", "PERCENTILE_CONT",
		"PERCENTILE_DISC", "CAST", "COALESCE", "NULLIF", "ROUND", "SIN", "COS",
		"TAN", "ASIN", "ACOS", "ATAN"
	],
	ho = ["ALL", "ALLOCATE", "ALTER", "ANY", "ARE", "AS", "ASC", "ASENSITIVE",
		"ASYMMETRIC", "AT", "ATOMIC", "AUTHORIZATION", "BEGIN", "BETWEEN",
		"BOTH", "BY", "CALL", "CALLED", "CASCADED", "CAST", "CHECK", "CLOSE",
		"COALESCE", "COLLATE", "COLUMN", "COMMIT", "CONDITION", "CONNECT",
		"CONSTRAINT", "CORRESPONDING", "CREATE", "CROSS", "CUBE", "CURRENT",
		"CURRENT_CATALOG", "CURRENT_DEFAULT_TRANSFORM_GROUP", "CURRENT_PATH",
		"CURRENT_ROLE", "CURRENT_SCHEMA", "CURRENT_TRANSFORM_GROUP_FOR_TYPE",
		"CURRENT_USER", "CURSOR", "CYCLE", "DEALLOCATE", "DAY", "DECLARE",
		"DEFAULT", "DELETE", "DEREF", "DESC", "DESCRIBE", "DETERMINISTIC",
		"DISCONNECT", "DISTINCT", "DROP", "DYNAMIC", "EACH", "ELEMENT",
		"END-EXEC", "ESCAPE", "EVERY", "EXCEPT", "EXEC", "EXECUTE", "EXISTS",
		"EXTERNAL", "FALSE", "FETCH", "FILTER", "FOR", "FOREIGN", "FREE",
		"FROM", "FULL", "FUNCTION", "GET", "GLOBAL", "GRANT", "GROUP", "HAVING",
		"HOLD", "HOUR", "IDENTITY", "IN", "INDICATOR", "INNER", "INOUT",
		"INSENSITIVE", "INSERT", "INTERSECT", "INTO", "IS", "LANGUAGE", "LARGE",
		"LATERAL", "LEADING", "LEFT", "LIKE", "LIKE_REGEX", "LOCAL", "MATCH",
		"MEMBER", "MERGE", "METHOD", "MINUTE", "MODIFIES", "MODULE", "MONTH",
		"NATURAL", "NEW", "NO", "NONE", "NOT", "NULL", "NULLIF", "OF", "OLD",
		"ON", "ONLY", "OPEN", "ORDER", "OUT", "OUTER", "OVER", "OVERLAPS",
		"PARAMETER", "PARTITION", "PRECISION", "PREPARE", "PRIMARY",
		"PROCEDURE", "RANGE", "READS", "REAL", "RECURSIVE", "REF", "REFERENCES",
		"REFERENCING", "RELEASE", "RESULT", "RETURN", "RETURNS", "REVOKE",
		"RIGHT", "ROLLBACK", "ROLLUP", "ROW", "ROWS", "SAVEPOINT", "SCOPE",
		"SCROLL", "SEARCH", "SECOND", "SELECT", "SENSITIVE", "SESSION_USER",
		"SET", "SIMILAR", "SOME", "SPECIFIC", "SQL", "SQLEXCEPTION", "SQLSTATE",
		"SQLWARNING", "START", "STATIC", "SUBMULTISET", "SYMMETRIC", "SYSTEM",
		"SYSTEM_USER", "TABLE", "TABLESAMPLE", "THEN", "TIMEZONE_HOUR",
		"TIMEZONE_MINUTE", "TO", "TRAILING", "TRANSLATION", "TREAT", "TRIGGER",
		"TRUE", "UESCAPE", "UNION", "UNIQUE", "UNKNOWN", "UNNEST", "UPDATE",
		"USER", "USING", "VALUE", "VALUES", "WHENEVER", "WINDOW", "WITHIN",
		"WITHOUT", "YEAR"
	],
	Go = ["ARRAY", "BIGINT", "BINARY LARGE OBJECT", "BINARY VARYING", "BINARY",
		"BLOB", "BOOLEAN", "CHAR LARGE OBJECT", "CHAR VARYING", "CHAR",
		"CHARACTER LARGE OBJECT", "CHARACTER VARYING", "CHARACTER", "CLOB",
		"DATE", "DEC", "DECIMAL", "DOUBLE", "FLOAT", "INT", "INTEGER",
		"INTERVAL", "MULTISET", "NATIONAL CHAR VARYING", "NATIONAL CHAR",
		"NATIONAL CHARACTER LARGE OBJECT", "NATIONAL CHARACTER VARYING",
		"NATIONAL CHARACTER", "NCHAR LARGE OBJECT", "NCHAR VARYING", "NCHAR",
		"NCLOB", "NUMERIC", "SMALLINT", "TIME", "TIMESTAMP", "VARBINARY",
		"VARCHAR"
	],
	go = v(["SELECT [ALL | DISTINCT]"]),
	Ho = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY [ALL | DISTINCT]",
		"HAVING", "WINDOW", "PARTITION BY", "ORDER BY", "LIMIT", "OFFSET",
		"FETCH {FIRST | NEXT}", "INSERT INTO", "VALUES", "SET"
	]),
	lr = v(["CREATE [GLOBAL TEMPORARY | LOCAL TEMPORARY] TABLE"]),
	tT = v(["CREATE [RECURSIVE] VIEW", "UPDATE", "WHERE CURRENT OF",
		"DELETE FROM", "DROP TABLE", "ALTER TABLE", "ADD COLUMN",
		"DROP [COLUMN]", "RENAME COLUMN", "RENAME TO", "ALTER [COLUMN]",
		"{SET | DROP} DEFAULT", "ADD SCOPE",
		"DROP SCOPE {CASCADE | RESTRICT}", "RESTART WITH", "TRUNCATE TABLE",
		"SET SCHEMA"
	]),
	bo = v(["UNION [ALL | DISTINCT]", "EXCEPT [ALL | DISTINCT]",
		"INTERSECT [ALL | DISTINCT]"
	]),
	yo = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "NATURAL [INNER] JOIN",
		"NATURAL {LEFT | RIGHT | FULL} [OUTER] JOIN"
	]),
	Bo = v(["ON {UPDATE | DELETE} [SET NULL | SET DEFAULT]",
		"{ROWS | RANGE} BETWEEN"
	]),
	vo = {
		name: "sql",
		tokenizerOptions: {
			reservedSelect: go,
			reservedClauses: [...Ho, ...lr, ...tT],
			reservedSetOperations: bo,
			reservedJoins: yo,
			reservedPhrases: Bo,
			reservedKeywords: ho,
			reservedDataTypes: Go,
			reservedFunctionNames: mo,
			stringTypes: [{
				quote: "''-qq-bs",
				prefixes: ["N", "U&"]
			}, {
				quote: "''-raw",
				prefixes: ["X"],
				requirePrefix: !0
			}],
			identTypes: ['""-qq', "``"],
			paramTypes: {
				positional: !0
			},
			operators: ["||"]
		},
		formatOptions: {
			onelineClauses: [...lr, ...tT],
			tabularOnelineClauses: tT
		}
	},
	Fo = ["ABS", "ACOS", "ALL_MATCH", "ANY_MATCH", "APPROX_DISTINCT",
		"APPROX_MOST_FREQUENT", "APPROX_PERCENTILE", "APPROX_SET", "ARBITRARY",
		"ARRAYS_OVERLAP", "ARRAY_AGG", "ARRAY_DISTINCT", "ARRAY_EXCEPT",
		"ARRAY_INTERSECT", "ARRAY_JOIN", "ARRAY_MAX", "ARRAY_MIN",
		"ARRAY_POSITION", "ARRAY_REMOVE", "ARRAY_SORT", "ARRAY_UNION", "ASIN",
		"ATAN", "ATAN2", "AT_TIMEZONE", "AVG", "BAR", "BETA_CDF", "BING_TILE",
		"BING_TILES_AROUND", "BING_TILE_AT", "BING_TILE_COORDINATES",
		"BING_TILE_POLYGON", "BING_TILE_QUADKEY", "BING_TILE_ZOOM_LEVEL",
		"BITWISE_AND", "BITWISE_AND_AGG", "BITWISE_LEFT_SHIFT", "BITWISE_NOT",
		"BITWISE_OR", "BITWISE_OR_AGG", "BITWISE_RIGHT_SHIFT",
		"BITWISE_RIGHT_SHIFT_ARITHMETIC", "BITWISE_XOR", "BIT_COUNT",
		"BOOL_AND", "BOOL_OR", "CARDINALITY", "CAST", "CBRT", "CEIL", "CEILING",
		"CHAR2HEXINT", "CHECKSUM", "CHR", "CLASSIFY", "COALESCE", "CODEPOINT",
		"COLOR", "COMBINATIONS", "CONCAT", "CONCAT_WS", "CONTAINS",
		"CONTAINS_SEQUENCE", "CONVEX_HULL_AGG", "CORR", "COS", "COSH",
		"COSINE_SIMILARITY", "COUNT", "COUNT_IF", "COVAR_POP", "COVAR_SAMP",
		"CRC32", "CUME_DIST", "CURRENT_CATALOG", "CURRENT_DATE",
		"CURRENT_GROUPS", "CURRENT_SCHEMA", "CURRENT_TIME", "CURRENT_TIMESTAMP",
		"CURRENT_TIMEZONE", "CURRENT_USER", "DATE", "DATE_ADD", "DATE_DIFF",
		"DATE_FORMAT", "DATE_PARSE", "DATE_TRUNC", "DAY", "DAY_OF_MONTH",
		"DAY_OF_WEEK", "DAY_OF_YEAR", "DEGREES", "DENSE_RANK", "DOW", "DOY",
		"E", "ELEMENT_AT", "EMPTY_APPROX_SET",
		"EVALUATE_CLASSIFIER_PREDICTIONS", "EVERY", "EXP", "EXTRACT",
		"FEATURES", "FILTER", "FIRST_VALUE", "FLATTEN", "FLOOR", "FORMAT",
		"FORMAT_DATETIME", "FORMAT_NUMBER", "FROM_BASE", "FROM_BASE32",
		"FROM_BASE64", "FROM_BASE64URL", "FROM_BIG_ENDIAN_32",
		"FROM_BIG_ENDIAN_64", "FROM_ENCODED_POLYLINE", "FROM_GEOJSON_GEOMETRY",
		"FROM_HEX", "FROM_IEEE754_32", "FROM_IEEE754_64", "FROM_ISO8601_DATE",
		"FROM_ISO8601_TIMESTAMP", "FROM_ISO8601_TIMESTAMP_NANOS",
		"FROM_UNIXTIME", "FROM_UNIXTIME_NANOS", "FROM_UTF8", "GEOMETRIC_MEAN",
		"GEOMETRY_FROM_HADOOP_SHAPE", "GEOMETRY_INVALID_REASON",
		"GEOMETRY_NEAREST_POINTS", "GEOMETRY_TO_BING_TILES", "GEOMETRY_UNION",
		"GEOMETRY_UNION_AGG", "GREATEST", "GREAT_CIRCLE_DISTANCE",
		"HAMMING_DISTANCE", "HASH_COUNTS", "HISTOGRAM", "HMAC_MD5", "HMAC_SHA1",
		"HMAC_SHA256", "HMAC_SHA512", "HOUR", "HUMAN_READABLE_SECONDS", "IF",
		"INDEX", "INFINITY", "INTERSECTION_CARDINALITY", "INVERSE_BETA_CDF",
		"INVERSE_NORMAL_CDF", "IS_FINITE", "IS_INFINITE", "IS_JSON_SCALAR",
		"IS_NAN", "JACCARD_INDEX", "JSON_ARRAY_CONTAINS", "JSON_ARRAY_GET",
		"JSON_ARRAY_LENGTH", "JSON_EXISTS", "JSON_EXTRACT",
		"JSON_EXTRACT_SCALAR", "JSON_FORMAT", "JSON_PARSE", "JSON_QUERY",
		"JSON_SIZE", "JSON_VALUE", "KURTOSIS", "LAG", "LAST_DAY_OF_MONTH",
		"LAST_VALUE", "LEAD", "LEARN_CLASSIFIER", "LEARN_LIBSVM_CLASSIFIER",
		"LEARN_LIBSVM_REGRESSOR", "LEARN_REGRESSOR", "LEAST", "LENGTH",
		"LEVENSHTEIN_DISTANCE", "LINE_INTERPOLATE_POINT",
		"LINE_INTERPOLATE_POINTS", "LINE_LOCATE_POINT", "LISTAGG", "LN",
		"LOCALTIME", "LOCALTIMESTAMP", "LOG", "LOG10", "LOG2", "LOWER", "LPAD",
		"LTRIM", "LUHN_CHECK", "MAKE_SET_DIGEST", "MAP", "MAP_AGG",
		"MAP_CONCAT", "MAP_ENTRIES", "MAP_FILTER", "MAP_FROM_ENTRIES",
		"MAP_KEYS", "MAP_UNION", "MAP_VALUES", "MAP_ZIP_WITH", "MAX", "MAX_BY",
		"MD5", "MERGE", "MERGE_SET_DIGEST", "MILLISECOND", "MIN", "MINUTE",
		"MIN_BY", "MOD", "MONTH", "MULTIMAP_AGG", "MULTIMAP_FROM_ENTRIES",
		"MURMUR3", "NAN", "NGRAMS", "NONE_MATCH", "NORMALIZE", "NORMAL_CDF",
		"NOW", "NTH_VALUE", "NTILE", "NULLIF", "NUMERIC_HISTOGRAM", "OBJECTID",
		"OBJECTID_TIMESTAMP", "PARSE_DATA_SIZE", "PARSE_DATETIME",
		"PARSE_DURATION", "PERCENT_RANK", "PI", "POSITION", "POW", "POWER",
		"QDIGEST_AGG", "QUARTER", "RADIANS", "RAND", "RANDOM", "RANK", "REDUCE",
		"REDUCE_AGG", "REGEXP_COUNT", "REGEXP_EXTRACT", "REGEXP_EXTRACT_ALL",
		"REGEXP_LIKE", "REGEXP_POSITION", "REGEXP_REPLACE", "REGEXP_SPLIT",
		"REGRESS", "REGR_INTERCEPT", "REGR_SLOPE", "RENDER", "REPEAT",
		"REPLACE", "REVERSE", "RGB", "ROUND", "ROW_NUMBER", "RPAD", "RTRIM",
		"SECOND", "SEQUENCE", "SHA1", "SHA256", "SHA512", "SHUFFLE", "SIGN",
		"SIMPLIFY_GEOMETRY", "SIN", "SKEWNESS", "SLICE", "SOUNDEX",
		"SPATIAL_PARTITIONING", "SPATIAL_PARTITIONS", "SPLIT", "SPLIT_PART",
		"SPLIT_TO_MAP", "SPLIT_TO_MULTIMAP", "SPOOKY_HASH_V2_32",
		"SPOOKY_HASH_V2_64", "SQRT", "STARTS_WITH", "STDDEV", "STDDEV_POP",
		"STDDEV_SAMP", "STRPOS", "ST_AREA", "ST_ASBINARY", "ST_ASTEXT",
		"ST_BOUNDARY", "ST_BUFFER", "ST_CENTROID", "ST_CONTAINS",
		"ST_CONVEXHULL", "ST_COORDDIM", "ST_CROSSES", "ST_DIFFERENCE",
		"ST_DIMENSION", "ST_DISJOINT", "ST_DISTANCE", "ST_ENDPOINT",
		"ST_ENVELOPE", "ST_ENVELOPEASPTS", "ST_EQUALS", "ST_EXTERIORRING",
		"ST_GEOMETRIES", "ST_GEOMETRYFROMTEXT", "ST_GEOMETRYN",
		"ST_GEOMETRYTYPE", "ST_GEOMFROMBINARY", "ST_INTERIORRINGN",
		"ST_INTERIORRINGS", "ST_INTERSECTION", "ST_INTERSECTS", "ST_ISCLOSED",
		"ST_ISEMPTY", "ST_ISRING", "ST_ISSIMPLE", "ST_ISVALID", "ST_LENGTH",
		"ST_LINEFROMTEXT", "ST_LINESTRING", "ST_MULTIPOINT", "ST_NUMGEOMETRIES",
		"ST_NUMINTERIORRING", "ST_NUMPOINTS", "ST_OVERLAPS", "ST_POINT",
		"ST_POINTN", "ST_POINTS", "ST_POLYGON", "ST_RELATE", "ST_STARTPOINT",
		"ST_SYMDIFFERENCE", "ST_TOUCHES", "ST_UNION", "ST_WITHIN", "ST_X",
		"ST_XMAX", "ST_XMIN", "ST_Y", "ST_YMAX", "ST_YMIN", "SUBSTR",
		"SUBSTRING", "SUM", "TAN", "TANH", "TDIGEST_AGG", "TIMESTAMP_OBJECTID",
		"TIMEZONE_HOUR", "TIMEZONE_MINUTE", "TO_BASE", "TO_BASE32", "TO_BASE64",
		"TO_BASE64URL", "TO_BIG_ENDIAN_32", "TO_BIG_ENDIAN_64", "TO_CHAR",
		"TO_DATE", "TO_ENCODED_POLYLINE", "TO_GEOJSON_GEOMETRY", "TO_GEOMETRY",
		"TO_HEX", "TO_IEEE754_32", "TO_IEEE754_64", "TO_ISO8601",
		"TO_MILLISECONDS", "TO_SPHERICAL_GEOGRAPHY", "TO_TIMESTAMP",
		"TO_UNIXTIME", "TO_UTF8", "TRANSFORM", "TRANSFORM_KEYS",
		"TRANSFORM_VALUES", "TRANSLATE", "TRIM", "TRIM_ARRAY", "TRUNCATE",
		"TRY", "TRY_CAST", "TYPEOF", "UPPER", "URL_DECODE", "URL_ENCODE",
		"URL_EXTRACT_FRAGMENT", "URL_EXTRACT_HOST", "URL_EXTRACT_PARAMETER",
		"URL_EXTRACT_PATH", "URL_EXTRACT_PORT", "URL_EXTRACT_PROTOCOL",
		"URL_EXTRACT_QUERY", "UUID", "VALUES_AT_QUANTILES", "VALUE_AT_QUANTILE",
		"VARIANCE", "VAR_POP", "VAR_SAMP", "VERSION", "WEEK", "WEEK_OF_YEAR",
		"WIDTH_BUCKET", "WILSON_INTERVAL_LOWER", "WILSON_INTERVAL_UPPER",
		"WITH_TIMEZONE", "WORD_STEM", "XXHASH64", "YEAR", "YEAR_OF_WEEK", "YOW",
		"ZIP", "ZIP_WITH", "CLASSIFIER", "FIRST", "LAST", "MATCH_NUMBER",
		"NEXT", "PERMUTE", "PREV"
	],
	Yo = ["ABSENT", "ADD", "ADMIN", "AFTER", "ALL", "ALTER", "ANALYZE", "AND",
		"ANY", "AS", "ASC", "AT", "AUTHORIZATION", "BERNOULLI", "BETWEEN",
		"BOTH", "BY", "CALL", "CASCADE", "CASE", "CATALOGS", "COLUMN",
		"COLUMNS", "COMMENT", "COMMIT", "COMMITTED", "CONDITIONAL",
		"CONSTRAINT", "COPARTITION", "CREATE", "CROSS", "CUBE", "CURRENT",
		"CURRENT_PATH", "CURRENT_ROLE", "DATA", "DEALLOCATE", "DEFAULT",
		"DEFINE", "DEFINER", "DELETE", "DENY", "DESC", "DESCRIBE", "DESCRIPTOR",
		"DISTINCT", "DISTRIBUTED", "DOUBLE", "DROP", "ELSE", "EMPTY",
		"ENCODING", "END", "ERROR", "ESCAPE", "EXCEPT", "EXCLUDING", "EXECUTE",
		"EXISTS", "EXPLAIN", "FALSE", "FETCH", "FINAL", "FIRST", "FOLLOWING",
		"FOR", "FROM", "FULL", "FUNCTIONS", "GRANT", "GRANTED", "GRANTS",
		"GRAPHVIZ", "GROUP", "GROUPING", "GROUPS", "HAVING", "IGNORE", "IN",
		"INCLUDING", "INITIAL", "INNER", "INPUT", "INSERT", "INTERSECT",
		"INTERVAL", "INTO", "INVOKER", "IO", "IS", "ISOLATION", "JOIN", "JSON",
		"JSON_ARRAY", "JSON_OBJECT", "KEEP", "KEY", "KEYS", "LAST", "LATERAL",
		"LEADING", "LEFT", "LEVEL", "LIKE", "LIMIT", "LOCAL", "LOGICAL",
		"MATCH", "MATCHED", "MATCHES", "MATCH_RECOGNIZE", "MATERIALIZED",
		"MEASURES", "NATURAL", "NEXT", "NFC", "NFD", "NFKC", "NFKD", "NO",
		"NONE", "NOT", "NULL", "NULLS", "OBJECT", "OF", "OFFSET", "OMIT", "ON",
		"ONE", "ONLY", "OPTION", "OR", "ORDER", "ORDINALITY", "OUTER", "OUTPUT",
		"OVER", "OVERFLOW", "PARTITION", "PARTITIONS", "PASSING", "PAST",
		"PATH", "PATTERN", "PER", "PERMUTE", "PRECEDING", "PRECISION",
		"PREPARE", "PRIVILEGES", "PROPERTIES", "PRUNE", "QUOTES", "RANGE",
		"READ", "RECURSIVE", "REFRESH", "RENAME", "REPEATABLE", "RESET",
		"RESPECT", "RESTRICT", "RETURNING", "REVOKE", "RIGHT", "ROLE", "ROLES",
		"ROLLBACK", "ROLLUP", "ROW", "ROWS", "RUNNING", "SCALAR", "SCHEMA",
		"SCHEMAS", "SECURITY", "SEEK", "SELECT", "SERIALIZABLE", "SESSION",
		"SET", "SETS", "SHOW", "SKIP", "SOME", "START", "STATS", "STRING",
		"SUBSET", "SYSTEM", "TABLE", "TABLES", "TABLESAMPLE", "TEXT", "THEN",
		"TIES", "TIME", "TIMESTAMP", "TO", "TRAILING", "TRANSACTION", "TRUE",
		"TYPE", "UESCAPE", "UNBOUNDED", "UNCOMMITTED", "UNCONDITIONAL", "UNION",
		"UNIQUE", "UNKNOWN", "UNMATCHED", "UNNEST", "UPDATE", "USE", "USER",
		"USING", "UTF16", "UTF32", "UTF8", "VALIDATE", "VALUE", "VALUES",
		"VERBOSE", "VIEW", "WHEN", "WHERE", "WINDOW", "WITH", "WITHIN",
		"WITHOUT", "WORK", "WRAPPER", "WRITE", "ZONE"
	],
	Vo = ["BIGINT", "INT", "INTEGER", "SMALLINT", "TINYINT", "BOOLEAN", "DATE",
		"DECIMAL", "REAL", "DOUBLE", "HYPERLOGLOG", "QDIGEST", "TDIGEST",
		"P4HYPERLOGLOG", "INTERVAL", "TIMESTAMP", "TIME", "VARBINARY",
		"VARCHAR", "CHAR", "ROW", "ARRAY", "MAP", "JSON", "JSON2016",
		"IPADDRESS", "GEOMETRY", "UUID", "SETDIGEST", "JONIREGEXP",
		"RE2JREGEXP", "LIKEPATTERN", "COLOR", "CODEPOINTS", "FUNCTION",
		"JSONPATH"
	],
	Wo = v(["SELECT [ALL | DISTINCT]"]),
	wo = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY [ALL | DISTINCT]",
		"HAVING", "WINDOW", "PARTITION BY", "ORDER BY", "LIMIT", "OFFSET",
		"FETCH {FIRST | NEXT}", "INSERT INTO", "VALUES", "SET",
		"MATCH_RECOGNIZE", "MEASURES", "ONE ROW PER MATCH",
		"ALL ROWS PER MATCH", "AFTER MATCH", "PATTERN", "SUBSET", "DEFINE"
	]),
	_r = v(["CREATE TABLE [IF NOT EXISTS]"]),
	TT = v(["CREATE [OR REPLACE] [MATERIALIZED] VIEW", "UPDATE", "DELETE FROM",
		"DROP TABLE [IF EXISTS]", "ALTER TABLE [IF EXISTS]",
		"ADD COLUMN [IF NOT EXISTS]", "DROP COLUMN [IF EXISTS]",
		"RENAME COLUMN [IF EXISTS]", "RENAME TO",
		"SET AUTHORIZATION [USER | ROLE]", "SET PROPERTIES", "EXECUTE",
		"TRUNCATE TABLE", "ALTER SCHEMA", "ALTER MATERIALIZED VIEW",
		"ALTER VIEW", "CREATE SCHEMA", "CREATE ROLE", "DROP SCHEMA",
		"DROP MATERIALIZED VIEW", "DROP VIEW", "DROP ROLE", "EXPLAIN",
		"ANALYZE", "EXPLAIN ANALYZE", "EXPLAIN ANALYZE VERBOSE", "USE",
		"DESCRIBE INPUT", "DESCRIBE OUTPUT", "REFRESH MATERIALIZED VIEW",
		"RESET SESSION", "SET SESSION", "SET PATH", "SET TIME ZONE",
		"SHOW GRANTS", "SHOW CREATE TABLE", "SHOW CREATE SCHEMA",
		"SHOW CREATE VIEW", "SHOW CREATE MATERIALIZED VIEW", "SHOW TABLES",
		"SHOW SCHEMAS", "SHOW CATALOGS", "SHOW COLUMNS", "SHOW STATS FOR",
		"SHOW ROLES", "SHOW CURRENT ROLES", "SHOW ROLE GRANTS",
		"SHOW FUNCTIONS", "SHOW SESSION"
	]),
	$o = v(["UNION [ALL | DISTINCT]", "EXCEPT [ALL | DISTINCT]",
		"INTERSECT [ALL | DISTINCT]"
	]),
	xo = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "NATURAL [INNER] JOIN",
		"NATURAL {LEFT | RIGHT | FULL} [OUTER] JOIN"
	]),
	Xo = v(["{ROWS | RANGE | GROUPS} BETWEEN", "IS [NOT] DISTINCT FROM"]),
	ko = {
		name: "trino",
		tokenizerOptions: {
			reservedSelect: Wo,
			reservedClauses: [...wo, ..._r, ...TT],
			reservedSetOperations: $o,
			reservedJoins: xo,
			reservedPhrases: Xo,
			reservedKeywords: Yo,
			reservedDataTypes: Vo,
			reservedFunctionNames: Fo,
			extraParens: ["[]", "{}"],
			stringTypes: [{
				quote: "''-qq",
				prefixes: ["U&"]
			}, {
				quote: "''-raw",
				prefixes: ["X"],
				requirePrefix: !0
			}],
			identTypes: ['""-qq'],
			paramTypes: {
				positional: !0
			},
			operators: ["%", "->", "=>", ":", "||", "|", "^", "$"]
		},
		formatOptions: {
			onelineClauses: [..._r, ...TT],
			tabularOnelineClauses: TT
		}
	},
	Ko = ["APPROX_COUNT_DISTINCT", "AVG", "CHECKSUM_AGG", "COUNT", "COUNT_BIG",
		"GROUPING", "GROUPING_ID", "MAX", "MIN", "STDEV", "STDEVP", "SUM",
		"VAR", "VARP", "CUME_DIST", "FIRST_VALUE", "LAG", "LAST_VALUE", "LEAD",
		"PERCENTILE_CONT", "PERCENTILE_DISC", "PERCENT_RANK",
		"Collation - COLLATIONPROPERTY", "Collation - TERTIARY_WEIGHTS",
		"@@DBTS", "@@LANGID", "@@LANGUAGE", "@@LOCK_TIMEOUT",
		"@@MAX_CONNECTIONS", "@@MAX_PRECISION", "@@NESTLEVEL", "@@OPTIONS",
		"@@REMSERVER", "@@SERVERNAME", "@@SERVICENAME", "@@SPID", "@@TEXTSIZE",
		"@@VERSION", "CAST", "CONVERT", "PARSE", "TRY_CAST", "TRY_CONVERT",
		"TRY_PARSE", "ASYMKEY_ID", "ASYMKEYPROPERTY", "CERTPROPERTY", "CERT_ID",
		"CRYPT_GEN_RANDOM", "DECRYPTBYASYMKEY", "DECRYPTBYCERT", "DECRYPTBYKEY",
		"DECRYPTBYKEYAUTOASYMKEY", "DECRYPTBYKEYAUTOCERT",
		"DECRYPTBYPASSPHRASE", "ENCRYPTBYASYMKEY", "ENCRYPTBYCERT",
		"ENCRYPTBYKEY", "ENCRYPTBYPASSPHRASE", "HASHBYTES", "IS_OBJECTSIGNED",
		"KEY_GUID", "KEY_ID", "KEY_NAME", "SIGNBYASYMKEY", "SIGNBYCERT",
		"SYMKEYPROPERTY", "VERIFYSIGNEDBYCERT", "VERIFYSIGNEDBYASYMKEY",
		"@@CURSOR_ROWS", "@@FETCH_STATUS", "CURSOR_STATUS", "DATALENGTH",
		"IDENT_CURRENT", "IDENT_INCR", "IDENT_SEED", "IDENTITY",
		"SQL_VARIANT_PROPERTY", "@@DATEFIRST", "CURRENT_TIMESTAMP",
		"CURRENT_TIMEZONE", "CURRENT_TIMEZONE_ID", "DATEADD", "DATEDIFF",
		"DATEDIFF_BIG", "DATEFROMPARTS", "DATENAME", "DATEPART",
		"DATETIME2FROMPARTS", "DATETIMEFROMPARTS", "DATETIMEOFFSETFROMPARTS",
		"DAY", "EOMONTH", "GETDATE", "GETUTCDATE", "ISDATE", "MONTH",
		"SMALLDATETIMEFROMPARTS", "SWITCHOFFSET", "SYSDATETIME",
		"SYSDATETIMEOFFSET", "SYSUTCDATETIME", "TIMEFROMPARTS",
		"TODATETIMEOFFSET", "YEAR", "JSON", "ISJSON", "JSON_VALUE",
		"JSON_QUERY", "JSON_MODIFY", "ABS", "ACOS", "ASIN", "ATAN", "ATN2",
		"CEILING", "COS", "COT", "DEGREES", "EXP", "FLOOR", "LOG", "LOG10",
		"PI", "POWER", "RADIANS", "RAND", "ROUND", "SIGN", "SIN", "SQRT",
		"SQUARE", "TAN", "CHOOSE", "GREATEST", "IIF", "LEAST", "@@PROCID",
		"APP_NAME", "APPLOCK_MODE", "APPLOCK_TEST", "ASSEMBLYPROPERTY",
		"COL_LENGTH", "COL_NAME", "COLUMNPROPERTY", "DATABASEPROPERTYEX",
		"DB_ID", "DB_NAME", "FILE_ID", "FILE_IDEX", "FILE_NAME", "FILEGROUP_ID",
		"FILEGROUP_NAME", "FILEGROUPPROPERTY", "FILEPROPERTY", "FILEPROPERTYEX",
		"FULLTEXTCATALOGPROPERTY", "FULLTEXTSERVICEPROPERTY", "INDEX_COL",
		"INDEXKEY_PROPERTY", "INDEXPROPERTY", "NEXT VALUE FOR",
		"OBJECT_DEFINITION", "OBJECT_ID", "OBJECT_NAME", "OBJECT_SCHEMA_NAME",
		"OBJECTPROPERTY", "OBJECTPROPERTYEX", "ORIGINAL_DB_NAME", "PARSENAME",
		"SCHEMA_ID", "SCHEMA_NAME", "SCOPE_IDENTITY", "SERVERPROPERTY",
		"STATS_DATE", "TYPE_ID", "TYPE_NAME", "TYPEPROPERTY", "DENSE_RANK",
		"NTILE", "RANK", "ROW_NUMBER", "PUBLISHINGSERVERNAME", "CERTENCODED",
		"CERTPRIVATEKEY", "CURRENT_USER", "DATABASE_PRINCIPAL_ID",
		"HAS_DBACCESS", "HAS_PERMS_BY_NAME", "IS_MEMBER", "IS_ROLEMEMBER",
		"IS_SRVROLEMEMBER", "LOGINPROPERTY", "ORIGINAL_LOGIN", "PERMISSIONS",
		"PWDENCRYPT", "PWDCOMPARE", "SESSION_USER", "SESSIONPROPERTY",
		"SUSER_ID", "SUSER_NAME", "SUSER_SID", "SUSER_SNAME", "SYSTEM_USER",
		"USER", "USER_ID", "USER_NAME", "ASCII", "CHAR", "CHARINDEX", "CONCAT",
		"CONCAT_WS", "DIFFERENCE", "FORMAT", "LEFT", "LEN", "LOWER", "LTRIM",
		"NCHAR", "PATINDEX", "QUOTENAME", "REPLACE", "REPLICATE", "REVERSE",
		"RIGHT", "RTRIM", "SOUNDEX", "SPACE", "STR", "STRING_AGG",
		"STRING_ESCAPE", "STUFF", "SUBSTRING", "TRANSLATE", "TRIM", "UNICODE",
		"UPPER", "$PARTITION", "@@ERROR", "@@IDENTITY", "@@PACK_RECEIVED",
		"@@ROWCOUNT", "@@TRANCOUNT", "BINARY_CHECKSUM", "CHECKSUM", "COMPRESS",
		"CONNECTIONPROPERTY", "CONTEXT_INFO", "CURRENT_REQUEST_ID",
		"CURRENT_TRANSACTION_ID", "DECOMPRESS", "ERROR_LINE", "ERROR_MESSAGE",
		"ERROR_NUMBER", "ERROR_PROCEDURE", "ERROR_SEVERITY", "ERROR_STATE",
		"FORMATMESSAGE", "GET_FILESTREAM_TRANSACTION_CONTEXT", "GETANSINULL",
		"HOST_ID", "HOST_NAME", "ISNULL", "ISNUMERIC", "MIN_ACTIVE_ROWVERSION",
		"NEWID", "NEWSEQUENTIALID", "ROWCOUNT_BIG", "SESSION_CONTEXT",
		"XACT_STATE", "@@CONNECTIONS", "@@CPU_BUSY", "@@IDLE", "@@IO_BUSY",
		"@@PACK_SENT", "@@PACKET_ERRORS", "@@TIMETICKS", "@@TOTAL_ERRORS",
		"@@TOTAL_READ", "@@TOTAL_WRITE", "TEXTPTR", "TEXTVALID",
		"COLUMNS_UPDATED", "EVENTDATA", "TRIGGER_NESTLEVEL", "UPDATE",
		"COALESCE", "NULLIF"
	],
	Jo = ["ADD", "ALL", "ALTER", "AND", "ANY", "AS", "ASC", "AUTHORIZATION",
		"BACKUP", "BEGIN", "BETWEEN", "BREAK", "BROWSE", "BULK", "BY",
		"CASCADE", "CHECK", "CHECKPOINT", "CLOSE", "CLUSTERED", "COALESCE",
		"COLLATE", "COLUMN", "COMMIT", "COMPUTE", "CONSTRAINT", "CONTAINS",
		"CONTAINSTABLE", "CONTINUE", "CONVERT", "CREATE", "CROSS", "CURRENT",
		"CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER",
		"CURSOR", "DATABASE", "DBCC", "DEALLOCATE", "DECLARE", "DEFAULT",
		"DELETE", "DENY", "DESC", "DISK", "DISTINCT", "DISTRIBUTED", "DROP",
		"DUMP", "ERRLVL", "ESCAPE", "EXEC", "EXECUTE", "EXISTS", "EXIT",
		"EXTERNAL", "FETCH", "FILE", "FILLFACTOR", "FOR", "FOREIGN", "FREETEXT",
		"FREETEXTTABLE", "FROM", "FULL", "FUNCTION", "GOTO", "GRANT", "GROUP",
		"HAVING", "HOLDLOCK", "IDENTITY", "IDENTITYCOL", "IDENTITY_INSERT",
		"IF", "IN", "INDEX", "INNER", "INSERT", "INTERSECT", "INTO", "IS",
		"JOIN", "KEY", "KILL", "LEFT", "LIKE", "LINENO", "LOAD", "MERGE",
		"NOCHECK", "NONCLUSTERED", "NOT", "NULL", "NULLIF", "OF", "OFF",
		"OFFSETS", "ON", "OPEN", "OPENDATASOURCE", "OPENQUERY", "OPENROWSET",
		"OPENXML", "OPTION", "OR", "ORDER", "OUTER", "OVER", "PERCENT", "PIVOT",
		"PLAN", "PRIMARY", "PRINT", "PROC", "PROCEDURE", "PUBLIC", "RAISERROR",
		"READ", "READTEXT", "RECONFIGURE", "REFERENCES", "REPLICATION",
		"RESTORE", "RESTRICT", "RETURN", "REVERT", "REVOKE", "RIGHT",
		"ROLLBACK", "ROWCOUNT", "ROWGUIDCOL", "RULE", "SAVE", "SCHEMA",
		"SECURITYAUDIT", "SELECT", "SEMANTICKEYPHRASETABLE",
		"SEMANTICSIMILARITYDETAILSTABLE", "SEMANTICSIMILARITYTABLE",
		"SESSION_USER", "SET", "SETUSER", "SHUTDOWN", "SOME", "STATISTICS",
		"SYSTEM_USER", "TABLE", "TABLESAMPLE", "TEXTSIZE", "THEN", "TO", "TOP",
		"TRAN", "TRANSACTION", "TRIGGER", "TRUNCATE", "TRY_CONVERT", "TSEQUAL",
		"UNION", "UNIQUE", "UNPIVOT", "UPDATE", "UPDATETEXT", "USE", "USER",
		"VALUES", "VIEW", "WAITFOR", "WHERE", "WHILE", "WITH", "WITHIN GROUP",
		"WRITETEXT", "ABSOLUTE", "ACTION", "ADA", "ALLOCATE", "ARE",
		"ASSERTION", "AT", "AVG", "BIT_LENGTH", "BOTH", "CASCADED", "CAST",
		"CATALOG", "CHARACTER_LENGTH", "CHAR_LENGTH", "COLLATION", "CONNECT",
		"CONNECTION", "CONSTRAINTS", "CORRESPONDING", "COUNT", "DAY",
		"DEFERRABLE", "DEFERRED", "DESCRIBE", "DESCRIPTOR", "DIAGNOSTICS",
		"DISCONNECT", "DOMAIN", "END-EXEC", "EXCEPTION", "EXTRACT", "FALSE",
		"FIRST", "FORTRAN", "FOUND", "GET", "GLOBAL", "GO", "HOUR", "IMMEDIATE",
		"INCLUDE", "INDICATOR", "INITIALLY", "INPUT", "INSENSITIVE", "INTERVAL",
		"ISOLATION", "LANGUAGE", "LAST", "LEADING", "LEVEL", "LOCAL", "LOWER",
		"MATCH", "MAX", "MIN", "MINUTE", "MODULE", "MONTH", "NAMES", "NATURAL",
		"NEXT", "NO", "NONE", "OCTET_LENGTH", "ONLY", "OUTPUT", "OVERLAPS",
		"PAD", "PARTIAL", "PASCAL", "POSITION", "PREPARE", "PRESERVE", "PRIOR",
		"PRIVILEGES", "RELATIVE", "ROWS", "SCROLL", "SECOND", "SECTION",
		"SESSION", "SIZE", "SPACE", "SQL", "SQLCA", "SQLCODE", "SQLERROR",
		"SQLSTATE", "SQLWARNING", "SUBSTRING", "SUM", "TEMPORARY",
		"TIMEZONE_HOUR", "TIMEZONE_MINUTE", "TRAILING", "TRANSLATE",
		"TRANSLATION", "TRIM", "TRUE", "UNKNOWN", "UPPER", "USAGE", "VALUE",
		"WHENEVER", "WORK", "WRITE", "YEAR", "ZONE"
	],
	qo = ["BINARY", "BIT", "CHAR", "CHAR", "CHARACTER", "DATE", "DATETIME2",
		"DATETIMEOFFSET", "DEC", "DECIMAL", "DOUBLE", "FLOAT", "INT", "INTEGER",
		"NATIONAL", "NCHAR", "NUMERIC", "NVARCHAR", "PRECISION", "REAL",
		"SMALLINT", "TIME", "TIMESTAMP", "VARBINARY", "VARCHAR"
	],
	Qo = v(["SELECT [ALL | DISTINCT]"]),
	Zo = v(["WITH", "INTO", "FROM", "WHERE", "GROUP BY", "HAVING", "WINDOW",
		"PARTITION BY", "ORDER BY", "OFFSET", "FETCH {FIRST | NEXT}",
		"FOR {BROWSE | XML | JSON}", "OPTION", "INSERT [INTO]", "VALUES",
		"SET", "MERGE [INTO]",
		"WHEN [NOT] MATCHED [BY TARGET | BY SOURCE] [THEN]", "UPDATE SET",
		"CREATE [OR ALTER] {PROC | PROCEDURE}"
	]),
	Lr = v(["CREATE TABLE"]),
	rT = v(["CREATE [OR ALTER] [MATERIALIZED] VIEW", "UPDATE",
		"WHERE CURRENT OF", "DELETE [FROM]", "DROP TABLE [IF EXISTS]",
		"ALTER TABLE", "ADD", "DROP COLUMN [IF EXISTS]", "ALTER COLUMN",
		"TRUNCATE TABLE", "ADD SENSITIVITY CLASSIFICATION", "ADD SIGNATURE",
		"AGGREGATE", "ANSI_DEFAULTS", "ANSI_NULLS", "ANSI_NULL_DFLT_OFF",
		"ANSI_NULL_DFLT_ON", "ANSI_PADDING", "ANSI_WARNINGS",
		"APPLICATION ROLE", "ARITHABORT", "ARITHIGNORE", "ASSEMBLY",
		"ASYMMETRIC KEY", "AUTHORIZATION", "AVAILABILITY GROUP", "BACKUP",
		"BACKUP CERTIFICATE", "BACKUP MASTER KEY",
		"BACKUP SERVICE MASTER KEY", "BEGIN CONVERSATION TIMER",
		"BEGIN DIALOG CONVERSATION", "BROKER PRIORITY", "BULK INSERT",
		"CERTIFICATE", "CLOSE MASTER KEY", "CLOSE SYMMETRIC KEY", "COLLATE",
		"COLUMN ENCRYPTION KEY", "COLUMN MASTER KEY", "COLUMNSTORE INDEX",
		"CONCAT_NULL_YIELDS_NULL", "CONTEXT_INFO", "CONTRACT", "CREDENTIAL",
		"CRYPTOGRAPHIC PROVIDER", "CURSOR_CLOSE_ON_COMMIT", "DATABASE",
		"DATABASE AUDIT SPECIFICATION", "DATABASE ENCRYPTION KEY",
		"DATABASE HADR", "DATABASE SCOPED CONFIGURATION",
		"DATABASE SCOPED CREDENTIAL", "DATABASE SET", "DATEFIRST",
		"DATEFORMAT", "DEADLOCK_PRIORITY", "DENY", "DENY XML",
		"DISABLE TRIGGER", "ENABLE TRIGGER", "END CONVERSATION", "ENDPOINT",
		"EVENT NOTIFICATION", "EVENT SESSION", "EXECUTE AS",
		"EXTERNAL DATA SOURCE", "EXTERNAL FILE FORMAT", "EXTERNAL LANGUAGE",
		"EXTERNAL LIBRARY", "EXTERNAL RESOURCE POOL", "EXTERNAL TABLE",
		"FIPS_FLAGGER", "FMTONLY", "FORCEPLAN", "FULLTEXT CATALOG",
		"FULLTEXT INDEX", "FULLTEXT STOPLIST", "FUNCTION",
		"GET CONVERSATION GROUP", "GET_TRANSMISSION_STATUS", "GRANT",
		"GRANT XML", "IDENTITY_INSERT", "IMPLICIT_TRANSACTIONS", "INDEX",
		"LANGUAGE", "LOCK_TIMEOUT", "LOGIN", "MASTER KEY", "MESSAGE TYPE",
		"MOVE CONVERSATION", "NOCOUNT", "NOEXEC", "NUMERIC_ROUNDABORT",
		"OFFSETS", "OPEN MASTER KEY", "OPEN SYMMETRIC KEY", "PARSEONLY",
		"PARTITION FUNCTION", "PARTITION SCHEME", "PROCEDURE",
		"QUERY_GOVERNOR_COST_LIMIT", "QUEUE", "QUOTED_IDENTIFIER",
		"RECEIVE", "REMOTE SERVICE BINDING", "REMOTE_PROC_TRANSACTIONS",
		"RESOURCE GOVERNOR", "RESOURCE POOL", "RESTORE",
		"RESTORE FILELISTONLY", "RESTORE HEADERONLY", "RESTORE LABELONLY",
		"RESTORE MASTER KEY", "RESTORE REWINDONLY",
		"RESTORE SERVICE MASTER KEY", "RESTORE VERIFYONLY", "REVERT",
		"REVOKE", "REVOKE XML", "ROLE", "ROUTE", "ROWCOUNT", "RULE",
		"SCHEMA", "SEARCH PROPERTY LIST", "SECURITY POLICY",
		"SELECTIVE XML INDEX", "SEND", "SENSITIVITY CLASSIFICATION",
		"SEQUENCE", "SERVER AUDIT", "SERVER AUDIT SPECIFICATION",
		"SERVER CONFIGURATION", "SERVER ROLE", "SERVICE",
		"SERVICE MASTER KEY", "SETUSER", "SHOWPLAN_ALL", "SHOWPLAN_TEXT",
		"SHOWPLAN_XML", "SIGNATURE", "SPATIAL INDEX", "STATISTICS",
		"STATISTICS IO", "STATISTICS PROFILE", "STATISTICS TIME",
		"STATISTICS XML", "SYMMETRIC KEY", "SYNONYM", "TABLE",
		"TABLE IDENTITY", "TEXTSIZE", "TRANSACTION ISOLATION LEVEL",
		"TRIGGER", "TYPE", "UPDATE STATISTICS", "USER", "WORKLOAD GROUP",
		"XACT_ABORT", "XML INDEX", "XML SCHEMA COLLECTION"
	]),
	jo = v(["UNION [ALL]", "EXCEPT", "INTERSECT"]),
	zo = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "{CROSS | OUTER} APPLY"
	]),
	eO = v(["ON {UPDATE | DELETE} [SET NULL | SET DEFAULT]",
		"{ROWS | RANGE} BETWEEN"
	]),
	EO = {
		name: "transactsql",
		tokenizerOptions: {
			reservedSelect: Qo,
			reservedClauses: [...Zo, ...Lr, ...rT],
			reservedSetOperations: jo,
			reservedJoins: zo,
			reservedPhrases: eO,
			reservedKeywords: Jo,
			reservedDataTypes: qo,
			reservedFunctionNames: Ko,
			nestedBlockComments: !0,
			stringTypes: [{
				quote: "''-qq",
				prefixes: ["N"]
			}],
			identTypes: ['""-qq', "[]"],
			identChars: {
				first: "#@",
				rest: "#@$"
			},
			paramTypes: {
				named: ["@"],
				quoted: ["@"]
			},
			operators: ["%", "&", "|", "^", "~", "!<", "!>", "+=", "-=", "*=",
				"/=", "%=", "|=", "&=", "^=", "::", ":"
			],
			propertyAccessOperators: [".."]
		},
		formatOptions: {
			alwaysDenseOperators: ["::"],
			onelineClauses: [...Lr, ...rT],
			tabularOnelineClauses: rT
		}
	},
	tO = ["ADD", "ALL", "ALTER", "ANALYZE", "AND", "AS", "ASC", "ASENSITIVE",
		"BEFORE", "BETWEEN", "_BINARY", "BOTH", "BY", "CALL", "CASCADE", "CASE",
		"CHANGE", "CHECK", "COLLATE", "COLUMN", "CONDITION", "CONSTRAINT",
		"CONTINUE", "CONVERT", "CREATE", "CROSS", "CURRENT_DATE",
		"CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", "CURSOR",
		"DATABASE", "DATABASES", "DAY_HOUR", "DAY_MICROSECOND", "DAY_MINUTE",
		"DAY_SECOND", "DECLARE", "DEFAULT", "DELAYED", "DELETE", "DESC",
		"DESCRIBE", "DETERMINISTIC", "DISTINCT", "DISTINCTROW", "DIV", "DROP",
		"DUAL", "EACH", "ELSE", "ELSEIF", "ENCLOSED", "ESCAPED", "EXCEPT",
		"EXISTS", "EXIT", "EXPLAIN", "EXTRA_JOIN", "FALSE", "FETCH", "FOR",
		"FORCE", "FORCE_COMPILED_MODE", "FORCE_INTERPRETER_MODE", "FOREIGN",
		"FROM", "FULL", "FULLTEXT", "GRANT", "GROUP", "HAVING",
		"HEARTBEAT_NO_LOGGING", "HIGH_PRIORITY", "HOUR_MICROSECOND",
		"HOUR_MINUTE", "HOUR_SECOND", "IF", "IGNORE", "IN", "INDEX", "INFILE",
		"INNER", "INOUT", "INSENSITIVE", "INSERT", "IN",
		"_INTERNAL_DYNAMIC_TYPECAST", "INTERSECT", "INTERVAL", "INTO",
		"ITERATE", "JOIN", "KEY", "KEYS", "KILL", "LEADING", "LEAVE", "LEFT",
		"LIKE", "LIMIT", "LINES", "LOAD", "LOCALTIME", "LOCALTIMESTAMP", "LOCK",
		"LOOP", "LOW_PRIORITY", "MATCH", "MAXVALUE", "MINUS",
		"MINUTE_MICROSECOND", "MINUTE_SECOND", "MOD", "MODIFIES", "NATURAL",
		"NO_QUERY_REWRITE", "NOT", "NO_WRITE_TO_BINLOG", "NO_QUERY_REWRITE",
		"NULL", "ON", "OPTIMIZE", "OPTION", "OPTIONALLY", "OR", "ORDER", "OUT",
		"OUTER", "OUTFILE", "OVER", "PRIMARY", "PROCEDURE", "PURGE", "RANGE",
		"READ", "READS", "REFERENCES", "REGEXP", "RELEASE", "RENAME", "REPEAT",
		"REPLACE", "REQUIRE", "RESTRICT", "RETURN", "REVOKE", "RIGHT",
		"RIGHT_ANTI_JOIN", "RIGHT_SEMI_JOIN", "RIGHT_STRAIGHT_JOIN", "RLIKE",
		"SCHEMA", "SCHEMAS", "SECOND_MICROSECOND", "SELECT", "SEMI_JOIN",
		"SENSITIVE", "SEPARATOR", "SET", "SHOW", "SIGNAL", "SPATIAL",
		"SPECIFIC", "SQL", "SQL_BIG_RESULT", "SQL_BUFFER_RESULT", "SQL_CACHE",
		"SQL_CALC_FOUND_ROWS", "SQLEXCEPTION", "SQL_NO_CACHE", "SQL_NO_LOGGING",
		"SQL_SMALL_RESULT", "SQLSTATE", "SQLWARNING", "STRAIGHT_JOIN", "TABLE",
		"TERMINATED", "THEN", "TO", "TRAILING", "TRIGGER", "TRUE", "UNBOUNDED",
		"UNDO", "UNION", "UNIQUE", "UNLOCK", "UPDATE", "USAGE", "USE", "USING",
		"UTC_DATE", "UTC_TIME", "UTC_TIMESTAMP", "_UTF8", "VALUES", "WHEN",
		"WHERE", "WHILE", "WINDOW", "WITH", "WITHIN", "WRITE", "XOR",
		"YEAR_MONTH", "ZEROFILL"
	],
	TO = ["BIGINT", "BINARY", "BIT", "BLOB", "CHAR", "CHARACTER", "DATETIME",
		"DEC", "DECIMAL", "DOUBLE PRECISION", "DOUBLE", "ENUM", "FIXED",
		"FLOAT", "FLOAT4", "FLOAT8", "INT", "INT1", "INT2", "INT3", "INT4",
		"INT8", "INTEGER", "LONG", "LONGBLOB", "LONGTEXT", "MEDIUMBLOB",
		"MEDIUMINT", "MEDIUMTEXT", "MIDDLEINT", "NATIONAL CHAR",
		"NATIONAL VARCHAR", "NUMERIC", "PRECISION", "REAL", "SMALLINT", "TEXT",
		"TIME", "TIMESTAMP", "TINYBLOB", "TINYINT", "TINYTEXT", "UNSIGNED",
		"VARBINARY", "VARCHAR", "VARCHARACTER", "YEAR"
	],
	rO = ["ABS", "ACOS", "ADDDATE", "ADDTIME", "AES_DECRYPT", "AES_ENCRYPT",
		"ANY_VALUE", "APPROX_COUNT_DISTINCT",
		"APPROX_COUNT_DISTINCT_ACCUMULATE", "APPROX_COUNT_DISTINCT_COMBINE",
		"APPROX_COUNT_DISTINCT_ESTIMATE", "APPROX_GEOGRAPHY_INTERSECTS",
		"APPROX_PERCENTILE", "ASCII", "ASIN", "ATAN", "ATAN2", "AVG", "BIN",
		"BINARY", "BIT_AND", "BIT_COUNT", "BIT_OR", "BIT_XOR", "CAST", "CEIL",
		"CEILING", "CHAR", "CHARACTER_LENGTH", "CHAR_LENGTH", "CHARSET",
		"COALESCE", "COERCIBILITY", "COLLATION", "COLLECT", "CONCAT",
		"CONCAT_WS", "CONNECTION_ID", "CONV", "CONVERT", "CONVERT_TZ", "COS",
		"COT", "COUNT", "CUME_DIST", "CURDATE", "CURRENT_DATE", "CURRENT_ROLE",
		"CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", "CURTIME",
		"DATABASE", "DATE", "DATE_ADD", "DATEDIFF", "DATE_FORMAT", "DATE_SUB",
		"DATE_TRUNC", "DAY", "DAYNAME", "DAYOFMONTH", "DAYOFWEEK", "DAYOFYEAR",
		"DECODE", "DEFAULT", "DEGREES", "DENSE_RANK", "DIV", "DOT_PRODUCT",
		"ELT", "EUCLIDEAN_DISTANCE", "EXP", "EXTRACT", "FIELD", "FIRST",
		"FIRST_VALUE", "FLOOR", "FORMAT", "FOUND_ROWS", "FROM_BASE64",
		"FROM_DAYS", "FROM_UNIXTIME", "GEOGRAPHY_AREA", "GEOGRAPHY_CONTAINS",
		"GEOGRAPHY_DISTANCE", "GEOGRAPHY_INTERSECTS", "GEOGRAPHY_LATITUDE",
		"GEOGRAPHY_LENGTH", "GEOGRAPHY_LONGITUDE", "GEOGRAPHY_POINT",
		"GEOGRAPHY_WITHIN_DISTANCE", "GEOMETRY_AREA", "GEOMETRY_CONTAINS",
		"GEOMETRY_DISTANCE", "GEOMETRY_FILTER", "GEOMETRY_INTERSECTS",
		"GEOMETRY_LENGTH", "GEOMETRY_POINT", "GEOMETRY_WITHIN_DISTANCE",
		"GEOMETRY_X", "GEOMETRY_Y", "GREATEST", "GROUPING", "GROUP_CONCAT",
		"HEX", "HIGHLIGHT", "HOUR", "ICU_VERSION", "IF", "IFNULL", "INET_ATON",
		"INET_NTOA", "INET6_ATON", "INET6_NTOA", "INITCAP", "INSERT", "INSTR",
		"INTERVAL", "IS", "IS NULL", "JSON_AGG", "JSON_ARRAY_CONTAINS_DOUBLE",
		"JSON_ARRAY_CONTAINS_JSON", "JSON_ARRAY_CONTAINS_STRING",
		"JSON_ARRAY_PUSH_DOUBLE", "JSON_ARRAY_PUSH_JSON",
		"JSON_ARRAY_PUSH_STRING", "JSON_DELETE_KEY", "JSON_EXTRACT_DOUBLE",
		"JSON_EXTRACT_JSON", "JSON_EXTRACT_STRING", "JSON_EXTRACT_BIGINT",
		"JSON_GET_TYPE", "JSON_LENGTH", "JSON_SET_DOUBLE", "JSON_SET_JSON",
		"JSON_SET_STRING", "JSON_SPLICE_DOUBLE", "JSON_SPLICE_JSON",
		"JSON_SPLICE_STRING", "LAG", "LAST_DAY", "LAST_VALUE", "LCASE", "LEAD",
		"LEAST", "LEFT", "LENGTH", "LIKE", "LN", "LOCALTIME", "LOCALTIMESTAMP",
		"LOCATE", "LOG", "LOG10", "LOG2", "LPAD", "LTRIM", "MATCH", "MAX",
		"MD5", "MEDIAN", "MICROSECOND", "MIN", "MINUTE", "MOD", "MONTH",
		"MONTHNAME", "MONTHS_BETWEEN", "NOT", "NOW", "NTH_VALUE", "NTILE",
		"NULLIF", "OCTET_LENGTH", "PERCENT_RANK", "PERCENTILE_CONT",
		"PERCENTILE_DISC", "PI", "PIVOT", "POSITION", "POW", "POWER", "QUARTER",
		"QUOTE", "RADIANS", "RAND", "RANK", "REGEXP", "REPEAT", "REPLACE",
		"REVERSE", "RIGHT", "RLIKE", "ROUND", "ROW_COUNT", "ROW_NUMBER", "RPAD",
		"RTRIM", "SCALAR", "SCHEMA", "SEC_TO_TIME", "SHA1", "SHA2", "SIGMOID",
		"SIGN", "SIN", "SLEEP", "SPLIT", "SOUNDEX", "SOUNDS LIKE",
		"SOURCE_POS_WAIT", "SPACE", "SQRT", "STDDEV", "STDDEV_POP",
		"STDDEV_SAMP", "STR_TO_DATE", "SUBDATE", "SUBSTR", "SUBSTRING",
		"SUBSTRING_INDEX", "SUM", "SYS_GUID", "TAN", "TIME", "TIMEDIFF",
		"TIME_BUCKET", "TIME_FORMAT", "TIMESTAMP", "TIMESTAMPADD",
		"TIMESTAMPDIFF", "TIME_TO_SEC", "TO_BASE64", "TO_CHAR", "TO_DAYS",
		"TO_JSON", "TO_NUMBER", "TO_SECONDS", "TO_TIMESTAMP", "TRIM", "TRUNC",
		"TRUNCATE", "UCASE", "UNHEX", "UNIX_TIMESTAMP", "UPDATEXML", "UPPER",
		"UTC_DATE", "UTC_TIME", "UTC_TIMESTAMP", "UUID", "VALUES", "VARIANCE",
		"VAR_POP", "VAR_SAMP", "VECTOR_SUB", "VERSION", "WEEK", "WEEKDAY",
		"WEEKOFYEAR", "YEAR"
	],
	RO = v(["SELECT [ALL | DISTINCT | DISTINCTROW]"]),
	nO = v(["WITH", "FROM", "WHERE", "GROUP BY", "HAVING", "PARTITION BY",
		"ORDER BY", "LIMIT", "OFFSET", "INSERT [IGNORE] [INTO]", "VALUES",
		"REPLACE [INTO]", "ON DUPLICATE KEY UPDATE", "SET",
		"CREATE [OR REPLACE] [TEMPORARY] PROCEDURE [IF NOT EXISTS]",
		"CREATE [OR REPLACE] [EXTERNAL] FUNCTION"
	]),
	Cr = v([
		"CREATE [ROWSTORE] [REFERENCE | TEMPORARY | GLOBAL TEMPORARY] TABLE [IF NOT EXISTS]"
	]),
	RT = v(["CREATE VIEW", "UPDATE", "DELETE [FROM]",
		"DROP [TEMPORARY] TABLE [IF EXISTS]", "ALTER [ONLINE] TABLE",
		"ADD [COLUMN]", "ADD [UNIQUE] {INDEX | KEY}", "DROP [COLUMN]",
		"MODIFY [COLUMN]", "CHANGE", "RENAME [TO | AS]", "TRUNCATE [TABLE]",
		"ADD AGGREGATOR", "ADD LEAF", "AGGREGATOR SET AS MASTER",
		"ALTER DATABASE", "ALTER PIPELINE", "ALTER RESOURCE POOL",
		"ALTER USER", "ALTER VIEW", "ANALYZE TABLE", "ATTACH DATABASE",
		"ATTACH LEAF", "ATTACH LEAF ALL", "BACKUP DATABASE", "BINLOG",
		"BOOTSTRAP AGGREGATOR", "CACHE INDEX", "CALL", "CHANGE",
		"CHANGE MASTER TO", "CHANGE REPLICATION FILTER",
		"CHANGE REPLICATION SOURCE TO", "CHECK BLOB CHECKSUM",
		"CHECK TABLE", "CHECKSUM TABLE", "CLEAR ORPHAN DATABASES", "CLONE",
		"COMMIT", "CREATE DATABASE", "CREATE GROUP", "CREATE INDEX",
		"CREATE LINK", "CREATE MILESTONE", "CREATE PIPELINE",
		"CREATE RESOURCE POOL", "CREATE ROLE", "CREATE USER",
		"DEALLOCATE PREPARE", "DESCRIBE", "DETACH DATABASE",
		"DETACH PIPELINE", "DROP DATABASE", "DROP FUNCTION", "DROP INDEX",
		"DROP LINK", "DROP PIPELINE", "DROP PROCEDURE",
		"DROP RESOURCE POOL", "DROP ROLE", "DROP USER", "DROP VIEW",
		"EXECUTE", "EXPLAIN", "FLUSH", "FORCE", "GRANT", "HANDLER", "HELP",
		"KILL CONNECTION", "KILLALL QUERIES", "LOAD DATA",
		"LOAD INDEX INTO CACHE", "LOAD XML", "LOCK INSTANCE FOR BACKUP",
		"LOCK TABLES", "MASTER_POS_WAIT", "OPTIMIZE TABLE", "PREPARE",
		"PURGE BINARY LOGS", "REBALANCE PARTITIONS", "RELEASE SAVEPOINT",
		"REMOVE AGGREGATOR", "REMOVE LEAF", "REPAIR TABLE", "REPLACE",
		"REPLICATE DATABASE", "RESET", "RESET MASTER", "RESET PERSIST",
		"RESET REPLICA", "RESET SLAVE", "RESTART", "RESTORE DATABASE",
		"RESTORE REDUNDANCY", "REVOKE", "ROLLBACK", "ROLLBACK TO SAVEPOINT",
		"SAVEPOINT", "SET CHARACTER SET", "SET DEFAULT ROLE", "SET NAMES",
		"SET PASSWORD", "SET RESOURCE GROUP", "SET ROLE", "SET TRANSACTION",
		"SHOW", "SHOW CHARACTER SET", "SHOW COLLATION", "SHOW COLUMNS",
		"SHOW CREATE DATABASE", "SHOW CREATE FUNCTION",
		"SHOW CREATE PIPELINE", "SHOW CREATE PROCEDURE",
		"SHOW CREATE TABLE", "SHOW CREATE USER", "SHOW CREATE VIEW",
		"SHOW DATABASES", "SHOW ENGINE", "SHOW ENGINES", "SHOW ERRORS",
		"SHOW FUNCTION CODE", "SHOW FUNCTION STATUS", "SHOW GRANTS",
		"SHOW INDEX", "SHOW MASTER STATUS", "SHOW OPEN TABLES",
		"SHOW PLUGINS", "SHOW PRIVILEGES", "SHOW PROCEDURE CODE",
		"SHOW PROCEDURE STATUS", "SHOW PROCESSLIST", "SHOW PROFILE",
		"SHOW PROFILES", "SHOW RELAYLOG EVENTS", "SHOW REPLICA STATUS",
		"SHOW REPLICAS", "SHOW SLAVE", "SHOW SLAVE HOSTS", "SHOW STATUS",
		"SHOW TABLE STATUS", "SHOW TABLES", "SHOW VARIABLES",
		"SHOW WARNINGS", "SHUTDOWN", "SNAPSHOT DATABASE", "SOURCE_POS_WAIT",
		"START GROUP_REPLICATION", "START PIPELINE", "START REPLICA",
		"START SLAVE", "START TRANSACTION", "STOP GROUP_REPLICATION",
		"STOP PIPELINE", "STOP REPLICA", "STOP REPLICATING", "STOP SLAVE",
		"TEST PIPELINE", "UNLOCK INSTANCE", "UNLOCK TABLES", "USE", "XA",
		"ITERATE", "LEAVE", "LOOP", "REPEAT", "RETURN", "WHILE"
	]),
	AO = v(["UNION [ALL | DISTINCT]", "EXCEPT", "INTERSECT", "MINUS"]),
	sO = v(["JOIN", "{LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{INNER | CROSS} JOIN", "NATURAL {LEFT | RIGHT} [OUTER] JOIN",
		"STRAIGHT_JOIN"
	]),
	SO = v(["ON DELETE", "ON UPDATE", "CHARACTER SET", "{ROWS | RANGE} BETWEEN",
		"IDENTIFIED BY"
	]),
	oO = {
		name: "singlestoredb",
		tokenizerOptions: {
			reservedSelect: RO,
			reservedClauses: [...nO, ...Cr, ...RT],
			reservedSetOperations: AO,
			reservedJoins: sO,
			reservedPhrases: SO,
			reservedKeywords: tO,
			reservedDataTypes: TO,
			reservedFunctionNames: rO,
			stringTypes: ['""-qq-bs', "''-qq-bs", {
				quote: "''-raw",
				prefixes: ["B", "X"],
				requirePrefix: !0
			}],
			identTypes: ["``"],
			identChars: {
				first: "$",
				rest: "$",
				allowFirstCharNumber: !0
			},
			variableTypes: [{
				regex: "@@?[A-Za-z0-9_$]+"
			}, {
				quote: "``",
				prefixes: ["@"],
				requirePrefix: !0
			}],
			lineCommentTypes: ["--", "#"],
			operators: [":=", "&", "|", "^", "~", "<<", ">>", "<=>", "&&", "||",
				"::", "::$", "::%", ":>", "!:>", "*.*"
			],
			postProcess: yt
		},
		formatOptions: {
			alwaysDenseOperators: ["::", "::$", "::%"],
			onelineClauses: [...Cr, ...RT],
			tabularOnelineClauses: RT
		}
	},
	OO = ["ABS", "ACOS", "ACOSH", "ADD_MONTHS", "ALL_USER_NAMES", "ANY_VALUE",
		"APPROX_COUNT_DISTINCT", "APPROX_PERCENTILE",
		"APPROX_PERCENTILE_ACCUMULATE", "APPROX_PERCENTILE_COMBINE",
		"APPROX_PERCENTILE_ESTIMATE", "APPROX_TOP_K", "APPROX_TOP_K_ACCUMULATE",
		"APPROX_TOP_K_COMBINE", "APPROX_TOP_K_ESTIMATE",
		"APPROXIMATE_JACCARD_INDEX", "APPROXIMATE_SIMILARITY", "ARRAY_AGG",
		"ARRAY_APPEND", "ARRAY_CAT", "ARRAY_COMPACT", "ARRAY_CONSTRUCT",
		"ARRAY_CONSTRUCT_COMPACT", "ARRAY_CONTAINS", "ARRAY_INSERT",
		"ARRAY_INTERSECTION", "ARRAY_POSITION", "ARRAY_PREPEND", "ARRAY_SIZE",
		"ARRAY_SLICE", "ARRAY_TO_STRING", "ARRAY_UNION_AGG", "ARRAY_UNIQUE_AGG",
		"ARRAYS_OVERLAP", "AS_ARRAY", "AS_BINARY", "AS_BOOLEAN", "AS_CHAR",
		"AS_VARCHAR", "AS_DATE", "AS_DECIMAL", "AS_NUMBER", "AS_DOUBLE",
		"AS_REAL", "AS_INTEGER", "AS_OBJECT", "AS_TIME", "AS_TIMESTAMP_LTZ",
		"AS_TIMESTAMP_NTZ", "AS_TIMESTAMP_TZ", "ASCII", "ASIN", "ASINH", "ATAN",
		"ATAN2", "ATANH", "AUTO_REFRESH_REGISTRATION_HISTORY",
		"AUTOMATIC_CLUSTERING_HISTORY", "AVG", "BASE64_DECODE_BINARY",
		"BASE64_DECODE_STRING", "BASE64_ENCODE", "BIT_LENGTH", "BITAND",
		"BITAND_AGG", "BITMAP_BIT_POSITION", "BITMAP_BUCKET_NUMBER",
		"BITMAP_CONSTRUCT_AGG", "BITMAP_COUNT", "BITMAP_OR_AGG", "BITNOT",
		"BITOR", "BITOR_AGG", "BITSHIFTLEFT", "BITSHIFTRIGHT", "BITXOR",
		"BITXOR_AGG", "BOOLAND", "BOOLAND_AGG", "BOOLNOT", "BOOLOR",
		"BOOLOR_AGG", "BOOLXOR", "BOOLXOR_AGG", "BUILD_SCOPED_FILE_URL",
		"BUILD_STAGE_FILE_URL", "CASE", "CAST", "CBRT", "CEIL", "CHARINDEX",
		"CHECK_JSON", "CHECK_XML", "CHR", "CHAR", "COALESCE", "COLLATE",
		"COLLATION", "COMPLETE_TASK_GRAPHS", "COMPRESS", "CONCAT", "CONCAT_WS",
		"CONDITIONAL_CHANGE_EVENT", "CONDITIONAL_TRUE_EVENT", "CONTAINS",
		"CONVERT_TIMEZONE", "COPY_HISTORY", "CORR", "COS", "COSH", "COT",
		"COUNT", "COUNT_IF", "COVAR_POP", "COVAR_SAMP", "CUME_DIST",
		"CURRENT_ACCOUNT", "CURRENT_AVAILABLE_ROLES", "CURRENT_CLIENT",
		"CURRENT_DATABASE", "CURRENT_DATE", "CURRENT_IP_ADDRESS",
		"CURRENT_REGION", "CURRENT_ROLE", "CURRENT_SCHEMA", "CURRENT_SCHEMAS",
		"CURRENT_SECONDARY_ROLES", "CURRENT_SESSION", "CURRENT_STATEMENT",
		"CURRENT_TASK_GRAPHS", "CURRENT_TIME", "CURRENT_TIMESTAMP",
		"CURRENT_TRANSACTION", "CURRENT_USER", "CURRENT_VERSION",
		"CURRENT_WAREHOUSE", "DATA_TRANSFER_HISTORY",
		"DATABASE_REFRESH_HISTORY", "DATABASE_REFRESH_PROGRESS",
		"DATABASE_REFRESH_PROGRESS_BY_JOB", "DATABASE_STORAGE_USAGE_HISTORY",
		"DATE_FROM_PARTS", "DATE_PART", "DATE_TRUNC", "DATEADD", "DATEDIFF",
		"DAYNAME", "DECODE", "DECOMPRESS_BINARY", "DECOMPRESS_STRING",
		"DECRYPT", "DECRYPT_RAW", "DEGREES", "DENSE_RANK", "DIV0",
		"EDITDISTANCE", "ENCRYPT", "ENCRYPT_RAW", "ENDSWITH", "EQUAL_NULL",
		"EXP", "EXPLAIN_JSON", "EXTERNAL_FUNCTIONS_HISTORY",
		"EXTERNAL_TABLE_FILES", "EXTERNAL_TABLE_FILE_REGISTRATION_HISTORY",
		"EXTRACT", "EXTRACT_SEMANTIC_CATEGORIES", "FACTORIAL", "FIRST_VALUE",
		"FLATTEN", "FLOOR", "GENERATE_COLUMN_DESCRIPTION", "GENERATOR", "GET",
		"GET_ABSOLUTE_PATH", "GET_DDL", "GET_IGNORE_CASE",
		"GET_OBJECT_REFERENCES", "GET_PATH", "GET_PRESIGNED_URL",
		"GET_RELATIVE_PATH", "GET_STAGE_LOCATION", "GETBIT", "GREATEST",
		"GROUPING", "GROUPING_ID", "HASH", "HASH_AGG", "HAVERSINE",
		"HEX_DECODE_BINARY", "HEX_DECODE_STRING", "HEX_ENCODE", "HLL",
		"HLL_ACCUMULATE", "HLL_COMBINE", "HLL_ESTIMATE", "HLL_EXPORT",
		"HLL_IMPORT", "HOUR", "MINUTE", "SECOND", "IFF", "IFNULL", "ILIKE",
		"ILIKE ANY", "INFER_SCHEMA", "INITCAP", "INSERT", "INVOKER_ROLE",
		"INVOKER_SHARE", "IS_ARRAY", "IS_BINARY", "IS_BOOLEAN", "IS_CHAR",
		"IS_VARCHAR", "IS_DATE", "IS_DATE_VALUE", "IS_DECIMAL", "IS_DOUBLE",
		"IS_REAL", "IS_GRANTED_TO_INVOKER_ROLE", "IS_INTEGER", "IS_NULL_VALUE",
		"IS_OBJECT", "IS_ROLE_IN_SESSION", "IS_TIME", "IS_TIMESTAMP_LTZ",
		"IS_TIMESTAMP_NTZ", "IS_TIMESTAMP_TZ", "JAROWINKLER_SIMILARITY",
		"JSON_EXTRACT_PATH_TEXT", "KURTOSIS", "LAG", "LAST_DAY",
		"LAST_QUERY_ID", "LAST_TRANSACTION", "LAST_VALUE", "LEAD", "LEAST",
		"LEFT", "LENGTH", "LEN", "LIKE", "LIKE ALL", "LIKE ANY", "LISTAGG",
		"LN", "LOCALTIME", "LOCALTIMESTAMP", "LOG", "LOGIN_HISTORY",
		"LOGIN_HISTORY_BY_USER", "LOWER", "LPAD", "LTRIM",
		"MATERIALIZED_VIEW_REFRESH_HISTORY", "MD5", "MD5_HEX", "MD5_BINARY",
		"MD5_NUMBER — Obsoleted", "MD5_NUMBER_LOWER64", "MD5_NUMBER_UPPER64",
		"MEDIAN", "MIN", "MAX", "MINHASH", "MINHASH_COMBINE", "MOD", "MODE",
		"MONTHNAME", "MONTHS_BETWEEN", "NEXT_DAY", "NORMAL", "NTH_VALUE",
		"NTILE", "NULLIF", "NULLIFZERO", "NVL", "NVL2", "OBJECT_AGG",
		"OBJECT_CONSTRUCT", "OBJECT_CONSTRUCT_KEEP_NULL", "OBJECT_DELETE",
		"OBJECT_INSERT", "OBJECT_KEYS", "OBJECT_PICK", "OCTET_LENGTH",
		"PARSE_IP", "PARSE_JSON", "PARSE_URL", "PARSE_XML", "PERCENT_RANK",
		"PERCENTILE_CONT", "PERCENTILE_DISC", "PI", "PIPE_USAGE_HISTORY",
		"POLICY_CONTEXT", "POLICY_REFERENCES", "POSITION", "POW", "POWER",
		"PREVIOUS_DAY", "QUERY_ACCELERATION_HISTORY", "QUERY_HISTORY",
		"QUERY_HISTORY_BY_SESSION", "QUERY_HISTORY_BY_USER",
		"QUERY_HISTORY_BY_WAREHOUSE", "RADIANS", "RANDOM", "RANDSTR", "RANK",
		"RATIO_TO_REPORT", "REGEXP", "REGEXP_COUNT", "REGEXP_INSTR",
		"REGEXP_LIKE", "REGEXP_REPLACE", "REGEXP_SUBSTR", "REGEXP_SUBSTR_ALL",
		"REGR_AVGX", "REGR_AVGY", "REGR_COUNT", "REGR_INTERCEPT", "REGR_R2",
		"REGR_SLOPE", "REGR_SXX", "REGR_SXY", "REGR_SYY", "REGR_VALX",
		"REGR_VALY", "REPEAT", "REPLACE", "REPLICATION_GROUP_REFRESH_HISTORY",
		"REPLICATION_GROUP_REFRESH_PROGRESS",
		"REPLICATION_GROUP_REFRESH_PROGRESS_BY_JOB",
		"REPLICATION_GROUP_USAGE_HISTORY", "REPLICATION_USAGE_HISTORY",
		"REST_EVENT_HISTORY", "RESULT_SCAN", "REVERSE", "RIGHT", "RLIKE",
		"ROUND", "ROW_NUMBER", "RPAD", "RTRIM", "RTRIMMED_LENGTH",
		"SEARCH_OPTIMIZATION_HISTORY", "SEQ1", "SEQ2", "SEQ4", "SEQ8",
		"SERVERLESS_TASK_HISTORY", "SHA1", "SHA1_HEX", "SHA1_BINARY", "SHA2",
		"SHA2_HEX", "SHA2_BINARY", "SIGN", "SIN", "SINH", "SKEW", "SOUNDEX",
		"SPACE", "SPLIT", "SPLIT_PART", "SPLIT_TO_TABLE", "SQRT", "SQUARE",
		"ST_AREA", "ST_ASEWKB", "ST_ASEWKT", "ST_ASGEOJSON", "ST_ASWKB",
		"ST_ASBINARY", "ST_ASWKT", "ST_ASTEXT", "ST_AZIMUTH", "ST_CENTROID",
		"ST_COLLECT", "ST_CONTAINS", "ST_COVEREDBY", "ST_COVERS",
		"ST_DIFFERENCE", "ST_DIMENSION", "ST_DISJOINT", "ST_DISTANCE",
		"ST_DWITHIN", "ST_ENDPOINT", "ST_ENVELOPE", "ST_GEOGFROMGEOHASH",
		"ST_GEOGPOINTFROMGEOHASH", "ST_GEOGRAPHYFROMWKB", "ST_GEOGRAPHYFROMWKT",
		"ST_GEOHASH", "ST_GEOMETRYFROMWKB", "ST_GEOMETRYFROMWKT",
		"ST_HAUSDORFFDISTANCE", "ST_INTERSECTION", "ST_INTERSECTS", "ST_LENGTH",
		"ST_MAKEGEOMPOINT", "ST_GEOM_POINT", "ST_MAKELINE", "ST_MAKEPOINT",
		"ST_POINT", "ST_MAKEPOLYGON", "ST_POLYGON", "ST_NPOINTS",
		"ST_NUMPOINTS", "ST_PERIMETER", "ST_POINTN", "ST_SETSRID",
		"ST_SIMPLIFY", "ST_SRID", "ST_STARTPOINT", "ST_SYMDIFFERENCE",
		"ST_UNION", "ST_WITHIN", "ST_X", "ST_XMAX", "ST_XMIN", "ST_Y",
		"ST_YMAX", "ST_YMIN", "STAGE_DIRECTORY_FILE_REGISTRATION_HISTORY",
		"STAGE_STORAGE_USAGE_HISTORY", "STARTSWITH", "STDDEV", "STDDEV_POP",
		"STDDEV_SAMP", "STRIP_NULL_VALUE", "STRTOK", "STRTOK_SPLIT_TO_TABLE",
		"STRTOK_TO_ARRAY", "SUBSTR", "SUBSTRING", "SUM", "SYSDATE",
		"SYSTEM$ABORT_SESSION", "SYSTEM$ABORT_TRANSACTION",
		"SYSTEM$AUTHORIZE_PRIVATELINK",
		"SYSTEM$AUTHORIZE_STAGE_PRIVATELINK_ACCESS",
		"SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS", "SYSTEM$CANCEL_ALL_QUERIES",
		"SYSTEM$CANCEL_QUERY", "SYSTEM$CLUSTERING_DEPTH",
		"SYSTEM$CLUSTERING_INFORMATION", "SYSTEM$CLUSTERING_RATIO ",
		"SYSTEM$CURRENT_USER_TASK_NAME", "SYSTEM$DATABASE_REFRESH_HISTORY ",
		"SYSTEM$DATABASE_REFRESH_PROGRESS",
		"SYSTEM$DATABASE_REFRESH_PROGRESS_BY_JOB ",
		"SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE",
		"SYSTEM$DISABLE_DATABASE_REPLICATION",
		"SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE",
		"SYSTEM$ESTIMATE_QUERY_ACCELERATION",
		"SYSTEM$ESTIMATE_SEARCH_OPTIMIZATION_COSTS",
		"SYSTEM$EXPLAIN_JSON_TO_TEXT", "SYSTEM$EXPLAIN_PLAN_JSON",
		"SYSTEM$EXTERNAL_TABLE_PIPE_STATUS", "SYSTEM$GENERATE_SAML_CSR",
		"SYSTEM$GENERATE_SCIM_ACCESS_TOKEN", "SYSTEM$GET_AWS_SNS_IAM_POLICY",
		"SYSTEM$GET_PREDECESSOR_RETURN_VALUE", "SYSTEM$GET_PRIVATELINK",
		"SYSTEM$GET_PRIVATELINK_AUTHORIZED_ENDPOINTS",
		"SYSTEM$GET_PRIVATELINK_CONFIG", "SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO",
		"SYSTEM$GET_TAG", "SYSTEM$GET_TAG_ALLOWED_VALUES",
		"SYSTEM$GET_TAG_ON_CURRENT_COLUMN", "SYSTEM$GET_TAG_ON_CURRENT_TABLE",
		"SYSTEM$GLOBAL_ACCOUNT_SET_PARAMETER", "SYSTEM$LAST_CHANGE_COMMIT_TIME",
		"SYSTEM$LINK_ACCOUNT_OBJECTS_BY_NAME",
		"SYSTEM$MIGRATE_SAML_IDP_REGISTRATION", "SYSTEM$PIPE_FORCE_RESUME",
		"SYSTEM$PIPE_STATUS", "SYSTEM$REVOKE_PRIVATELINK",
		"SYSTEM$REVOKE_STAGE_PRIVATELINK_ACCESS", "SYSTEM$SET_RETURN_VALUE",
		"SYSTEM$SHOW_OAUTH_CLIENT_SECRETS", "SYSTEM$STREAM_GET_TABLE_TIMESTAMP",
		"SYSTEM$STREAM_HAS_DATA", "SYSTEM$TASK_DEPENDENTS_ENABLE",
		"SYSTEM$TYPEOF", "SYSTEM$USER_TASK_CANCEL_ONGOING_EXECUTIONS",
		"SYSTEM$VERIFY_EXTERNAL_OAUTH_TOKEN", "SYSTEM$WAIT", "SYSTEM$WHITELIST",
		"SYSTEM$WHITELIST_PRIVATELINK", "TAG_REFERENCES",
		"TAG_REFERENCES_ALL_COLUMNS", "TAG_REFERENCES_WITH_LINEAGE", "TAN",
		"TANH", "TASK_DEPENDENTS", "TASK_HISTORY", "TIME_FROM_PARTS",
		"TIME_SLICE", "TIMEADD", "TIMEDIFF", "TIMESTAMP_FROM_PARTS",
		"TIMESTAMPADD", "TIMESTAMPDIFF", "TO_ARRAY", "TO_BINARY", "TO_BOOLEAN",
		"TO_CHAR", "TO_VARCHAR", "TO_DATE", "DATE", "TO_DECIMAL", "TO_NUMBER",
		"TO_NUMERIC", "TO_DOUBLE", "TO_GEOGRAPHY", "TO_GEOMETRY", "TO_JSON",
		"TO_OBJECT", "TO_TIME", "TIME", "TO_TIMESTAMP", "TO_TIMESTAMP_LTZ",
		"TO_TIMESTAMP_NTZ", "TO_TIMESTAMP_TZ", "TO_VARIANT", "TO_XML",
		"TRANSLATE", "TRIM", "TRUNCATE", "TRUNC", "TRUNC",
		"TRY_BASE64_DECODE_BINARY", "TRY_BASE64_DECODE_STRING", "TRY_CAST",
		"TRY_HEX_DECODE_BINARY", "TRY_HEX_DECODE_STRING", "TRY_PARSE_JSON",
		"TRY_TO_BINARY", "TRY_TO_BOOLEAN", "TRY_TO_DATE", "TRY_TO_DECIMAL",
		"TRY_TO_NUMBER", "TRY_TO_NUMERIC", "TRY_TO_DOUBLE", "TRY_TO_GEOGRAPHY",
		"TRY_TO_GEOMETRY", "TRY_TO_TIME", "TRY_TO_TIMESTAMP",
		"TRY_TO_TIMESTAMP_LTZ", "TRY_TO_TIMESTAMP_NTZ", "TRY_TO_TIMESTAMP_TZ",
		"TYPEOF", "UNICODE", "UNIFORM", "UPPER", "UUID_STRING", "VALIDATE",
		"VALIDATE_PIPE_LOAD", "VAR_POP", "VAR_SAMP", "VARIANCE",
		"VARIANCE_SAMP", "VARIANCE_POP", "WAREHOUSE_LOAD_HISTORY",
		"WAREHOUSE_METERING_HISTORY", "WIDTH_BUCKET", "XMLGET", "YEAR",
		"YEAROFWEEK", "YEAROFWEEKISO", "DAY", "DAYOFMONTH", "DAYOFWEEK",
		"DAYOFWEEKISO", "DAYOFYEAR", "WEEK", "WEEK", "WEEKOFYEAR", "WEEKISO",
		"MONTH", "QUARTER", "ZEROIFNULL", "ZIPF"
	],
	iO = ["ACCOUNT", "ALL", "ALTER", "AND", "ANY", "AS", "BETWEEN", "BY",
		"CASE", "CAST", "CHECK", "COLUMN", "CONNECT", "CONNECTION",
		"CONSTRAINT", "CREATE", "CROSS", "CURRENT", "CURRENT_DATE",
		"CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", "DATABASE",
		"DELETE", "DISTINCT", "DROP", "ELSE", "EXISTS", "FALSE", "FOLLOWING",
		"FOR", "FROM", "FULL", "GRANT", "GROUP", "GSCLUSTER", "HAVING", "ILIKE",
		"IN", "INCREMENT", "INNER", "INSERT", "INTERSECT", "INTO", "IS",
		"ISSUE", "JOIN", "LATERAL", "LEFT", "LIKE", "LOCALTIME",
		"LOCALTIMESTAMP", "MINUS", "NATURAL", "NOT", "NULL", "OF", "ON", "OR",
		"ORDER", "ORGANIZATION", "QUALIFY", "REGEXP", "REVOKE", "RIGHT",
		"RLIKE", "ROW", "ROWS", "SAMPLE", "SCHEMA", "SELECT", "SET", "SOME",
		"START", "TABLE", "TABLESAMPLE", "THEN", "TO", "TRIGGER", "TRUE",
		"TRY_CAST", "UNION", "UNIQUE", "UPDATE", "USING", "VALUES", "VIEW",
		"WHEN", "WHENEVER", "WHERE", "WITH", "COMMENT"
	],
	aO = ["NUMBER", "DECIMAL", "NUMERIC", "INT", "INTEGER", "BIGINT",
		"SMALLINT", "TINYINT", "BYTEINT", "FLOAT", "FLOAT4", "FLOAT8", "DOUBLE",
		"DOUBLE PRECISION", "REAL", "VARCHAR", "CHAR", "CHARACTER", "STRING",
		"TEXT", "BINARY", "VARBINARY", "BOOLEAN", "DATE", "DATETIME", "TIME",
		"TIMESTAMP", "TIMESTAMP_LTZ", "TIMESTAMP_NTZ", "TIMESTAMP",
		"TIMESTAMP_TZ", "VARIANT", "OBJECT", "ARRAY", "GEOGRAPHY", "GEOMETRY"
	],
	IO = v(["SELECT [ALL | DISTINCT]"]),
	NO = v(["WITH [RECURSIVE]", "FROM", "WHERE", "GROUP BY", "HAVING",
		"PARTITION BY", "ORDER BY", "QUALIFY", "LIMIT", "OFFSET",
		"FETCH [FIRST | NEXT]",
		"INSERT [OVERWRITE] [ALL INTO | INTO | ALL | FIRST]",
		"{THEN | ELSE} INTO", "VALUES", "SET", "CLUSTER BY",
		"[WITH] {MASKING POLICY | TAG | ROW ACCESS POLICY}", "COPY GRANTS",
		"USING TEMPLATE", "MERGE INTO", "WHEN MATCHED [AND]",
		"THEN {UPDATE SET | DELETE}", "WHEN NOT MATCHED THEN INSERT"
	]),
	ur = v(["CREATE [OR REPLACE] [VOLATILE] TABLE [IF NOT EXISTS]",
		"CREATE [OR REPLACE] [LOCAL | GLOBAL] {TEMP|TEMPORARY} TABLE [IF NOT EXISTS]"
	]),
	nT = v(["CREATE [OR REPLACE] [SECURE] [RECURSIVE] VIEW [IF NOT EXISTS]",
		"UPDATE", "DELETE FROM", "DROP TABLE [IF EXISTS]",
		"ALTER TABLE [IF EXISTS]", "RENAME TO", "SWAP WITH",
		"[SUSPEND | RESUME] RECLUSTER", "DROP CLUSTERING KEY",
		"ADD [COLUMN]", "RENAME COLUMN", "{ALTER | MODIFY} [COLUMN]",
		"DROP [COLUMN]", "{ADD | ALTER | MODIFY | DROP} [CONSTRAINT]",
		"RENAME CONSTRAINT", "{ADD | DROP} SEARCH OPTIMIZATION",
		"{SET | UNSET} TAG", "{ADD | DROP} ROW ACCESS POLICY",
		"DROP ALL ROW ACCESS POLICIES", "{SET | DROP} DEFAULT",
		"{SET | DROP} NOT NULL", "[SET DATA] TYPE", "UNSET COMMENT",
		"{SET | UNSET} MASKING POLICY", "TRUNCATE [TABLE] [IF EXISTS]",
		"ALTER ACCOUNT", "ALTER API INTEGRATION", "ALTER CONNECTION",
		"ALTER DATABASE", "ALTER EXTERNAL TABLE", "ALTER FAILOVER GROUP",
		"ALTER FILE FORMAT", "ALTER FUNCTION", "ALTER INTEGRATION",
		"ALTER MASKING POLICY", "ALTER MATERIALIZED VIEW",
		"ALTER NETWORK POLICY", "ALTER NOTIFICATION INTEGRATION",
		"ALTER PIPE", "ALTER PROCEDURE", "ALTER REPLICATION GROUP",
		"ALTER RESOURCE MONITOR", "ALTER ROLE", "ALTER ROW ACCESS POLICY",
		"ALTER SCHEMA", "ALTER SECURITY INTEGRATION", "ALTER SEQUENCE",
		"ALTER SESSION", "ALTER SESSION POLICY", "ALTER SHARE",
		"ALTER STAGE", "ALTER STORAGE INTEGRATION", "ALTER STREAM",
		"ALTER TAG", "ALTER TASK", "ALTER USER", "ALTER VIEW",
		"ALTER WAREHOUSE", "BEGIN", "CALL", "COMMIT", "COPY INTO",
		"CREATE ACCOUNT", "CREATE API INTEGRATION", "CREATE CONNECTION",
		"CREATE DATABASE", "CREATE EXTERNAL FUNCTION",
		"CREATE EXTERNAL TABLE", "CREATE FAILOVER GROUP",
		"CREATE FILE FORMAT", "CREATE FUNCTION", "CREATE INTEGRATION",
		"CREATE MANAGED ACCOUNT", "CREATE MASKING POLICY",
		"CREATE MATERIALIZED VIEW", "CREATE NETWORK POLICY",
		"CREATE NOTIFICATION INTEGRATION", "CREATE PIPE",
		"CREATE PROCEDURE", "CREATE REPLICATION GROUP",
		"CREATE RESOURCE MONITOR", "CREATE ROLE",
		"CREATE ROW ACCESS POLICY", "CREATE SCHEMA",
		"CREATE SECURITY INTEGRATION", "CREATE SEQUENCE",
		"CREATE SESSION POLICY", "CREATE SHARE", "CREATE STAGE",
		"CREATE STORAGE INTEGRATION", "CREATE STREAM", "CREATE TAG",
		"CREATE TASK", "CREATE USER", "CREATE WAREHOUSE", "DELETE",
		"DESCRIBE DATABASE", "DESCRIBE EXTERNAL TABLE",
		"DESCRIBE FILE FORMAT", "DESCRIBE FUNCTION", "DESCRIBE INTEGRATION",
		"DESCRIBE MASKING POLICY", "DESCRIBE MATERIALIZED VIEW",
		"DESCRIBE NETWORK POLICY", "DESCRIBE PIPE", "DESCRIBE PROCEDURE",
		"DESCRIBE RESULT", "DESCRIBE ROW ACCESS POLICY", "DESCRIBE SCHEMA",
		"DESCRIBE SEQUENCE", "DESCRIBE SESSION POLICY", "DESCRIBE SHARE",
		"DESCRIBE STAGE", "DESCRIBE STREAM", "DESCRIBE TABLE",
		"DESCRIBE TASK", "DESCRIBE TRANSACTION", "DESCRIBE USER",
		"DESCRIBE VIEW", "DESCRIBE WAREHOUSE", "DROP CONNECTION",
		"DROP DATABASE", "DROP EXTERNAL TABLE", "DROP FAILOVER GROUP",
		"DROP FILE FORMAT", "DROP FUNCTION", "DROP INTEGRATION",
		"DROP MANAGED ACCOUNT", "DROP MASKING POLICY",
		"DROP MATERIALIZED VIEW", "DROP NETWORK POLICY", "DROP PIPE",
		"DROP PROCEDURE", "DROP REPLICATION GROUP", "DROP RESOURCE MONITOR",
		"DROP ROLE", "DROP ROW ACCESS POLICY", "DROP SCHEMA",
		"DROP SEQUENCE", "DROP SESSION POLICY", "DROP SHARE", "DROP STAGE",
		"DROP STREAM", "DROP TAG", "DROP TASK", "DROP USER", "DROP VIEW",
		"DROP WAREHOUSE", "EXECUTE IMMEDIATE", "EXECUTE TASK", "EXPLAIN",
		"GET", "GRANT OWNERSHIP", "GRANT ROLE", "INSERT", "LIST", "MERGE",
		"PUT", "REMOVE", "REVOKE ROLE", "ROLLBACK", "SHOW COLUMNS",
		"SHOW CONNECTIONS", "SHOW DATABASES",
		"SHOW DATABASES IN FAILOVER GROUP",
		"SHOW DATABASES IN REPLICATION GROUP",
		"SHOW DELEGATED AUTHORIZATIONS", "SHOW EXTERNAL FUNCTIONS",
		"SHOW EXTERNAL TABLES", "SHOW FAILOVER GROUPS", "SHOW FILE FORMATS",
		"SHOW FUNCTIONS", "SHOW GLOBAL ACCOUNTS", "SHOW GRANTS",
		"SHOW INTEGRATIONS", "SHOW LOCKS", "SHOW MANAGED ACCOUNTS",
		"SHOW MASKING POLICIES", "SHOW MATERIALIZED VIEWS",
		"SHOW NETWORK POLICIES", "SHOW OBJECTS",
		"SHOW ORGANIZATION ACCOUNTS", "SHOW PARAMETERS", "SHOW PIPES",
		"SHOW PRIMARY KEYS", "SHOW PROCEDURES", "SHOW REGIONS",
		"SHOW REPLICATION ACCOUNTS", "SHOW REPLICATION DATABASES",
		"SHOW REPLICATION GROUPS", "SHOW RESOURCE MONITORS", "SHOW ROLES",
		"SHOW ROW ACCESS POLICIES", "SHOW SCHEMAS", "SHOW SEQUENCES",
		"SHOW SESSION POLICIES", "SHOW SHARES",
		"SHOW SHARES IN FAILOVER GROUP", "SHOW SHARES IN REPLICATION GROUP",
		"SHOW STAGES", "SHOW STREAMS", "SHOW TABLES", "SHOW TAGS",
		"SHOW TASKS", "SHOW TRANSACTIONS", "SHOW USER FUNCTIONS",
		"SHOW USERS", "SHOW VARIABLES", "SHOW VIEWS", "SHOW WAREHOUSES",
		"TRUNCATE MATERIALIZED VIEW", "UNDROP DATABASE", "UNDROP SCHEMA",
		"UNDROP TABLE", "UNDROP TAG", "UNSET", "USE DATABASE", "USE ROLE",
		"USE SCHEMA", "USE SECONDARY ROLES", "USE WAREHOUSE"
	]),
	lO = v(["UNION [ALL]", "MINUS", "EXCEPT", "INTERSECT"]),
	_O = v(["[INNER] JOIN", "[NATURAL] {LEFT | RIGHT | FULL} [OUTER] JOIN",
		"{CROSS | NATURAL} JOIN"
	]),
	LO = v(["{ROWS | RANGE} BETWEEN",
		"ON {UPDATE | DELETE} [SET NULL | SET DEFAULT]"
	]),
	CO = {
		name: "snowflake",
		tokenizerOptions: {
			reservedSelect: IO,
			reservedClauses: [...NO, ...ur, ...nT],
			reservedSetOperations: lO,
			reservedJoins: _O,
			reservedPhrases: LO,
			reservedKeywords: iO,
			reservedDataTypes: aO,
			reservedFunctionNames: OO,
			stringTypes: ["$$", "''-qq-bs"],
			identTypes: ['""-qq'],
			variableTypes: [{
				regex: "[$][1-9]\\\\d*"
			}, {
				regex: "[$][_a-zA-Z][_a-zA-Z0-9$]*"
			}],
			extraParens: ["[]"],
			identChars: {
				rest: "$"
			},
			lineCommentTypes: ["--", "//"],
			operators: ["%", "::", "||", "=>"],
			propertyAccessOperators: [":"]
		},
		formatOptions: {
			alwaysDenseOperators: ["::"],
			onelineClauses: [...ur, ...nT],
			tabularOnelineClauses: nT
		}
	},
	ot = E => E[E.length - 1],
	$R = E => E.sort((e, T) => T.length - e.length || e.localeCompare(T)),
	Dt = E => E.replace(/\\s+/gu, " "),
	AT = E => /\\n/.test(E),
	CE = E => E.replace(/[.*+?^${}()|[\\]\\\\]/gu, "\\\\$&"),
	cr = /\\s+/uy,
	wE = E => new RegExp(`(?:${E})`, "uy"),
	uO = E => E.split("")
	.map(e => / /gu.test(e) ? "\\\\s+" :
		`[${e.toUpperCase()}${e.toLowerCase()}]`)
	.join(""),
	cO = E => E + "(?:-" + E + ")*",
	fO = ({
		prefixes: E,
		requirePrefix: e
	}) => `(?:${E.map(uO).join("|")}${e?"":"|"})`,
	PO = E => new RegExp(`(?:${E.map(CE).join("|")}).*?(?=\\r
|\\r|
|$)`, "uy"),
	fr = (E, e = []) => {
		const T = E === "open" ? 0 : 1,
			t = ["()", ...e].map(r => r[T]);
		return wE(t.map(CE)
			.join("|"))
	},
	Pr = E => wE(`${$R(E).map(CE).join("|")}`),
	DO = ({
		rest: E,
		dashes: e
	}) => E || e ? `(?![${E||""}${e?"-":""}])` : "",
	hE = (E, e = {}) => {
		if (E.length === 0) return /^\\b$/u;
		const T = DO(e),
			t = $R(E)
			.map(CE)
			.join("|")
			.replace(/ /gu, "\\\\s+");
		return new RegExp(`(?:${t})${T}\\\\b`, "iuy")
	},
	sT = (E, e) => {
		if (!E.length) return;
		const T = E.map(CE)
			.join("|");
		return wE(`(?:${T})(?:${e})`)
	},
	dO = () => {
		const E = {
				"<": ">",
				"[": "]",
				"(": ")",
				"{": "}"
			},
			e = "{left}(?:(?!{right}').)*?{right}",
			T = Object.entries(E)
			.map(([n, s]) => e.replace(/{left}/g, CE(n))
				.replace(/{right}/g, CE(s))),
			t = CE(Object.keys(E)
				.join(""));
		return `[Qq]'(?:${String.raw`(?<tag>[^\\s${t}])(?:(?!\\k<tag>').)*?\\k<tag>`}|${T.join("|")})'`
	},
	Dr = {
		"``": "(?:`[^`]*`)+",
		"[]": String.raw `(?:\\[[^\\]]*\\])(?:\\][^\\]]*\\])*`,
		'""-qq': String.raw `(?:"[^"]*")+`,
		'""-bs': String.raw `(?:"[^"\\\\]*(?:\\\\.[^"\\\\]*)*")`,
		'""-qq-bs': String.raw `(?:"[^"\\\\]*(?:\\\\.[^"\\\\]*)*")+`,
		'""-raw': String.raw `(?:"[^"]*")`,
		"''-qq": String.raw `(?:'[^']*')+`,
		"''-bs": String.raw `(?:'[^'\\\\]*(?:\\\\.[^'\\\\]*)*')`,
		"''-qq-bs": String.raw `(?:'[^'\\\\]*(?:\\\\.[^'\\\\]*)*')+`,
		"''-raw": String.raw `(?:'[^']*')`,
		$$: String.raw `(?<tag>\\$\\w*\\$)[\\s\\S]*?\\k<tag>`,
		"\'\'\'..\'\'\'": String.raw `\'\'\'[^\\\\]*?(?:\\\\.[^\\\\]*?)*?\'\'\'`,
		'""".."""': String.raw `"""[^\\\\]*?(?:\\\\.[^\\\\]*?)*?"""`,
		"{}": String.raw `(?:\\{[^\\}]*\\})`,
		"q''": dO()
	},
	xR = E => typeof E == "string" ? Dr[E] : "regex" in E ? E.regex : fO(E) +
	Dr[E.quote],
	pO = E => wE(E.map(e => "regex" in e ? e.regex : xR(e))
		.join("|")),
	XR = E => E.map(xR)
	.join("|"),
	dr = E => wE(XR(E)),
	MO = (E = {}) => wE(kR(E)),
	kR = ({
		first: E,
		rest: e,
		dashes: T,
		allowFirstCharNumber: t
	} = {}) => {
		const r = "\\\\p{Alphabetic}\\\\p{Mark}_",
			R = "\\\\p{Decimal_Number}",
			n = CE(E ? ? ""),
			s = CE(e ? ? ""),
			S = t ? `[${r}${R}${n}][${r}${R}${s}]*` :
			`[${r}${n}][${r}${R}${s}]*`;
		return T ? cO(S) : S
	};

function KR(E, e) {
	const T = E.slice(0, e)
		.split(/\\n/);
	return {
		line: T.length,
		col: T[T.length - 1].length + 1
	}
}
var UO = class {
		constructor(E, e) {
			this.rules = E, this.dialectName = e, this.input = "", this.index =
				0
		}
		tokenize(E) {
			this.input = E, this.index = 0;
			const e = [];
			let T;
			for (; this.index < this.input.length;) {
				const t = this.getWhitespace();
				if (this.index < this.input.length) {
					if (T = this.getNextToken(), !T) throw this.createParseError();
					e.push(AE(EE({}, T), {
						precedingWhitespace: t
					}))
				}
			}
			return e
		}
		createParseError() {
			const E = this.input.slice(this.index, this.index + 10),
				{
					line: e,
					col: T
				} = KR(this.input, this.index);
			return new Error(
				`Parse error: Unexpected "${E}" at line ${e} column ${T}.
${this.dialectInfo()}`
			)
		}
		dialectInfo() {
			return this.dialectName === "sql" ?
				`This likely happens because you're using the default "sql" dialect.
If possible, please select a more specific dialect (like sqlite, postgresql, etc).` :
				`SQL dialect used: "${this.dialectName}".`
		}
		getWhitespace() {
			cr.lastIndex = this.index;
			const E = cr.exec(this.input);
			if (E) return this.index += E[0].length, E[0]
		}
		getNextToken() {
			for (const E of this.rules) {
				const e = this.match(E);
				if (e) return e
			}
		}
		match(E) {
			E.regex.lastIndex = this.index;
			const e = E.regex.exec(this.input);
			if (e) {
				const T = e[0],
					t = {
						type: E.type,
						raw: T,
						text: E.text ? E.text(T) : T,
						start: this.index
					};
				return E.key && (t.key = E.key(T)), this.index += T.length,
					t
			}
		}
	},
	pr = /\\/\\ * /uy,mO=/([ ^
			/*]|\\*[^/]|\\/[^*])+/uy,hO=/\\*\\//uy,GO=class{constructor(){this.lastIndex=0}exec(E){let e="",T,t=0;if(T=this.matchSection(pr,E))e+=T,t++;else return null;for(;t>0;)if(T=this.matchSection(pr,E))e+=T,t++;else if(T=this.matchSection(hO,E))e+=T,t--;else if(T=this.matchSection(mO,E))e+=T;else return null;return[e]}matchSection(E,e){E.lastIndex=this.lastIndex;const T=E.exec(e);return T&&(this.lastIndex+=T[0].length),T?T[0]:null}},gO=class{constructor(E,e){this.cfg=E,this.dialectName=e,this.rulesBeforeParams=this.buildRulesBeforeParams(E),this.rulesAfterParams=this.buildRulesAfterParams(E)}tokenize(E,e){const T=[...this.rulesBeforeParams,...this.buildParamRules(this.cfg,e),...this.rulesAfterParams],t=new UO(T,this.dialectName).tokenize(E);return this.cfg.postProcess?this.cfg.postProcess(t):t}buildRulesBeforeParams(E){var e,T;return this.validRules([{type:"BLOCK_COMMENT",regex:/(\\/\\* *sql-formatter-disable *\\*\\/[\\s\\S]*?(?:\\/\\* *sql-formatter-enable *\\*\\/|$))/uy},{type:"BLOCK_COMMENT",regex:E.nestedBlockComments?new GO:/(\\/\\*[^]*?\\*\\/)/uy},{type:"LINE_COMMENT",regex:PO((e=E.lineCommentTypes)!=null?e:["--"])},{type:"QUOTED_IDENTIFIER",regex:dr(E.identTypes)},{type:"NUMBER",regex:/(?:0x[0-9a-fA-F]+|0b[01]+|(?:-\\s*)?[0-9]+(?:\\.[0-9]*)?(?:[eE][-+]?[0-9]+(?:\\.[0-9]+)?)?)(?![\\w\\p{Alphabetic}])/uy},{type:"RESERVED_PHRASE",regex:hE((T=E.reservedPhrases)!=null?T:[],E.identChars),text:Je},{type:"CASE",regex:/CASE\\b/iuy,text:Je},{type:"END",regex:/END\\b/iuy,text:Je},{type:"BETWEEN",regex:/BETWEEN\\b/iuy,text:Je},{type:"LIMIT",regex:E.reservedClauses.includes("LIMIT")?/LIMIT\\b/iuy:void 0,text:Je},{type:"RESERVED_CLAUSE",regex:hE(E.reservedClauses,E.identChars),text:Je},{type:"RESERVED_SELECT",regex:hE(E.reservedSelect,E.identChars),text:Je},{type:"RESERVED_SET_OPERATION",regex:hE(E.reservedSetOperations,E.identChars),text:Je},{type:"WHEN",regex:/WHEN\\b/iuy,text:Je},{type:"ELSE",regex:/ELSE\\b/iuy,text:Je},{type:"THEN",regex:/THEN\\b/iuy,text:Je},{type:"RESERVED_JOIN",regex:hE(E.reservedJoins,E.identChars),text:Je},{type:"AND",regex:/AND\\b/iuy,text:Je},{type:"OR",regex:/OR\\b/iuy,text:Je},{type:"XOR",regex:E.supportsXor?/XOR\\b/iuy:void 0,text:Je},{type:"RESERVED_FUNCTION_NAME",regex:hE(E.reservedFunctionNames,E.identChars),text:Je},{type:"RESERVED_DATA_TYPE",regex:hE(E.reservedDataTypes,E.identChars),text:Je},{type:"RESERVED_KEYWORD",regex:hE(E.reservedKeywords,E.identChars),text:Je}])}buildRulesAfterParams(E){var e,T;return this.validRules([{type:"VARIABLE",regex:E.variableTypes?pO(E.variableTypes):void 0},{type:"STRING",regex:dr(E.stringTypes)},{type:"IDENTIFIER",regex:MO(E.identChars)},{type:"DELIMITER",regex:/[;]/uy},{type:"COMMA",regex:/[,]/y},{type:"OPEN_PAREN",regex:fr("open",E.extraParens)},{type:"CLOSE_PAREN",regex:fr("close",E.extraParens)},{type:"OPERATOR",regex:Pr(["+","-","/",">","<","=","<>","<=",">=","!=",...(e=E.operators)!=null?e:[]])},{type:"ASTERISK",regex:/[*]/uy},{type:"PROPERTY_ACCESS_OPERATOR",regex:Pr([".",...(T=E.propertyAccessOperators)!=null?T:[]])}])}buildParamRules(E,e){var T,t,r,R,n;const s={named:(e==null?void 0:e.named)||((T=E.paramTypes)==null?void 0:T.named)||[],quoted:(e==null?void 0:e.quoted)||((t=E.paramTypes)==null?void 0:t.quoted)||[],numbered:(e==null?void 0:e.numbered)||((r=E.paramTypes)==null?void 0:r.numbered)||[],positional:typeof(e==null?void 0:e.positional)=="boolean"?e.positional:(R=E.paramTypes)==null?void 0:R.positional,custom:(e==null?void 0:e.custom)||((n=E.paramTypes)==null?void 0:n.custom)||[]};return this.validRules([{type:"NAMED_PARAMETER",regex:sT(s.named,kR(E.paramChars||E.identChars)),key:S=>S.slice(1)},{type:"QUOTED_PARAMETER",regex:sT(s.quoted,XR(E.identTypes)),key:S=>(({tokenKey:A,quoteChar:o})=>A.replace(new RegExp(CE("\\\\"+o),"gu"),o))({tokenKey:S.slice(2,-1),quoteChar:S.slice(-1)})},{type:"NUMBERED_PARAMETER",regex:sT(s.numbered,"[0-9]+"),key:S=>S.slice(1)},{type:"POSITIONAL_PARAMETER",regex:s.positional?/[?]/y:void 0},...s.custom.map(S=>{var A;return{type:"CUSTOM_PARAMETER",regex:wE(S.regex),key:(A=S.key)!=null?A:o=>o}})])}validRules(E){return E.filter(e=>!!e.regex)}},Je=E=>Dt(E.toUpperCase()),Mr=new Map,HO=E=>{let e=Mr.get(E);return e||(e=bO(E),Mr.set(E,e)),e},bO=E=>({tokenizer:new gO(E.tokenizerOptions,E.name),formatOptions:yO(E.formatOptions)}),yO=E=>{var e;return{alwaysDenseOperators:E.alwaysDenseOperators||[],onelineClauses:Object.fromEntries(E.onelineClauses.map(T=>[T,!0])),tabularOnelineClauses:Object.fromEntries(((e=E.tabularOnelineClauses)!=null?e:E.onelineClauses).map(T=>[T,!0]))}};function BO(E){return E.indentStyle==="tabularLeft"||E.indentStyle==="tabularRight"?" ".repeat(10):E.useTabs?"	":" ".repeat(E.tabWidth)}function ZE(E){return E.indentStyle==="tabularLeft"||E.indentStyle==="tabularRight"}var vO=class{constructor(E){this.params=E,this.index=0}get({key:E,text:e}){return this.params?E?this.params[E]:this.params[this.index++]:e}getPositionalParameterIndex(){return this.index}setPositionalParameterIndex(E){this.index=E}};function FO(E){return E.map(YO).map(VO).map(WO).map(wO).map($O)}var YO=(E,e,T)=>{if(wR(E.type)){const t=xO(T,e);if(t&&t.type==="PROPERTY_ACCESS_OPERATOR")return AE(EE({},E),{type:"IDENTIFIER",text:E.raw})}return E},VO=(E,e,T)=>{if(E.type==="RESERVED_FUNCTION_NAME"){const t=It(T,e);if(!t||!JR(t))return AE(EE({},E),{type:"RESERVED_KEYWORD"})}return E},WO=(E,e,T)=>{if(E.type==="RESERVED_DATA_TYPE"){const t=It(T,e);if(t&&JR(t))return AE(EE({},E),{type:"RESERVED_PARAMETERIZED_DATA_TYPE"})}return E},wO=(E,e,T)=>{if(E.type==="IDENTIFIER"){const t=It(T,e);if(t&&qR(t))return AE(EE({},E),{type:"ARRAY_IDENTIFIER"})}return E},$O=(E,e,T)=>{if(E.type==="RESERVED_DATA_TYPE"){const t=It(T,e);if(t&&qR(t))return AE(EE({},E),{type:"ARRAY_KEYWORD"})}return E},xO=(E,e)=>It(E,e,-1),It=(E,e,T=1)=>{let t=1;for(;E[e+t*T]&&XO(E[e+t*T]);)t++;return E[e+t*T]},JR=E=>E.type==="OPEN_PAREN"&&E.text==="(",qR=E=>E.type==="OPEN_PAREN"&&E.text==="[",XO=E=>E.type==="BLOCK_COMMENT"||E.type==="LINE_COMMENT",QR=class{constructor(E){this.tokenize=E,this.index=0,this.tokens=[],this.input=""}reset(E,e){this.input=E,this.index=0,this.tokens=this.tokenize(E)}next(){return this.tokens[this.index++]}save(){}formatError(E){const{line:e,col:T}=KR(this.input,E.start);return`Parse error at token: ${E.text} at line ${e} column ${T}`}has(E){return E in VR}};function ST(E){return E[0]}var Re=new QR(E=>[]),yE=([[E]])=>E,qe=E=>({type:"keyword",tokenType:E.type,text:E.text,raw:E.raw}),Ur=E=>({type:"data_type",text:E.text,raw:E.raw}),Qe=(E,{leading:e,trailing:T})=>(e!=null&&e.length&&(E=AE(EE({},E),{leadingComments:e})),T!=null&&T.length&&(E=AE(EE({},E),{trailingComments:T})),E),kO=(E,{leading:e,trailing:T})=>{if(e!=null&&e.length){const[t,...r]=E;E=[Qe(t,{leading:e}),...r]}if(T!=null&&T.length){const t=E.slice(0,-1),r=E[E.length-1];E=[...t,Qe(r,{trailing:T})]}return E},KO={Lexer:Re,ParserRules:[{name:"main$ebnf$1",symbols:[]},{name:"main$ebnf$1",symbols:["main$ebnf$1","statement"],postprocess:E=>E[0].concat([E[1]])},{name:"main",symbols:["main$ebnf$1"],postprocess:([E])=>{const e=E[E.length-1];return e&&!e.hasSemicolon?e.children.length>0?E:E.slice(0,-1):E}},{name:"statement$subexpression$1",symbols:[Re.has("DELIMITER")?{type:"DELIMITER"}:DELIMITER]},{name:"statement$subexpression$1",symbols:[Re.has("EOF")?{type:"EOF"}:EOF]},{name:"statement",symbols:["expressions_or_clauses","statement$subexpression$1"],postprocess:([E,[e]])=>({type:"statement",children:E,hasSemicolon:e.type==="DELIMITER"})},{name:"expressions_or_clauses$ebnf$1",symbols:[]},{name:"expressions_or_clauses$ebnf$1",symbols:["expressions_or_clauses$ebnf$1","free_form_sql"],postprocess:E=>E[0].concat([E[1]])},{name:"expressions_or_clauses$ebnf$2",symbols:[]},{name:"expressions_or_clauses$ebnf$2",symbols:["expressions_or_clauses$ebnf$2","clause"],postprocess:E=>E[0].concat([E[1]])},{name:"expressions_or_clauses",symbols:["expressions_or_clauses$ebnf$1","expressions_or_clauses$ebnf$2"],postprocess:([E,e])=>[...E,...e]},{name:"clause$subexpression$1",symbols:["limit_clause"]},{name:"clause$subexpression$1",symbols:["select_clause"]},{name:"clause$subexpression$1",symbols:["other_clause"]},{name:"clause$subexpression$1",symbols:["set_operation"]},{name:"clause",symbols:["clause$subexpression$1"],postprocess:yE},{name:"limit_clause$ebnf$1$subexpression$1$ebnf$1",symbols:["free_form_sql"]},{name:"limit_clause$ebnf$1$subexpression$1$ebnf$1",symbols:["limit_clause$ebnf$1$subexpression$1$ebnf$1","free_form_sql"],postprocess:E=>E[0].concat([E[1]])},{name:"limit_clause$ebnf$1$subexpression$1",symbols:[Re.has("COMMA")?{type:"COMMA"}:COMMA,"limit_clause$ebnf$1$subexpression$1$ebnf$1"]},{name:"limit_clause$ebnf$1",symbols:["limit_clause$ebnf$1$subexpression$1"],postprocess:ST},{name:"limit_clause$ebnf$1",symbols:[],postprocess:()=>null},{name:"limit_clause",symbols:[Re.has("LIMIT")?{type:"LIMIT"}:LIMIT,"_","expression_chain_","limit_clause$ebnf$1"],postprocess:([E,e,T,t])=>{if(t){const[r,R]=t;return{type:"limit_clause",limitKw:Qe(qe(E),{trailing:e}),offset:T,count:R}}else return{type:"limit_clause",limitKw:Qe(qe(E),{trailing:e}),count:T}}},{name:"select_clause$subexpression$1$ebnf$1",symbols:[]},{name:"select_clause$subexpression$1$ebnf$1",symbols:["select_clause$subexpression$1$ebnf$1","free_form_sql"],postprocess:E=>E[0].concat([E[1]])},{name:"select_clause$subexpression$1",symbols:["all_columns_asterisk","select_clause$subexpression$1$ebnf$1"]},{name:"select_clause$subexpression$1$ebnf$2",symbols:[]},{name:"select_clause$subexpression$1$ebnf$2",symbols:["select_clause$subexpression$1$ebnf$2","free_form_sql"],postprocess:E=>E[0].concat([E[1]])},{name:"select_clause$subexpression$1",symbols:["asteriskless_free_form_sql","select_clause$subexpression$1$ebnf$2"]},{name:"select_clause",symbols:[Re.has("RESERVED_SELECT")?{type:"RESERVED_SELECT"}:RESERVED_SELECT,"select_clause$subexpression$1"],postprocess:([E,[e,T]])=>({type:"clause",nameKw:qe(E),children:[e,...T]})},{name:"select_clause",symbols:[Re.has("RESERVED_SELECT")?{type:"RESERVED_SELECT"}:RESERVED_SELECT],postprocess:([E])=>({type:"clause",nameKw:qe(E),children:[]})},{name:"all_columns_asterisk",symbols:[Re.has("ASTERISK")?{type:"ASTERISK"}:ASTERISK],postprocess:()=>({type:"all_columns_asterisk"})},{name:"other_clause$ebnf$1",symbols:[]},{name:"other_clause$ebnf$1",symbols:["other_clause$ebnf$1","free_form_sql"],postprocess:E=>E[0].concat([E[1]])},{name:"other_clause",symbols:[Re.has("RESERVED_CLAUSE")?{type:"RESERVED_CLAUSE"}:RESERVED_CLAUSE,"other_clause$ebnf$1"],postprocess:([E,e])=>({type:"clause",nameKw:qe(E),children:e})},{name:"set_operation$ebnf$1",symbols:[]},{name:"set_operation$ebnf$1",symbols:["set_operation$ebnf$1","free_form_sql"],postprocess:E=>E[0].concat([E[1]])},{name:"set_operation",symbols:[Re.has("RESERVED_SET_OPERATION")?{type:"RESERVED_SET_OPERATION"}:RESERVED_SET_OPERATION,"set_operation$ebnf$1"],postprocess:([E,e])=>({type:"set_operation",nameKw:qe(E),children:e})},{name:"expression_chain_$ebnf$1",symbols:["expression_with_comments_"]},{name:"expression_chain_$ebnf$1",symbols:["expression_chain_$ebnf$1","expression_with_comments_"],postprocess:E=>E[0].concat([E[1]])},{name:"expression_chain_",symbols:["expression_chain_$ebnf$1"],postprocess:ST},{name:"expression_chain$ebnf$1",symbols:[]},{name:"expression_chain$ebnf$1",symbols:["expression_chain$ebnf$1","_expression_with_comments"],postprocess:E=>E[0].concat([E[1]])},{name:"expression_chain",symbols:["expression","expression_chain$ebnf$1"],postprocess:([E,e])=>[E,...e]},{name:"andless_expression_chain$ebnf$1",symbols:[]},{name:"andless_expression_chain$ebnf$1",symbols:["andless_expression_chain$ebnf$1","_andless_expression_with_comments"],postprocess:E=>E[0].concat([E[1]])},{name:"andless_expression_chain",symbols:["andless_expression","andless_expression_chain$ebnf$1"],postprocess:([E,e])=>[E,...e]},{name:"expression_with_comments_",symbols:["expression","_"],postprocess:([E,e])=>Qe(E,{trailing:e})},{name:"_expression_with_comments",symbols:["_","expression"],postprocess:([E,e])=>Qe(e,{leading:E})},{name:"_andless_expression_with_comments",symbols:["_","andless_expression"],postprocess:([E,e])=>Qe(e,{leading:E})},{name:"free_form_sql$subexpression$1",symbols:["asteriskless_free_form_sql"]},{name:"free_form_sql$subexpression$1",symbols:["asterisk"]},{name:"free_form_sql",symbols:["free_form_sql$subexpression$1"],postprocess:yE},{name:"asteriskless_free_form_sql$subexpression$1",symbols:["asteriskless_andless_expression"]},{name:"asteriskless_free_form_sql$subexpression$1",symbols:["logic_operator"]},{name:"asteriskless_free_form_sql$subexpression$1",symbols:["comma"]},{name:"asteriskless_free_form_sql$subexpression$1",symbols:["comment"]},{name:"asteriskless_free_form_sql$subexpression$1",symbols:["other_keyword"]},{name:"asteriskless_free_form_sql",symbols:["asteriskless_free_form_sql$subexpression$1"],postprocess:yE},{name:"expression$subexpression$1",symbols:["andless_expression"]},{name:"expression$subexpression$1",symbols:["logic_operator"]},{name:"expression",symbols:["expression$subexpression$1"],postprocess:yE},{name:"andless_expression$subexpression$1",symbols:["asteriskless_andless_expression"]},{name:"andless_expression$subexpression$1",symbols:["asterisk"]},{name:"andless_expression",symbols:["andless_expression$subexpression$1"],postprocess:yE},{name:"asteriskless_andless_expression$subexpression$1",symbols:["atomic_expression"]},{name:"asteriskless_andless_expression$subexpression$1",symbols:["between_predicate"]},{name:"asteriskless_andless_expression$subexpression$1",symbols:["case_expression"]},{name:"asteriskless_andless_expression",symbols:["asteriskless_andless_expression$subexpression$1"],postprocess:yE},{name:"atomic_expression$subexpression$1",symbols:["array_subscript"]},{name:"atomic_expression$subexpression$1",symbols:["function_call"]},{name:"atomic_expression$subexpression$1",symbols:["property_access"]},{name:"atomic_expression$subexpression$1",symbols:["parenthesis"]},{name:"atomic_expression$subexpression$1",symbols:["curly_braces"]},{name:"atomic_expression$subexpression$1",symbols:["square_brackets"]},{name:"atomic_expression$subexpression$1",symbols:["operator"]},{name:"atomic_expression$subexpression$1",symbols:["identifier"]},{name:"atomic_expression$subexpression$1",symbols:["parameter"]},{name:"atomic_expression$subexpression$1",symbols:["literal"]},{name:"atomic_expression$subexpression$1",symbols:["data_type"]},{name:"atomic_expression$subexpression$1",symbols:["keyword"]},{name:"atomic_expression",symbols:["atomic_expression$subexpression$1"],postprocess:yE},{name:"array_subscript",symbols:[Re.has("ARRAY_IDENTIFIER")?{type:"ARRAY_IDENTIFIER"}:ARRAY_IDENTIFIER,"_","square_brackets"],postprocess:([E,e,T])=>({type:"array_subscript",array:Qe({type:"identifier",quoted:!1,text:E.text},{trailing:e}),parenthesis:T})},{name:"array_subscript",symbols:[Re.has("ARRAY_KEYWORD")?{type:"ARRAY_KEYWORD"}:ARRAY_KEYWORD,"_","square_brackets"],postprocess:([E,e,T])=>({type:"array_subscript",array:Qe(qe(E),{trailing:e}),parenthesis:T})},{name:"function_call",symbols:[Re.has("RESERVED_FUNCTION_NAME")?{type:"RESERVED_FUNCTION_NAME"}:RESERVED_FUNCTION_NAME,"_","parenthesis"],postprocess:([E,e,T])=>({type:"function_call",nameKw:Qe(qe(E),{trailing:e}),parenthesis:T})},{name:"parenthesis",symbols:[{literal:"("},"expressions_or_clauses",{literal:")"}],postprocess:([E,e,T])=>({type:"parenthesis",children:e,openParen:"(",closeParen:")"})},{name:"curly_braces$ebnf$1",symbols:[]},{name:"curly_braces$ebnf$1",symbols:["curly_braces$ebnf$1","free_form_sql"],postprocess:E=>E[0].concat([E[1]])},{name:"curly_braces",symbols:[{literal:"{"},"curly_braces$ebnf$1",{literal:"}"}],postprocess:([E,e,T])=>({type:"parenthesis",children:e,openParen:"{",closeParen:"}"})},{name:"square_brackets$ebnf$1",symbols:[]},{name:"square_brackets$ebnf$1",symbols:["square_brackets$ebnf$1","free_form_sql"],postprocess:E=>E[0].concat([E[1]])},{name:"square_brackets",symbols:[{literal:"["},"square_brackets$ebnf$1",{literal:"]"}],postprocess:([E,e,T])=>({type:"parenthesis",children:e,openParen:"[",closeParen:"]"})},{name:"property_access$subexpression$1",symbols:["identifier"]},{name:"property_access$subexpression$1",symbols:["array_subscript"]},{name:"property_access$subexpression$1",symbols:["all_columns_asterisk"]},{name:"property_access$subexpression$1",symbols:["parameter"]},{name:"property_access",symbols:["atomic_expression","_",Re.has("PROPERTY_ACCESS_OPERATOR")?{type:"PROPERTY_ACCESS_OPERATOR"}:PROPERTY_ACCESS_OPERATOR,"_","property_access$subexpression$1"],postprocess:([E,e,T,t,[r]])=>({type:"property_access",object:Qe(E,{trailing:e}),operator:T.text,property:Qe(r,{leading:t})})},{name:"between_predicate",symbols:[Re.has("BETWEEN")?{type:"BETWEEN"}:BETWEEN,"_","andless_expression_chain","_",Re.has("AND")?{type:"AND"}:AND,"_","andless_expression"],postprocess:([E,e,T,t,r,R,n])=>({type:"between_predicate",betweenKw:qe(E),expr1:kO(T,{leading:e,trailing:t}),andKw:qe(r),expr2:[Qe(n,{leading:R})]})},{name:"case_expression$ebnf$1",symbols:["expression_chain_"],postprocess:ST},{name:"case_expression$ebnf$1",symbols:[],postprocess:()=>null},{name:"case_expression$ebnf$2",symbols:[]},{name:"case_expression$ebnf$2",symbols:["case_expression$ebnf$2","case_clause"],postprocess:E=>E[0].concat([E[1]])},{name:"case_expression",symbols:[Re.has("CASE")?{type:"CASE"}:CASE,"_","case_expression$ebnf$1","case_expression$ebnf$2",Re.has("END")?{type:"END"}:END],postprocess:([E,e,T,t,r])=>({type:"case_expression",caseKw:Qe(qe(E),{trailing:e}),endKw:qe(r),expr:T||[],clauses:t})},{name:"case_clause",symbols:[Re.has("WHEN")?{type:"WHEN"}:WHEN,"_","expression_chain_",Re.has("THEN")?{type:"THEN"}:THEN,"_","expression_chain_"],postprocess:([E,e,T,t,r,R])=>({type:"case_when",whenKw:Qe(qe(E),{trailing:e}),thenKw:Qe(qe(t),{trailing:r}),condition:T,result:R})},{name:"case_clause",symbols:[Re.has("ELSE")?{type:"ELSE"}:ELSE,"_","expression_chain_"],postprocess:([E,e,T])=>({type:"case_else",elseKw:Qe(qe(E),{trailing:e}),result:T})},{name:"comma$subexpression$1",symbols:[Re.has("COMMA")?{type:"COMMA"}:COMMA]},{name:"comma",symbols:["comma$subexpression$1"],postprocess:([[E]])=>({type:"comma"})},{name:"asterisk$subexpression$1",symbols:[Re.has("ASTERISK")?{type:"ASTERISK"}:ASTERISK]},{name:"asterisk",symbols:["asterisk$subexpression$1"],postprocess:([[E]])=>({type:"operator",text:E.text})},{name:"operator$subexpression$1",symbols:[Re.has("OPERATOR")?{type:"OPERATOR"}:OPERATOR]},{name:"operator",symbols:["operator$subexpression$1"],postprocess:([[E]])=>({type:"operator",text:E.text})},{name:"identifier$subexpression$1",symbols:[Re.has("IDENTIFIER")?{type:"IDENTIFIER"}:IDENTIFIER]},{name:"identifier$subexpression$1",symbols:[Re.has("QUOTED_IDENTIFIER")?{type:"QUOTED_IDENTIFIER"}:QUOTED_IDENTIFIER]},{name:"identifier$subexpression$1",symbols:[Re.has("VARIABLE")?{type:"VARIABLE"}:VARIABLE]},{name:"identifier",symbols:["identifier$subexpression$1"],postprocess:([[E]])=>({type:"identifier",quoted:E.type!=="IDENTIFIER",text:E.text})},{name:"parameter$subexpression$1",symbols:[Re.has("NAMED_PARAMETER")?{type:"NAMED_PARAMETER"}:NAMED_PARAMETER]},{name:"parameter$subexpression$1",symbols:[Re.has("QUOTED_PARAMETER")?{type:"QUOTED_PARAMETER"}:QUOTED_PARAMETER]},{name:"parameter$subexpression$1",symbols:[Re.has("NUMBERED_PARAMETER")?{type:"NUMBERED_PARAMETER"}:NUMBERED_PARAMETER]},{name:"parameter$subexpression$1",symbols:[Re.has("POSITIONAL_PARAMETER")?{type:"POSITIONAL_PARAMETER"}:POSITIONAL_PARAMETER]},{name:"parameter$subexpression$1",symbols:[Re.has("CUSTOM_PARAMETER")?{type:"CUSTOM_PARAMETER"}:CUSTOM_PARAMETER]},{name:"parameter",symbols:["parameter$subexpression$1"],postprocess:([[E]])=>({type:"parameter",key:E.key,text:E.text})},{name:"literal$subexpression$1",symbols:[Re.has("NUMBER")?{type:"NUMBER"}:NUMBER]},{name:"literal$subexpression$1",symbols:[Re.has("STRING")?{type:"STRING"}:STRING]},{name:"literal",symbols:["literal$subexpression$1"],postprocess:([[E]])=>({type:"literal",text:E.text})},{name:"keyword$subexpression$1",symbols:[Re.has("RESERVED_KEYWORD")?{type:"RESERVED_KEYWORD"}:RESERVED_KEYWORD]},{name:"keyword$subexpression$1",symbols:[Re.has("RESERVED_PHRASE")?{type:"RESERVED_PHRASE"}:RESERVED_PHRASE]},{name:"keyword$subexpression$1",symbols:[Re.has("RESERVED_JOIN")?{type:"RESERVED_JOIN"}:RESERVED_JOIN]},{name:"keyword",symbols:["keyword$subexpression$1"],postprocess:([[E]])=>qe(E)},{name:"data_type$subexpression$1",symbols:[Re.has("RESERVED_DATA_TYPE")?{type:"RESERVED_DATA_TYPE"}:RESERVED_DATA_TYPE]},{name:"data_type",symbols:["data_type$subexpression$1"],postprocess:([[E]])=>Ur(E)},{name:"data_type",symbols:[Re.has("RESERVED_PARAMETERIZED_DATA_TYPE")?{type:"RESERVED_PARAMETERIZED_DATA_TYPE"}:RESERVED_PARAMETERIZED_DATA_TYPE,"_","parenthesis"],postprocess:([E,e,T])=>({type:"parameterized_data_type",dataType:Qe(Ur(E),{trailing:e}),parenthesis:T})},{name:"logic_operator$subexpression$1",symbols:[Re.has("AND")?{type:"AND"}:AND]},{name:"logic_operator$subexpression$1",symbols:[Re.has("OR")?{type:"OR"}:OR]},{name:"logic_operator$subexpression$1",symbols:[Re.has("XOR")?{type:"XOR"}:XOR]},{name:"logic_operator",symbols:["logic_operator$subexpression$1"],postprocess:([[E]])=>qe(E)},{name:"other_keyword$subexpression$1",symbols:[Re.has("WHEN")?{type:"WHEN"}:WHEN]},{name:"other_keyword$subexpression$1",symbols:[Re.has("THEN")?{type:"THEN"}:THEN]},{name:"other_keyword$subexpression$1",symbols:[Re.has("ELSE")?{type:"ELSE"}:ELSE]},{name:"other_keyword$subexpression$1",symbols:[Re.has("END")?{type:"END"}:END]},{name:"other_keyword",symbols:["other_keyword$subexpression$1"],postprocess:([[E]])=>qe(E)},{name:"_$ebnf$1",symbols:[]},{name:"_$ebnf$1",symbols:["_$ebnf$1","comment"],postprocess:E=>E[0].concat([E[1]])},{name:"_",symbols:["_$ebnf$1"],postprocess:([E])=>E},{name:"comment",symbols:[Re.has("LINE_COMMENT")?{type:"LINE_COMMENT"}:LINE_COMMENT],postprocess:([E])=>({type:"line_comment",text:E.text,precedingWhitespace:E.precedingWhitespace})},{name:"comment",symbols:[Re.has("BLOCK_COMMENT")?{type:"BLOCK_COMMENT"}:BLOCK_COMMENT],postprocess:([E])=>({type:"block_comment",text:E.text,precedingWhitespace:E.precedingWhitespace})},{name:"comment",symbols:[Re.has("DISABLE_COMMENT")?{type:"DISABLE_COMMENT"}:DISABLE_COMMENT],postprocess:([E])=>({type:"disable_comment",text:E.text,precedingWhitespace:E.precedingWhitespace})}],ParserStart:"main"},JO=KO,{Parser:qO,Grammar:QO}=zA;function ZO(E){let e={};const T=new QR(r=>[...FO(E.tokenize(r,e)),WR(r.length)]),t=new qO(QO.fromCompiled(JO),{lexer:T});return{parse:(r,R)=>{e=R;const{results:n}=t.feed(r);if(n.length===1)return n[0];throw n.length===0?new Error("Parse error: Invalid SQL"):new Error(`Parse error: Ambiguous grammar
			${JSON.stringify(n,void 0,2)}`)}}}var ZR=class{constructor(E){this.indentation=E,this.items=[]}add(...E){for(const e of E)switch(e){case 0:this.items.push(0);break;case 1:this.trimHorizontalWhitespace();break;case 2:this.trimWhitespace();break;case 3:this.trimHorizontalWhitespace(),this.addNewline(3);break;case 4:this.trimHorizontalWhitespace(),this.addNewline(4);break;case 5:this.addIndentation();break;case 6:this.items.push(6);break;default:this.items.push(e)}}trimHorizontalWhitespace(){for(;jO(ot(this.items));)this.items.pop()}trimWhitespace(){for(;zO(ot(this.items));)this.items.pop()}addNewline(E){if(this.items.length>0)switch(ot(this.items)){case 3:this.items.pop(),this.items.push(E);break;case 4:break;default:this.items.push(E);break}}addIndentation(){for(let E=0;E<this.indentation.getLevel();E++)this.items.push(6)}toString(){return this.items.map(E=>this.itemToString(E)).join("")}getLayoutItems(){return this.items}itemToString(E){switch(E){case 0:return" ";case 3:case 4:return`
			`;case 6:return this.indentation.getSingleIndent();default:return E}}},jO=E=>E===0||E===6,zO=E=>E===0||E===6||E===3;function mr(E,e){if(e==="standard")return E;let T=[];return E.length>=10&&E.includes(" ")&&([E,...T]=E.split(" ")),e==="tabularLeft"?E=E.padEnd(9," "):E=E.padStart(9," "),E+["",...T].join(" ")}function hr(E){return is(E)||E==="RESERVED_CLAUSE"||E==="RESERVED_SELECT"||E==="RESERVED_SET_OPERATION"||E==="RESERVED_JOIN"||E==="LIMIT"}var oT="top-level",ei="block-level",jR=class{constructor(E){this.indent=E,this.indentTypes=[]}getSingleIndent(){return this.indent}getLevel(){return this.indentTypes.length}increaseTopLevel(){this.indentTypes.push(oT)}increaseBlockLevel(){this.indentTypes.push(ei)}decreaseTopLevel(){this.indentTypes.length>0&&ot(this.indentTypes)===oT&&this.indentTypes.pop()}decreaseBlockLevel(){for(;this.indentTypes.length>0&&this.indentTypes.pop()===oT;);}},Ei=class extends ZR{constructor(E){super(new jR("")),this.expressionWidth=E,this.length=0,this.trailingSpace=!1}add(...E){if(E.forEach(e=>this.addToLength(e)),this.length>this.expressionWidth)throw new NT;super.add(...E)}addToLength(E){if(typeof E=="string")this.length+=E.length,this.trailingSpace=!1;else{if(E===4||E===3)throw new NT;E===5||E===6||E===0?this.trailingSpace||(this.length++,this.trailingSpace=!0):(E===2||E===1)&&this.trailingSpace&&(this.trailingSpace=!1,this.length--)}}},NT=class extends Error{},ti=class lT{constructor({cfg:e,dialectCfg:T,params:t,layout:r,inline:R=!1}){this.inline=!1,this.nodes=[],this.index=-1,this.cfg=e,this.dialectCfg=T,this.inline=R,this.params=t,this.layout=r}format(e){for(this.nodes=e,this.index=0;this.index<this.nodes.length;this.index++)this.formatNode(this.nodes[this.index]);return this.layout}formatNode(e){this.formatComments(e.leadingComments),this.formatNodeWithoutComments(e),this.formatComments(e.trailingComments)}formatNodeWithoutComments(e){switch(e.type){case"function_call":return this.formatFunctionCall(e);case"parameterized_data_type":return this.formatParameterizedDataType(e);case"array_subscript":return this.formatArraySubscript(e);case"property_access":return this.formatPropertyAccess(e);case"parenthesis":return this.formatParenthesis(e);case"between_predicate":return this.formatBetweenPredicate(e);case"case_expression":return this.formatCaseExpression(e);case"case_when":return this.formatCaseWhen(e);case"case_else":return this.formatCaseElse(e);case"clause":return this.formatClause(e);case"set_operation":return this.formatSetOperation(e);case"limit_clause":return this.formatLimitClause(e);case"all_columns_asterisk":return this.formatAllColumnsAsterisk(e);case"literal":return this.formatLiteral(e);case"identifier":return this.formatIdentifier(e);case"parameter":return this.formatParameter(e);case"operator":return this.formatOperator(e);case"comma":return this.formatComma(e);case"line_comment":return this.formatLineComment(e);case"block_comment":return this.formatBlockComment(e);case"disable_comment":return this.formatBlockComment(e);case"data_type":return this.formatDataType(e);case"keyword":return this.formatKeywordNode(e)}}formatFunctionCall(e){this.withComments(e.nameKw,()=>{this.layout.add(this.showFunctionKw(e.nameKw))}),this.formatNode(e.parenthesis)}formatParameterizedDataType(e){this.withComments(e.dataType,()=>{this.layout.add(this.showDataType(e.dataType))}),this.formatNode(e.parenthesis)}formatArraySubscript(e){let T;switch(e.array.type){case"data_type":T=this.showDataType(e.array);break;case"keyword":T=this.showKw(e.array);break;default:T=this.showIdentifier(e.array);break}this.withComments(e.array,()=>{this.layout.add(T)}),this.formatNode(e.parenthesis)}formatPropertyAccess(e){this.formatNode(e.object),this.layout.add(1,e.operator),this.formatNode(e.property)}formatParenthesis(e){const T=this.formatInlineExpression(e.children);T?(this.layout.add(e.openParen),this.layout.add(...T.getLayoutItems()),this.layout.add(1,e.closeParen,0)):(this.layout.add(e.openParen,3),ZE(this.cfg)?(this.layout.add(5),this.layout=this.formatSubExpression(e.children)):(this.layout.indentation.increaseBlockLevel(),this.layout.add(5),this.layout=this.formatSubExpression(e.children),this.layout.indentation.decreaseBlockLevel()),this.layout.add(3,5,e.closeParen,0))}formatBetweenPredicate(e){this.layout.add(this.showKw(e.betweenKw),0),this.layout=this.formatSubExpression(e.expr1),this.layout.add(1,0,this.showNonTabularKw(e.andKw),0),this.layout=this.formatSubExpression(e.expr2),this.layout.add(0)}formatCaseExpression(e){this.formatNode(e.caseKw),this.layout.indentation.increaseBlockLevel(),this.layout=this.formatSubExpression(e.expr),this.layout=this.formatSubExpression(e.clauses),this.layout.indentation.decreaseBlockLevel(),this.layout.add(3,5),this.formatNode(e.endKw)}formatCaseWhen(e){this.layout.add(3,5),this.formatNode(e.whenKw),this.layout=this.formatSubExpression(e.condition),this.formatNode(e.thenKw),this.layout=this.formatSubExpression(e.result)}formatCaseElse(e){this.layout.add(3,5),this.formatNode(e.elseKw),this.layout=this.formatSubExpression(e.result)}formatClause(e){this.isOnelineClause(e)?this.formatClauseInOnelineStyle(e):ZE(this.cfg)?this.formatClauseInTabularStyle(e):this.formatClauseInIndentedStyle(e)}isOnelineClause(e){return ZE(this.cfg)?this.dialectCfg.tabularOnelineClauses[e.nameKw.text]:this.dialectCfg.onelineClauses[e.nameKw.text]}formatClauseInIndentedStyle(e){this.layout.add(3,5,this.showKw(e.nameKw),3),this.layout.indentation.increaseTopLevel(),this.layout.add(5),this.layout=this.formatSubExpression(e.children),this.layout.indentation.decreaseTopLevel()}formatClauseInOnelineStyle(e){this.layout.add(3,5,this.showKw(e.nameKw),0),this.layout=this.formatSubExpression(e.children)}formatClauseInTabularStyle(e){this.layout.add(3,5,this.showKw(e.nameKw),0),this.layout.indentation.increaseTopLevel(),this.layout=this.formatSubExpression(e.children),this.layout.indentation.decreaseTopLevel()}formatSetOperation(e){this.layout.add(3,5,this.showKw(e.nameKw),3),this.layout.add(5),this.layout=this.formatSubExpression(e.children)}formatLimitClause(e){this.withComments(e.limitKw,()=>{this.layout.add(3,5,this.showKw(e.limitKw))}),this.layout.indentation.increaseTopLevel(),ZE(this.cfg)?this.layout.add(0):this.layout.add(3,5),e.offset?(this.layout=this.formatSubExpression(e.offset),this.layout.add(1,",",0),this.layout=this.formatSubExpression(e.count)):this.layout=this.formatSubExpression(e.count),this.layout.indentation.decreaseTopLevel()}formatAllColumnsAsterisk(e){this.layout.add("*",0)}formatLiteral(e){this.layout.add(e.text,0)}formatIdentifier(e){this.layout.add(this.showIdentifier(e),0)}formatParameter(e){this.layout.add(this.params.get(e),0)}formatOperator({text:e}){this.cfg.denseOperators||this.dialectCfg.alwaysDenseOperators.includes(e)?this.layout.add(1,e):e===":"?this.layout.add(1,e,0):this.layout.add(e,0)}formatComma(e){this.inline?this.layout.add(1,",",0):this.layout.add(1,",",3,5)}withComments(e,T){this.formatComments(e.leadingComments),T(),this.formatComments(e.trailingComments)}formatComments(e){e&&e.forEach(T=>{T.type==="line_comment"?this.formatLineComment(T):this.formatBlockComment(T)})}formatLineComment(e){AT(e.precedingWhitespace||"")?this.layout.add(3,5,e.text,4,5):this.layout.getLayoutItems().length>0?this.layout.add(2,0,e.text,4,5):this.layout.add(e.text,4,5)}formatBlockComment(e){e.type==="block_comment"&&this.isMultilineBlockComment(e)?(this.splitBlockComment(e.text).forEach(T=>{this.layout.add(3,5,T)}),this.layout.add(3,5)):this.layout.add(e.text,0)}isMultilineBlockComment(e){return AT(e.text)||AT(e.precedingWhitespace||"")}isDocComment(e){const T=e.split(/\\n/);return/^\\/\\*\\*?$/.test(T[0])&&T.slice(1,T.length-1).every(t=>/^\\s*\\*/
			.test(t)) && /^\\s*\\*\\/$ / .test(ot(T))
	}
splitBlockComment(e) {
	return this.isDocComment(e) ? e.split(/\\n/)
		.map(T => /^\\s*\\*/.test(T) ? " " + T.replace(/^\\s*/, "") : T) :
		e.split(/\\n/)
		.map(T => T.replace(/^\\s*/, ""))
}
formatSubExpression(e) {
	return new lT({
			cfg: this.cfg,
			dialectCfg: this.dialectCfg,
			params: this.params,
			layout: this.layout,
			inline: this.inline
		})
		.format(e)
}
formatInlineExpression(e) {
	const T = this.params.getPositionalParameterIndex();
	try {
		return new lT({
				cfg: this.cfg,
				dialectCfg: this.dialectCfg,
				params: this.params,
				layout: new Ei(this.cfg.expressionWidth),
				inline: !0
			})
			.format(e)
	} catch (t) {
		if (t instanceof NT) {
			this.params.setPositionalParameterIndex(T);
			return
		} else throw t
	}
}
formatKeywordNode(e) {
	switch (e.tokenType) {
		case "RESERVED_JOIN":
			return this.formatJoin(e);
		case "AND":
		case "OR":
		case "XOR":
			return this.formatLogicalOperator(e);
		default:
			return this.formatKeyword(e)
	}
}
formatJoin(e) {
	ZE(this.cfg) ? (this.layout.indentation.decreaseTopLevel(), this.layout
		.add(3, 5, this.showKw(e), 0), this.layout.indentation.increaseTopLevel()
	) : this.layout.add(3, 5, this.showKw(e), 0)
}
formatKeyword(e) {
	this.layout.add(this.showKw(e), 0)
}
formatLogicalOperator(e) {
	this.cfg.logicalOperatorNewline === "before" ? ZE(this.cfg) ? (this.layout
			.indentation.decreaseTopLevel(), this.layout.add(3, 5, this.showKw(
				e), 0), this.layout.indentation.increaseTopLevel()) : this.layout
		.add(3, 5, this.showKw(e), 0) : this.layout.add(this.showKw(e), 3,
			5)
}
formatDataType(e) {
	this.layout.add(this.showDataType(e), 0)
}
showKw(e) {
	return hr(e.tokenType) ? mr(this.showNonTabularKw(e), this.cfg.indentStyle) :
		this.showNonTabularKw(e)
}
showNonTabularKw(e) {
	switch (this.cfg.keywordCase) {
		case "preserve":
			return Dt(e.raw);
		case "upper":
			return e.text;
		case "lower":
			return e.text.toLowerCase()
	}
}
showFunctionKw(e) {
	return hr(e.tokenType) ? mr(this.showNonTabularFunctionKw(e), this.cfg.indentStyle) :
		this.showNonTabularFunctionKw(e)
}
showNonTabularFunctionKw(e) {
	switch (this.cfg.functionCase) {
		case "preserve":
			return Dt(e.raw);
		case "upper":
			return e.text;
		case "lower":
			return e.text.toLowerCase()
	}
}
showIdentifier(e) {
	if (e.quoted) return e.text;
	switch (this.cfg.identifierCase) {
		case "preserve":
			return e.text;
		case "upper":
			return e.text.toUpperCase();
		case "lower":
			return e.text.toLowerCase()
	}
}
showDataType(e) {
	switch (this.cfg.dataTypeCase) {
		case "preserve":
			return Dt(e.raw);
		case "upper":
			return e.text;
		case "lower":
			return e.text.toLowerCase()
	}
}
}, Ti = class {
	constructor(E, e) {
		this.dialect = E, this.cfg = e, this.params = new vO(this.cfg.params)
	}
	format(E) {
		const e = this.parse(E);
		return this.formatAst(e)
			.trimEnd()
	}
	parse(E) {
		return ZO(this.dialect.tokenizer)
			.parse(E, this.cfg.paramTypes || {})
	}
	formatAst(E) {
		return E.map(e => this.formatStatement(e))
			.join(`
`.repeat(this.cfg.linesBetweenQueries + 1))
	}
	formatStatement(E) {
		const e = new ti({
				cfg: this.cfg,
				dialectCfg: this.dialect.formatOptions,
				params: this.params,
				layout: new ZR(new jR(BO(this.cfg)))
			})
			.format(E.children);
		return E.hasSemicolon && (this.cfg.newlineBeforeSemicolon ? e.add(
			3, ";") : e.add(2, ";")), e.toString()
	}
}, _T = class extends Error {};

function ri(E) {
	const e = ["multilineLists", "newlineBeforeOpenParen",
		"newlineBeforeCloseParen", "aliasAs", "commaPosition",
		"tabulateAlias"
	];
	for (const T of e)
		if (T in E) throw new _T(`${T} config is no more supported.`);
	if (E.expressionWidth <= 0) throw new _T(
		`expressionWidth config must be positive number. Received ${E.expressionWidth} instead.`
	);
	return E.params && !Ri(E.params) && console.warn(
		'WARNING: All "params" option values should be strings.'), E
}

function Ri(E) {
	return (E instanceof Array ? E : Object.values(E))
		.every(T => typeof T == "string")
}
var zR = {
		bigquery: "bigquery",
		db2: "db2",
		db2i: "db2i",
		hive: "hive",
		mariadb: "mariadb",
		mysql: "mysql",
		n1ql: "n1ql",
		plsql: "plsql",
		postgresql: "postgresql",
		redshift: "redshift",
		spark: "spark",
		sqlite: "sqlite",
		sql: "sql",
		tidb: "tidb",
		trino: "trino",
		transactsql: "transactsql",
		tsql: "transactsql",
		singlestoredb: "singlestoredb",
		snowflake: "snowflake"
	},
	ni = Object.keys(zR),
	Ai = {
		tabWidth: 2,
		useTabs: !1,
		keywordCase: "preserve",
		identifierCase: "preserve",
		dataTypeCase: "preserve",
		functionCase: "preserve",
		indentStyle: "standard",
		logicalOperatorNewline: "before",
		expressionWidth: 50,
		linesBetweenQueries: 1,
		denseOperators: !1,
		newlineBeforeSemicolon: !1
	},
	Gr = (E, e = {}) => {
		if (typeof e.language == "string" && !ni.includes(e.language)) throw new _T(
			`Unsupported SQL dialect: ${e.language}`);
		const T = zR[e.language || "sql"];
		return si(E, AE(EE({}, e), {
			dialect: YR[T]
		}))
	},
	si = (E, e) => {
		var T = e,
			{
				dialect: t
			} = T,
			r = ts(T, ["dialect"]);
		if (typeof E != "string") throw new Error(
			"Invalid query argument. Expected string, instead got " +
			typeof E);
		const R = ri(EE(EE({}, Ai), r));
		return new Ti(HO(t), R)
			.format(E)
	};

function gr(E, e, T) {
	const t = E.slice();
	return t[1] = e[T], t
}

function Hr(E, e) {
	let T, t = e[1].name + "",
		r, R, n, s = e[1].instantiated_value + "",
		S, A;
	return {
		key: E,
		first: null,
		c() {
			T = f("b"), r = te(t), R = te(":"), n = $(), S = te(s), A = f("br"),
				this.first = T
		},
		m(o, i) {
			V(o, T, i), l(T, r), l(T, R), V(o, n, i), V(o, S, i), V(o, A, i)
		},
		p(o, i) {
			e = o, i & 1 && t !== (t = e[1].name + "") && Le(r, t), i & 1 && s !==
				(s = e[1].instantiated_value + "") && Le(S, s)
		},
		d(o) {
			o && (Y(T), Y(n), Y(S), Y(A))
		}
	}
}

function Si(E) {
	let e, T, t, r, R, n, s, S = E[0].function_name + "",
		A, o, i, _ = [],
		c = new Map,
		P, p, C, L, I, u, H, b = E[0].description + "",
		M, O, N, D, B = Gr(E[0].instantiated_sql) + "",
		h, G, F, W, x = E[0].sql_template + "",
		J, oe = De(E[0].arguments);
	const z = Oe => Oe[1].name;
	for (let Oe = 0; Oe < oe.length; Oe += 1) {
		let Ue = gr(E, oe, Oe),
			ye = z(Ue);
		c.set(ye, _[Oe] = Hr(ye, Ue))
	}
	return {
		c() {
			e = f("div"), T = f("div"), t = f("div"), t.innerHTML =
				'<span class="inline-flex justify-center items-center size-8 rounded-full border-4 border-teal-100 bg-teal-200 text-teal-800 dark:border-teal-900 dark:bg-teal-800 dark:text-teal-400"><svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"></path><path d="m9 12 2 2 4-4"></path></svg></span>',
				r = $(), R = f("div"), n = f("h3"), s = te("Function: "), A =
				te(S), o = $(), i = f("p");
			for (let Oe = 0; Oe < _.length; Oe += 1) _[Oe].c();
			P = $(), p = f("div"), C = f("div"), C.innerHTML =
				'<nav class="flex space-x-2" aria-label="Tabs"><button type="button" class="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500 active" id="basic-tabs-item-1" data-hs-tab="#basic-tabs-1" aria-controls="basic-tabs-1" role="tab">Description</button> <button type="button" class="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500" id="basic-tabs-item-2" data-hs-tab="#basic-tabs-2" aria-controls="basic-tabs-2" role="tab">SQL</button> <button type="button" class="hs-tab-active:font-semibold hs-tab-active:border-blue-600 hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap text-gray-500 hover:text-blue-600 disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400 dark:hover:text-blue-500" id="basic-tabs-item-3" data-hs-tab="#basic-tabs-3" aria-controls="basic-tabs-3" role="tab">Template</button></nav>',
				L = $(), I = f("div"), u = f("div"), H = f("p"), M = te(b), O =
				$(), N = f("div"), D = f("p"), h = te(B), G = $(), F = f("div"),
				W = f("p"), J = te(x), a(t, "class", "flex-shrink-0"), a(n,
					"class", "text-gray-800 font-semibold dark:text-white"), a(
					i, "class", "text-sm text-gray-700 dark:text-neutral-400"),
				a(R, "class", "ms-3"), a(T, "class", "flex"), a(C, "class",
					"border-b border-gray-200 px-4 dark:border-neutral-700"), a(
					H, "class", "text-gray-500 dark:text-neutral-400"), a(u,
					"id", "basic-tabs-1"), a(u, "role", "tabpanel"), a(u,
					"aria-labelledby", "basic-tabs-item-1"), a(D, "class",
					"text-gray-500 dark:text-neutral-400 font-mono text-teal-800"
				), a(N, "id", "basic-tabs-2"), a(N, "class", "hidden"), a(N,
					"role", "tabpanel"), a(N, "aria-labelledby",
					"basic-tabs-item-2"), a(W, "class",
					"text-gray-500 dark:text-neutral-400 font-mono"), a(F, "id",
					"basic-tabs-3"), a(F, "class", "hidden"), a(F, "role",
					"tabpanel"), a(F, "aria-labelledby", "basic-tabs-item-3"),
				a(I, "class", "px-4"), a(p, "class",
					"w-full bg-white rounded-lg shadow-md dark:bg-neutral-800"),
				a(e, "class",
					"bg-teal-50 border-t-2 border-teal-500 rounded-lg p-4 dark:bg-teal-800/30"
				), a(e, "role", "alert")
		},
		m(Oe, Ue) {
			V(Oe, e, Ue), l(e, T), l(T, t), l(T, r), l(T, R), l(R, n), l(n, s),
				l(n, A), l(R, o), l(R, i);
			for (let ye = 0; ye < _.length; ye += 1) _[ye] && _[ye].m(i, null);
			l(e, P), l(e, p), l(p, C), l(p, L), l(p, I), l(I, u), l(u, H), l(H,
				M), l(I, O), l(I, N), l(N, D), l(D, h), l(I, G), l(I, F), l(
				F, W), l(W, J)
		},
		p(Oe, [Ue]) {
			Ue & 1 && S !== (S = Oe[0].function_name + "") && Le(A, S), Ue & 1 &&
				(oe = De(Oe[0].arguments), _ = un(_, Ue, z, 1, Oe, oe, c, i, Cn,
					Hr, null, gr)), Ue & 1 && b !== (b = Oe[0].description + "") &&
				Le(M, b), Ue & 1 && B !== (B = Gr(Oe[0].instantiated_sql) + "") &&
				Le(h, B), Ue & 1 && x !== (x = Oe[0].sql_template + "") && Le(J,
					x)
		},
		i: j,
		o: j,
		d(Oe) {
			Oe && Y(e);
			for (let Ue = 0; Ue < _.length; Ue += 1) _[Ue].d()
		}
	}
}

function oi(E, e, T) {
	let {
		functionData: t
	} = e;
	return E.$$set = r => {
		"functionData" in r && T(0, t = r.functionData)
	}, [t]
}
class Oi extends ue {
	constructor(e) {
		super(), Ce(this, e, oi, Si, _e, {
			functionData: 0
		})
	}
}

function br(E, e, T) {
	const t = E.slice();
	return t[12] = e[T], t
}

function yr(E, e, T) {
	const t = E.slice();
	return t[12] = e[T], t[13] = e, t[14] = T, t
}

function ii(E) {
	let e, T, t, r = E[0].function_name + "",
		R, n, s, S = E[0].description + "",
		A, o, i, _, c, P, p, C, L, I = De(E[0].arguments),
		u = [];
	for (let H = 0; H < I.length; H += 1) u[H] = Br(br(E, I, H));
	return {
		c() {
			e = f("div"), T = f("div"), t = f("h3"), R = te(r), n = $(), s = f(
				"p"), A = te(S), o = $(), i = f("ul");
			for (let H = 0; H < u.length; H += 1) u[H].c();
			_ = $(), c = f("button"), c.textContent = "Delete", P = $(), p = f(
				"button"), p.textContent = "Edit", a(t, "class",
				"text-lg font-bold text-gray-800 dark:text-white"), a(s,
				"class",
				"mt-1 text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
			), a(i, "class",
				"mt-1 marker:text-blue-600 list-disc ps-5 space-y-2 text-sm text-gray-600 dark:text-neutral-400"
			), a(T, "class", "flex-grow"), a(c, "class",
				"mt-3 inline-flex items-center gap-x-1 text-sm font-semibold rounded-lg border border-red-600 text-red-600 hover:border-red-500 hover:text-red-500 disabled:opacity-50 disabled:pointer-events-none dark:border-red-500 dark:text-red-500 dark:hover:text-red-400 dark:hover:border-red-400 py-1 px-4 max-w-fit"
			), a(p, "class",
				"mt-3 inline-flex items-center gap-x-1 text-sm font-semibold rounded-lg border border-blue-600 text-blue-600 hover:border-blue-500 hover:text-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:border-blue-500 dark:text-blue-500 dark:hover:text-blue-400 dark:hover:border-blue-400 py-1 px-4 max-w-fit"
			), a(e, "class",
				"p-4 flex flex-col bg-white border border-t-4 border-t-blue-600 shadow-sm rounded-xl dark:bg-neutral-900 dark:border-neutral-7000 dark:border-t-blue-500 dark:shadow-neutral-700/70"
			)
		},
		m(H, b) {
			V(H, e, b), l(e, T), l(T, t), l(t, R), l(T, n), l(T, s), l(s, A), l(
				T, o), l(T, i);
			for (let M = 0; M < u.length; M += 1) u[M] && u[M].m(i, null);
			l(e, _), l(e, c), l(e, P), l(e, p), C || (L = [Ne(c, "click", E[10]),
				Ne(p, "click", E[11])
			], C = !0)
		},
		p(H, b) {
			if (b & 1 && r !== (r = H[0].function_name + "") && Le(R, r), b & 1 &&
				S !== (S = H[0].description + "") && Le(A, S), b & 1) {
				I = De(H[0].arguments);
				let M;
				for (M = 0; M < I.length; M += 1) {
					const O = br(H, I, M);
					u[M] ? u[M].p(O, b) : (u[M] = Br(O), u[M].c(), u[M].m(i,
						null))
				}
				for (; M < u.length; M += 1) u[M].d(1);
				u.length = I.length
			}
		},
		d(H) {
			H && Y(e), nE(u, H), C = !1, NE(L)
		}
	}
}

function ai(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _, c, P, p, C, L, I, u, H, b, M, O, N,
		D, B = De(E[1].arguments),
		h = [];
	for (let G = 0; G < B.length; G += 1) h[G] = vr(yr(E, B, G));
	return {
		c() {
			e = f("div"), T = f("form"), t = f("div"), r = f("div"), R = f(
					"span"), R.textContent = "Function Name", n = $(), s = f(
					"input"), S = $(), A = f("div"), o = f("span"), o.textContent =
				"Function Description", i = $(), _ = f("textarea"), c = $(), P =
				f("div"), p = f("span"), p.textContent = "SQL Template", C = $(),
				L = f("textarea"), I = $();
			for (let G = 0; G < h.length; G += 1) h[G].c();
			u = $(), H = f("div"), b = f("button"), b.textContent = "Cancel", M =
				$(), O = f("button"), O.textContent = "Save", a(R, "class",
					"inline-block text-sm font-bold text-gray-800 mt-2.5 dark:text-neutral-200"
				), a(s, "type", "text"), a(s, "class",
					"py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
				), a(s, "placeholder", "Enter function name"), a(r, "class",
					"space-y-2"), a(t, "class", "space-y-4 sm:space-y-6"), a(o,
					"class",
					"inline-block text-sm font-bold text-gray-800 mt-2.5 dark:text-neutral-200"
				), a(_, "class",
					"py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
				), a(_, "placeholder", "Enter function description"), a(A,
					"class", "space-y-2"), a(p, "class",
					"inline-block text-sm font-bold text-gray-800 mt-2.5 dark:text-neutral-200"
				), a(L, "class",
					"py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600 font-mono"
				), a(L, "placeholder", "Enter function description"), a(P,
					"class", "space-y-2"), a(b, "class",
					"py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-red-500 text-red-500 hover:border-red-400 hover:text-red-400 disabled:opacity-50 disabled:pointer-events-none"
				), a(O, "class",
					"py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none"
				), a(H, "class", "mt-3 flex gap-x-2"), a(e, "class",
					"p-4 flex flex-col bg-white border border-t-4 border-t-red-600 shadow-sm rounded-xl dark:bg-neutral-900 dark:border-neutral-7000 dark:border-t-red-500 dark:shadow-neutral-700/70"
				)
		},
		m(G, F) {
			V(G, e, F), l(e, T), l(T, t), l(t, r), l(r, R), l(r, n), l(r, s),
				Ye(s, E[1].function_name), l(T, S), l(T, A), l(A, o), l(A, i),
				l(A, _), Ye(_, E[1].description), l(T, c), l(T, P), l(P, p), l(
					P, C), l(P, L), Ye(L, E[1].sql_template), l(T, I);
			for (let W = 0; W < h.length; W += 1) h[W] && h[W].m(T, null);
			l(e, u), l(e, H), l(H, b), l(H, M), l(H, O), N || (D = [Ne(s,
					"input", E[2]), Ne(_, "input", E[3]), Ne(L, "input",
					E[4]), Ne(b, "click", E[8]), Ne(O, "click", E[9])], N = !
				0)
		},
		p(G, F) {
			if (F & 2 && s.value !== G[1].function_name && Ye(s, G[1].function_name),
				F & 2 && Ye(_, G[1].description), F & 2 && Ye(L, G[1].sql_template),
				F & 2) {
				B = De(G[1].arguments);
				let W;
				for (W = 0; W < B.length; W += 1) {
					const x = yr(G, B, W);
					h[W] ? h[W].p(x, F) : (h[W] = vr(x), h[W].c(), h[W].m(T,
						null))
				}
				for (; W < h.length; W += 1) h[W].d(1);
				h.length = B.length
			}
		},
		d(G) {
			G && Y(e), nE(h, G), N = !1, NE(D)
		}
	}
}

function Br(E) {
	let e, T, t = E[12].name + "",
		r, R, n, s = E[12].description + "",
		S;
	return {
		c() {
			e = f("li"), T = f("b"), r = te(t), R = te(":"), n = $(), S = te(s)
		},
		m(A, o) {
			V(A, e, o), l(e, T), l(T, r), l(T, R), l(e, n), l(e, S)
		},
		p(A, o) {
			o & 1 && t !== (t = A[12].name + "") && Le(r, t), o & 1 && s !== (s =
				A[12].description + "") && Le(S, s)
		},
		d(A) {
			A && Y(e)
		}
	}
}

function vr(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _, c, P, p, C, L, I, u, H, b;

	function M() {
		E[5].call(R, E[13], E[14])
	}

	function O() {
		E[6].call(o, E[13], E[14])
	}

	function N() {
		E[7].call(p, E[13], E[14])
	}
	return {
		c() {
			e = f("div"), T = f("div"), t = f("span"), t.textContent =
				"Argument Name", r = $(), R = f("input"), n = $(), s = f("div"),
				S = f("span"), S.textContent = "Argument Description", A = $(),
				o = f("input"), i = $(), _ = f("div"), c = f("span"), c.textContent =
				"Argument Type", P = $(), p = f("select"), C = f("option"), C.textContent =
				"String", L = f("option"), L.textContent = "Numeric", I = f(
					"option"), I.textContent = "Boolean", u = $(), a(t, "class",
					"inline-block text-sm font-bold text-gray-800 mt-2.5 dark:text-neutral-200"
				), a(R, "type", "text"), a(R, "class",
					"py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
				), a(R, "placeholder", "Enter argument name"), a(T, "class",
					"space-y-2"), a(S, "class",
					"inline-block text-sm font-bold text-gray-800 mt-2.5 dark:text-neutral-200"
				), a(o, "type", "text"), a(o, "class",
					"py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
				), a(o, "placeholder", "Enter argument description"), a(s,
					"class", "space-y-2"), a(c, "class",
					"inline-block text-sm font-bold text-gray-800 mt-2.5 dark:text-neutral-200"
				), C.__value = "STRING", Ye(C, C.__value), L.__value =
				"NUMERIC", Ye(L, L.__value), I.__value = "BOOLEAN", Ye(I, I.__value),
				a(p, "class",
					"py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
				), E[12].general_type === void 0 && dt(N), a(_, "class",
					"space-y-2"), a(e, "class", "space-y-4")
		},
		m(D, B) {
			V(D, e, B), l(e, T), l(T, t), l(T, r), l(T, R), Ye(R, E[12].name),
				l(e, n), l(e, s), l(s, S), l(s, A), l(s, o), Ye(o, E[12].description),
				l(e, i), l(e, _), l(_, c), l(_, P), l(_, p), l(p, C), l(p, L),
				l(p, I), WT(p, E[12].general_type, !0), l(e, u), H || (b = [Ne(
					R, "input", M), Ne(o, "input", O), Ne(p, "change",
					N)], H = !0)
		},
		p(D, B) {
			E = D, B & 2 && R.value !== E[12].name && Ye(R, E[12].name), B & 2 &&
				o.value !== E[12].description && Ye(o, E[12].description), B &
				2 && WT(p, E[12].general_type)
		},
		d(D) {
			D && Y(e), H = !1, NE(b)
		}
	}
}

function Ii(E) {
	let e;

	function T(R, n) {
		return R[1] != null ? ai : ii
	}
	let t = T(E),
		r = t(E);
	return {
		c() {
			r.c(), e = je()
		},
		m(R, n) {
			r.m(R, n), V(R, e, n)
		},
		p(R, [n]) {
			t === (t = T(R)) && r ? r.p(R, n) : (r.d(1), r = t(R), r && (r.c(),
				r.m(e.parentNode, e)))
		},
		i: j,
		o: j,
		d(R) {
			R && Y(e), r.d(R)
		}
	}
}

function Ni(E, e, T) {
	let {
		functionTemplate: t
	} = e, r = null;

	function R() {
		r.function_name = this.value, T(1, r)
	}

	function n() {
		r.description = this.value, T(1, r)
	}

	function s() {
		r.sql_template = this.value, T(1, r)
	}

	function S(p, C) {
		p[C].name = this.value, T(1, r)
	}

	function A(p, C) {
		p[C].description = this.value, T(1, r)
	}

	function o(p, C) {
		p[C].general_type = On(this), T(1, r)
	}
	const i = () => {
			T(1, r = null)
		},
		_ = () => {
			r && (Vn(t.function_name, r), T(0, t = r), T(1, r = null))
		},
		c = () => {
			t && window.confirm(
				"Are you sure you want to delete this function?") && Wn(t.function_name)
		},
		P = () => {
			T(1, r = structuredClone(t))
		};
	return E.$$set = p => {
		"functionTemplate" in p && T(0, t = p.functionTemplate)
	}, [t, r, R, n, s, S, A, o, i, _, c, P]
}
class en extends ue {
	constructor(e) {
		super(), Ce(this, e, Ni, Ii, _e, {
			functionTemplate: 0
		})
	}
}

function Fr(E, e, T) {
	const t = E.slice();
	return t[15] = e[T], t
}

function Yr(E, e, T) {
	const t = E.slice();
	return t[18] = e[T], t
}

function Vr(E, e, T) {
	const t = E.slice();
	return t[21] = e[T], t
}

function Wr(E, e, T) {
	const t = E.slice();
	return t[21] = e[T], t
}

function wr(E) {
	let e, T;
	return e = new ZA({}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function $r(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [_i]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108866 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function xr(E) {
	let e, T;
	return e = new IE({
		props: {
			message: E[21],
			onSubmit: uT
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 2 && (R.message = t[21]), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function li(E) {
	let e = E[1].header + "",
		T, t, r, R, n = De(E[1].questions),
		s = [];
	for (let A = 0; A < n.length; A += 1) s[A] = xr(Wr(E, n, A));
	const S = A => y(s[A], 1, 1, () => {
		s[A] = null
	});
	return {
		c() {
			T = te(e), t = $();
			for (let A = 0; A < s.length; A += 1) s[A].c();
			r = je()
		},
		m(A, o) {
			V(A, T, o), V(A, t, o);
			for (let i = 0; i < s.length; i += 1) s[i] && s[i].m(A, o);
			V(A, r, o), R = !0
		},
		p(A, o) {
			if ((!R || o & 2) && e !== (e = A[1].header + "") && Le(T, e), o &
				2) {
				n = De(A[1].questions);
				let i;
				for (i = 0; i < n.length; i += 1) {
					const _ = Wr(A, n, i);
					s[i] ? (s[i].p(_, o), m(s[i], 1)) : (s[i] = xr(_), s[i].c(),
						m(s[i], 1), s[i].m(r.parentNode, r))
				}
				for (Ge(), i = n.length; i < s.length; i += 1) S(i);
				ge()
			}
		},
		i(A) {
			if (!R) {
				for (let o = 0; o < n.length; o += 1) m(s[o]);
				R = !0
			}
		},
		o(A) {
			s = s.filter(Boolean);
			for (let o = 0; o < s.length; o += 1) y(s[o]);
			R = !1
		},
		d(A) {
			A && (Y(T), Y(t), Y(r)), nE(s, A)
		}
	}
}

function _i(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [li]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108866 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Li(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [Fi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Ci(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [Vi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108888 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function ui(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [Wi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function ci(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [wi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function fi(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [xi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Pi(E) {
	let e, T;
	return e = new WE({
		props: {
			message: "Put your SQL here",
			$$slots: {
				default: [Xi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108864 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Di(E) {
	let e, T, t, r, R, n, s, S, A, o;
	e = new WE({
		props: {
			message: E[18].question
		}
	}), t = new Ze({
		props: {
			$$slots: {
				default: [Ji]
			},
			$$scope: {
				ctx: E
			}
		}
	}), R = new Ze({
		props: {
			$$slots: {
				default: [qi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), s = new Ze({
		props: {
			$$slots: {
				default: [Qi]
			},
			$$scope: {
				ctx: E
			}
		}
	});
	let i = E[18].summary && Xr(E);
	return {
		c() {
			K(e.$$.fragment), T = $(), K(t.$$.fragment), r = $(), K(R.$$.fragment),
				n = $(), K(s.$$.fragment), S = $(), i && i.c(), A = je()
		},
		m(_, c) {
			X(e, _, c), V(_, T, c), X(t, _, c), V(_, r, c), X(R, _, c), V(_, n,
					c), X(s, _, c), V(_, S, c), i && i.m(_, c), V(_, A, c), o = !
				0
		},
		p(_, c) {
			const P = {};
			c & 8 && (P.message = _[18].question), e.$set(P);
			const p = {};
			c & 67108872 && (p.$$scope = {
				dirty: c,
				ctx: _
			}), t.$set(p);
			const C = {};
			c & 67108872 && (C.$$scope = {
				dirty: c,
				ctx: _
			}), R.$set(C);
			const L = {};
			c & 67108872 && (L.$$scope = {
					dirty: c,
					ctx: _
				}), s.$set(L), _[18].summary ? i ? (i.p(_, c), c & 8 && m(i, 1)) :
				(i = Xr(_), i.c(), m(i, 1), i.m(A.parentNode, A)) : i && (Ge(),
					y(i, 1, 1, () => {
						i = null
					}), ge())
		},
		i(_) {
			o || (m(e.$$.fragment, _), m(t.$$.fragment, _), m(R.$$.fragment, _),
				m(s.$$.fragment, _), m(i), o = !0)
		},
		o(_) {
			y(e.$$.fragment, _), y(t.$$.fragment, _), y(R.$$.fragment, _), y(s.$$
				.fragment, _), y(i), o = !1
		},
		d(_) {
			_ && (Y(T), Y(r), Y(n), Y(S), Y(A)), k(e, _), k(t, _), k(R, _), k(s,
				_), i && i.d(_)
		}
	}
}

function di(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [zi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108873 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function pi(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [ea]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Mi(E) {
	let e, T;
	return e = new WE({
		props: {
			message: "No, the results were not correct."
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p: j,
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Ui(E) {
	let e, T;
	return e = new WE({
		props: {
			message: "Yes, the results were correct."
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p: j,
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function mi(E) {
	let e, T, t = E[0].ask_results_correct && Kr(E);
	return {
		c() {
			t && t.c(), e = je()
		},
		m(r, R) {
			t && t.m(r, R), V(r, e, R), T = !0
		},
		p(r, R) {
			r[0].ask_results_correct ? t ? (t.p(r, R), R & 1 && m(t, 1)) : (t =
				Kr(r), t.c(), m(t, 1), t.m(e.parentNode, e)) : t && (Ge(),
				y(t, 1, 1, () => {
					t = null
				}), ge())
		},
		i(r) {
			T || (m(t), T = !0)
		},
		o(r) {
			y(t), T = !1
		},
		d(r) {
			r && Y(e), t && t.d(r)
		}
	}
}

function hi(E) {
	let e, T, t = E[0].ask_results_correct && qr(E);
	return {
		c() {
			t && t.c(), e = je()
		},
		m(r, R) {
			t && t.m(r, R), V(r, e, R), T = !0
		},
		p(r, R) {
			r[0].ask_results_correct ? t ? R & 1 && m(t, 1) : (t = qr(r), t.c(),
				m(t, 1), t.m(e.parentNode, e)) : t && (Ge(), y(t, 1, 1, () => {
				t = null
			}), ge())
		},
		i(r) {
			T || (m(t), T = !0)
		},
		o(r) {
			y(t), T = !1
		},
		d(r) {
			r && Y(e), t && t.d(r)
		}
	}
}

function Gi(E) {
	let e, T;
	return e = new WE({
		props: {
			message: "Change the chart based on these instructions",
			$$slots: {
				default: [Ra]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108864 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function gi(E) {
	let e, T, t = E[0].chart && Qr(E);
	return {
		c() {
			t && t.c(), e = je()
		},
		m(r, R) {
			t && t.m(r, R), V(r, e, R), T = !0
		},
		p(r, R) {
			r[0].chart ? t ? (t.p(r, R), R & 1 && m(t, 1)) : (t = Qr(r), t.c(),
				m(t, 1), t.m(e.parentNode, e)) : t && (Ge(), y(t, 1, 1, () => {
				t = null
			}), ge())
		},
		i(r) {
			T || (m(t), T = !0)
		},
		o(r) {
			y(t), T = !1
		},
		d(r) {
			r && Y(e), t && t.d(r)
		}
	}
}

function Hi(E) {
	let e, T, t = E[0].table && jr(E);
	return {
		c() {
			t && t.c(), e = je()
		},
		m(r, R) {
			t && t.m(r, R), V(r, e, R), T = !0
		},
		p(r, R) {
			r[0].table ? t ? (t.p(r, R), R & 1 && m(t, 1)) : (t = jr(r), t.c(),
				m(t, 1), t.m(e.parentNode, e)) : t && (Ge(), y(t, 1, 1, () => {
				t = null
			}), ge())
		},
		i(r) {
			T || (m(t), T = !0)
		},
		o(r) {
			y(t), T = !1
		},
		d(r) {
			r && Y(e), t && t.d(r)
		}
	}
}

function bi(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [oa]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function yi(E) {
	let e, T, t = E[0].sql == !0 && eR(E);
	return {
		c() {
			t && t.c(), e = je()
		},
		m(r, R) {
			t && t.m(r, R), V(r, e, R), T = !0
		},
		p(r, R) {
			r[0].sql == !0 ? t ? (t.p(r, R), R & 1 && m(t, 1)) : (t = eR(r), t.c(),
				m(t, 1), t.m(e.parentNode, e)) : t && (Ge(), y(t, 1, 1, () => {
				t = null
			}), ge())
		},
		i(r) {
			T || (m(t), T = !0)
		},
		o(r) {
			y(t), T = !1
		},
		d(r) {
			r && Y(e), t && t.d(r)
		}
	}
}

function Bi(E) {
	let e, T;
	return e = new WE({
		props: {
			message: E[18].question
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.message = t[18].question), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function vi(E) {
	let e = JSON.stringify(E[18]) + "",
		T;
	return {
		c() {
			T = te(e)
		},
		m(t, r) {
			V(t, T, r)
		},
		p(t, r) {
			r & 8 && e !== (e = JSON.stringify(t[18]) + "") && Le(T, e)
		},
		d(t) {
			t && Y(T)
		}
	}
}

function Fi(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [vi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Yi(E) {
	let e, T = E[18].question + "",
		t;
	return {
		c() {
			e = te("I interpreted your question as: "), t = te(T)
		},
		m(r, R) {
			V(r, e, R), V(r, t, R)
		},
		p(r, R) {
			R & 8 && T !== (T = r[18].question + "") && Le(t, T)
		},
		d(r) {
			r && (Y(e), Y(t))
		}
	}
}

function Vi(E) {
	let e, T, t, r, R, n;
	e = new aE({
		props: {
			$$slots: {
				default: [Yi]
			},
			$$scope: {
				ctx: E
			}
		}
	});

	function s() {
		return E[12](E[18])
	}
	return t = new IE({
		props: {
			message: "Edit Question",
			onSubmit: s
		}
	}), R = new IE({
		props: {
			message: "New Question",
			onSubmit: E[13]
		}
	}), {
		c() {
			K(e.$$.fragment), T = $(), K(t.$$.fragment), r = $(), K(R.$$.fragment)
		},
		m(S, A) {
			X(e, S, A), V(S, T, A), X(t, S, A), V(S, r, A), X(R, S, A), n = !
				0
		},
		p(S, A) {
			E = S;
			const o = {};
			A & 67108872 && (o.$$scope = {
				dirty: A,
				ctx: E
			}), e.$set(o);
			const i = {};
			A & 24 && (i.onSubmit = s), t.$set(i)
		},
		i(S) {
			n || (m(e.$$.fragment, S), m(t.$$.fragment, S), m(R.$$.fragment,
				S), n = !0)
		},
		o(S) {
			y(e.$$.fragment, S), y(t.$$.fragment, S), y(R.$$.fragment, S),
				n = !1
		},
		d(S) {
			S && (Y(T), Y(r)), k(e, S), k(t, S), k(R, S)
		}
	}
}

function Wi(E) {
	let e, T;
	return e = new en({
		props: {
			functionTemplate: E[18].function_template
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.functionTemplate = t[18].function_template), e.$set(
				R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function wi(E) {
	let e, T;
	return e = new Oi({
		props: {
			functionData: E[18].function
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.functionData = t[18].function), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function $i(E) {
	let e = E[18].text + "",
		T;
	return {
		c() {
			T = te(e)
		},
		m(t, r) {
			V(t, T, r)
		},
		p(t, r) {
			r & 8 && e !== (e = t[18].text + "") && Le(T, e)
		},
		d(t) {
			t && Y(T)
		}
	}
}

function xi(E) {
	let e, T, t, r;
	return e = new aE({
		props: {
			$$slots: {
				default: [$i]
			},
			$$scope: {
				ctx: E
			}
		}
	}), t = new qA({
		props: {
			message: E[18].text
		}
	}), {
		c() {
			K(e.$$.fragment), T = $(), K(t.$$.fragment)
		},
		m(R, n) {
			X(e, R, n), V(R, T, n), X(t, R, n), r = !0
		},
		p(R, n) {
			const s = {};
			n & 67108872 && (s.$$scope = {
				dirty: n,
				ctx: R
			}), e.$set(s);
			const S = {};
			n & 8 && (S.message = R[18].text), t.$set(S)
		},
		i(R) {
			r || (m(e.$$.fragment, R), m(t.$$.fragment, R), r = !0)
		},
		o(R) {
			y(e.$$.fragment, R), y(t.$$.fragment, R), r = !1
		},
		d(R) {
			R && Y(T), k(e, R), k(t, R)
		}
	}
}

function Xi(E) {
	let e, T;
	return e = new $A({
		props: {
			onSubmit: vn
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p: j,
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function ki(E) {
	let e = E[18].sql + "",
		T;
	return {
		c() {
			T = te(e)
		},
		m(t, r) {
			V(t, T, r)
		},
		p(t, r) {
			r & 8 && e !== (e = t[18].sql + "") && Le(T, e)
		},
		d(t) {
			t && Y(T)
		}
	}
}

function Ki(E) {
	let e, T;
	return e = new bR({
		props: {
			$$slots: {
				default: [ki]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Ji(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [Ki]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function qi(E) {
	let e, T;
	return e = new gR({
		props: {
			id: E[18].id,
			df: E[18].df
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.id = t[18].id), r & 8 && (R.df = t[18].df), e.$set(
				R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Qi(E) {
	let e, T;
	return e = new HR({
		props: {
			fig: E[18].fig
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.fig = t[18].fig), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Xr(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [ji]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Zi(E) {
	let e = E[18].summary + "",
		T;
	return {
		c() {
			T = te(e)
		},
		m(t, r) {
			V(t, T, r)
		},
		p(t, r) {
			r & 8 && e !== (e = t[18].summary + "") && Le(T, e)
		},
		d(t) {
			t && Y(T)
		}
	}
}

function ji(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [Zi]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function kr(E) {
	let e, T;

	function t() {
		return E[11](E[18])
	}
	return e = new IE({
		props: {
			message: "Auto Fix",
			onSubmit: t
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(r, R) {
			X(e, r, R), T = !0
		},
		p(r, R) {
			E = r;
			const n = {};
			R & 8 && (n.onSubmit = t), e.$set(n)
		},
		i(r) {
			T || (m(e.$$.fragment, r), T = !0)
		},
		o(r) {
			y(e.$$.fragment, r), T = !1
		},
		d(r) {
			k(e, r)
		}
	}
}

function zi(E) {
	let e, T, t, r, R, n;
	e = new PT({
		props: {
			message: E[18].error
		}
	}), t = new IE({
		props: {
			message: "Manually Fix",
			onSubmit: E[10]
		}
	});
	let s = E[0].auto_fix_sql && kr(E);
	return {
		c() {
			K(e.$$.fragment), T = $(), K(t.$$.fragment), r = $(), s && s.c(), R =
				je()
		},
		m(S, A) {
			X(e, S, A), V(S, T, A), X(t, S, A), V(S, r, A), s && s.m(S, A), V(S,
				R, A), n = !0
		},
		p(S, A) {
			const o = {};
			A & 8 && (o.message = S[18].error), e.$set(o), S[0].auto_fix_sql ?
				s ? (s.p(S, A), A & 1 && m(s, 1)) : (s = kr(S), s.c(), m(s, 1),
					s.m(R.parentNode, R)) : s && (Ge(), y(s, 1, 1, () => {
					s = null
				}), ge())
		},
		i(S) {
			n || (m(e.$$.fragment, S), m(t.$$.fragment, S), m(s), n = !0)
		},
		o(S) {
			y(e.$$.fragment, S), y(t.$$.fragment, S), y(s), n = !1
		},
		d(S) {
			S && (Y(T), Y(r), Y(R)), k(e, S), k(t, S), s && s.d(S)
		}
	}
}

function ea(E) {
	let e, T;
	return e = new PT({
		props: {
			message: E[18].error
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.message = t[18].error), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Kr(E) {
	let e, T;
	return e = new WE({
		props: {
			message: "",
			$$slots: {
				default: [ta]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108865 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Ea(E) {
	let e, T, t, r = E[0].function_generation && Jr(E);
	return T = new IE({
		props: {
			message: "Yes, train as Question-SQL pair",
			onSubmit: E[8]
		}
	}), {
		c() {
			r && r.c(), e = $(), K(T.$$.fragment)
		},
		m(R, n) {
			r && r.m(R, n), V(R, e, n), X(T, R, n), t = !0
		},
		p(R, n) {
			R[0].function_generation ? r ? n & 1 && m(r, 1) : (r = Jr(R), r
				.c(), m(r, 1), r.m(e.parentNode, e)) : r && (Ge(), y(r,
				1, 1, () => {
					r = null
				}), ge())
		},
		i(R) {
			t || (m(r), m(T.$$.fragment, R), t = !0)
		},
		o(R) {
			y(r), y(T.$$.fragment, R), t = !1
		},
		d(R) {
			R && Y(e), r && r.d(R), k(T, R)
		}
	}
}

function Jr(E) {
	let e, T;
	return e = new IE({
		props: {
			message: "Yes, create function",
			onSubmit: E[7]
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function ta(E) {
	let e = fT() !== null,
		T, t, r, R = e && Ea(E);
	return t = new IE({
		props: {
			message: "No",
			onSubmit: E[9]
		}
	}), {
		c() {
			R && R.c(), T = $(), K(t.$$.fragment)
		},
		m(n, s) {
			R && R.m(n, s), V(n, T, s), X(t, n, s), r = !0
		},
		p(n, s) {
			e && R.p(n, s)
		},
		i(n) {
			r || (m(R), m(t.$$.fragment, n), r = !0)
		},
		o(n) {
			y(R), y(t.$$.fragment, n), r = !1
		},
		d(n) {
			n && Y(T), R && R.d(n), k(t, n)
		}
	}
}

function qr(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [ra]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Ta(E) {
	let e;
	return {
		c() {
			e = te("Were the results correct?")
		},
		m(T, t) {
			V(T, e, t)
		},
		d(T) {
			T && Y(e)
		}
	}
}

function ra(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [Ta]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108864 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Ra(E) {
	let e, T;
	return e = new kA({
		props: {
			onSubmit: E[6],
			placeholder: "Make the line red",
			buttonText: "Update Chart",
			currentValue: ""
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p: j,
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Qr(E) {
	let e, T, t, r;
	e = new Ze({
		props: {
			$$slots: {
				default: [na]
			},
			$$scope: {
				ctx: E
			}
		}
	});
	let R = E[0].redraw_chart && Zr(E);
	return {
		c() {
			K(e.$$.fragment), T = $(), R && R.c(), t = je()
		},
		m(n, s) {
			X(e, n, s), V(n, T, s), R && R.m(n, s), V(n, t, s), r = !0
		},
		p(n, s) {
			const S = {};
			s & 67108872 && (S.$$scope = {
				dirty: s,
				ctx: n
			}), e.$set(S), n[0].redraw_chart ? R ? s & 1 && m(R, 1) : (R =
				Zr(n), R.c(), m(R, 1), R.m(t.parentNode, t)) : R && (Ge(),
				y(R, 1, 1, () => {
					R = null
				}), ge())
		},
		i(n) {
			r || (m(e.$$.fragment, n), m(R), r = !0)
		},
		o(n) {
			y(e.$$.fragment, n), y(R), r = !1
		},
		d(n) {
			n && (Y(T), Y(t)), k(e, n), R && R.d(n)
		}
	}
}

function na(E) {
	let e, T;
	return e = new HR({
		props: {
			fig: E[18].fig
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.fig = t[18].fig), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Zr(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [Aa]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Aa(E) {
	let e, T;
	return e = new IE({
		props: {
			message: "Redraw Chart",
			onSubmit: Fn
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p: j,
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function jr(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [sa]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function sa(E) {
	let e, T;
	return e = new gR({
		props: {
			id: E[18].id,
			df: E[18].df
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.id = t[18].id), r & 8 && (R.df = t[18].df), e.$set(
				R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function zr(E) {
	let e, T;
	return e = new IE({
		props: {
			message: E[21],
			onSubmit: uT
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 8 && (R.message = t[21]), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Sa(E) {
	let e = E[18].header + "",
		T, t, r, R, n = De(E[18].questions),
		s = [];
	for (let A = 0; A < n.length; A += 1) s[A] = zr(Vr(E, n, A));
	const S = A => y(s[A], 1, 1, () => {
		s[A] = null
	});
	return {
		c() {
			T = te(e), t = $();
			for (let A = 0; A < s.length; A += 1) s[A].c();
			r = je()
		},
		m(A, o) {
			V(A, T, o), V(A, t, o);
			for (let i = 0; i < s.length; i += 1) s[i] && s[i].m(A, o);
			V(A, r, o), R = !0
		},
		p(A, o) {
			if ((!R || o & 8) && e !== (e = A[18].header + "") && Le(T, e), o &
				8) {
				n = De(A[18].questions);
				let i;
				for (i = 0; i < n.length; i += 1) {
					const _ = Vr(A, n, i);
					s[i] ? (s[i].p(_, o), m(s[i], 1)) : (s[i] = zr(_), s[i].c(),
						m(s[i], 1), s[i].m(r.parentNode, r))
				}
				for (Ge(), i = n.length; i < s.length; i += 1) S(i);
				ge()
			}
		},
		i(A) {
			if (!R) {
				for (let o = 0; o < n.length; o += 1) m(s[o]);
				R = !0
			}
		},
		o(A) {
			s = s.filter(Boolean);
			for (let o = 0; o < s.length; o += 1) y(s[o]);
			R = !1
		},
		d(A) {
			A && (Y(T), Y(t), Y(r)), nE(s, A)
		}
	}
}

function oa(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [Sa]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function eR(E) {
	let e, T;
	return e = new Ze({
		props: {
			$$slots: {
				default: [aa]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Oa(E) {
	let e = E[18].text + "",
		T;
	return {
		c() {
			T = te(e)
		},
		m(t, r) {
			V(t, T, r)
		},
		p(t, r) {
			r & 8 && e !== (e = t[18].text + "") && Le(T, e)
		},
		d(t) {
			t && Y(T)
		}
	}
}

function ia(E) {
	let e, T;
	return e = new bR({
		props: {
			$$slots: {
				default: [Oa]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function aa(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [ia]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 67108872 && (R.$$scope = {
				dirty: r,
				ctx: t
			}), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function ER(E) {
	let e, T, t, r;
	const R = [Bi, yi, bi, Hi, gi, Gi, hi, mi, Ui, Mi, pi, di, Di, Pi, fi, ci,
			ui, Ci, Li
		],
		n = [];

	function s(S, A) {
		return S[18].type === "user_question" ? 0 : S[18].type === "sql" ? 1 :
			S[18].type === "question_list" ? 2 : S[18].type === "df" ? 3 : S[18]
			.type === "plotly_figure" ? 4 : S[18].type === "chart_modification" ?
			5 : S[18].type === "feedback_question" ? 6 : S[18].type ===
			"feedback_buttons" ? 7 : S[18].type === "feedback_correct" ? 8 : S[
				18].type === "feedback_incorrect" ? 9 : S[18].type === "error" ?
			10 : S[18].type === "sql_error" ? 11 : S[18].type ===
			"question_cache" ? 12 : S[18].type === "user_sql" ? 13 : S[18].type ===
			"text" ? 14 : S[18].type === "function" ? 15 : S[18].type ===
			"function_template" ? 16 : S[18].type === "rewritten_question" ? 17 :
			18
	}
	return e = s(E), T = n[e] = R[e](E), {
		c() {
			T.c(), t = je()
		},
		m(S, A) {
			n[e].m(S, A), V(S, t, A), r = !0
		},
		p(S, A) {
			let o = e;
			e = s(S), e === o ? n[e].p(S, A) : (Ge(), y(n[o], 1, 1, () => {
				n[o] = null
			}), ge(), T = n[e], T ? T.p(S, A) : (T = n[e] = R[e](S),
				T.c()), m(T, 1), T.m(t.parentNode, t))
		},
		i(S) {
			r || (m(T), r = !0)
		},
		o(S) {
			y(T), r = !1
		},
		d(S) {
			S && Y(t), n[e].d(S)
		}
	}
}

function tR(E) {
	let e, T;
	return e = new dA({}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function TR(E) {
	let e, T, t = De(E[3]),
		r = [];
	for (let n = 0; n < t.length; n += 1) r[n] = RR(Fr(E, t, n));
	const R = n => y(r[n], 1, 1, () => {
		r[n] = null
	});
	return {
		c() {
			for (let n = 0; n < r.length; n += 1) r[n].c();
			e = je()
		},
		m(n, s) {
			for (let S = 0; S < r.length; S += 1) r[S] && r[S].m(n, s);
			V(n, e, s), T = !0
		},
		p(n, s) {
			if (s & 8) {
				t = De(n[3]);
				let S;
				for (S = 0; S < t.length; S += 1) {
					const A = Fr(n, t, S);
					r[S] ? (r[S].p(A, s), m(r[S], 1)) : (r[S] = RR(A), r[S].c(),
						m(r[S], 1), r[S].m(e.parentNode, e))
				}
				for (Ge(), S = t.length; S < r.length; S += 1) R(S);
				ge()
			}
		},
		i(n) {
			if (!T) {
				for (let s = 0; s < t.length; s += 1) m(r[s]);
				T = !0
			}
		},
		o(n) {
			r = r.filter(Boolean);
			for (let s = 0; s < r.length; s += 1) y(r[s]);
			T = !1
		},
		d(n) {
			n && Y(e), nE(r, n)
		}
	}
}

function rR(E) {
	let e, T;

	function t() {
		return E[14](E[15])
	}
	return e = new yA({
		props: {
			message: "Re-Run SQL",
			onSubmit: t
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(r, R) {
			X(e, r, R), T = !0
		},
		p(r, R) {
			E = r;
			const n = {};
			R & 8 && (n.onSubmit = t), e.$set(n)
		},
		i(r) {
			T || (m(e.$$.fragment, r), T = !0)
		},
		o(r) {
			y(e.$$.fragment, r), T = !1
		},
		d(r) {
			k(e, r)
		}
	}
}

function RR(E) {
	let e, T, t = E[15].type === "question_cache" && rR(E);
	return {
		c() {
			t && t.c(), e = je()
		},
		m(r, R) {
			t && t.m(r, R), V(r, e, R), T = !0
		},
		p(r, R) {
			r[15].type === "question_cache" ? t ? (t.p(r, R), R & 8 && m(t, 1)) :
				(t = rR(r), t.c(), m(t, 1), t.m(e.parentNode, e)) : t && (Ge(),
					y(t, 1, 1, () => {
						t = null
					}), ge())
		},
		i(r) {
			T || (m(t), T = !0)
		},
		o(r) {
			y(t), T = !1
		},
		d(r) {
			r && Y(e), t && t.d(r)
		}
	}
}

function Ia(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _, c, P, p;
	t = new EA({});
	let C = E[0].debug && wr(),
		L = E[1] && E[1].type == "question_list" && !E[2] && $r(E),
		I = De(E[3]),
		u = [];
	for (let O = 0; O < I.length; O += 1) u[O] = ER(Yr(E, I, O));
	const H = O => y(u[O], 1, 1, () => {
		u[O] = null
	});
	let b = E[5] && tR();
	i = new lA({});
	let M = E[2] && TR(E);
	return P = new IA({
		props: {
			onSubmit: uT
		}
	}), {
		c() {
			e = f("div"), T = f("div"), K(t.$$.fragment), r = $(), C && C.c(),
				R = $(), L && L.c(), n = $(), s = f("ul");
			for (let O = 0; O < u.length; O += 1) u[O].c();
			S = $(), b && b.c(), A = $(), o = f("footer"), K(i.$$.fragment),
				_ = $(), M && M.c(), c = $(), K(P.$$.fragment), a(s,
					"class", "mt-16 space-y-5"), a(T, "class",
					"py-10 lg:py-14"), a(o, "class",
					"max-w-4xl mx-auto sticky bottom-0 z-10 p-3 sm:py-6"),
				a(e, "class", "relative h-screen w-full lg:pl-64")
		},
		m(O, N) {
			V(O, e, N), l(e, T), X(t, T, null), l(T, r), C && C.m(T, null),
				l(T, R), L && L.m(T, null), l(T, n), l(T, s);
			for (let D = 0; D < u.length; D += 1) u[D] && u[D].m(s, null);
			l(s, S), b && b.m(s, null), l(e, A), l(e, o), X(i, o, null), l(
					o, _), M && M.m(o, null), l(o, c), X(P, o, null), p = !
				0
		},
		p(O, [N]) {
			if (O[0].debug ? C ? N & 1 && m(C, 1) : (C = wr(), C.c(), m(C,
					1), C.m(T, R)) : C && (Ge(), y(C, 1, 1, () => {
					C = null
				}), ge()), O[1] && O[1].type == "question_list" && !O[2] ?
				L ? (L.p(O, N), N & 6 && m(L, 1)) : (L = $r(O), L.c(), m(L,
					1), L.m(T, n)) : L && (Ge(), y(L, 1, 1, () => {
					L = null
				}), ge()), N & 25) {
				I = De(O[3]);
				let D;
				for (D = 0; D < I.length; D += 1) {
					const B = Yr(O, I, D);
					u[D] ? (u[D].p(B, N), m(u[D], 1)) : (u[D] = ER(B), u[D]
						.c(), m(u[D], 1), u[D].m(s, S))
				}
				for (Ge(), D = I.length; D < u.length; D += 1) H(D);
				ge()
			}
			O[5] ? b ? N & 32 && m(b, 1) : (b = tR(), b.c(), m(b, 1), b.m(s,
				null)) : b && (Ge(), y(b, 1, 1, () => {
				b = null
			}), ge()), O[2] ? M ? (M.p(O, N), N & 4 && m(M, 1)) : (M =
				TR(O), M.c(), m(M, 1), M.m(o, c)) : M && (Ge(), y(M, 1,
				1, () => {
					M = null
				}), ge())
		},
		i(O) {
			if (!p) {
				m(t.$$.fragment, O), m(C), m(L);
				for (let N = 0; N < I.length; N += 1) m(u[N]);
				m(b), m(i.$$.fragment, O), m(M), m(P.$$.fragment, O), p = !
					0
			}
		},
		o(O) {
			y(t.$$.fragment, O), y(C), y(L), u = u.filter(Boolean);
			for (let N = 0; N < u.length; N += 1) y(u[N]);
			y(b), y(i.$$.fragment, O), y(M), y(P.$$.fragment, O), p = !1
		},
		d(O) {
			O && Y(e), k(t), C && C.d(), L && L.d(), nE(u, O), b && b.d(),
				k(i), M && M.d(), k(P)
		}
	}
}

function Na(E, e, T) {
	let t, r, R, n, s, S;
	return eE(E, VE, I => T(0, t = I)), eE(E, LT, I => T(1, r = I)), eE(E, Ht,
		I => T(2, R = I)), eE(E, YE, I => T(3, n = I)), eE(E, BE, I => T(4,
		s = I)), eE(E, St, I => T(5, S = I)), [t, r, R, n, s, S, I => {
		$n(I)
	}, () => {
		Yn()
	}, () => {
		wn()
	}, () => {
		wT()
	}, () => {
		wT()
	}, I => {
		Bn(I.error)
	}, I => {
		it(), OT(BE, s = I.question, s)
	}, () => {
		it()
	}, I => I.type === "question_cache" ? dn(I.id) : void 0]
}
class la extends ue {
	constructor(e) {
		super(), Ce(this, e, Na, Ia, _e, {})
	}
}

function _a(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _, c, P, p, C, L, I, u;
	return {
		c() {
			e = f("div"), T = f("div"), t = f("div"), r = f("div"), R = f("h3"),
				R.textContent = "Are you sure?", n = $(), s = f("button"), s.innerHTML =
				'<span class="sr-only">Close</span> <svg class="w-3.5 h-3.5" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.258206 1.00652C0.351976 0.912791 0.479126 0.860131 0.611706 0.860131C0.744296 0.860131 0.871447 0.912791 0.965207 1.00652L3.61171 3.65302L6.25822 1.00652C6.30432 0.958771 6.35952 0.920671 6.42052 0.894471C6.48152 0.868271 6.54712 0.854471 6.61352 0.853901C6.67992 0.853321 6.74572 0.865971 6.80722 0.891111C6.86862 0.916251 6.92442 0.953381 6.97142 1.00032C7.01832 1.04727 7.05552 1.1031 7.08062 1.16454C7.10572 1.22599 7.11842 1.29183 7.11782 1.35822C7.11722 1.42461 7.10342 1.49022 7.07722 1.55122C7.05102 1.61222 7.01292 1.6674 6.96522 1.71352L4.31871 4.36002L6.96522 7.00648C7.05632 7.10078 7.10672 7.22708 7.10552 7.35818C7.10442 7.48928 7.05182 7.61468 6.95912 7.70738C6.86642 7.80018 6.74102 7.85268 6.60992 7.85388C6.47882 7.85498 6.35252 7.80458 6.25822 7.71348L3.61171 5.06702L0.965207 7.71348C0.870907 7.80458 0.744606 7.85498 0.613506 7.85388C0.482406 7.85268 0.357007 7.80018 0.264297 7.70738C0.171597 7.61468 0.119017 7.48928 0.117877 7.35818C0.116737 7.22708 0.167126 7.10078 0.258206 7.00648L2.90471 4.36002L0.258206 1.71352C0.164476 1.61976 0.111816 1.4926 0.111816 1.36002C0.111816 1.22744 0.164476 1.10028 0.258206 1.00652Z" fill="currentColor"></path></svg>',
				S = $(), A = f("div"), o = f("p"), i = te(E[0]), _ = $(), c = f(
					"div"), P = f("button"), P.textContent = "Close", p = $(),
				C = f("button"), L = te(E[1]), a(R, "class",
					"font-bold text-gray-800 dark:text-white"), a(s, "type",
					"button"), a(s, "class",
					"hs-dropdown-toggle inline-flex flex-shrink-0 justify-center items-center h-8 w-8 rounded-md text-gray-500 hover:text-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-offset-2 focus:ring-offset-white transition-all text-sm dark:focus:ring-gray-700 dark:focus:ring-offset-gray-800"
				), a(s, "data-hs-overlay", "#hs-vertically-centered-modal"), a(
					r, "class",
					"flex justify-between items-center py-3 px-4 border-b dark:border-gray-700"
				), a(o, "class", "text-gray-800 dark:text-gray-400"), a(A,
					"class", "p-4 overflow-y-auto"), a(P, "type", "button"), a(
					P, "class",
					"hs-dropdown-toggle py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 transition-all text-sm dark:bg-slate-900 dark:hover:bg-slate-800 dark:border-gray-700 dark:text-gray-400 dark:hover:text-white dark:focus:ring-offset-gray-800"
				), a(P, "data-hs-overlay", "#hs-vertically-centered-modal"), a(
					C, "class",
					"py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border border-transparent font-semibold bg-blue-500 text-white hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all text-sm dark:focus:ring-offset-gray-800"
				), a(c, "class",
					"flex justify-end items-center gap-x-2 py-3 px-4 border-t dark:border-gray-700"
				), a(t, "class",
					"flex flex-col bg-white border shadow-sm rounded-xl dark:bg-gray-800 dark:border-gray-700 dark:shadow-slate-700/[.7]"
				), a(T, "class",
					"hs-overlay-open:mt-7 hs-overlay-open:opacity-100 hs-overlay-open:duration-500 mt-0 opacity-0 ease-out transition-all sm:max-w-lg sm:w-full m-3 sm:mx-auto min-h-[calc(100%-3.5rem)] flex items-center"
				), a(e, "class",
					"hs-overlay open w-full h-full fixed top-0 left-0 z-[60] overflow-x-hidden overflow-y-auto"
				)
		},
		m(H, b) {
			V(H, e, b), l(e, T), l(T, t), l(t, r), l(r, R), l(r, n), l(r, s), l(
					t, S), l(t, A), l(A, o), l(o, i), l(t, _), l(t, c), l(c, P),
				l(c, p), l(c, C), l(C, L), I || (u = [Ne(s, "click", function() {
					zE(E[2]) && E[2].apply(this, arguments)
				}), Ne(P, "click", function() {
					zE(E[2]) && E[2].apply(this, arguments)
				}), Ne(C, "click", function() {
					zE(E[3]) && E[3].apply(this, arguments)
				})], I = !0)
		},
		p(H, [b]) {
			E = H, b & 1 && Le(i, E[0]), b & 2 && Le(L, E[1])
		},
		i: j,
		o: j,
		d(H) {
			H && Y(e), I = !1, NE(u)
		}
	}
}

function La(E, e, T) {
	let {
		message: t
	} = e, {
		buttonLabel: r
	} = e, {
		onClose: R
	} = e, {
		onConfirm: n
	} = e;
	return E.$$set = s => {
		"message" in s && T(0, t = s.message), "buttonLabel" in s && T(1, r =
				s.buttonLabel), "onClose" in s && T(2, R = s.onClose),
			"onConfirm" in s && T(3, n = s.onConfirm)
	}, [t, r, R, n]
}
class Ca extends ue {
	constructor(e) {
		super(), Ce(this, e, La, _a, _e, {
			message: 0,
			buttonLabel: 1,
			onClose: 2,
			onConfirm: 3
		})
	}
}

function nR(E, e, T) {
	const t = E.slice();
	return t[10] = e[T].name, t[11] = e[T].description, t[12] = e[T].example, t
}

function AR(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _;
	return o = Sn(E[7][0]), {
		c() {
			e = f("div"), T = f("div"), t = f("input"), r = $(), R = f(
					"label"), n = f("span"), n.textContent = `${E[10]}`, s =
				$(), S = f("span"), S.textContent = `${E[11]}`, A = $(), a(
					t, "id", "hs-radio-" + E[10]), t.__value = E[10], Ye(t,
					t.__value), a(t, "name", "hs-radio-with-description"),
				a(t, "type", "radio"), a(t, "class",
					"border-gray-200 rounded-full text-blue-600 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:checked:bg-blue-500 dark:checked:border-blue-500 dark:focus:ring-offset-gray-800"
				), a(t, "aria-describedby", "hs-radio-delete-description"),
				a(T, "class", "flex items-center h-5 mt-1"), a(n, "class",
					"block text-sm font-semibold text-gray-800 dark:text-gray-300"
				), a(S, "id", "hs-radio-ddl-description"), a(S, "class",
					"block text-sm text-gray-600 dark:text-gray-500"), a(R,
					"for", "hs-radio-" + E[10]), a(R, "class", "ml-3"), a(e,
					"class", "relative flex items-start"), o.p(t)
		},
		m(c, P) {
			V(c, e, P), l(e, T), l(T, t), t.checked = t.__value === E[0], l(
					e, r), l(e, R), l(R, n), l(R, s), l(R, S), l(e, A), i ||
				(_ = Ne(t, "change", E[6]), i = !0)
		},
		p(c, P) {
			P & 1 && (t.checked = t.__value === c[0])
		},
		d(c) {
			c && Y(e), o.r(), i = !1, _()
		}
	}
}

function ua(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _, c, P, p, C, L, I, u, H, b, M, O, N,
		D, B = De(E[3]),
		h = [];
	for (let G = 0; G < B.length; G += 1) h[G] = AR(nR(E, B, G));
	return {
		c() {
			var G;
			e = f("div"), T = f("div"), t = f("div"), r = f("div"), R = f("h2"),
				R.textContent = "Add Training Data", n = $(), s = f("button"),
				s.innerHTML =
				'<span class="sr-only">Close</span> <svg class="w-3.5 h-3.5" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.258206 1.00652C0.351976 0.912791 0.479126 0.860131 0.611706 0.860131C0.744296 0.860131 0.871447 0.912791 0.965207 1.00652L3.61171 3.65302L6.25822 1.00652C6.30432 0.958771 6.35952 0.920671 6.42052 0.894471C6.48152 0.868271 6.54712 0.854471 6.61352 0.853901C6.67992 0.853321 6.74572 0.865971 6.80722 0.891111C6.86862 0.916251 6.92442 0.953381 6.97142 1.00032C7.01832 1.04727 7.05552 1.1031 7.08062 1.16454C7.10572 1.22599 7.11842 1.29183 7.11782 1.35822C7.11722 1.42461 7.10342 1.49022 7.07722 1.55122C7.05102 1.61222 7.01292 1.6674 6.96522 1.71352L4.31871 4.36002L6.96522 7.00648C7.05632 7.10078 7.10672 7.22708 7.10552 7.35818C7.10442 7.48928 7.05182 7.61468 6.95912 7.70738C6.86642 7.80018 6.74102 7.85268 6.60992 7.85388C6.47882 7.85498 6.35252 7.80458 6.25822 7.71348L3.61171 5.06702L0.965207 7.71348C0.870907 7.80458 0.744606 7.85498 0.613506 7.85388C0.482406 7.85268 0.357007 7.80018 0.264297 7.70738C0.171597 7.61468 0.119017 7.48928 0.117877 7.35818C0.116737 7.22708 0.167126 7.10078 0.258206 7.00648L2.90471 4.36002L0.258206 1.71352C0.164476 1.61976 0.111816 1.4926 0.111816 1.36002C0.111816 1.22744 0.164476 1.10028 0.258206 1.00652Z" fill="currentColor"></path></svg>',
				S = $(), A = f("span"), A.textContent = "Training Data Type", o =
				$(), i = f("div");
			for (let F = 0; F < h.length; F += 1) h[F].c();
			_ = $(), c = f("div"), P = f("label"), p = te("Your "), C = te(E[0]),
				L = $(), I = f("div"), u = f("textarea"), b = $(), M = f("div"),
				O = f("button"), O.textContent = "Save", a(R, "class",
					"text-xl text-gray-800 font-bold sm:text-3xl dark:text-white"
				), a(s, "type", "button"), a(s, "class",
					"hs-dropdown-toggle inline-flex flex-shrink-0 justify-center items-center h-8 w-8 rounded-md text-gray-500 hover:text-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-offset-2 focus:ring-offset-white transition-all text-sm dark:focus:ring-gray-700 dark:focus:ring-offset-gray-800"
				), a(s, "data-hs-overlay", "#hs-vertically-centered-modal"), a(
					r, "class",
					"flex justify-between items-center py-3 px-4 border-b dark:border-gray-700 mb-2"
				), a(A, "class",
					"block mb-2 text-sm font-medium dark:text-white"), a(i,
					"class", "grid space-y-3 mb-1"), a(P, "for",
					"hs-feedback-post-comment-textarea-1"), a(P, "class",
					"block mt-2 mb-2 text-sm font-medium dark:text-white"), a(u,
					"id", "hs-feedback-post-comment-textarea-1"), a(u, "name",
					"hs-feedback-post-comment-textarea-1"), a(u, "rows", "3"),
				a(u, "class",
					"py-3 px-4 block w-full border border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 sm:p-4 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400"
				), a(u, "placeholder", H = ((G = E[3].find(E[8])) == null ?
					void 0 : G.example) ? ? "No example available"), a(I,
					"class", "mt-1"), a(c, "class",
					"mt-2 border-t dark:border-gray-700"), a(O, "class",
					"py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border border-transparent font-semibold bg-blue-500 text-white hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all dark:focus:ring-offset-gray-800"
				), a(M, "class", "mt-6 grid"), a(t, "class",
					"mt-5 p-4 relative z-10 bg-white border rounded-xl sm:mt-10 md:p-10 dark:bg-gray-800 dark:border-gray-700"
				), a(T, "class", "mx-auto max-w-2xl"), a(e, "class",
					"max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto"
				)
		},
		m(G, F) {
			V(G, e, F), l(e, T), l(T, t), l(t, r), l(r, R), l(r, n), l(r, s), l(
				t, S), l(t, A), l(t, o), l(t, i);
			for (let W = 0; W < h.length; W += 1) h[W] && h[W].m(i, null);
			l(t, _), l(t, c), l(c, P), l(P, p), l(P, C), l(c, L), l(c, I), l(I,
				u), Ye(u, E[2]), l(t, b), l(t, M), l(M, O), N || (D = [Ne(s,
				"click",
				function() {
					zE(E[1]) && E[1].apply(this, arguments)
				}), Ne(u, "input", E[9]), Ne(O, "click", E[4])], N = !0)
		},
		p(G, [F]) {
			var W;
			if (E = G, F & 9) {
				B = De(E[3]);
				let x;
				for (x = 0; x < B.length; x += 1) {
					const J = nR(E, B, x);
					h[x] ? h[x].p(J, F) : (h[x] = AR(J), h[x].c(), h[x].m(i,
						null))
				}
				for (; x < h.length; x += 1) h[x].d(1);
				h.length = B.length
			}
			F & 1 && Le(C, E[0]), F & 1 && H !== (H = ((W = E[3].find(E[8])) ==
				null ? void 0 : W.example) ? ? "No example available") && a(
				u, "placeholder", H), F & 4 && Ye(u, E[2])
		},
		i: j,
		o: j,
		d(G) {
			G && Y(e), nE(h, G), N = !1, NE(D)
		}
	}
}

function ca(E, e, T) {
	let {
		onDismiss: t
	} = e, {
		onTrain: r
	} = e, {
		selectedTrainingDataType: R = "SQL"
	} = e, n = [{
		name: "DDL",
		description: "These are the CREATE TABLE statements that define your database structure.",
		example: "CREATE TABLE table_name (column_1 datatype, column_2 datatype, column_3 datatype);"
	}, {
		name: "Documentation",
		description: "This can be any text-based documentation. Keep the chunks small and focused on a single topic.",
		example: "Our definition of ABC is XYZ."
	}, {
		name: "SQL",
		description: "This can be any SQL statement that works. The more the merrier.",
		example: "SELECT column_1, column_2 FROM table_name;"
	}, {
		name: "Question",
		description: "This can be any natural language.",
		example: "排名前10的作家都有哪些？"
	}], s = "";
	const S = () => {
			r(s, R.toLowerCase())
		},
		A = [
			[]
		];

	function o() {
		R = this.__value, T(0, R)
	}
	const i = c => c.name === R;

	function _() {
		s = this.value, T(2, s)
	}
	return E.$$set = c => {
		"onDismiss" in c && T(1, t = c.onDismiss), "onTrain" in c && T(5, r =
			c.onTrain), "selectedTrainingDataType" in c && T(0, R = c.selectedTrainingDataType)
	}, [R, t, s, n, S, r, o, A, i, _]
}
class fa extends ue {
	constructor(e) {
		super(), Ce(this, e, ca, ua, _e, {
			onDismiss: 1,
			onTrain: 5,
			selectedTrainingDataType: 0
		})
	}
}

function sR(E, e, T) {
	const t = E.slice();
	return t[21] = e[T], t
}

function SR(E, e, T) {
	const t = E.slice();
	return t[24] = e[T], t
}

function oR(E, e, T) {
	const t = E.slice();
	return t[24] = e[T], t
}

function iR(E) {
	let e, T;
	return e = new fa({
		props: {
			onDismiss: E[13],
			onTrain: E[0]
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 1 && (R.onTrain = t[0]), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Pa(E) {
	let e;
	return {
		c() {
			e = te("Action")
		},
		m(T, t) {
			V(T, e, t)
		},
		p: j,
		d(T) {
			T && Y(e)
		}
	}
}

function Da(E) {
	let e = E[24] + "",
		T;
	return {
		c() {
			T = te(e)
		},
		m(t, r) {
			V(t, T, r)
		},
		p: j,
		d(t) {
			t && Y(T)
		}
	}
}

function aR(E) {
	let e, T, t, r;

	function R(S, A) {
		return S[24] != "id" ? Da : Pa
	}
	let s = R(E)(E);
	return {
		c() {
			e = f("th"), T = f("div"), t = f("span"), s.c(), r = $(), a(t,
				"class",
				"text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200"
			), a(T, "class", "flex items-center gap-x-2"), a(e, "scope",
				"col"), a(e, "class", "px-6 py-3 text-left")
		},
		m(S, A) {
			V(S, e, A), l(e, T), l(T, t), s.m(t, null), l(e, r)
		},
		p(S, A) {
			s.p(S, A)
		},
		d(S) {
			S && Y(e), s.d()
		}
	}
}

function da(E) {
	let e, T, t;

	function r() {
		return E[18](E[21], E[24])
	}
	return {
		c() {
			e = f("button"), e.textContent = "Delete", a(e, "type", "button"),
				a(e, "class",
					"py-2 px-3 inline-flex justify-center items-center gap-2 rounded-md border-2 border-red-200 font-semibold text-red-500 hover:text-white hover:bg-red-500 hover:border-red-500 focus:outline-none focus:ring-2 focus:ring-red-200 focus:ring-offset-2 transition-all text-sm dark:focus:ring-offset-gray-800"
				)
		},
		m(R, n) {
			V(R, e, n), T || (t = Ne(e, "click", r), T = !0)
		},
		p(R, n) {
			E = R
		},
		d(R) {
			R && Y(e), T = !1, t()
		}
	}
}

function pa(E) {
	let e, T = E[21][E[24]] + "",
		t;
	return {
		c() {
			e = f("span"), t = te(T), a(e, "class",
				"text-gray-800 dark:text-gray-200")
		},
		m(r, R) {
			V(r, e, R), l(e, t)
		},
		p(r, R) {
			R & 16 && T !== (T = r[21][r[24]] + "") && Le(t, T)
		},
		d(r) {
			r && Y(e)
		}
	}
}

function IR(E) {
	let e, T;

	function t(n, s) {
		return n[24] != "id" ? pa : da
	}
	let R = t(E)(E);
	return {
		c() {
			e = f("td"), T = f("div"), R.c(), a(T, "class", "px-6 py-3"), a(e,
				"class", "h-px w-px ")
		},
		m(n, s) {
			V(n, e, s), l(e, T), R.m(T, null)
		},
		p(n, s) {
			R.p(n, s)
		},
		d(n) {
			n && Y(e), R.d()
		}
	}
}

function NR(E) {
	let e, T, t = De(E[8]),
		r = [];
	for (let R = 0; R < t.length; R += 1) r[R] = IR(SR(E, t, R));
	return {
		c() {
			e = f("tr");
			for (let R = 0; R < r.length; R += 1) r[R].c();
			T = $()
		},
		m(R, n) {
			V(R, e, n);
			for (let s = 0; s < r.length; s += 1) r[s] && r[s].m(e, null);
			l(e, T)
		},
		p(R, n) {
			if (n & 304) {
				t = De(R[8]);
				let s;
				for (s = 0; s < t.length; s += 1) {
					const S = SR(R, t, s);
					r[s] ? r[s].p(S, n) : (r[s] = IR(S), r[s].c(), r[s].m(e, T))
				}
				for (; s < r.length; s += 1) r[s].d(1);
				r.length = t.length
			}
		},
		d(R) {
			R && Y(e), nE(r, R)
		}
	}
}

function lR(E) {
	let e, T;
	return e = new Ca({
		props: {
			message: "Are you sure you want to delete this?",
			buttonLabel: "Delete",
			onClose: E[19],
			onConfirm: E[20]
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 32 && (R.onClose = t[19]), r & 34 && (R.onConfirm = t[20]),
				e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Ma(E) {
	let e, T, t, r, R, n, s, S, A, o, i, _, c, P, p, C, L, I, u, H, b, M, O, N,
		D, B, h, G = E[2] + 1 + "",
		F, W, x = Math.min(E[3], E[7].length) + "",
		J, oe, z, Oe, Ue, ye, TE, dE, me, fE, rE, pE, Tt, rt, Ve = E[6] && iR(E),
		ME = De(E[8]),
		$e = [];
	for (let Te = 0; Te < ME.length; Te += 1) $e[Te] = aR(oR(E, ME, Te));
	let ze = De(E[4]),
		ve = [];
	for (let Te = 0; Te < ze.length; Te += 1) ve[Te] = NR(sR(E, ze, Te));
	let Fe = E[5] != null && lR(E);
	return {
		c() {
			Ve && Ve.c(), e = $(), T = f("div"), t = f("div"), r = f("div"), R =
				f("div"), n = f("div"), s = f("div"), S = f("div"), S.innerHTML =
				'<h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200">Training Data</h2> <p class="text-sm text-gray-600 dark:text-gray-400">Add or remove training data. Good training data is the key to accuracy.</p>',
				A = $(), o = f("div"), i = f("div"), _ = f("button"), _.textContent =
				"View all", c = $(), P = f("button"), P.innerHTML =
				`<svg class="w-3 h-3" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2.63452 7.50001L13.6345 7.5M8.13452 13V2" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path></svg>
                    Add training data`,
				p = $(), C = f("table"), L = f("thead"), I = f("tr");
			for (let Te = 0; Te < $e.length; Te += 1) $e[Te].c();
			u = $(), H = f("tbody");
			for (let Te = 0; Te < ve.length; Te += 1) ve[Te].c();
			b = $(), M = f("div"), O = f("div"), N = f("p"), N.textContent =
				"Showing:", D = $(), B = f("div"), h = f("span"), F = te(G), W =
				te(" - "), J = te(x), oe = $(), z = f("p"), z.textContent =
				`of ${E[7].length}`, Oe = $(), Ue = f("div"), ye = f("div"), TE =
				f("button"), TE.innerHTML =
				`<svg class="w-3 h-3" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"></path></svg>
                    Prev`,
				dE = $(), me = f("button"), me.innerHTML =
				`Next
                    <svg class="w-3 h-3" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"></path></svg>`,
				fE = $(), Fe && Fe.c(), rE = je(), a(_, "class",
					"py-2 px-3 inline-flex justify-center items-center gap-2 rounded-md border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 transition-all text-sm dark:bg-slate-900 dark:hover:bg-slate-800 dark:border-gray-700 dark:text-gray-400 dark:hover:text-white dark:focus:ring-offset-gray-800"
				), a(P, "class",
					"py-2 px-3 inline-flex justify-center items-center gap-2 rounded-md border border-transparent font-semibold bg-blue-500 text-white hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all text-sm dark:focus:ring-offset-gray-800"
				), a(i, "class", "inline-flex gap-x-2"), a(s, "class",
					"px-6 py-4 grid gap-3 md:flex md:justify-between md:items-center border-b border-gray-200 dark:border-gray-700"
				), a(L, "class", "bg-gray-50 dark:bg-slate-800"), a(H, "class",
					"divide-y divide-gray-200 dark:divide-gray-700"), a(C,
					"class",
					"min-w-full divide-y divide-gray-200 dark:divide-gray-700"),
				a(N, "class", "text-sm text-gray-600 dark:text-gray-400"), a(h,
					"class",
					"py-2 px-3 pr-9 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
				), a(B, "class", "max-w-sm space-y-3"), a(z, "class",
					"text-sm text-gray-600 dark:text-gray-400"), a(O, "class",
					"inline-flex items-center gap-x-2"), a(TE, "type", "button"),
				a(TE, "class",
					"py-2 px-3 inline-flex justify-center items-center gap-2 rounded-md border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 transition-all text-sm dark:bg-slate-900 dark:hover:bg-slate-800 dark:border-gray-700 dark:text-gray-400 dark:hover:text-white dark:focus:ring-offset-gray-800"
				), a(me, "type", "button"), a(me, "class",
					"py-2 px-3 inline-flex justify-center items-center gap-2 rounded-md border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 transition-all text-sm dark:bg-slate-900 dark:hover:bg-slate-800 dark:border-gray-700 dark:text-gray-400 dark:hover:text-white dark:focus:ring-offset-gray-800"
				), a(ye, "class", "inline-flex gap-x-2"), a(M, "class",
					"px-6 py-4 grid gap-3 md:flex md:justify-between md:items-center border-t border-gray-200 dark:border-gray-700"
				), a(n, "class",
					"bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden dark:bg-slate-900 dark:border-gray-700"
				), a(R, "class", "p-1.5 min-w-full inline-block align-middle"),
				a(r, "class", "-m-1.5 overflow-x-auto"), a(t, "class",
					"flex flex-col"), a(T, "class",
					"max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto"
				)
		},
		m(Te, Xe) {
			Ve && Ve.m(Te, Xe), V(Te, e, Xe), V(Te, T, Xe), l(T, t), l(t, r), l(
					r, R), l(R, n), l(n, s), l(s, S), l(s, A), l(s, o), l(o, i),
				l(i, _), l(i, c), l(i, P), l(n, p), l(n, C), l(C, L), l(L, I);
			for (let se = 0; se < $e.length; se += 1) $e[se] && $e[se].m(I,
				null);
			l(C, u), l(C, H);
			for (let se = 0; se < ve.length; se += 1) ve[se] && ve[se].m(H,
				null);
			l(n, b), l(n, M), l(M, O), l(O, N), l(O, D), l(O, B), l(B, h), l(h,
					F), l(h, W), l(h, J), l(O, oe), l(O, z), l(M, Oe), l(M, Ue),
				l(Ue, ye), l(ye, TE), l(ye, dE), l(ye, me), V(Te, fE, Xe), Fe &&
				Fe.m(Te, Xe), V(Te, rE, Xe), pE = !0, Tt || (rt = [Ne(_,
					"click", E[11]), Ne(P, "click", E[12]), Ne(TE,
					"click", E[9]), Ne(me, "click", E[10])], Tt = !0)
		},
		p(Te, [Xe]) {
			if (Te[6] ? Ve ? (Ve.p(Te, Xe), Xe & 64 && m(Ve, 1)) : (Ve = iR(Te),
				Ve.c(), m(Ve, 1), Ve.m(e.parentNode, e)) : Ve && (Ge(), y(
				Ve, 1, 1, () => {
					Ve = null
				}), ge()), Xe & 256) {
				ME = De(Te[8]);
				let se;
				for (se = 0; se < ME.length; se += 1) {
					const gE = oR(Te, ME, se);
					$e[se] ? $e[se].p(gE, Xe) : ($e[se] = aR(gE), $e[se].c(),
						$e[se].m(I, null))
				}
				for (; se < $e.length; se += 1) $e[se].d(1);
				$e.length = ME.length
			}
			if (Xe & 304) {
				ze = De(Te[4]);
				let se;
				for (se = 0; se < ze.length; se += 1) {
					const gE = sR(Te, ze, se);
					ve[se] ? ve[se].p(gE, Xe) : (ve[se] = NR(gE), ve[se].c(),
						ve[se].m(H, null))
				}
				for (; se < ve.length; se += 1) ve[se].d(1);
				ve.length = ze.length
			}(!pE || Xe & 4) && G !== (G = Te[2] + 1 + "") && Le(F, G), (!pE ||
					Xe & 8) && x !== (x = Math.min(Te[3], Te[7].length) + "") &&
				Le(J, x), Te[5] != null ? Fe ? (Fe.p(Te, Xe), Xe & 32 && m(Fe,
					1)) : (Fe = lR(Te), Fe.c(), m(Fe, 1), Fe.m(rE.parentNode,
					rE)) : Fe && (Ge(), y(Fe, 1, 1, () => {
					Fe = null
				}), ge())
		},
		i(Te) {
			pE || (m(Ve), m(Fe), pE = !0)
		},
		o(Te) {
			y(Ve), y(Fe), pE = !1
		},
		d(Te) {
			Te && (Y(e), Y(T), Y(fE), Y(rE)), Ve && Ve.d(Te), nE($e, Te), nE(ve,
				Te), Fe && Fe.d(Te), Tt = !1, NE(rt)
		}
	}
}

function Ua(E, e, T) {
	let {
		df: t
	} = e, {
		onTrain: r
	} = e, {
		removeTrainingData: R
	} = e, n = JSON.parse(t), s = n.length > 0 ? Object.keys(n[0]) : [], S = 10,
		A = 1, o = Math.ceil(n.length / S), i = (A - 1) * S, _ = A * S, c = n.slice(
			i, _);
	const P = () => {
			A > 1 && T(16, A--, A)
		},
		p = () => {
			A < o && T(16, A++, A)
		},
		C = () => {
			T(16, A = 1), T(15, S = n.length)
		};
	let L = null,
		I = !1;
	const u = () => {
			T(6, I = !0)
		},
		H = () => {
			T(6, I = !1)
		},
		b = (N, D) => {
			T(5, L = N[D])
		},
		M = () => {
			T(5, L = null)
		},
		O = () => {
			L && R(L)
		};
	return E.$$set = N => {
		"df" in N && T(14, t = N.df), "onTrain" in N && T(0, r = N.onTrain),
			"removeTrainingData" in N && T(1, R = N.removeTrainingData)
	}, E.$$.update = () => {
		E.$$.dirty & 98304 && T(2, i = (A - 1) * S), E.$$.dirty & 98304 &&
			T(3, _ = A * S), E.$$.dirty & 12 && T(4, c = n.slice(i, _)), E.$$
			.dirty & 32768 && T(17, o = Math.ceil(n.length / S)), E.$$.dirty &
			196608 && console.log(A, o)
	}, [r, R, i, _, c, L, I, n, s, P, p, C, u, H, t, S, A, o, b, M, O]
}
class ma extends ue {
	constructor(e) {
		super(), Ce(this, e, Ua, Ma, _e, {
			df: 14,
			onTrain: 0,
			removeTrainingData: 1
		})
	}
}

function ha(E) {
	let e;
	return {
		c() {
			e = f("div"), e.innerHTML =
				'<div class="flex flex-auto flex-col justify-center items-center p-4 md:p-5"><div class="flex justify-center"><div class="animate-spin inline-block w-6 h-6 border-[3px] border-current border-t-transparent text-blue-600 rounded-full" role="status" aria-label="loading"><span class="sr-only">Loading...</span></div></div></div>',
				a(e, "class",
					"min-h-[15rem] flex flex-col bg-white border shadow-sm rounded-xl dark:bg-gray-800 dark:border-gray-700 dark:shadow-slate-700/[.7]"
				)
		},
		m(T, t) {
			V(T, e, t)
		},
		p: j,
		i: j,
		o: j,
		d(T) {
			T && Y(e)
		}
	}
}

function Ga(E) {
	let e, T, t, r;
	const R = [Ha, ga],
		n = [];

	function s(S, A) {
		return S[0].type === "df" ? 0 : S[0].type === "error" ? 1 : -1
	}
	return ~(e = s(E)) && (T = n[e] = R[e](E)), {
		c() {
			T && T.c(), t = je()
		},
		m(S, A) {
			~e && n[e].m(S, A), V(S, t, A), r = !0
		},
		p(S, A) {
			let o = e;
			e = s(S), e === o ? ~e && n[e].p(S, A) : (T && (Ge(), y(n[o], 1,
					1, () => {
						n[o] = null
					}), ge()), ~e ? (T = n[e], T ? T.p(S, A) : (T = n[e] =
					R[e](S), T.c()), m(T, 1), T.m(t.parentNode, t)) : T =
				null)
		},
		i(S) {
			r || (m(T), r = !0)
		},
		o(S) {
			y(T), r = !1
		},
		d(S) {
			S && Y(t), ~e && n[e].d(S)
		}
	}
}

function ga(E) {
	let e, T;
	return e = new PT({
		props: {
			message: E[0].error
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 1 && (R.message = t[0].error), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Ha(E) {
	let e, T;
	return e = new ma({
		props: {
			df: E[0].df,
			removeTrainingData: Un,
			onTrain: Hn
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 1 && (R.df = t[0].df), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function ba(E) {
	let e, T, t, r, R;
	const n = [Ga, ha],
		s = [];

	function S(A, o) {
		return A[0] !== null ? 0 : 1
	}
	return t = S(E), r = s[t] = n[t](E), {
		c() {
			e = f("div"), T = f("div"), r.c(), a(T, "class",
				"py-10 lg:py-14"), a(e, "class",
				"relative h-screen w-full lg:pl-64")
		},
		m(A, o) {
			V(A, e, o), l(e, T), s[t].m(T, null), R = !0
		},
		p(A, [o]) {
			let i = t;
			t = S(A), t === i ? s[t].p(A, o) : (Ge(), y(s[i], 1, 1, () => {
				s[i] = null
			}), ge(), r = s[t], r ? r.p(A, o) : (r = s[t] = n[t](A),
				r.c()), m(r, 1), r.m(T, null))
		},
		i(A) {
			R || (m(r), R = !0)
		},
		o(A) {
			y(r), R = !1
		},
		d(A) {
			A && Y(e), s[t].d()
		}
	}
}

function ya(E, e, T) {
	let t;
	return eE(E, gt, r => T(0, t = r)), [t]
}
class Ba extends ue {
	constructor(e) {
		super(), Ce(this, e, ya, ba, _e, {})
	}
}

function va(E) {
	let e;
	return {
		c() {
			e = f("body"), e.innerHTML =
				`<div class="max-w-[50rem] flex flex-col mx-auto size-full"><header class="mb-auto flex justify-center z-50 w-full py-4"><nav class="px-4 sm:px-6 lg:px-8" aria-label="Global"><span class="flex-none text-xl font-semibold sm:text-3xl dark:text-white">Jenasi.AI</span></nav></header> <div class="text-center py-10 px-4 sm:px-6 lg:px-8"><h1 class="block text-7xl font-bold text-gray-800 sm:text-9xl dark:text-white">No Training Data</h1> <h1 class="block text-2xl font-bold text-white">Did you read the docs?</h1> <p class="mt-3 text-gray-600 dark:text-gray-400">Oops, something went wrong.</p> <p class="text-gray-600 dark:text-gray-400">You need some training data before you can use Jenasi</p> <div class="mt-5 flex flex-col justify-center items-center gap-2 sm:flex-row sm:gap-3"><a class="w-full sm:w-auto py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="https://github.com/htmlstreamofficial/preline/tree/main/examples/html" target="_blank"><svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
            Get the source code</a> <a class="w-full sm:w-auto py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 disabled:opacity-50 disabled:pointer-events-none dark:text-blue-500 dark:hover:text-blue-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="../examples.html"><svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"></path></svg>
            Back to examples</a></div></div> <footer class="mt-auto text-center py-5"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><p class="text-sm text-gray-500">© All Rights Reserved. 2022.</p></div></footer></div>`,
				a(e, "class", "flex h-full")
		},
		m(T, t) {
			V(T, e, t)
		},
		p: j,
		i: j,
		o: j,
		d(T) {
			T && Y(e)
		}
	}
}
class Fa extends ue {
	constructor(e) {
		super(), Ce(this, e, null, va, _e, {})
	}
}

function Ya(E) {
	let e, T, t;
	return {
		c() {
			e = f("div"), T = f("div"), t = f("div"), a(t, "class",
				"mt-7 bg-white border border-gray-200 rounded-xl shadow-sm dark:bg-gray-800 dark:border-gray-700"
			), a(T, "class", "w-full max-w-md mx-auto p-6"), a(e, "class",
				"dark:bg-slate-900 bg-gray-100 flex h-screen items-center py-16"
			)
		},
		m(r, R) {
			V(r, e, R), l(e, T), l(T, t), t.innerHTML = E[0]
		},
		p(r, [R]) {
			R & 1 && (t.innerHTML = r[0])
		},
		i: j,
		o: j,
		d(r) {
			r && Y(e)
		}
	}
}

function Va(E, e, T) {
	let t;
	return eE(E, bt, r => T(0, t = r)), [t]
}
class Wa extends ue {
	constructor(e) {
		super(), Ce(this, e, Va, Ya, _e, {})
	}
}

function wa(E) {
	let e, T, t, r, R, n;
	return {
		c() {
			e = f("div"), T = f("div"), T.innerHTML =
				'<h3 class="text-lg font-bold text-gray-800 dark:text-white">New</h3> <p class="mt-1 text-xs font-medium uppercase text-gray-500 dark:text-neutral-500">Create a New Function</p>',
				t = $(), r = f("button"), r.innerHTML =
				`Create
    <svg class="flex-shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"></path></svg>`,
				a(r, "class",
					"mt-3 inline-flex items-center gap-x-1 text-sm font-semibold rounded-lg border border-transparent text-green-600 hover:text-green-800 disabled:opacity-50 disabled:pointer-events-none dark:text-green-500 dark:hover:text-green-400"
				), a(e, "class",
					"p-4 flex flex-col justify-between bg-white border border-t-4 border-t-green-600 shadow-sm rounded-xl dark:bg-neutral-900 dark:border-neutral-700 dark:border-t-green-500 dark:shadow-neutral-700/70"
				)
		},
		m(s, S) {
			V(s, e, S), l(e, T), l(e, t), l(e, r), R || (n = Ne(r, "click", E[0]),
				R = !0)
		},
		p: j,
		i: j,
		o: j,
		d(s) {
			s && Y(e), R = !1, n()
		}
	}
}

function $a(E) {
	return [() => {
		it()
	}]
}
class xa extends ue {
	constructor(e) {
		super(), Ce(this, e, $a, wa, _e, {})
	}
}

function _R(E, e, T) {
	const t = E.slice();
	return t[1] = e[T], t
}

function LR(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [Xa]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Xa(E) {
	let e;
	return {
		c() {
			e = te("No functions found")
		},
		m(T, t) {
			V(T, e, t)
		},
		d(T) {
			T && Y(e)
		}
	}
}

function CR(E) {
	let e, T;
	return e = new en({
		props: {
			functionTemplate: E[1]
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		p(t, r) {
			const R = {};
			r & 1 && (R.functionTemplate = t[1]), e.$set(R)
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function ka(E) {
	let e, T, t, r, R, n, s, S, A, o = E[0].length == 0 && LR(E),
		i = De(E[0]),
		_ = [];
	for (let P = 0; P < i.length; P += 1) _[P] = CR(_R(E, i, P));
	const c = P => y(_[P], 1, 1, () => {
		_[P] = null
	});
	return S = new xa({}), {
		c() {
			e = f("div"), T = f("div"), t = f("h1"), t.textContent =
				"Functions", r = $(), o && o.c(), R = $(), n = f("div");
			for (let P = 0; P < _.length; P += 1) _[P].c();
			s = $(), K(S.$$.fragment), a(t, "class",
				"text-3xl font-bold text-gray-800 sm:text-4xl dark:text-white text-center"
			), a(n, "class", "grid grid-cols-4 gap-4 p-4"), a(T,
				"class", "py-10 lg:py-14"), a(e, "class",
				"relative h-screen w-full lg:pl-64")
		},
		m(P, p) {
			V(P, e, p), l(e, T), l(T, t), l(T, r), o && o.m(T, null), l(T,
				R), l(T, n);
			for (let C = 0; C < _.length; C += 1) _[C] && _[C].m(n, null);
			l(n, s), X(S, n, null), A = !0
		},
		p(P, [p]) {
			if (P[0].length == 0 ? o ? p & 1 && m(o, 1) : (o = LR(P), o.c(),
				m(o, 1), o.m(T, R)) : o && (Ge(), y(o, 1, 1, () => {
				o = null
			}), ge()), p & 1) {
				i = De(P[0]);
				let C;
				for (C = 0; C < i.length; C += 1) {
					const L = _R(P, i, C);
					_[C] ? (_[C].p(L, p), m(_[C], 1)) : (_[C] = CR(L), _[C]
						.c(), m(_[C], 1), _[C].m(n, s))
				}
				for (Ge(), C = i.length; C < _.length; C += 1) c(C);
				ge()
			}
		},
		i(P) {
			if (!A) {
				m(o);
				for (let p = 0; p < i.length; p += 1) m(_[p]);
				m(S.$$.fragment, P), A = !0
			}
		},
		o(P) {
			y(o), _ = _.filter(Boolean);
			for (let p = 0; p < _.length; p += 1) y(_[p]);
			y(S.$$.fragment, P), A = !1
		},
		d(P) {
			P && Y(e), o && o.d(), nE(_, P), k(S)
		}
	}
}

function Ka(E, e, T) {
	let t;
	return eE(E, MR, r => T(0, t = r)), [t]
}
class Ja extends ue {
	constructor(e) {
		super(), Ce(this, e, Ka, ka, _e, {})
	}
}

function uR(E) {
	let e, T;
	return e = new Kn({}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function qa(E) {
	let e, T;
	return e = new aE({
		props: {
			$$slots: {
				default: [EI]
			},
			$$scope: {
				ctx: E
			}
		}
	}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Qa(E) {
	let e, T;
	return e = new Ja({}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function Za(E) {
	let e, T;
	return e = new Wa({}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function ja(E) {
	let e, T;
	return e = new Fa({}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function za(E) {
	let e, T;
	return e = new Ba({}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function eI(E) {
	let e, T;
	return e = new la({}), {
		c() {
			K(e.$$.fragment)
		},
		m(t, r) {
			X(e, t, r), T = !0
		},
		i(t) {
			T || (m(e.$$.fragment, t), T = !0)
		},
		o(t) {
			y(e.$$.fragment, t), T = !1
		},
		d(t) {
			k(e, t)
		}
	}
}

function EI(E) {
	let e;
	return {
		c() {
			e = te("Unknown page")
		},
		m(T, t) {
			V(T, e, t)
		},
		d(T) {
			T && Y(e)
		}
	}
}

function tI(E) {
	let e, T, t, r, R, n = E[0] !== "login" && uR();
	const s = [eI, za, ja, Za, Qa, qa],
		S = [];

	function A(o, i) {
		return o[0] === "chat" ? 0 : o[0] === "training-data" ? 1 : o[0] ===
			"no-training-data" ? 2 : o[0] === "login" ? 3 : o[0] ===
			"functions" ? 4 : 5
	}
	return t = A(E), r = S[t] = s[t](E), {
		c() {
			e = f("main"), n && n.c(), T = $(), r.c()
		},
		m(o, i) {
			V(o, e, i), n && n.m(e, null), l(e, T), S[t].m(e, null), R = !0
		},
		p(o, [i]) {
			o[0] !== "login" ? n ? i & 1 && m(n, 1) : (n = uR(), n.c(), m(n,
				1), n.m(e, T)) : n && (Ge(), y(n, 1, 1, () => {
				n = null
			}), ge());
			let _ = t;
			t = A(o), t !== _ && (Ge(), y(S[_], 1, 1, () => {
				S[_] = null
			}), ge(), r = S[t], r || (r = S[t] = s[t](o), r.c()), m(
				r, 1), r.m(e, null))
		},
		i(o) {
			R || (m(n), m(r), R = !0)
		},
		o(o) {
			y(n), y(r), R = !1
		},
		d(o) {
			o && Y(e), n && n.d(), S[t].d()
		}
	}
}

function TI(E, e, T) {
	let t;
	return eE(E, DE, r => T(0, t = r)), DR(async () => {
		pn(), mR();
		const R = new URL(window.location.href)
			.hash.slice(1);
		R === "training-data" ? hR() : R === "functions" ? cT() :
			it()
	}), [t]
}
class rI extends ue {
	constructor(e) {
		super(), Ce(this, e, TI, tI, _e, {})
	}
}
new rI({
	target: document.getElementById("app")
});

'''
