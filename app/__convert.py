def __convert(text, header=None):
	# Replace document line breaks with html line breaks
	text = text.replace('\n', '<br /><br />')

	# Replace header codes with html header tags
	if not header == None:
		header = 'h' + str(header)
	else:
		header = 'hd'
	text = text.replace('[h]', '<' + header + '>')
	text = text.replace('[/h]', '</' + header + '><br />')

	# Replace list codes with html list tags
	text = text.replace('[ul]', '<ul><li>')
	text = text.replace('[/li/]', '</li><li>')
	text = text.replace('[/ul]', '</li></ul>\n')

	# Replace table codes with html table tags
	text = text.replace('[/t]', '</table>\n')
	text = text.replace('[tc]', '<table>\n<caption>')
	text = text.replace('[/tc]', '</caption>\n')
	text = text.replace('[th]', '<thead>\n<tr><th>')
	text = text.replace('[/th/]', '</th><th>')
	text = text.replace('[/th]', '</th></tr>\n</thead>\n<tbody>\n')
	text = text.replace('[tr]', '<tr><td>')
	text = text.replace('[td]', '</td><td>')
	text = text.replace('[/tr]', '</td></tr>\n')
	text = text.replace('[/t]', '</tbody>\n</table>\n')

	return text