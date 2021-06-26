var convert = function(document)
{
    var
intValue = parseInt(document.field, 10);
db.collection.update(
    {_id: document._id},
    {$set: {field: intValue}}
);
}

db.collection.find({field: {$type: 2}}, {field: 1}).forEach(convert)