## method to merge two sorted linked lists

def mergeSortLL(ll1,ll2):
	ptr1,ptr2 = (ll1.head,ll2.head)
	
	if ptr1.data < ptr2.data:
		dummyHead = ptr1
		lastEle = ptr1
		ptr1 = ptr1.next
	else:
		dummyHead = ptr2
		lastEle = ptr2
		ptr2 = ptr2.next
	
	while ptr1 is not None and ptr2 is not None:
		if ptr1.data < ptr2.data:
			lastEle.next = ptr1
			lastEle = ptr1
			ptr1 = ptr1.next
		else:
			lastEle.next = ptr2
			lastEle = ptr2
			ptr2 = ptr2.next
			
	
	if ptr1 is not None:
		lastEle.next = ptr1
	
	if ptr2 is not None:
		lastEle.next = ptr2
		
	ll1.head = dummyHead