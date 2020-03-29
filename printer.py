import json,sys,click,pydoc,requests

def main():

	jData = {}

	dataUrl = "https://raw.githubusercontent.com/busterbenson/public/master/cognitive-bias-cheat-sheet.json"

	getData = requests.get(dataUrl)

	dataJson = getData.text

	jData = json.loads(dataJson)


	cNames = []

	for child in jData["children"]:
		for key in child.keys():
			if key == "name":
				cNames.append(child[key])

	allChar = 'a'
	exitChar = 'e'

	runProgram = True
	errorAction = True

	selectIndex = ""

	while runProgram:

		click.clear()

		page = ""

		print()

		print("\nOptions:")

		for name in cNames:
			print("     "+name)

		print(
		"\n     Select '"+allChar+"' to view all.",
		"\n     Select '"+exitChar+"' to exit.")

		print("\nResults will appear in paginated form.",
			"\nTo return to this menu, hit 'q'.")

		if selectIndex != "":
			print("\nLast selection: "+selectIndex)

		selectIndex = input("\nSelect index and press enter: ")

		try:
			if (int(selectIndex) > 0 and int(selectIndex) <= len(cNames)):
				# click.clear()
				fmtIndex = int(selectIndex)-1

				selectName = cNames[fmtIndex]

				page += "\n"+selectName+"\n"

				for child in jData["children"]:
					for key in child.keys():
						if key == "name" and child["name"] == selectName:
							for grandchild in child["children"]:
								page += "\n     "+grandchild["name"]
								for greatgrandchild in grandchild["children"]:
									page += "\n          "+greatgrandchild["name"]
								page += "\n\n"
				errorAction = False
			else:
				errorAction = True
		except:
			if selectIndex.lower() == allChar:
				# click.clear()
				for child in jData["children"]:
					page += "\n\n"+child["name"]+"\n"

					for grandchild in child["children"]:
						page += "\n     "+grandchild["name"]
						for greatgrandchild in grandchild["children"]:
							page += "\n          "+greatgrandchild["name"]

						page += "\n\n"
				errorAction = False
			elif selectIndex.lower() == exitChar:
				errorAction = False
				runProgram = False
			else:
				errorAction = True

		if not errorAction and runProgram:
			pydoc.pager(page)

if __name__ == "__main__":
	main()
