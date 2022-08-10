In Code Fragment 6.5 we assume that opening tags in HTML have form
`<name>`, as with `<li>`. More generally, HTML allows optional attributes
to be expressed as part of an opening tag. The general form used is
`<name attribute1="value1" attribute2="value2">`; for example,
a table can be given a border and additional padding by using an opening
tag of `<table border="3" cellpadding="5">`. Modify Code Fragment 6.5 so that it can properly match tags, even when an
opening tag may include one or more such attributes.