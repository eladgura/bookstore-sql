def display_page(items, page_size, page_number):
    start_idx = (page_number - 1) * page_size
    end_idx = min(start_idx + page_size, len(items))

    print(f"Page {page_number} of {len(items) // page_size + 1}:")
    for i in range(start_idx, end_idx):
        print(items[i])
