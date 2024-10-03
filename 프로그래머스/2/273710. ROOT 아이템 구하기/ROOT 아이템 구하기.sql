-- 코드를 작성해주세요
select i.ITEM_ID, i.ITEM_NAME from item_info i join item_tree t on t.item_id = i.item_id where t.PARENT_ITEM_ID is null