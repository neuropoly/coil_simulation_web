__author__ = 'willispinaud'


def email_template(confirm_url):
    template = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style type="text/css">
.font-sans-serif {
  font-family: sans-serif;
}
.font-avenir {
  font-family: Avenir, sans-serif;
}
.mso .font-avenir {
  font-family: sans-serif !important;
}
.font-lato {
  font-family: Lato, Tahoma, sans-serif;
}
.mso .font-lato {
  font-family: Tahoma, sans-serif !important;
}
.font-cabin {
  font-family: Cabin, Avenir, sans-serif;
}
.mso .font-cabin {
  font-family: sans-serif !important;
}
.font-open-Sans {
  font-family: "Open Sans", sans-serif;
}
.mso .font-open-Sans {
  font-family: sans-serif !important;
}
.font-roboto {
  font-family: Roboto, Tahoma, sans-serif;
}
.mso .font-roboto {
  font-family: Tahoma, sans-serif !important;
}
.font-ubuntu {
  font-family: Ubuntu, sans-serif;
}
.mso .font-ubuntu {
  font-family: sans-serif !important;
}
.font-pt-sans {
  font-family: "PT Sans", "Trebuchet MS", sans-serif;
}
.mso .font-pt-sans {
  font-family: "Trebuchet MS", sans-serif !important;
}
.font-georgia {
  font-family: Georgia, serif;
}
.font-merriweather {
  font-family: Merriweather, Georgia, serif;
}
.mso .font-merriweather {
  font-family: Georgia, serif !important;
}
.font-bitter {
  font-family: Bitter, Georgia, serif;
}
.mso .font-bitter {
  font-family: Georgia, serif !important;
}
.font-pt-serif {
  font-family: "PT Serif", Georgia, serif;
}
.mso .font-pt-serif {
  font-family: Georgia, serif !important;
}
.font-pompiere {
  font-family: Pompiere, "Trebuchet MS", sans-serif;
}
.mso .font-pompiere {
  font-family: "Trebuchet MS", sans-serif !important;
}
.font-roboto-slab {
  font-family: "Roboto Slab", Georgia, serif;
}
.mso .font-roboto-slab {
  font-family: Georgia, serif !important;
}
@media only screen and (max-width: 620px) {
  .wrapper .column .size-8 {
    font-size: 8px !important;
    line-height: 14px !important;
  }
  .wrapper .column .size-9 {
    font-size: 9px !important;
    line-height: 16px !important;
  }
  .wrapper .column .size-10 {
    font-size: 10px !important;
    line-height: 18px !important;
  }
  .wrapper .column .size-11 {
    font-size: 11px !important;
    line-height: 19px !important;
  }
  .wrapper .column .size-12 {
    font-size: 12px !important;
    line-height: 19px !important;
  }
  .wrapper .column .size-13 {
    font-size: 13px !important;
    line-height: 21px !important;
  }
  .wrapper .column .size-14 {
    font-size: 14px !important;
    line-height: 21px !important;
  }
  .wrapper .column .size-15 {
    font-size: 15px !important;
    line-height: 23px !important;
  }
  .wrapper .column .size-16 {
    font-size: 16px !important;
    line-height: 24px !important;
  }
  .wrapper .column .size-17 {
    font-size: 17px !important;
    line-height: 26px !important;
  }
  .wrapper .column .size-18 {
    font-size: 17px !important;
    line-height: 26px !important;
  }
  .wrapper .column .size-20 {
    font-size: 17px !important;
    line-height: 26px !important;
  }
  .wrapper .column .size-22 {
    font-size: 18px !important;
    line-height: 26px !important;
  }
  .wrapper .column .size-24 {
    font-size: 20px !important;
    line-height: 28px !important;
  }
  .wrapper .column .size-26 {
    font-size: 22px !important;
    line-height: 31px !important;
  }
  .wrapper .column .size-28 {
    font-size: 24px !important;
    line-height: 32px !important;
  }
  .wrapper .column .size-30 {
    font-size: 26px !important;
    line-height: 34px !important;
  }
  .wrapper .column .size-32 {
    font-size: 28px !important;
    line-height: 36px !important;
  }
  .wrapper .column .size-34 {
    font-size: 30px !important;
    line-height: 38px !important;
  }
  .wrapper .column .size-36 {
    font-size: 30px !important;
    line-height: 38px !important;
  }
  .wrapper .column .size-40 {
    font-size: 32px !important;
    line-height: 40px !important;
  }
  .wrapper .column .size-44 {
    font-size: 34px !important;
    line-height: 43px !important;
  }
  .wrapper .column .size-48 {
    font-size: 36px !important;
    line-height: 43px !important;
  }
  .wrapper .column .size-56 {
    font-size: 40px !important;
    line-height: 47px !important;
  }
  .wrapper .column .size-64 {
    font-size: 44px !important;
    line-height: 50px !important;
  }
}
body {
  margin: 0;
  padding: 0;
  min-width: 100%;
}
.mso body {
  mso-line-height-rule: exactly;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td {
  padding: 0;
  vertical-align: top;
}
.spacer,
.border {
  font-size: 1px;
  line-height: 1px;
}
.spacer {
  width: 100%;
}
img {
  border: 0;
  -ms-interpolation-mode: bicubic;
}
.image {
  font-size: 12px;
  Margin-bottom: 24px;
  mso-line-height-rule: at-least;
}
.image img {
  display: block;
}
.logo {
  mso-line-height-rule: at-least;
}
.logo img {
  display: block;
}
strong {
  font-weight: bold;
}
h1,
h2,
h3,
p,
ol,
ul,
li {
  Margin-top: 0;
}
h1,
h2,
h3,
p,
ol,
ul,
blockquote,
.image {
  font-style: normal;
  font-weight: 400;
}
ol,
ul,
li {
  padding-left: 0;
}
blockquote {
  Margin-top: 0;
  Margin-right: 0;
  Margin-bottom: 0;
  padding-right: 0;
}
.column-top {
  font-size: 32px;
  line-height: 32px;
}
.column-bottom {
  font-size: 8px;
  line-height: 8px;
}
.column {
  text-align: left;
}
.contents {
  table-layout: fixed;
  width: 100%;
}
.padded {
  padding-left: 32px;
  padding-right: 32px;
  word-break: break-word;
  word-wrap: break-word;
}
.wrapper {
  display: table;
  table-layout: fixed;
  width: 100%;
  min-width: 620px;
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
}
.wrapper a {
  transition: opacity 0.2s ease-in;
}
table.wrapper {
  table-layout: fixed;
}
.one-col,
.two-col,
.three-col {
  Margin-left: auto;
  Margin-right: auto;
  width: 600px;
}
.centered {
  Margin-left: auto;
  Margin-right: auto;
}
.btn {
  Margin-bottom: 24px;
}
.btn a {
  border-radius: 3px;
  display: inline-block;
  font-size: 14px;
  font-weight: 700;
  line-height: 24px;
  padding: 13px 35px 12px 35px;
  text-align: center;
  text-decoration: none !important;
}
.btn a:hover {
  opacity: 0.8;
}
.two-col .btn {
  Margin-bottom: 23px;
}
.two-col .btn a {
  font-size: 12px;
  line-height: 22px;
  padding: 10px 28px;
}
.three-col .btn {
  Margin-bottom: 21px;
}
.three-col .btn a {
  font-size: 11px;
  line-height: 19px;
  padding: 6px 18px 5px 18px;
}
@media only screen and (max-width: 620px) {
  .btn {
    margin-bottom: 24px !important;
  }
  .btn a {
    display: block !important;
    font-size: 14px !important;
    line-height: 24px !important;
    padding: 13px 10px 12px 10px !important;
  }
}
.two-col .image {
  Margin-bottom: 23px;
}
.two-col .column-bottom {
  font-size: 9px;
  line-height: 9px;
}
.two-col .column {
  width: 300px;
}
.three-col .image {
  Margin-bottom: 21px;
}
.three-col .column-bottom {
  font-size: 11px;
  line-height: 11px;
}
.three-col .column {
  width: 200px;
}
.three-col .first .padded {
  padding-left: 32px;
  padding-right: 16px;
}
.three-col .second .padded {
  padding-left: 24px;
  padding-right: 24px;
}
.three-col .third .padded {
  padding-left: 16px;
  padding-right: 32px;
}
@media only screen and (min-width: 0) {
  .wrapper {
    text-rendering: optimizeLegibility;
  }
}
@media only screen and (max-width: 620px) {
  [class=wrapper] {
    min-width: 318px !important;
    width: 100% !important;
  }
  [class=wrapper] .one-col,
  [class=wrapper] .two-col,
  [class=wrapper] .three-col {
    width: 318px !important;
  }
  [class=wrapper] .column,
  [class=wrapper] .gutter {
    display: block;
    float: left;
    width: 318px !important;
  }
  [class=wrapper] .padded {
    padding-left: 32px !important;
    padding-right: 32px !important;
  }
  [class=wrapper] .block {
    display: block !important;
  }
  [class=wrapper] .hide {
    display: none !important;
  }
  [class=wrapper] .image {
    margin-bottom: 24px !important;
  }
  [class=wrapper] .image img {
    height: auto !important;
    width: 100% !important;
  }
}
td.border {
  width: 1px;
}
tr.border {
  background-color: #e9e9e9;
  height: 1px;
}
tr.border td {
  line-height: 1px;
}
.one-col,
.two-col,
.three-col,
.one-col-feature {
  background-color: #ffffff;
  font-size: 14px;
  table-layout: fixed;
}
.one-col,
.two-col,
.three-col,
.one-col-feature,
.preheader,
.header,
.footer {
  Margin-left: auto;
  Margin-right: auto;
}
.preheader table {
  width: 602px;
}
.preheader .title,
.preheader .webversion {
  padding-top: 10px;
  padding-bottom: 12px;
  font-size: 12px;
  line-height: 21px;
}
.preheader .title {
  text-align: left;
}
.preheader .webversion {
  text-align: right;
  width: 300px;
}
.header {
  width: 602px;
}
.header .logo {
  padding-top: 6px;
  padding-bottom: 20px;
}
.header .logo div {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 32px;
}
.header .logo div.logo-center {
  text-align: center;
}
.header .logo div.logo-center img {
  Margin-left: auto;
  Margin-right: auto;
}
.gmail {
  width: 650px;
  min-width: 650px;
}
.gmail td {
  font-size: 1px;
  line-height: 1px;
}
.wrapper h1 {
  font-size: 36px;
  line-height: 44px;
  Margin-bottom: 18px;
}
.wrapper h2 {
  font-size: 26px;
  line-height: 32px;
  Margin-bottom: 20px;
}
.wrapper h3 {
  font-size: 18px;
  line-height: 22px;
  Margin-bottom: 16px;
}
.wrapper h1 a,
.wrapper h2 a,
.wrapper h3 a {
  text-decoration: none;
}
.wrapper p,
.wrapper ol,
.wrapper ul {
  line-height: 24px;
  Margin-bottom: 24px;
}
.one-col blockquote,
.two-col blockquote,
.three-col blockquote {
  font-size: 14px;
  border-left: 2px solid #e9e9e9;
  Margin-left: 0;
  padding-left: 16px;
}
table.divider {
  width: 100%;
}
.divider .inner {
  padding-bottom: 24px;
}
.divider table {
  background-color: #e9e9e9;
  font-size: 2px;
  line-height: 2px;
  width: 60px;
}
.padded .image {
  font-size: 0;
}
.image-frame {
  border-style: solid;
  border-width: 8px;
  display: inline-block;
  font-size: 12px;
}
.one-col .column table:nth-last-child(2) td h1:last-child,
.one-col .column table:nth-last-child(2) td h2:last-child,
.one-col .column table:nth-last-child(2) td h3:last-child,
.one-col .column table:nth-last-child(2) td p:last-child,
.one-col .column table:nth-last-child(2) td ol:last-child,
.one-col .column table:nth-last-child(2) td ul:last-child {
  Margin-bottom: 24px;
}
.one-col p,
.one-col ol,
.one-col ul {
  font-size: 16px;
  line-height: 24px;
}
.one-col ol,
.one-col ul {
  Margin-left: 18px;
}
.two-col .column table:nth-last-child(2) td h1:last-child,
.two-col .column table:nth-last-child(2) td h2:last-child,
.two-col .column table:nth-last-child(2) td h3:last-child,
.two-col .column table:nth-last-child(2) td p:last-child,
.two-col .column table:nth-last-child(2) td ol:last-child,
.two-col .column table:nth-last-child(2) td ul:last-child {
  Margin-bottom: 23px;
}
.two-col .image-frame {
  border-width: 6px;
}
.two-col ol,
.two-col ul {
  Margin-left: 16px;
}
.two-col li {
  padding-left: 5px;
}
.two-col .divider .inner {
  padding-bottom: 23px;
}
.two-col blockquote {
  padding-left: 16px;
}
.three-col .column table:nth-last-child(2) td h1:last-child,
.three-col .column table:nth-last-child(2) td h2:last-child,
.three-col .column table:nth-last-child(2) td h3:last-child,
.three-col .column table:nth-last-child(2) td p:last-child,
.three-col .column table:nth-last-child(2) td ol:last-child,
.three-col .column table:nth-last-child(2) td ul:last-child {
  Margin-bottom: 21px;
}
.three-col .image-frame {
  border-width: 4px;
}
.three-col ol,
.three-col ul {
  Margin-left: 14px;
}
.three-col li {
  padding-left: 6px;
}
.three-col .divider .inner {
  padding-bottom: 21px;
}
.three-col blockquote {
  padding-left: 16px;
}
.one-col-feature {
  width: 600px;
}
@media only screen and (max-width: 620px) {
  .one-col-feature {
    width: 318px !important;
  }
}
.one-col-feature .column-top {
  font-size: 36px;
  line-height: 36px;
}
.one-col-feature .column-bottom {
  font-size: 4px;
  line-height: 4px;
}
.one-col-feature .column {
  text-align: center;
  width: 600px;
}
.one-col-feature .image {
  Margin-bottom: 32px;
}
.one-col-feature .column table:nth-last-child(2) td h1:last-child,
.one-col-feature .column table:nth-last-child(2) td h2:last-child,
.one-col-feature .column table:nth-last-child(2) td h3:last-child,
.one-col-feature .column table:nth-last-child(2) td p:last-child,
.one-col-feature .column table:nth-last-child(2) td ol:last-child,
.one-col-feature .column table:nth-last-child(2) td ul:last-child {
  Margin-bottom: 32px;
}
.one-col-feature h1,
.one-col-feature h2,
.one-col-feature h3,
.one-col-feature p {
  text-align: center;
}
.one-col-feature ol,
.one-col-feature ul {
  Margin-left: 40px;
  text-align: left;
}
.one-col-feature li {
  padding-left: 3px;
}
.one-col-feature .btn {
  Margin-bottom: 32px;
  text-align: center;
}
.one-col-feature .divider .inner {
  padding-bottom: 32px;
}
.one-col-feature blockquote {
  border-bottom: 2px solid #e9e9e9;
  border-left-color: #ffffff;
  border-left-width: 0;
  border-left-style: none;
  border-top: 2px solid #e9e9e9;
  Margin-bottom: 32px;
  Margin-left: 0;
  padding-bottom: 42px;
  padding-left: 0;
  padding-top: 42px;
}
.wrapper .one-col-feature blockquote p,
.wrapper .one-col-feature blockquote ol,
.wrapper .one-col-feature blockquote ul {
  font-size: 42px;
  line-height: 48px;
  Margin-bottom: 48px;
}
.one-col-feature blockquote p:last-child,
.one-col-feature blockquote ol:last-child,
.one-col-feature blockquote ul:last-child {
  Margin-bottom: 0 !important;
}
.wrapper h1 {
  font-weight: 700;
}
.wrapper h2 {
  font-style: italic;
  font-weight: normal;
}
.wrapper h3 {
  font-weight: normal;
}
.wrapper blockquote {
  font-style: italic;
}
.wrapper .one-col-feature h1 {
  font-weight: normal;
}
.wrapper .one-col-feature h2 {
  font-style: normal;
  font-weight: bold;
}
.wrapper .one-col-feature h3 {
  font-style: italic;
}
.preheader a,
.header a,
.footer a {
  font-weight: bold;
  text-decoration: none;
}
.footer {
  width: 602px;
}
.footer .padded {
  font-size: 12px;
  line-height: 20px;
}
.social {
  padding-top: 32px;
  padding-bottom: 22px;
}
.social img {
  display: block;
}
.social .divider {
  font-family: sans-serif;
  font-size: 10px;
  line-height: 21px;
  text-align: center;
  padding-left: 14px;
  padding-right: 14px;
}
.social .social-text {
  height: 21px;
  vertical-align: middle !important;
  font-size: 10px;
  font-weight: bold;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
.address {
  width: 250px;
}
.address .padded {
  text-align: left;
  padding-left: 0;
  padding-right: 10px;
}
.subscription {
  width: 350px;
}
.subscription .padded {
  text-align: right;
  padding-right: 0;
  padding-left: 10px;
}
.address,
.subscription {
  padding-top: 32px;
  padding-bottom: 64px;
}
.address table,
.subscription table {
  width: 100%;
}
@media only screen and (max-width: 651px) {
  .gmail {
    display: none !important;
  }
}
@media only screen and (max-width: 620px) {
  [class=wrapper] .one-col .column:last-child table:nth-last-child(2) td h1:last-child,
  [class=wrapper] .two-col .column:last-child table:nth-last-child(2) td h1:last-child,
  [class=wrapper] .three-col .column:last-child table:nth-last-child(2) td h1:last-child,
  [class=wrapper] .one-col-feature .column:last-child table:nth-last-child(2) td h1:last-child,
  [class=wrapper] .one-col .column:last-child table:nth-last-child(2) td h2:last-child,
  [class=wrapper] .two-col .column:last-child table:nth-last-child(2) td h2:last-child,
  [class=wrapper] .three-col .column:last-child table:nth-last-child(2) td h2:last-child,
  [class=wrapper] .one-col-feature .column:last-child table:nth-last-child(2) td h2:last-child,
  [class=wrapper] .one-col .column:last-child table:nth-last-child(2) td h3:last-child,
  [class=wrapper] .two-col .column:last-child table:nth-last-child(2) td h3:last-child,
  [class=wrapper] .three-col .column:last-child table:nth-last-child(2) td h3:last-child,
  [class=wrapper] .one-col-feature .column:last-child table:nth-last-child(2) td h3:last-child,
  [class=wrapper] .one-col .column:last-child table:nth-last-child(2) td p:last-child,
  [class=wrapper] .two-col .column:last-child table:nth-last-child(2) td p:last-child,
  [class=wrapper] .three-col .column:last-child table:nth-last-child(2) td p:last-child,
  [class=wrapper] .one-col-feature .column:last-child table:nth-last-child(2) td p:last-child,
  [class=wrapper] .one-col .column:last-child table:nth-last-child(2) td ol:last-child,
  [class=wrapper] .two-col .column:last-child table:nth-last-child(2) td ol:last-child,
  [class=wrapper] .three-col .column:last-child table:nth-last-child(2) td ol:last-child,
  [class=wrapper] .one-col-feature .column:last-child table:nth-last-child(2) td ol:last-child,
  [class=wrapper] .one-col .column:last-child table:nth-last-child(2) td ul:last-child,
  [class=wrapper] .two-col .column:last-child table:nth-last-child(2) td ul:last-child,
  [class=wrapper] .three-col .column:last-child table:nth-last-child(2) td ul:last-child,
  [class=wrapper] .one-col-feature .column:last-child table:nth-last-child(2) td ul:last-child {
    Margin-bottom: 24px !important;
  }
  [class=wrapper] .address,
  [class=wrapper] .subscription {
    display: block;
    float: left;
    text-align: center !important;
    width: 100% !important;
  }
  [class=wrapper] .address {
    padding-bottom: 0 !important;
  }
  [class=wrapper] .subscription {
    padding-top: 0 !important;
  }
  [class=wrapper] h1 {
    font-size: 36px !important;
    line-height: 42px !important;
    Margin-bottom: 18px !important;
  }
  [class=wrapper] h2 {
    font-size: 26px !important;
    line-height: 32px !important;
    Margin-bottom: 20px !important;
  }
  [class=wrapper] h3 {
    font-size: 18px !important;
    line-height: 22px !important;
    Margin-bottom: 16px !important;
  }
  [class=wrapper] p,
  [class=wrapper] ol,
  [class=wrapper] ul {
    font-size: 16px !important;
    line-height: 24px !important;
    Margin-bottom: 24px !important;
  }
  [class=wrapper] ol,
  [class=wrapper] ul {
    Margin-left: 18px !important;
  }
  [class=wrapper] li {
    padding-left: 2px !important;
  }
  [class=wrapper] blockquote {
    padding-left: 16px !important;
  }
  [class=wrapper] .two-col .column:nth-child(n + 3) {
    border-top: 1px solid #e9e9e9;
  }
  [class=wrapper] .column-bottom {
    font-size: 8px !important;
    line-height: 8px !important;
  }
  [class=wrapper] .first .column-bottom,
  [class=wrapper] .three-col .second .column-bottom {
    display: none;
  }
  [class=wrapper] .second .column-top,
  [class=wrapper] .third .column-top {
    display: none;
  }
  [class=wrapper] .image-frame {
    border-width: 4px !important;
  }
  [class=wrapper] .header .logo {
    padding-left: 10px !important;
    padding-right: 10px !important;
  }
  [class=wrapper] .header .logo div {
    font-size: 26px !important;
    line-height: 32px !important;
  }
  [class=wrapper] .header .logo div img {
    display: inline-block !important;
    max-width: 280px !important;
    height: auto !important;
  }
  [class=wrapper] table.border,
  [class=wrapper] .header,
  [class=wrapper] .webversion,
  [class=wrapper] .footer {
    width: 320px !important;
  }
  [class=wrapper] .preheader .webversion,
  [class=wrapper] .header .logo a {
    text-align: center !important;
  }
  [class=wrapper] .preheader table,
  [class=wrapper] .border td {
    width: 318px !important;
  }
  [class=wrapper] .border td.border {
    width: 1px !important;
  }
  [class=wrapper] .image .border td {
    width: auto !important;
  }
  [class=wrapper] .title {
    display: none;
  }
  [class=wrapper] .footer .padded {
    text-align: center !important;
  }
  [class=wrapper] .footer .subscription .padded {
    padding-top: 20px !important;
  }
  [class=wrapper] .footer .social-link {
    display: block !important;
  }
  [class=wrapper] .footer .social-link table {
    margin: 0 auto 10px !important;
  }
  [class=wrapper] .footer .divider {
    display: none !important;
  }
  [class=wrapper] .one-col-feature .btn {
    margin-bottom: 28px !important;
  }
  [class=wrapper] .one-col-feature .image {
    margin-bottom: 28px !important;
  }
  [class=wrapper] .one-col-feature .divider .inner {
    padding-bottom: 28px !important;
  }
  [class=wrapper] .one-col-feature p,
  [class=wrapper] .one-col-feature ol,
  [class=wrapper] .one-col-feature ul {
    line-height: 28px !important;
    margin-bottom: 28px !important;
  }
  [class=wrapper] .one-col-feature blockquote {
    font-size: 18px !important;
    line-height: 26px !important;
    margin-bottom: 28px !important;
    padding-bottom: 26px !important;
    padding-left: 0 !important;
    padding-top: 26px !important;
  }
  [class=wrapper] .one-col-feature blockquote p,
  [class=wrapper] .one-col-feature blockquote ol,
  [class=wrapper] .one-col-feature blockquote ul {
    font-size: 26px !important;
    line-height: 32px !important;
  }
  [class=wrapper] .one-col-feature blockquote p:last-child,
  [class=wrapper] .one-col-feature blockquote ol:last-child,
  [class=wrapper] .one-col-feature blockquote ul:last-child {
    margin-bottom: 0 !important;
  }
  [class=wrapper] .one-col-feature .column table:last-of-type h1:last-child,
  [class=wrapper] .one-col-feature .column table:last-of-type h2:last-child,
  [class=wrapper] .one-col-feature .column table:last-of-type h3:last-child {
    margin-bottom: 28px !important;
  }
}
@media only screen and (max-width: 320px) {
  [class=wrapper] td.border {
    display: none;
  }
  [class=wrapper] table.border,
  [class=wrapper] .header,
  [class=wrapper] .webversion,
  [class=wrapper] .footer {
    width: 318px !important;
  }
}
</style>
  <style type="text/css">
.wrapper h1{}.wrapper h1{font-family:Avenir,sans-serif}.mso .wrapper h1{font-family:sans-serif !important}.wrapper h2{}.wrapper h2{font-family:Georgia,serif}.wrapper h3{}.wrapper h3{font-family:Georgia,serif}.wrapper p,.wrapper ol,.wrapper ul,.wrapper .image{}.wrapper p,.wrapper ol,.wrapper ul,.wrapper .image{font-family:Georgia,serif}.wrapper .btn a{}.wrapper .btn a{font-family:Georgia,serif}.logo div{}.logo div{font-family:Avenir,sans-serif}.mso .logo div{font-family:sans-serif !important}.title,.webversion,.facebook,.twitter,.forward,.permission,.left,.right,.social,.address,.campaign{}.title,.webversion,.facebook,.twitter,.forward,.permission,.left,.right,.social,.address,.campaign{font-family:Georgia,serif}body,.wrapper,.emb-editor-canvas{background-color:#fbfbfb}.border{background-color:#e9e9e9}.social{border-bottom:1px solid #e9e9e9}.wrapper h1{color:#565656}.wrapper
h2{color:#555}.wrapper h3{color:#555}.wrapper p,.wrapper ol,.wrapper ul{color:#565656}.wrapper .image{color:#565656}.wrapper a{color:#41637e}.wrapper a:hover{color:#30495c !important}.wrapper .one-col-feature p a:hover,.wrapper .one-col-feature ol a:hover,.wrapper .one-col-feature ul a:hover{color:#30495c !important}.wrapper .btn a{background-color:#41637e;color:#fff}.wrapper .btn a:hover{color:#fff !important}.logo div{color:#41637e}.logo div a{color:#41637e}.logo div a:hover{color:#41637e !important}.preheader .title,.preheader .webversion,.footer .padded{color:#999}.preheader .title a,.preheader .webversion a,.footer .padded a{color:#999}.preheader .title a:hover,.preheader .webversion a:hover,.footer .padded a:hover{color:#737373 !important}.footer .social .divider{color:#e9e9e9}.footer .social .social-text,.footer .social a{color:#999}.footer .social .social-text:hover,.footer
.social a:hover{color:#737373 !important}.image-frame{background-color:#f7f7f7;border-color:#dadada}
</style><meta name="robots" content="noindex,nofollow" />
<meta property="og:title" content="My First Campaign" />
</head>
<!--[if mso]>
  <body class="mso">
<![endif]-->
<!--[if !mso]><!-->
  <body style="margin: 0;padding: 0;min-width: 100%;background-color: #fbfbfb">
<!--<![endif]-->
    <center class="wrapper" style="display: table;table-layout: fixed;width: 100%;min-width: 620px;-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;background-color: #fbfbfb">
    	<table class="gmail" style="border-collapse: collapse;border-spacing: 0;width: 650px;min-width: 650px"><tbody><tr><td style="padding: 0;vertical-align: top;font-size: 1px;line-height: 1px">&nbsp;</td></tr></tbody></table>
      <table class="preheader centered" style="border-collapse: collapse;border-spacing: 0;Margin-left: auto;Margin-right: auto">
        <tbody><tr>
          <td style="padding: 0;vertical-align: top">
            <table style="border-collapse: collapse;border-spacing: 0;width: 602px">
              <tbody><tr>
                <td class="title" style="padding: 0;vertical-align: top;font-family: Georgia,serif;padding-top: 10px;padding-bottom: 12px;font-size: 12px;line-height: 21px;text-align: left;color: #999">
                  &nbsp;
                </td>
              </tr>
            </tbody></table>
          </td>
        </tr>
          <table class="border" style="border-collapse: collapse;border-spacing: 0;font-size: 1px;line-height: 1px;background-color: #e9e9e9;Margin-left: auto;Margin-right: auto" width="602">
            <tbody><tr><td style="padding: 0;vertical-align: top">&#8203;</td></tr>
          </tbody></table>
          <table class="centered" style="border-collapse: collapse;border-spacing: 0;Margin-left: auto;Margin-right: auto">
            <tbody><tr>
              <td class="border" style="padding: 0;vertical-align: top;font-size: 1px;line-height: 1px;background-color: #e9e9e9;width: 1px">&#8203;</td>
              <td style="padding: 0;vertical-align: top">
                <table class="one-col" style="border-collapse: collapse;border-spacing: 0;Margin-left: auto;Margin-right: auto;width: 600px;background-color: #ffffff;font-size: 14px;table-layout: fixed" emb-background-style>
                  <tbody><tr>
                    <td class="column" style="padding: 0;vertical-align: top;text-align: left">
                      <div><div class="column-top" style="font-size: 32px;line-height: 32px">&nbsp;</div></div>
                        <table class="contents" style="border-collapse: collapse;border-spacing: 0;table-layout: fixed;width: 100%">
                          <tbody><tr>
                            <td class="padded" style="padding: 0;vertical-align: top;padding-left: 32px;padding-right: 32px;word-break: break-word;word-wrap: break-word">
            <h1 style="Margin-top: 0;font-style: normal;font-weight: 700;font-size: 36px;line-height: 44px;Margin-bottom: 18px;font-family: Avenir,sans-serif;color: #565656">Welcome on <span style="color:#10a350">iSCT</span> !</h1><h3 style="Margin-top: 0;font-style: normal;font-weight: normal;font-size: 18px;line-height: 22px;Margin-bottom: 16px;font-family: Georgia,serif;color: #555"><span>Thanks for signing up.&nbsp;</span></h3>
                            </td>
                          </tr>
                        </tbody></table>
                        <table class="contents" style="border-collapse: collapse;border-spacing: 0;table-layout: fixed;width: 100%">
                          <tbody><tr>
                            <td class="padded" style="padding: 0;vertical-align: top;padding-left: 32px;padding-right: 32px;word-break: break-word;word-wrap: break-word">
            <div class="btn" style="Margin-bottom: 24px;text-align: left">
              <![if !mso]><a style="border-radius: 3px;display: inline-block;font-size: 14px;font-weight: 700;line-height: 24px;padding: 13px 35px 12px 35px;text-align: center;text-decoration: none !important;transition: opacity 0.2s ease-in;color: #fff;font-family: Georgia,serif;background-color: #41637e" href="'''+confirm_url+'''">Activate your account</a><![endif]>
            <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="'''+confirm_url+'''" style="width:226px" arcsize="7%" fillcolor="#41637E" stroke="f"><v:textbox style="mso-fit-shape-to-text:t" inset="0px,12px,0px,11px"><center style="font-size:14px;line-height:24px;color:#FFFFFF;font-family:Georgia,serif;font-weight:700;mso-line-height-rule:exactly;mso-text-raise:4px">Activate your account</center></v:textbox></v:roundrect><![endif]--></div>
                            </td>
                          </tr>
                        </tbody></table>
                      <div class="column-bottom" style="font-size: 8px;line-height: 8px">&nbsp;</div>
                    </td>
                  </tr>
                </tbody></table>
              </td>
              <td class="border" style="padding: 0;vertical-align: top;font-size: 1px;line-height: 1px;background-color: #e9e9e9;width: 1px">&#8203;</td>
            </tr>
          </tbody></table>
          <table class="border" style="border-collapse: collapse;border-spacing: 0;font-size: 1px;line-height: 1px;background-color: #e9e9e9;Margin-left: auto;Margin-right: auto" width="602">
            <tbody><tr class="border" style="font-size: 1px;line-height: 1px;background-color: #e9e9e9;height: 1px">
              <td class="border" style="padding: 0;vertical-align: top;font-size: 1px;line-height: 1px;background-color: #e9e9e9;width: 1px">&#8203;</td>
              <td style="padding: 0;vertical-align: top;line-height: 1px">&#8203;</td>
              <td class="border" style="padding: 0;vertical-align: top;font-size: 1px;line-height: 1px;background-color: #e9e9e9;width: 1px">&#8203;</td>
            </tr>
          </tbody></table>
          <table class="centered" style="border-collapse: collapse;border-spacing: 0;Margin-left: auto;Margin-right: auto">
            <tbody><tr>
              <td class="border" style="padding: 0;vertical-align: top;font-size: 1px;line-height: 1px;background-color: #e9e9e9;width: 1px">&#8203;</td>
              <td style="padding: 0;vertical-align: top">
                <table class="one-col" style="border-collapse: collapse;border-spacing: 0;Margin-left: auto;Margin-right: auto;width: 600px;background-color: #ffffff;font-size: 14px;table-layout: fixed" emb-background-style>
                  <tbody><tr>
                    <td class="column" style="padding: 0;vertical-align: top;text-align: left">
                      <div><div class="column-top" style="font-size: 32px;line-height: 32px">&nbsp;</div></div>
                        <table class="contents" style="border-collapse: collapse;border-spacing: 0;table-layout: fixed;width: 100%">
                          <tbody><tr>
                            <td class="padded" style="padding: 0;vertical-align: top;padding-left: 32px;padding-right: 32px;word-break: break-word;word-wrap: break-word">
            <p style="Margin-top: 0;font-style: normal;font-weight: 400;line-height: 24px;Margin-bottom: 24px;font-family: Georgia,serif;color: #565656;font-size: 16px">Or please follow this link to activate your account: '''+confirm_url+''' &nbsp;</p><p style="Margin-top: 0;font-style: normal;font-weight: 400;line-height: 24px;Margin-bottom: 24px;font-family: Georgia,serif;color: #565656;font-size: 16px"><span style="color:#008f05">Cheers!</span></p>
                            </td>
                          </tr>
                        </tbody></table>
                      <div class="column-bottom" style="font-size: 8px;line-height: 8px">&nbsp;</div>
                    </td>
                  </tr>
                </tbody></table>
              </td>
              <td class="border" style="padding: 0;vertical-align: top;font-size: 1px;line-height: 1px;background-color: #e9e9e9;width: 1px">&#8203;</td>
            </tr>
          </tbody></table>
          <table class="border" style="border-collapse: collapse;border-spacing: 0;font-size: 1px;line-height: 1px;background-color: #e9e9e9;Margin-left: auto;Margin-right: auto" width="602">
            <tbody><tr><td style="padding: 0;vertical-align: top">&#8203;</td></tr>
          </tbody></table>
      <table class="footer centered" style="border-collapse: collapse;border-spacing: 0;Margin-left: auto;Margin-right: auto;width: 602px">
        <tbody><tr>
          <td class="social" style="padding: 0;vertical-align: top;padding-top: 32px;padding-bottom: 22px;font-family: Georgia,serif;border-bottom: 1px solid #e9e9e9" align="center">
            <table style="border-collapse: collapse;border-spacing: 0">
              <tbody><tr>
                <td class="social-link" style="padding: 0;vertical-align: top">
                  <table style="border-collapse: collapse;border-spacing: 0">
                    <tbody><tr>
                      <td style="padding: 0;vertical-align: top">
                        <fblike style="text-decoration:none;">
                          <img style="border: 0;-ms-interpolation-mode: bicubic;display: block" src="https://i5.createsend1.com/static/eb/master/01-mason/images/facebook-dark.png" width="26" height="21" />
                        </fblike>
                      </td>
                      <td class="social-text" style="padding: 0;vertical-align: middle !important;height: 21px;font-size: 10px;font-weight: bold;letter-spacing: 0.05em;text-transform: uppercase;color: #999">
                        <fblike style="text-decoration:none;">
                          Like
                        </fblike>
                      </td>
                    </tr>
                  </tbody></table>
                </td>
                <td class="divider" style="padding: 0;vertical-align: top;font-family: sans-serif;font-size: 10px;line-height: 21px;text-align: center;padding-left: 14px;padding-right: 14px;color: #e9e9e9">
                  <img style="border: 0;-ms-interpolation-mode: bicubic;display: block" src="https://i6.createsend1.com/static/eb/master/01-mason/images/diamond.png" width="5" height="21" alt="" />
                </td>
                <td class="social-link" style="padding: 0;vertical-align: top">
                  <table style="border-collapse: collapse;border-spacing: 0">
                    <tbody><tr>
                      <td style="padding: 0;vertical-align: top">
                        <tweet style="text-decoration:none;">
                          <img style="border: 0;-ms-interpolation-mode: bicubic;display: block" src="https://i7.createsend1.com/static/eb/master/01-mason/images/twitter-dark.png" width="26" height="21" />
                        </tweet>
                      </td>
                      <td class="social-text" style="padding: 0;vertical-align: middle !important;height: 21px;font-size: 10px;font-weight: bold;letter-spacing: 0.05em;text-transform: uppercase;color: #999">
                        <tweet style="text-decoration:none;">
                          Tweet
                        </tweet>
                      </td>
                    </tr>
                  </tbody></table>
                </td>
                <td class="divider" style="padding: 0;vertical-align: top;font-family: sans-serif;font-size: 10px;line-height: 21px;text-align: center;padding-left: 14px;padding-right: 14px;color: #e9e9e9">
                  <img style="border: 0;-ms-interpolation-mode: bicubic;display: block" src="https://i6.createsend1.com/static/eb/master/01-mason/images/diamond.png" width="5" height="21" alt="" />
                </td>
                <td class="social-link" style="padding: 0;vertical-align: top">
                  <table style="border-collapse: collapse;border-spacing: 0">
                    <tbody><tr>
                      <td style="padding: 0;vertical-align: top">
                        <forwardtoafriend style="text-decoration:none;" lang="en">
                          <img style="border: 0;-ms-interpolation-mode: bicubic;display: block" src="https://i8.createsend1.com/static/eb/master/01-mason/images/forward-dark.png" width="26" height="21" />
                        </forwardtoafriend>
                      </td>
                      <td class="social-text" style="padding: 0;vertical-align: middle !important;height: 21px;font-size: 10px;font-weight: bold;letter-spacing: 0.05em;text-transform: uppercase;color: #999">
                        <forwardtoafriend style="text-decoration:none;" lang="en">
                          Forward
                        </forwardtoafriend>
                      </td>
                    </tr>
                  </tbody></table>
                </td>
              </tr>
            </tbody></table>
          </td>
        </tr>
        <tr>
          <td style="padding: 0;vertical-align: top">
            <table style="border-collapse: collapse;border-spacing: 0">
              <tbody><tr>
                <td class="address" style="padding: 0;vertical-align: top;width: 250px;padding-top: 32px;padding-bottom: 64px;font-family: Georgia,serif">
                  <table class="contents" style="border-collapse: collapse;border-spacing: 0;table-layout: fixed;width: 100%">
                    <tbody><tr>
                      <td class="padded" style="padding: 0;vertical-align: top;padding-left: 0;padding-right: 10px;word-break: break-word;word-wrap: break-word;text-align: left;font-size: 12px;line-height: 20px;color: #999">
                        <div class="address" style="width: 250px;padding-top: 32px;padding-bottom: 64px;font-family: Georgia,serif">
                        </div>
                      </td>
                    </tr>
                  </tbody></table>
                </td>
                <td class="subscription" style="padding: 0;vertical-align: top;width: 350px;padding-top: 32px;padding-bottom: 64px">
                  <table class="contents" style="border-collapse: collapse;border-spacing: 0;table-layout: fixed;width: 100%">
                    <tbody><tr>
                      <td class="padded" style="padding: 0;vertical-align: top;padding-left: 10px;padding-right: 0;word-break: break-word;word-wrap: break-word;font-size: 12px;line-height: 20px;color: #999;text-align: right">
                        <div class="permission" style="font-family: Georgia,serif">
                        </div>
                      </td>
                    </tr>
                  </tbody></table>
                </td>
              </tr>
            </tbody></table>
          </td>
        </tr>
      </tbody></table>
    </center>
</body></html>
'''

    return template